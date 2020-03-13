#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
Main entrance of programme.
"""

import datetime as dt
import pandas as pd
import portfolio.portfolio as pf
import quotation.quotation as qt
import strategy.strategy as stg


class QuantSim(object):
    def __init__(self, startDate: dt.datetime, endDate: dt.datetime, quotation: qt.Quotation, strategy: stg.Strategy, portfolio: pf.Portfolio,
                 freq):
        self._quotation = quotation
        self._strategy = strategy
        self._portfolio = portfolio
        self._freq = freq

    def backtesting(self):
        for bar in self._quotation.push_bars():
            if self._freq[0:1].upper() == "D" or bar.datetime.time() == dt.time(9, 30):
                self._portfolio.reset_available_sell()
            transInfo = self._strategy.execution(bar)
            print(transInfo)
            # self._portfolio.update_positions(transInfo)


class MyStrategy(stg.Strategy):
    def __init__(self):
        super(MyStrategy, self).__init__()
        self._bars = []

    def execution(self, bar):
        self._bars.append(bar)
        df = pd.concat(self._bars)
        if len(df) >= 20:
            ma5 = df["Close"].rolling(5).mean()
            ma20 = df["Close"].rolling(20).mean()
            if ma5 > ma20:
                self.market_order(size=100)
            else:
                self.market_order(percent=-1)
