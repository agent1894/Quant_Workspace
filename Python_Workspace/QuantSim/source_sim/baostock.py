#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
This module fetch raw data from BaoStock and try not to manipulate any byte.
The raw data should be feed to other module for further processing, only pd.DataFrame is returned.
"""
from abc import ABCMeta, abstractmethod
import pandas as pd
import baostock as bs


# TODO: TWAP/VWAP price calculation. move to utility package
# TODO: provide BaoStock API for daily/N-minutes bar
# TODO: BaoStock origin data provides more K-bar data than other sources,
#  thus there should be an option for switch on/off


class BaoStock(object):
    __metaclass__ = ABCMeta

    def __init__(self, symbols: list, use_unique_fields: bool = False):
        self.symbols = symbols
        self.use_unique_fields = use_unique_fields
        lg = bs.login()
        if lg.error_msg != '0':
            print("login respond error_code: ", lg.error_code)
            print("login respond error_msg: ", lg.error_msg)
            raise RuntimeError("BaoStock login failed, try to subscribe another data sources.")
        else:
            print("BaoStock data subscription succeed.")

    @abstractmethod
    def get_k_bars(self):
        raise NotImplementedError("Should implement get_k_bars()")

    @abstractmethod
    def feed_k_bars(self):
        raise NotImplementedError("Should implement feed_k_bars()")


class GetDailyBars(BaoStock):
    def __init__(self, symbols: list, use_unique_fields: bool = False):
        super(GetDailyBars, self).__init__(symbols, use_unique_fields)

    def get_k_bars(self):
        if not self.use_unique_fields:
            for symbol in self.symbols:
                rs = bs.query_history_k_data_plus(symbol,
                                                  "date, code, open, high, low, close, preclose, volume, amount, "
                                                  "adjustflag ")

    def feed_k_bars(self):
        pass
