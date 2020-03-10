#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
This module simulates the exchange. It standardizes the input and try to get stock data for both simulator and broker.
"""
import re
import datetime as dt
from abc import ABCMeta, abstractmethod
from copy import deepcopy
import pandas as pd
import source.baoStock as sbs


class TradingDatetime(object):
    def __init__(self, startDate: str, endDate: str, freq: str):
        self._startDate = startDate
        self._endDate = endDate
        self._freq = freq

    def trade_datetimes(self) -> list:
        dates = pd.date_range(start=self._startDate, end=self._endDate, freq=self._freq)
        dates = [date for date in dates if date.weekday() not in (5, 6)]
        if self._freq.capitalize()[0:1] == 'D':
            dates.sort()
            return dates
        else:
            dates = [date for date in dates if
                     dt.time(9, 30) < date.time() <= dt.time(11, 30) or dt.time(13, 0) < date.time() <= dt.time(15, 0)]
            dates.sort()
            return dates


class Quotation(object):
    __metaclass__ = ABCMeta

    def __init__(self, startDate: str, endDate: str):
        patternDate = re.compile(r"\d{4}-?\d{2}-?\d{2}")
        if patternDate.match(startDate) is not None and patternDate.match(endDate) is not None:
            if len(startDate) == 8:
                startDate = '-'.join((startDate[0:4], startDate[4:6], startDate[6:8]))
            if len(endDate) == 8:
                endDate = '-'.join((endDate[0:4], endDate[4:6], endDate[6:8]))
            self.startDate = startDate
            self.endDate = endDate
        else:
            raise ValueError("Input date should be in format 'yyyymmdd' or 'yyyy-mm-dd'")

    @abstractmethod
    def push_bars(self) -> pd.DataFrame:
        raise NotImplementedError("Should implement push_bars()")

    @abstractmethod
    def push_data(self) -> pd.DataFrame:
        raise NotImplementedError("Should implement push_data()")


class QuotationDailyBar(Quotation):
    def __init__(self, symbols, startDate: str, endDate: str, dividendAdjustment: str):
        super(QuotationDailyBar, self).__init__(startDate=startDate, endDate=endDate)
        self.symbols = symbols if isinstance(symbols, list) else [symbols]
        patternSymbols = re.compile(r"s[hz]\.\d{6}")
        for match in map(lambda sym: patternSymbols.match(sym), self.symbols):
            if match is None:
                raise ValueError("All input _symbols should be in format 'sh.600000'")
        self.dividend_adjustment = dividendAdjustment.capitalize()
        obj = sbs.GetDailyBars(self.symbols, self.startDate, self.endDate, self.dividend_adjustment)
        self.baseData = obj.feed_k_bars()
        self.tradings = TradingDatetime(startDate=self.startDate, endDate=self.endDate, freq='D').trade_datetimes()

    def push_bars(self) -> pd.DataFrame:
        for datetime in self.tradings:
            try:
                yield self.baseData.loc[datetime, :]
            except KeyError:
                print("Datetime: {} do not have valid bars.".format(datetime.strftime("%Y-%m-%d")))
                yield pd.DataFrame()

    def push_data(self) -> pd.DataFrame:
        return deepcopy(self.baseData)


class QuotationMinuteBar(Quotation):
    def __init__(self, symbols, startDate: str, endDate: str, dividendAdjustment: str, freq: str):
        super(QuotationMinuteBar, self).__init__(startDate=startDate, endDate=endDate)
        self.symbols = symbols if isinstance(symbols, list) else [symbols]
        patternSymbols = re.compile(r"s[hz]\.\d{6}")
        for match in map(lambda sym: patternSymbols.match(sym), self.symbols):
            if match is None:
                raise ValueError("All input _symbols should be in format 'sh.600000'")
        self.dividend_adjustment = dividendAdjustment.capitalize()
        if not freq.startswith(('5', '15', '30', '60')):
            raise TypeError("Now only support 5/15/30/60 minutes bars.")
        obj = sbs.GetMinuteBars(self.symbols, self.startDate, self.endDate, self.dividend_adjustment, freq)
        self.baseData = obj.feed_k_bars()
        self.tradings = TradingDatetime(startDate=self.startDate, endDate=self.endDate,
                                        freq=freq[0:1] + 'T').trade_datetimes()

    def push_bars(self) -> pd.DataFrame:
        for datetime in self.tradings:
            try:
                yield self.baseData.loc[datetime, :]
            except KeyError:
                print("Datetime: {} do not have valid bars.".format(datetime.strftime("%Y-%m-%d %H:%M:%S")))
                yield pd.DataFrame()

    def push_data(self) -> pd.DataFrame:
        return deepcopy(self.baseData)


class QuotationTick(Quotation):
    def __init__(self, symbols, startDate: str, endDate: str):
        super(QuotationTick, self).__init__(startDate=startDate, endDate=endDate)
        self.symbols = symbols

    def push_bars(self) -> pd.DataFrame:
        pass

    def push_data(self) -> pd.DataFrame:
        pass