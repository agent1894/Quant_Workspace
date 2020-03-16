#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
This module simulates the broker. The broker have all historical data and calculates the TWAP/VWAP for order making.
If the broker uses the tick data, the matching of transactions should take book depth into consideration.
"""

import datetime as dt
from random import randint
import numpy as np
import pandas as pd
import utility.tradingDays as td


class Broker(object):
    def __init__(self, symbols: list, startDate: str, endDate: str, freq: str, data: pd.DataFrame, commission: float,
                 slippage: float):
        self.symbols = symbols
        self._startDate = startDate
        self._endDate = endDate
        self._commission = commission
        self._slippage = slippage
        if freq.capitalize()[0:1] == 'D':
            self._tradingDatetime = td.Trading(startDate=self._startDate, endDate=self._endDate,
                                               freq='D').trade_datetimes()
        elif freq.startswith(("5", "15", "30", "60")):
            self._tradingDatetime = td.Trading(startDate=self._startDate, endDate=self._endDate,
                                               freq=freq + 'T').trade_datetimes()
        # TODO: add tick data trading time
        elif freq.capitalize() == "Tick":
            pass
        else:
            raise ValueError("Now only support tick or 5/15/30/60 minutes or daily data.")
        self._baseData = data
        self._baseData["Mid"] = self._baseData[['High', 'Low', 'Close']].mean(axis=1)
        self._transInfo = dict()

    def market_order(self, datetime: dt.datetime, symbol: str, orderSize: int, completeInstant: bool = True,
                     useWap: str = None, completeBars: int = 0) -> dict:

        def instantlyComplete(basePrice: pd.DataFrame, slippage: float = 0):
            self._transInfo["Order Price"] = round(basePrice.Mid * (1 + np.sign(orderSize) * slippage), 2)

        def graduallyComplete(basePrice: pd.DataFrame, slippage: float = 0):
            if not (useWap and completeBars > 0):
                raise KeyError("Should implement useWap and completeBars, completeBars should greater than 0.")
            if useWap.upper() == "TWAP":
                self._transInfo["Order Price"] = round(basePrice.Mid.mean() * (1 + np.sign(orderSize) * slippage), 2)
            elif useWap.upper() == "VWAP":
                self._transInfo["Order Price"] = round(
                    sum(basePrice["Mid"] * basePrice["Volume"]) / basePrice["Volume"].sum() * (
                            1 + np.sign(orderSize) * slippage), 2)
            else:
                raise KeyError("Order price should be simulated by TWAP or VWAP.")

        self._transInfo["Order Time"] = datetime
        self._transInfo["Symbol"] = symbol
        self._transInfo["Order Type"] = "Market Order"
        self._transInfo["Commission Fee"] = self._commission
        self._transInfo["Order ID"] = randint(1, 1e8)
        orderTimeIndex = self._tradingDatetime[self._tradingDatetime == pd.Timestamp(datetime)].index.values[0]

        if completeInstant:
            completeTime = self._tradingDatetime[orderTimeIndex + 1]
        else:
            completeTime = self._tradingDatetime[orderTimeIndex + 1: orderTimeIndex + 1 + completeBars]

        try:
            marketMaker = self._baseData.loc[self._baseData['Code'] == symbol].loc[completeTime]
        except KeyError:
            self._transInfo["Completion Time"] = datetime
            self._transInfo["Order Price"] = 0.0
            self._transInfo["Order Status"] = "Order rejected, no sufficient quote."
            self._transInfo["Order Size"] = 0.0
        else:
            maxMarketVolume = np.floor(marketMaker.Volume.sum() / 4.0)
            if completeInstant:
                self._transInfo["Completion Time"] = marketMaker.name
                instantlyComplete(basePrice=marketMaker, slippage=self._slippage)
            else:
                self._transInfo["Completion Time"] = marketMaker.index[-1]
                graduallyComplete(basePrice=marketMaker, slippage=self._slippage)
            if abs(orderSize) < maxMarketVolume:
                self._transInfo["Order Status"] = "Order received and try to execute."
                self._transInfo["Order Size"] = int(orderSize / 100.0) * 100
            else:
                self._transInfo["Order Status"] = "Order received and try to partial execute."
                self._transInfo["Order Size"] = int(maxMarketVolume / 100.0) * 100

        return self._transInfo

        # if not marketMaker.empty:
        #     maxMarketVolume = np.floor(marketMaker.Volume.sum() / 4.0)
        #     if completeInstant:
        #         self._transInfo["Completion Time"] = marketMaker.name
        #         instantlyComplete(basePrice=marketMaker, slippage=self._slippage)
        #     else:
        #         self._transInfo["Completion Time"] = marketMaker.index[-1]
        #         graduallyComplete(basePrice=marketMaker, slippage=self._slippage)
        #     if abs(orderSize) < maxMarketVolume:
        #         self._transInfo["Order Status"] = "Order received and try to execute."
        #         self._transInfo["Order Size"] = int(orderSize / 100.0) * 100
        #     else:
        #         self._transInfo["Order Status"] = "Order received and try to partial execute."
        #         self._transInfo["Order Size"] = int(maxMarketVolume / 100.0) * 100
        # else:
        #     self._transInfo["Completion Time"] = datetime
        #     self._transInfo["Order Price"] = 0.0
        #     self._transInfo["Order Status"] = "Order rejected, no sufficient quote."
        #     self._transInfo["Order Size"] = 0.0

    # TODO: transaction completion probability
    def limit_order(self, datetime: dt.datetime, symbol: str, orderPrice: float, orderSize: int,
                    completeBars: int = 3) -> dict:
        self._transInfo["Order Time"] = datetime
        self._transInfo["Symbol"] = symbol
        self._transInfo["Order Type"] = "Limit Order"
        self._transInfo["Commission Fee"] = self._commission
        self._transInfo["Order ID"] = randint(1, 1e8)
        orderTimeIndex = self._tradingDatetime[self._tradingDatetime == pd.Timestamp(datetime)].index.values[0]
        completeTime = self._tradingDatetime[orderTimeIndex + 1: orderTimeIndex + 1 + completeBars]

        try:
            marketMaker = self._baseData.loc[self._baseData['Code'] == symbol].loc[completeTime]
        except KeyError:
            self._transInfo["Completion Time"] = datetime
            self._transInfo["Order Price"] = 0.0
            self._transInfo["Order Size"] = 0
            self._transInfo["Order Status"] = "Order rejected, no sufficient quote."
        else:
            if not marketMaker.empty and marketMaker.Low.min() <= orderPrice <= marketMaker.High.max():
                maxMarketVolume = np.floor(marketMaker.Volume.sum() / 4.0)
                self._transInfo["Order Price"] = orderPrice
                if abs(orderSize) < maxMarketVolume:
                    self._transInfo["Completion Time"] = marketMaker.index[-1]
                    self._transInfo["Order Status"] = "Order received and try to execute."
                    self._transInfo["Order Size"] = int(orderSize / 100.0) * 100
                else:
                    self._transInfo["Completion Time"] = marketMaker.index[-1]
                    self._transInfo["Order Status"] = "Order received and try to partial execute."
                    self._transInfo["Order Size"] = int(maxMarketVolume / 100.0) * 100
            else:
                self._transInfo["Completion Time"] = datetime
                self._transInfo["Order Price"] = 0.0
                self._transInfo["Order Size"] = 0
                self._transInfo["Order Status"] = "Order rejected, order price is not acceptable."

        return self._transInfo

        # if not marketMaker.empty and marketMaker.Low.min() <= orderPrice <= marketMaker.High.max():
        #     maxMarketVolume = np.floor(marketMaker.Volume.sum() / 4.0)
        #     self._transInfo["Order Price"] = orderPrice
        #     if abs(orderSize) < maxMarketVolume:
        #         self._transInfo["Completion Time"] = marketMaker.index[-1]
        #         self._transInfo["Order Status"] = "Order received and try to execute."
        #         self._transInfo["Order Size"] = int(orderSize / 100.0) * 100
        #     else:
        #         self._transInfo["Completion Time"] = marketMaker.index[-1]
        #         self._transInfo["Order Status"] = "Order received and try to partial execute."
        #         self._transInfo["Order Size"] = int(maxMarketVolume / 100.0) * 100
        # else:
        #     self._transInfo["Completion Time"] = datetime
        #     self._transInfo["Order Price"] = 0.0
        #     self._transInfo["Order Size"] = 0
        #     if marketMaker.empty:
        #         self._transInfo["Order Status"] = "Order rejected, no sufficient quote."
        #     if abs(orderPrice) < marketMaker.Low.min() or abs(orderPrice) > marketMaker.High.max():
        #         self._transInfo["Order Status"] = "Order rejected, order price is not acceptable."
