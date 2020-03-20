#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import datetime as dt
import pandas as pd
import main
import strategy.strategy as stg
import portfolio.portfolio as pf
import random


class MyStrategy(stg.Strategy):
    def __init__(self, symbols: list):
        super(MyStrategy, self).__init__(symbols=symbols)
        self.__count = 0

    def execute(self, bar):
        self._bars.append(bar)
        self.__count += 1
        df = pd.concat(self._bars)
        if self.__count >= 20:
            for symbol in self._symbols:
                # dfSymbol = df.loc[df["Code"] == symbol]
                # ma5 = dfSymbol.loc[:, "Close"].iloc[-6:-1].mean()
                # ma20 = dfSymbol.loc[:, "Close"].iloc[-21:-1].mean()
                # if ma5 > ma20:
                #     self.market_order(bar.index[-1], symbol, size=100)
                # else:
                #     self.market_order(bar.index[-1], symbol, size=-100)
                if random.random() > 0.5:
                    self.market_order(bar.index[-1], symbol, size=100)
                else:
                    self.market_order(bar.index[-1], symbol, size=-100)


instr = ["sh.600000", "sz.000001"]
strtgy = MyStrategy(symbols=instr)
port = pf.Portfolio(initDatetime=dt.datetime(2019, 1, 1))
obj = main.QuantSim(symbols=instr, startDate='20190101', endDate='20190301', dividendAdjustment='Forward',
                    strategy=strtgy, portfolio=port, freq='D')
print(obj.backtesting())
