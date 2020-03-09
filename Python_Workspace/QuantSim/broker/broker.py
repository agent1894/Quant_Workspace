#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
This module simulates the broker. The broker have all historical data and calculates the TWAP/VWAP for order making.
If the broker uses the tick data, the matching of transactions should take book depth into consideration.
"""

# TODO: Calculate TWAP/VWAP

import quotation.quotation as qt


class Broker(object):
    def __init__(self, symbols: list, startDate: str, endDate: str, dividendAdjustment: str, freq: str,
                 commission: float, slipper: float):
        self.symbols = symbols
        self.startDate = startDate
        self.endDate = endDate
        self.dividendAdjustment = dividendAdjustment
        self.freq = freq
        self._commission = commission
        self._slipper = slipper
        if self.freq.capitalize()[0:1] == 'D':
            obj = qt.QuotationDailyBar(self.symbols, self.startDate, self.endDate, self.dividendAdjustment)
        elif self.freq.capitalize() == "Tick":
            obj = qt.QuotationTick(self.symbols, self.startDate, self.endDate)
        elif self.freq.capitalize() in ["5", "15", "30", "60"]:
            obj = qt.QuotationMinuteBar(self.symbols, self.startDate, self.endDate, self.dividendAdjustment, self.freq)
        else:
            raise ValueError("Now only support tick or 5/15/30/60 minutes or daily data.")
        self._baseData = obj.push_data()

    @property
    def commission(self):
        return self._commission

    @commission.setter
    def commission(self, value: float):
        self._commission = value

    @property
    def slipper(self):
        return self._slipper

    @slipper.setter
    def slipper(self, value: float):
        self._slipper = value

    def market_order(self):
        pass

    def limit_order(self):
        pass
