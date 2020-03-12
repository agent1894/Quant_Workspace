#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import numpy as np
import pandas as pd
import quotation.quotation as qt
import broker.broker as bk
import portfolio.portfolio as pf


class Strategy(object):
    __metaclass__ = ABCMeta

    def __init__(self, symbols: list, portfolio: pf.Portfolio):
        pass

    @abstractmethod
    def calculate_signals(self):
        raise NotImplementedError("Should implement calculate_signals().")

    @abstractmethod
    def execution(self, *args):
        raise NotImplementedError("Should implement execution().")


class Test(Strategy):
    def __init__(self, symbols, portfolio):
        super(Test, self).__init__(symbols=symbols, portfolio=portfolio)
        self._symbol = symbols
        self._obj = bk.Broker(self._symbol, '20190101', '20200101', 'non', '5')
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

    def execution(self, *args):
        if args[0] > args[1]:
            return self._obj.market_order(args[2], 'sh.600000', 100)
        else:
            return self._obj.market_order(args[2], 'sh.600000', -100)


demo = Test(['sh.600000'], portfolio=None)
quote = qt.QuotationMinuteBar(['sh.600000'], '20190101', '20190501', 'non', '5')
for bar in quote.push_bars():
    demo.get_bars(bar)
    ma5, ma20, time = demo.calculate_signals()
    if ma5 and ma20 and time:
        print(demo.execution(ma5, ma20, time))
