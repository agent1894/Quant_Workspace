#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import broker.broker as bk
import portfolio.portfolio as pf
import utility.tradingLog as tlog


class Strategy(object):
    __metaclass__ = ABCMeta

    def __init__(self, symbols: list):
        self._symbols = symbols if isinstance(symbols, list) else [symbols]
        self._broker = None
        self._portfolio = None
        self._bars = []
        self._log = tlog.Order()

    def report(self):
        return self._log.print_report()

    def set_broker(self, broker: bk.Broker):
        self._broker = broker

    def set_portfolio(self, portfolio: pf.Portfolio):
        self._portfolio = portfolio

    def market_order(self, datetime, symbol, size: int = 0, percent: float = None):
        if percent is not None:
            currentCash = self._portfolio.cash
            currentPrice = self._bars[-1]["Close"]
            size = int(currentCash * percent / currentPrice / 100.0) * 100
        result = self._broker.market_order(datetime, symbol, orderSize=size)
        if result is not None:
            self._log.append_report(result)
            self._portfolio.update_positions(result)
            self._portfolio.update_datetime(result["Completion Time"])

    def limit_order(self):
        return self._broker.limit_order()

    @abstractmethod
    def execute(self, data):
        raise NotImplementedError("Should implement execute().")
