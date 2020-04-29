#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from math import isclose
import warnings
from enum import Enum
from collections import OrderedDict
import datetime as dt
import pandas as pd
import prettytable as pt

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


class Instrument(object):
    def __init__(self, name: str, code: str, instrType=InstrType.Stock, percent: float = 0.0):
        self.__name = name
        self.__code = code
        self.__instrType = instrType
        self._percent = percent

    @property
    def name(self):
        return self.__name

    @property
    def code(self):
        return self.__code

    @property
    def instrType(self):
        return self.__instrType

    @instrType.setter
    def instrType(self, value: str):
        self.__instrType = InstrType[value]

    @property
    def percent(self):
        return self._percent

    @percent.setter
    def percent(self, value: float):
        if 0.0 <= value <= 1.0:
            self._percent = value
        else:
            raise ValueError("The percent is illegal.")


class Portfolio(object):
    def __init__(self, csv_path: str):
        self.__path = csv_path
        self._stockPercent = float(input("Enter the percent of stocks: "))
        assert (0.0 <= self._stockPercent <= 1.0)
        self._bondPercent = 1.0 - self._stockPercent
        self._initialBalance = float(input("Enter the initial balance: "))
        assert (self._initialBalance >= 1)
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

        orderedInstrs = OrderedDict(zip(instr[0], instr[1]))  # only for dataframe headers
        print("Check the instrument codes: ")
        for key in orderedInstrs.keys():
            print("Code for instrument {} is {}".format(key, orderedInstrs[key]))

        self._df = pd.read_csv(csv_path, encoding=self.__encoding, header=3)
        self._df.dropna(inplace=True, axis=1)
        self._numOfFields = self._df.shape[1] // 2
        self._df = self._df.iloc[:, [0] + [2 * x + 1 for x in range(self._numOfFields)]]
        if self._df.shape[1] - 1 == len(orderedInstrs.keys()):
            self._df.columns = ["Date"] + [item + "_nav" for item in orderedInstrs.keys()]
            self._df.index = self._df["Date"].apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%d"))
            self._df.drop(columns='Date', inplace=True)
        else:
            raise ValueError("Unmatched fields length. File gives fields: {}, DataFrame resolves fields: {}".format(
                orderedInstrs.keys(), self._df.columns))

        self._instrs = list()
        for i in range(len(instr[0])):
            instrObj = Instrument(name=instr[0][i], code=instr[1][i])
            tempType = input("Enter the instrument {} type: ".format(instrObj.name))
            instrObj.instrType = tempType  # InstrType[tempType]
            tempPercent = float(input("Enter the percent of the instrument {}: ".format(instrObj.name)))
            instrObj.percent = tempPercent
            self._instrs.append(instrObj)

        self._check_percents()
        self.display_instruments()

    @property
    def stockPercent(self):
        return self._stockPercent

    @property
    def bondPercent(self):
        return self._bondPercent

    @property
    def initialBalance(self):
        return self._initialBalance

    def _check_percents(self):
        stockPercent = 0.0
        bondPercent = 0.0
        for instr in self._instrs:
            if instr.instrType == InstrType.Stock:
                stockPercent += instr.percent
            else:
                bondPercent += instr.percent
        if not isclose(stockPercent, self._stockPercent):
            raise ValueError(
                "The sum of stocks ({:.2%}) unequal to the given percent of stock ({:.2%}).".format(stockPercent,
                                                                                                    self._stockPercent))
        if not isclose(bondPercent, self._bondPercent):
            raise ValueError(
                "The sum of bonds ({:.2%}) unequal to the given percent of bond ({:.2%}).".format(bondPercent,
                                                                                                  self._bondPercent))

    def display_instruments(self):
        tb = pt.PrettyTable()
        tb.field_names = ["InstrName", "InstrCode", "InstrType", "InstrPercent"]
        for instr in self._instrs:
            tb.add_row([instr.name, instr.code, instr.instrType, "{:.2%}".format(instr.percent)])
        print(tb)

    def cal_pnl(self):
        for instr in self._instrs:
            self._df.loc[:, "{}_ret".format(instr.name)] = self._df.loc[:, "{}_nav".format(instr.name)] / \
                                                           self._df.iloc[0]["{}_nav".format(instr.name)] - 1.0
            self._df.loc[:, "{}_value".format(instr.name)] = instr.percent * self._initialBalance * (
                        self._df.loc[:, "{}_nav".format(instr.name)] / self._df.iloc[0]["{}_nav".format(instr.name)])
        valueColumns = [item for item in self._df.columns if item.endswith('value')]
        returnColumns = [item for item in self._df.columns if item.endswith('ret')]
        self._df.loc[:, "ValuePnL"] = self._df.loc[:, valueColumns].sum(axis=1)
        self._df.loc[:, "retPnL"] = self._df.loc[:, returnColumns].sum(axis=1)

    def adjust_percent(self, instr):
        pass

    def plot(self):
        pass

    def cal_drawdown(self):
        pass
