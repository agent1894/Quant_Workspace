#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from collections import OrderedDict
import pandas as pd
import prettytable as pt
from enum import Enum
import warnings

warnings.filterwarnings("ignore")
# TODO: for further updates, use Wind Python API for better performance
# import WindPy as wp
class InstrType(Enum):
    Stock = 1
    stock = 1
    STOCK = 1
    S = 1
    s = 1
    Bond = 2
    bond = 2
    BOND = 2
    B = 2
    b = 2


class Portfolio(object):
    def __init__(self, csv_path: str, stock_percent: float, initial_balance: float):
        self.__path = csv_path
        self._initialBalance = initial_balance
        assert (initial_balance > 0)
        self.__encoding = "utf-8"
        try:
            with open(csv_path, encoding=self.__encoding) as f:
                instr = f.readlines()[:2]
        except UnicodeDecodeError:
            self.__encoding = "gbk"
            with open(csv_path, encoding=self.__encoding) as f:
                instr = f.readlines()[:2]
        instr = [item[1:].split('\n')[0] for item in instr]
        instr = [item.split(',,,') for item in instr]
        self._instrs = dict(zip(instr[0], list(instr[1])))
        orderedInstrs = OrderedDict(zip(instr[0], instr[1]))
        # self.__tb = pt.PrettyTable()
        # self.__tb.field_names = ["InstrName", "InstrCode"]
        # for row in self._instrs.items():
        #     self.__tb.add_row(row)

        self._df = pd.read_csv(csv_path, encoding=self.__encoding, header=3)
        self._df.dropna(inplace=True, axis=1)
        self._numOfFields = self._df.shape[1] // 2
        self._df = self._df.iloc[:, [0] + [2 * x + 1 for x in range(self._numOfFields)]]
        if self._df.shape[1] - 1 == len(self._instrs):
            self._df.columns = ["Date"] + [item + "_NAV" for item in orderedInstrs.keys()]
        else:
            raise ValueError("Unmatched fields length. File gives fields: {}, DataFrame resolves fields: {}".format(
                orderedInstrs.keys(), self._df.columns))

    def set_percent(self, value: float):
        self.stockPercent = value
        self.bondPercent = 1.0 - stock_percent

    @property
    def initialBalance(self):
        return self._initialBalance

    def enter_single_percent(self, value: float):
        for instr in self._instrs.keys():
            instrPercent = float(input("Enter the percent of this instrument {} in the portfolio.".format(instr)))
            instrType = int(input("Enter the percent of this instrument {} in the portfolio.".format(instr)))
            assert (0.0 <= instrPercent <= 1.0)

    def display_instruments(self):
        pass
        # print(self.__tb)

    def _cal_accumulative_return(self):
        for instr in self._instrs.keys():
            self._df.loc[:, "{}_ret".format(instr)] = self._df.loc[:, "{}_NAV".format(instr)] / self._df.loc[
                0, "{}_NAV".format(instr)] - 1.0

    def _cal_value(self):
        for instr in self._instrs.keys():
            self._df.loc[:, "{}_value".format(instr)] = (self._df.loc[:, "{}_ret".format(instr)] + 1.0) *

    def _input_single_stock_weight(self):
        pass
