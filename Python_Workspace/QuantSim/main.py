#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
Main entrance of programme.
"""

import re
import datetime as dt
import pandas as pd
from tqdm import tqdm
import strategy.strategy as stg
import quotation.quotation as qt
import broker.broker as bk
import portfolio.portfolio as pf


class QuantSim(object):
    def __init__(self, symbols: list, startDate: str, endDate: str, dividendAdjustment: str, strategy: stg.Strategy,
                 portfolio: pf.Portfolio, freq: str = 'D', commission: float = 7e-4, slippage: float = 0.0015):
        self._strategy = strategy
        print("Strategy initialized.")
        self._portfolio = portfolio
        print("Portfolio initialized.")

        self._dividendAdjustment = dividendAdjustment
        self._commission = commission
        self._slippage = slippage
        self._freq = freq
        self._symbols = symbols if isinstance(symbols, list) else [symbols]

        def date_test(value):
            patternDate = re.compile(r"\d{4}-?\d{2}-?\d{2}")
            if patternDate.match(value) is not None:
                if len(value) == 8:
                    value = '-'.join((value[0:4], value[4:6], value[6:8]))
                date = value
                return date
            else:
                raise ValueError("Input date should be in format 'yyyymmdd' or 'yyyy-mm-dd'")

        self._startDate = date_test(startDate)
        self._endDate = date_test(endDate)

        if self._freq[0:1].upper() == 'D':
            self._quotation = qt.QuotationDailyBar(self._symbols, self._startDate, self._endDate,
                                                   self._dividendAdjustment)
            pushData = self._quotation.push_data()
        elif self._freq.startswith(("5", "15", "30", "60")):
            self._quotation = qt.QuotationMinuteBar(self._symbols, self._startDate, self._endDate,
                                                    self._dividendAdjustment, self._freq)
            pushData = self._quotation.push_data()
        else:
            raise RuntimeError("Now only support tick or 5/15/30/60 minutes or daily data.")
        print("Quotation is online.")

        self._broker = bk.Broker(symbols=self._symbols, startDate=self._startDate, endDate=self._endDate,
                                 freq=self._freq, data=pushData, commission=self._commission, slippage=self._slippage)
        print("Broker is online.")
        self._strategy.set_broker(self._broker)

    @property
    def freq(self):
        return self._freq

    @freq.setter
    def freq(self, value: str):
        self._freq = value

    @property
    def commission(self):
        return self._commission

    @commission.setter
    def commission(self, value: float):
        self._commission = value

    @property
    def slippage(self):
        return self._slippage

    @slippage.setter
    def slippage(self, value: float):
        self._slippage = value

    def backtesting(self):
        log = []
        for bar in self._quotation.push_bars():
            log.append(self._strategy.execute(bar))
        return log
        # if self._freq[0:1].upper() == "D" or bar.datetime.time() == dt.time(9, 30):
        #     self._portfolio.reset_available_sell()
        # print(transInfo)
        # self._portfolio.update_positions(transInfo)


class MyStrategy(stg.Strategy):
    def __init__(self, symbols: list):
        super(MyStrategy, self).__init__(symbols=symbols)
        # self._bars = []

    def execute(self, bar):
        if bar["Open"][-1] > bar["Close"][-1]:
            return self.market_order(bar.index[-1], bar.Code[-1], size=100)
        # self._bars.append(bar)
        # if len(df) >= 20:
        #     ma5 = df["Close"].rolling(5).mean()
        #     ma20 = df["Close"].rolling(20).mean()
        #     if ma5 > ma20:
        #         return self.market_order(size=100)
        #     else:
        #         # self.market_order(percent=-1)
        #         return self.market_order(size=-100)


if __name__ == "__main__":
    stra = MyStrategy(['sh.600000'])
    test = QuantSim(['sh.600000'], '20190101', '20190301', 'non', stra, None)
    print(test.backtesting())
