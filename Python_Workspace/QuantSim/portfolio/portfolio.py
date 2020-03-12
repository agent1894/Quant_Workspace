#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import datetime as dt


class Stock(object):
    def __init__(self, symbol: str = '', totalPosition: int = 0, availableSell: int = 0, orderCosts: float = 0):
        self._symbol = symbol
        self._totalPosition = totalPosition
        self._availableSell = availableSell
        self._orderCosts = orderCosts

    @property
    def symbol(self):
        return self._symbol

    @property
    def totalPosition(self):
        return self._totalPosition

    @property
    def availableSell(self):
        return self._availableSell

    @property
    def orderCosts(self):
        return self._orderCosts


class Portfolio(object):
    def __init__(self, initDatetime: dt.datetime, cash: float = 1000000, stock: dict = None):
        self._datetime = initDatetime  # datetime of opening position
        self._cash = cash
        if stock is None:
            stock = dict()
        self._stock = stock
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

    def update_positions(self, transInfo: dict):
        symbol = transInfo["Symbol"]
        orderPrice = transInfo["Order Price"]
        orderSize = transInfo["Order Size"]
        fees = transInfo["Commission Fee"]
        self._stock[symbol]["totalPosition"] += orderSize
        if orderSize < 0:
            self._stock[symbol]["availableSell"] += orderSize
        self._stock[symbol]["currentPrice"] = orderPrice
        self._fees += fees

    def reset_available_sell(self):
        for stock in self._stock.keys():
            self._stock[stock]["availableSell"] = self._stock[stock]["totalPosition"]
