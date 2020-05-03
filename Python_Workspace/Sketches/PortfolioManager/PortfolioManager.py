#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""Portfolio manager
This project works for a friend works in ZOFund.

With given funds' net asset value and initial investment,
this project will calculate the PnL and drawdowns for given portfolio positions.

In future, this project should be compatible with Wind API.
"""

from math import isclose
import warnings
from enum import Enum
from collections import OrderedDict
import datetime as dt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
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
    """Define instrument class for portfolio

    When the portfolio has to change the positions of the instruments in it,
    giving these instruments an abstract class may improved the performance.

    Attributes:
        name (Chinese): string, for users output and display.
        code: string, which corresponds to the instrument, usually for double check.
        instrType: InstrType, most of the time, the portfolio is constructed from some stocks and bonds funds.
            this attribute can help check the corresponding type.
        percnet: float, define the percentage of the instrument in the portfolio.
    """
    def __init__(self, name: str, code: str, instrType=InstrType.Stock, percent: float = 0.0):
        """The default constructor for Instrument gives the Stock type and 0% percent."""
        self.__name = name
        self.__code = code
        self.__type = instrType
        self._percent = percent

    @property
    def name(self):
        return self.__name

    @property
    def code(self):
        return self.__code

    @property
    def instrType(self):
        return self.__type

    @instrType.setter
    def instrType(self, value: str):
        self.__type = InstrType[value]

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
        self._stockPercent = 0.0
        self._bondPercent = 0.0
        self._initialBalance = float(input("Enter the initial balance: "))
        assert (self._initialBalance >= 1)
        self._alarmThreshold = 0.0
        self._recoveryThreshold = 0.0
        self._recoveryThresholdInterval = 0
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
        print("*" * 10 + "Check the instrument codes: " + "*" * 10)
        for key in orderedInstrs.keys():
            print("Code for instrument {} is {}".format(key, orderedInstrs[key]))
        print("*" * 48)

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
            self._instrs.append(instrObj)

    def set_percent(self):
        self._stockPercent = float(input("Enter the percent of stocks: "))
        assert (0.0 <= self._stockPercent <= 1.0)
        self._bondPercent = 1.0 - self._stockPercent
        for instr in self._instrs:
            tempPercent = float(input("Enter the percent of the instrument {}: ".format(instr.name)))
            instr.percent = tempPercent
        self._check_percents()
        self._display_instruments()

    # TODO: add methods for defining thresholds
    def set_parameters(self):
        pass

    @property
    def stockPercent(self):
        return self._stockPercent

    @stockPercent.setter
    def stockPercent(self, value: float):
        assert (0.0 <= value <= 1.0)
        self._stockPercent = value
        self._bondPercent = 1.0 - self._stockPercent

    @property
    def bondPercent(self):
        return self._bondPercent

    @bondPercent.setter
    def bondPercent(self, value: float):
        assert (0.0 <= value <= 1.0)
        self._bondPercent = value
        self._stockPercent = 1.0 - self._bondPercent

    @property
    def initialBalance(self):
        return self._initialBalance

    @property
    def alarmThreshold(self):
        return self._alarmThreshold

    @alarmThreshold.setter
    def alarmThreshold(self, value: float):
        self._alarmThreshold = value

    @property
    def recoveryThreshold(self):
        return self._recoveryThreshold

    @recoveryThreshold.setter
    def recoveryThreshold(self, value: float):
        self._recoveryThreshold = value

    @property
    def recoveryThresholdInterval(self):
        return self._recoveryThresholdInterval

    @recoveryThresholdInterval.setter
    def recoveryThresholdInterval(self, value: int):
        self._recoveryThresholdInterval = value

    def _check_percents(self):
        stockPercent = 0.0
        bondPercent = 0.0
        for instr in self._instrs:
            if instr.instrType == InstrType.Stock:
                stockPercent += instr.percent
            else:
                bondPercent += instr.percent
        if not isclose(stockPercent, self._stockPercent):
            raise ValueError("The sum of stocks ({:.2%}) unequal to the given percent of stock ({:.2%}).".format(
                stockPercent, self._stockPercent))
        if not isclose(bondPercent, self._bondPercent):
            raise ValueError("The sum of bonds ({:.2%}) unequal to the given percent of bond ({:.2%}).".format(
                bondPercent, self._bondPercent))

    def _display_instruments(self):
        tb = pt.PrettyTable()
        tb.field_names = ["InstrName", "InstrCode", "InstrType", "InstrPercent"]
        for instr in self._instrs:
            tb.add_row([instr.name, instr.code, instr.instrType, "{:.2%}".format(instr.percent)])
        print(tb)

    def _display_parameters(self):
        tb = pt.PrettyTable()
        tb.field_names = ["Parameter", "Value"]
        tb.add_row(["Stock Percent", "{:.2%}".format(self._stockPercent)])
        tb.add_row(["Bond Percent", "{:.2%}".format(self._bondPercent)])
        tb.add_row(["Initial Balance", "${:.0f}".format(self._initialBalance)])
        tb.add_row(["Alarm Threshold Percent", "{:.2%}".format(self._alarmThreshold)])
        tb.add_row(["Recovery Threshold Percent", "{:.2%}".format(self._recoveryThreshold)])
        tb.add_row(["Recovery Threshold Time Interval", "{:.0f} days".format(self._recoveryThresholdInterval)])
        print(tb)

    @staticmethod
    def plot(series: pd.Series, begIndex: int = None, endIndex: int = None):
        plt.plot(series[begIndex:endIndex])

    @staticmethod
    def cal_max_drawdown(series: pd.Series) -> (dt.datetime, dt.datetime, float):
        """Reference: https://blog.csdn.net/tz_zs/article/details/80335238"""
        endIndex = np.argmax(np.maximum.accumulate(series) - series)
        begIndex = np.argmax(series[:endIndex])
        maxDrawdown = series[begIndex] - series[endIndex]
        return begIndex, endIndex, maxDrawdown

    def _alarm_drawdown_index(self, series: pd.Series) -> dt.datetime:
        index = series[(np.maximum.accumulate(series) - series) >= self._alarmThreshold].index[0]
        return index

    def update_pnl(self, idx: dt.datetime = None) -> pd.DataFrame:
        if idx is None:
            balance = self._initialBalance
            for instr in self._instrs:
                self._df.loc[:, "{}_ret".format(instr.name)] = self._df.loc[:, "{}_nav".format(instr.name)] / \
                                                            self._df.iloc[0]["{}_nav".format(instr.name)] - 1.0
                self._df.loc[:, "{}_value".format(instr.name)] = balance * instr.percent * (
                    self._df.loc[:, "{}_ret".format(instr.name)] + 1.0)
                # (
                #     df.loc[:, "{}_nav".format(instr.name)] / df.iloc[0]["{}_nav".format(instr.name)])
        else:
            prevIdx = self._df.index[np.argwhere(self._df.index == idx) - 1][0]
            balance = self._df.loc[prevIdx, "PnL"].sum()
            for instr in self._instrs:
                self._df.loc[idx:, "{}_ret".format(instr.name)] = self._df.loc[
                    idx:, "{}_nav".format(instr.name)] / self._df.loc[idx]["{}_nav".format(instr.name)] - 1.0
                self._df.loc[idx:, "{}_value".format(instr.name)] = balance * instr.percent * (
                    self._df.loc[:, "{}_ret".format(instr.name)] + 1.0)
                # = balance * instr.percent * (
                #     df.loc[:, "{}_nav".format(instr.name)] / df.iloc[0]["{}_nav".format(instr.name)])
        self._df.loc[:, "PnL"] = self._df.loc[:,
                                              [item for item in self._df.columns if item.endswith('value')]].sum(axis=1)
        self._df.loc[:, "TotRet"] = self._df.loc[:, "PnL"] / self._initialBalance - 1.0
        return self._df.PnL, self._df.TotRet


if __name__ == "__main__":
    pass
