#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
This module simulates the broker. The broker have all historical data and calculates the TWAP/VWAP for order making.
If the broker uses the tick data, the matching of transactions should take book depth into consideration.
"""

# TODO: Consider market order or limit order.
# TODO: Calculate TWAP/VWAP

class Broker(object):
    def __init__(self):
        pass

    def _fetch_data(self):
        pass

    def long(self):
        pass

    def short(self):
        pass
