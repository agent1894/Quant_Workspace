#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import datetime as dt
import utility.tradingLog as tlog


class Stock(object):
    def __init__(self, totalPosition: int = 0, availableSell: int = 0, orderCosts: float = 0, currentPrice: float = 0):
        self._totalPosition = totalPosition
        self._availableSell = availableSell
        self._orderCosts = orderCosts
        self._currentPrice = currentPrice

    def update_positions(self, position: int):
        newTotalPosition = self._totalPosition + position
        if newTotalPosition < 0:
            return "Over-sell is illegal, order cancelled."
        self._totalPosition += position

    def update_availableSell(self, position: int):
        newAvailableSell = self._availableSell + position
        if newAvailableSell < 0:
            return "Over-sell is illegal, order cancelled."
        self._availableSell += position

    def update_cost(self, cost: float):
        self._orderCosts += cost

    def update_currentPrice(self, price: float):
        self._currentPrice = price

    @property
    def totalPosition(self):
        return self._totalPosition

    @property
    def availableSell(self):
        return self._availableSell

    @availableSell.setter
    def availableSell(self, value: float):
        self._availableSell = value

    @property
    def orderCosts(self):
        return self._orderCosts


class Portfolio(object):
    def __init__(self, initDatetime: dt.datetime, cash: float = 100000, stock: dict = None):
        self._datetime = initDatetime  # datetime of portfolio opening position
        self._cash = cash
        if stock is None:
            stock = dict()
        self._stock = stock
        self._fees = 0
        self._log = tlog.Execute()
        print("Portfolio initialized, opening status: Cash holding: {}, Stocks holding: {}".format(self._cash,
                                                                                                   self._stock))

    @property
    def cash(self):
        return self._cash

    @property
    def positions(self):
        return {"Cash": self._cash, "Stock": self._stock}

    @property
    def symbols(self):
        return set(self._stock.keys())

    def update_cash(self, value: float):
        if value < 0 and abs(value) > self._cash:
            self._log.append_report("Over-sell is illegal, order cancelled.")
        else:
            self._cash += value
            if value < 0:
                self._log.append_report("Withdraw cash: {}".format(value))
            elif value > 0:
                self._log.append_report("Deposit cash: {}".format(value))
            else:
                self._log.append_report("No cash change made.")

    def update_datetime(self, datetime: dt.datetime):
        self._datetime = datetime

    def reset_available_sell(self):
        for stock in self._stock.keys():
            self._stock[stock].availableSell = self._stock[stock].totalPosition

    def update_positions(self, transInfo: dict):
        symbol = transInfo["Symbol"]
        orderPrice = transInfo["Order Price"]
        orderSize = transInfo["Order Size"]
        feeRate = transInfo["Commission Fee"]
        if self._stock.get(symbol) is None:
            self._stock[symbol] = Stock()
        stock = self._stock[symbol]
        result = stock.update_positions(orderSize)
        self._log.append_report(result)
        if orderSize < 0:
            stock.update_availableSell(orderSize)
        stock.update_currentPrice(orderPrice)
        fees = feeRate * orderPrice * orderSize
        fees = fees if fees >= 5.0 else 5.0
        stock.update_cost(fees)
        self._fees += fees

    def check_positions(self):
        if self._cash < 0:
            raise RuntimeError("The account cash can not be negative.")
        if self._stock is not None:
            for key in self._stock:
                if self._stock[key].totalPosition < 0 or self._stock[key].availableSell < 0:
                    raise RuntimeError("The {} stock has incorrect position.".format(key))
