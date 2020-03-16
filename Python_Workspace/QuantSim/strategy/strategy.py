#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import broker.broker as bk


class Strategy(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self._broker = None

    def set_broker(self, broker: bk.Broker):
        self._broker = broker

    def market_order(self, datetime, symbol, size: int = 0, percent: float = None):
        if percent:
            pass
        else:
            return self._broker.market_order(datetime, symbol, orderSize=size)

    def limit_order(self):
        return self._broker.limit_order()

    @abstractmethod
    def execute(self, data):
        raise NotImplementedError("Should implement execute().")
