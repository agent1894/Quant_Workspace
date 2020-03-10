#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
This module simulates the broker. The broker have all historical data and calculates the TWAP/VWAP for order making.
If the broker uses the tick data, the matching of transactions should take book depth into consideration.
"""

# TODO: Calculate TWAP/VWAP

import datetime as dt
import random
import numpy as np
import pandas as pd
import quotation.quotation as qt
import utility.tradingDays as td


class Broker(object):
    def __init__(self, symbols: list, startDate: str, endDate: str, dividendAdjustment: str, freq: str,
                 commission: float, slipper: float):
        self.symbols = symbols
        self.startDate = startDate
        self.endDate = endDate
        self.dividendAdjustment = dividendAdjustment
        self._commission = commission
        self._slipper = slipper
        if freq.capitalize()[0:1] == 'D':
            obj = qt.QuotationDailyBar(self.symbols, self.startDate, self.endDate, self.dividendAdjustment)
            self._tradingDatetime = td.Trading(startDate=self.startDate, endDate=self.endDate,
                                               freq='D').trade_datetimes()
        elif freq.capitalize() == "Tick":
            # TODO: add Tick data trading time
            obj = qt.QuotationTick(self.symbols, self.startDate, self.endDate)
        elif freq.startswith(("5", "15", "30", "60")):
            obj = qt.QuotationMinuteBar(self.symbols, self.startDate, self.endDate, self.dividendAdjustment, freq)
            self._tradingDatetime = td.Trading(startDate=self.startDate, endDate=self.endDate,
                                               freq=freq + 'T').trade_datetimes()
        else:
            raise ValueError("Now only support tick or 5/15/30/60 minutes or daily data.")
        self._baseData = obj.push_data()
        self._baseData["Mid"] = self._baseData[['High', 'Low', 'Close']].mean(axis=1).round(2)
        self._transInfo = dict()

    @property
    def commission(self):
        return self._commission

    @commission.setter
    def commission(self, value: float):
        self._commission = value

    @property
    def slipper(self):
        return self._slipper

    @slipper.setter
    def slipper(self, value: float):
        self._slipper = value

    # TODO: order by 1. shares, 2. lots, 3. value, 4. percent, 5. target_value
    def market_order(self, datetime: dt.datetime, symbol: str, orderSize: int, orderDirection: int,
                     completeInstant: bool = True, useWap: str = None, completeBars: int = 0):

        def instantlyComplete(size, maxSize, basePrice, direction, slipper):
            self._transInfo["Order Price"] = basePrice + direction * slipper
            if size < maxSize:
                self._transInfo["Order Status"] = "Completed"
                self._transInfo["Order Size"] = size
            else:
                self._transInfo["Order Status"] = "Partial Completed"
                self._transInfo["Order Size"] = maxSize

        def graduallyComplete():
            if not (useWap and completeBars <= 0):
                raise KeyError("Should implement useWap and completeBars, completeBars should greater than 0.")
            if useWap.upper() == "TWAP":
                pass
            elif useWap.upper() == "VWAP":
                pass
            else:
                raise KeyError("Order price should be simulated by TWAP or VWAP.")

        self._transInfo["Order Time"] = datetime
        self._transInfo["Symbol"] = symbol
        self._transInfo["Order Type"] = "Market Order"
        self._transInfo["Commission Fee"] = self._commission
        self._transInfo["Order ID"] = random.randint(1, 1e8)
        orderTimeIndex = self._tradingDatetime[self._tradingDatetime == pd.Timestamp(datetime)].index
        if completeInstant:
            completeTime = self._tradingDatetime[orderTimeIndex + 1]
        else:
            completeTime = self._tradingDatetime[orderTimeIndex + 1: orderTimeIndex + 1 + completeBars]
        marketMaker = self._baseData.loc[self._baseData['Code'] == symbol].loc[completeTime]

        if not marketMaker.empty:
            maxMarketVolume = np.floor(marketMaker.Volume.sum() / 3.0)
            self._transInfo["Completion Time"] = marketMaker.index[-1]
            self._transInfo["Order Direction"] = orderDirection
            if completeInstant:
                instantlyComplete(orderSize, maxMarketVolume, marketMaker.Mid, orderDirection, self._slipper)
            else:
                graduallyComplete()
        else:
            self._transInfo["Completion Time"] = datetime
            self._transInfo["Order Price"] = 0.0
            self._transInfo["Order Status"] = "Rejected"
            self._transInfo["Order Size"] = 0
            self._transInfo["Order Direction"] = 0

        # if completeInstant:
        #     marketMaker = self._baseData.loc[self._baseData['Code'] == symbol].loc[completeTime]
        #     if not marketMaker.empty:
        #         maxMarketVolume = marketMaker.Volume[0] * 0.25
        #         theoMarketPrice = round((marketMaker.High[0] + marketMaker.Low[0] + marketMaker.Close[0]) / 3.0, 2)
        #         self._transInfo["Completion Time"] = marketMaker.index[0]
        #         self._transInfo["Order Price"] = theoMarketPrice + self._slipper
        #         if orderSize < maxMarketVolume:
        #             self._transInfo["Order Status"] = "Completed"
        #             self._transInfo["Order Size"] = orderSize
        #             self._transInfo["Order Direction"] = orderDirection
        #         else:
        #             self._transInfo["Order Status"] = "Partial Completed"
        #             self._transInfo["Order Size"] = maxMarketVolume
        #             self._transInfo["Order Direction"] = orderDirection
        #     else:
        #         self._transInfo["Order Status"] = "Rejected"
        #         self._transInfo["Order Size"] = 0
        #         self._transInfo["Order Direction"] = 0
        #     return self._transInfo
        # else:
        #     if not (useWap and completeBars <= 0):
        #         raise KeyError("Should implement useWap and completeBars, completeBars should greater than 0.")
        #     if useWap.upper() == "TWAP":
        #         pass
        #     elif useWap.upper() == "VWAP":
        #         pass
        #     else:
        #         raise KeyError("Order price should be simulated by TWAP or VWAP.")

    def limit_order(self, orderSize: int, orderDirection: int, useWap: bool):
        pass


class Report(object):
    pass
