#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import random
import datetime as dt
import pandas as pd
import main
import strategy.strategy as stg
import portfolio.portfolio as pf


class MyStrategyRandom(stg.Strategy):
    def __init__(self, symbols: list):
        super(MyStrategyRandom, self).__init__(symbols=symbols)
        self.__count = 0

    def execute(self, bar):
        self._bars.append(bar)
        self.__count += 1
        for symbol in self._symbols:
            if random.random() > 0.5:
                self.market_order(bar.index[-1], symbol, size=100)
            else:
                self.market_order(bar.index[-1], symbol, size=-100)


class MyStrategyMA(stg.Strategy):
    def __init__(self, symbols: list):
        super(MyStrategyMA, self).__init__(symbols=symbols)
        self.__count = 0

    def execute(self, bar):
        self._bars.append(bar)
        self.__count += 1
        if self.__count >= 10:
            for symbol in self._symbols:
                df = pd.concat(self._bars)
                dfSymbol = df.loc[df["Code"] == symbol]
                ma5 = dfSymbol.loc[:, "Close"].iloc[-6:].mean()
                ma10 = dfSymbol.loc[:, "Close"].iloc[-11:].mean()
                if ma5 < ma10:
                    self.market_order(bar.index[-1], symbol, size=100)
                else:
                    self.market_order(bar.index[-1], symbol, size=-100)


instr = ["sh.600000", "sz.000001"]
# demoStrategy = MyStrategyRandom(symbols=instr)
demoStrategy = MyStrategyMA(symbols=instr)
port = pf.Portfolio(initDatetime=dt.datetime(2019, 1, 1))
obj = main.QuantSim(symbols=instr, startDate='20190101', endDate='20200301', dividendAdjustment='Non',
                    strategy=demoStrategy, portfolio=port, freq='D')
obj.backtesting()
obj.report()
obj.analyse()
