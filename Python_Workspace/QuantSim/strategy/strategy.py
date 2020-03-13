#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import datetime as dt
import pandas as pd
import quotation.quotation as qt
import broker.broker as bk
import portfolio.portfolio as pf


class Strategy(object):
    __metaclass__ = ABCMeta

    def __init__(self, broker: bk.Broker):
        self._broker = broker
        self._startDate = None
        self._endDate = None

    @property
    def start(self):
        if self._startDate is None:
            raise RuntimeError("Start date must be named.")

    @start.setter
    def start(self, value: dt.datetime):
        if isinstance(value, dt.datetime):
            self._startDate = value
        else:
            raise TypeError("Start date should be a datetime.datetime object.")

    @property
    def end(self):
        if self._endDate is None:
            raise RuntimeError("End date must be named.")

    @end.setter
    def end(self, value: dt.datetime):
        if isinstance(value, dt.datetime):
            self._endDate = value
        else:
            raise TypeError("End date should be a datetime.datetime object.")
        if self._startDate > self._endDate:
            raise RuntimeError("End date can not set before start date.")

    def market_order(self, percent: float = None, size: int = 0):
        if percent:
            pass
        else:
            return self._broker.market_order()

    def limit_order(self):
        return self._broker.limit_order()

    @abstractmethod
    def execution(self, data):
        raise NotImplementedError("Should implement execution().")


class Test(Strategy):
    def __init__(self, symbols):
        super(Test, self).__init__(symbols=symbols)
        self._symbol = symbols
        self._obj = bk.Broker(self._symbol, '20190101', '20200101', 'non', 'd')
        self._count = 0
        self._bars = []

    def get_bars(self, data):
        self._count += 1
        if not data.empty:
            self._bars.append(data.to_frame().T)

    def calculate_signals(self):
        if len(self._bars) > 20:
            df = pd.concat(self._bars)
            sig5 = df["Close"].rolling(5).mean()[-1]
            sig20 = df["Close"].rolling(20).mean()[-1]
            return sig5, sig20, df.index[-1]
        else:
            return None, None, None

    def execution(self):
        if args[0] > args[1]:
            brokerRepo = self._obj.market_order(args[2], 'sh.600000', 100)
        else:
            brokerRepo = self._obj.market_order(args[2], 'sh.600000', -100)
        return brokerRepo



port = pf.Portfolio(dt.datetime(2019, 1, 1))
demo = Test(['sh.600000'], portfolio=port)
quote = qt.QuotationDailyBar(['sh.600000'], '20190101', '20190501', 'non')
for bar in quote.push_bars():
    demo.get_bars(bar)
    ma5, ma20, time = demo.calculate_signals()
    if ma5 and ma20 and time:
        demo.execution(ma5, ma20, time)
print(demo._portfolio.positions)
