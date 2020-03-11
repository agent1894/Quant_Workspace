#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
Main entrance of programme.
"""


def main(symbols):
    symbols = symbols if isinstance(symbols, list) else [symbols]
    print("Total {} stocks are under subscription".format(len(symbols)))
