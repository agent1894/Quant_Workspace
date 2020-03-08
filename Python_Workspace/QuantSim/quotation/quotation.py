#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
This module simulates the exchange. It standardizes the input and try to get stock data for both simulator and broker.
"""
# TODO: TWAP/VWAP calculation
# TODO: isST list
import re
from source import *

dict_Adj = {"baostock": {'1': "", '2': "", '3': ""}, "tushare": {"qfq": "", "hfq": "", None: ""}}


class Quotation(object):
    def __init__(self, freq: str, src: str):
        self.freq = freq
        self.src = src

    def _fetch_data(self):
        pass

    def push_data(self):
        pass
