#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import datetime as dt
import numpy as np
import pandas as pd
import broker.broker as bk


class Stock(object):
    def __init__(self, symbol: str = '', totalPosition: int = 0, todayLong: int = 0, todayShort: int = 0,
                 availableSell: int = 0, currentPrice: float = 0):
        self._symbol = symbol
        self._totalPosition = totalPosition
        self._todayLong = todayLong
        self._todayShort = todayShort
        self._availableSell = availableSell
        self._currentPrice = currentPrice

    @property
    def symbol(self):
        return self._symbol

    @property
    def totalPosition(self):
        return self._totalPosition

    @property
    def todayLong(self):
        return self._todayLong

    @property
    def todayShort(self):
        return self._todayShort

    @property
    def availableSell(self):
        return self._availableSell

    @property
    def currentPrice(self):
        return self._currentPrice


class Portfolio(object):
    def __init__(self, initDatetime: dt.datetime, stock: Stock, cash: float = 1000000):
        self._datetime = initDatetime
        if stock is None:
            self._stock = dict()
        self._cash = cash
        self._fees = 0

    @property
    def positions(self):
        return {"Cash": self._cash, "Stock": self._stock}

    def cash_change(self, value: float):
        if value < 0 and abs(value) > self._cash:
            raise RuntimeError("Can not withdraw cash over current holdings.")
        else:
            self._cash += value

    def update_datetime(self, datetime: dt.datetime):
        self._datetime = datetime

    def update_positions(self, transInfo: dict, stock):
        symbol = transInfo["Symbol"]
        orderTime = transInfo["Completion Time"]
        orderType = transInfo["Order Type"]
        orderPrice = transInfo["Order Price"]
        orderSize = transInfo["Order Size"]
        orderTime = transInfo["Order Time"]
        fees = transInfo["Commission Fee"]

    def reset_available_sell(self):
        for stock in self._stock.items():
            pass
