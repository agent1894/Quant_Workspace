#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
This module fetch raw data from BaoStock and try not to manipulate any byte.
It returns pd.DataFrame only with dt.datetime as DataFrame's index.
"""
import datetime as dt
from enum import Enum
from abc import ABCMeta, abstractmethod
import pandas as pd
import baostock as bs


class DivAdjType(Enum):
    Backward = '1'
    Forward = '2'
    Non = '3'


class BaoStock(object):
    __metaclass__ = ABCMeta

    def __init__(self, symbols: list, startDate: str, endDate: str, dividend_adjustment: str):
        if not isinstance(symbols, list):
            raise TypeError("Symbols should be list type.")
        self.symbols = symbols
        self.startDate = startDate
        self.endDate = endDate
        self.dividend_adjustment = DivAdjType[dividend_adjustment].value
        lg = bs.login()
        if lg.error_code != '0':
            print("login respond error_code: ", lg.error_code)
            print("login respond error_msg: ", lg.error_msg)
            raise RuntimeError("BaoStock login failed, try to subscribe another data sources.")
        else:
            print("BaoStock data subscription succeed.")

    @abstractmethod
    def _get_k_bars(self) -> pd.DataFrame:
        raise NotImplementedError("Should implement get_k_bars()")

    @abstractmethod
    def feed_k_bars(self) -> pd.DataFrame:
        raise NotImplementedError("Should implement feed_k_bars()")


class GetDailyBars(BaoStock):
    def __init__(self, symbols: list, startDate: str, endDate: str,
                 dividend_adjustment: str = DivAdjType.Non.value):
        super(GetDailyBars, self).__init__(symbols, startDate, endDate, dividend_adjustment)

    def _get_k_bars(self) -> pd.DataFrame:
        data = []
        for symbol in self.symbols:
            rs = bs.query_history_k_data_plus(symbol,
                                              "date, code, open, high, low, close, volume, amount, adjustflag, "
                                              "tradestatus, isST",
                                              start_date=self.startDate, end_date=self.endDate, frequency='D',
                                              adjustflag=self.dividend_adjustment)
            dfResult = rs.get_data()
            dfResult = dfResult.loc[dfResult['tradestatus'] == '1']
            if not dfResult.empty:
                data.append(dfResult)
        if len(data) != 0:
            return pd.concat(data)
        else:
            raise ValueError("No sufficient data returned.")

    def feed_k_bars(self) -> pd.DataFrame:
        df = self._get_k_bars()
        df.columns = ['Datetime', 'Code', 'Open', 'High', 'Low', 'Close', 'Volume', 'Amount', 'AdjustFlag',
                      'TradeStatus', 'isST']
        df[['Open', 'High', 'Low', 'Close', 'Volume', 'Amount']] = df[
            ['Open', 'High', 'Low', 'Close', 'Volume', 'Amount']].astype('float')
        df.index = df.Datetime.astype('datetime64')
        df.drop(columns=["Datetime", "TradeStatus"], inplace=True)
        return df


class GetMinuteBars(BaoStock):
    def __init__(self, symbols: list, startDate: str, endDate: str,
                 dividend_adjustment: str = DivAdjType.Non.value,
                 freq: str = '5'):
        super(GetMinuteBars, self).__init__(symbols, startDate, endDate, dividend_adjustment)
        self.freq = freq

    def _get_k_bars(self) -> pd.DataFrame:
        data = []
        for symbol in self.symbols:
            rs = bs.query_history_k_data_plus(symbol,
                                              "date, time, code, open, high, low, close, volume, amount, adjustflag",
                                              start_date=self.startDate, end_date=self.endDate, frequency=self.freq,
                                              adjustflag=self.dividend_adjustment)
            dfResult = rs.get_data()
            if not dfResult.empty:
                data.append(dfResult)
        if len(data) != 0:
            return pd.concat(data)
        else:
            raise ValueError("No sufficient data returned.")

    def feed_k_bars(self) -> pd.DataFrame:
        df = self._get_k_bars()
        df.columns = ['Date', 'Time', 'Code', 'Open', 'High', 'Low', 'Close', 'Volume', 'Amount', 'AdjustFlag']
        df[['Open', 'High', 'Low', 'Close', 'Volume', 'Amount']] = df[
            ['Open', 'High', 'Low', 'Close', 'Volume', 'Amount']].astype('float')
        df.index = df.Time.apply(lambda x: dt.datetime.strptime(x, "%Y%m%d%H%M%S%f"))
        df.index.name = "Datetime"
        df.drop(columns=['Date', 'Time'], inplace=True)
        return df
