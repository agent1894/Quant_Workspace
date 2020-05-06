#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""Portfolio manager
This project works for a friend works in ZOFund.

With given funds' net asset value and initial investment,
this project will calculate the PnL and drawdowns for given portfolio positions.

In future, this project should be compatible with Wind API.
"""

import os
from math import isclose
from copy import deepcopy
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
    def __init__(self, name: str, code: str, instrType=InstrType.Stock, percent: float = 0.0):
        """Define instrument class for portfolio.

        When the portfolio has to change the positions of the instruments in it,
        giving these instruments an abstract class may improved the performance.
        The default constructor for Instrument gives the Stock type and 0% percent.

        :param name: Chinese, for users output and display.
        :type name: str
        :param code: which corresponds to the instrument, usually for double check.
        :type code: str
        :param instrType: InstrType, most of the time, the portfolio is constructed from some stocks and bonds funds.
        :type instrType: InstrType
        :param percent: define the percentage of the instrument in the portfolio.
        :type percent: float
        """
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
        """To initialize the portfolio class, the raw data must be given.

        In future, the data should be fetched by Wind Python API, which can improve the performance.

        :param csv_path: the full absolute path of raw data.
        :type csv_path: str
        """
        self.__path = csv_path
        self._stockPercent = 0.0
        self._bondPercent = 0.0
        self._initialBalance = float(input("Enter the initial balance: "))
        assert (self._initialBalance >= 1)
        self._alarmThreshold = 0.0
        self._recoveryThreshold = 0.0
        self._recoveryThresholdInterval = 0
        self.__encoding = "utf-8"

        # Read .csv files from Wind and keep the instruments and fields.
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

        # Basic manipulation of compulsory data.
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

        # Save all instruments for further uses.
        self._instrs = list()
        for i in range(len(instr[0])):
            instrObj = Instrument(name=instr[0][i], code=instr[1][i])
            tempType = input("Enter the instrument {} type (Stock or Bond): ".format(instrObj.name))
            instrObj.instrType = tempType  # InstrType[tempType]
            self._instrs.append(instrObj)

        self.set_percent()
        self._set_parameters()

    def set_percent(self) -> None:
        """Set percent for all instruments.

        This method is called firstly in __init__ method, after that, this method should be called
        for each time the instruments' percent is changed.

        :return: None
        :rtype: None
        """
        print("*" * 5, "Setting the percent", "*" * 5)
        self._stockPercent = float(input("Enter the percent of stocks: "))
        assert (0.0 <= self._stockPercent <= 1.0)
        self._bondPercent = 1.0 - self._stockPercent
        for instr in self._instrs:
            tempPercent = float(input("Enter the percent of the instrument {}: ".format(instr.name)))
            instr.percent = tempPercent
        self._check_percents()
        self.display_instruments()

    def _set_parameters(self) -> None:
        """Set parameters for the portfolio.

        This method is called firstly in __init__ method. It defines the alarm threshold, recovery threshold and
        recovery interval threshold. Generally, this function should not be called again.

        :return: None
        :rtype: None
        """
        self._alarmThreshold = float(input("Enter the alarm threshold: "))
        assert (0.0 <= self._alarmThreshold <= 1.0)
        self._recoveryThreshold = float(input("Enter the recovery threshold: "))
        assert (0.0 <= self._recoveryThreshold <= 1.0)
        self._recoveryThresholdInterval = int(input("Enter the recovery threshold interval: "))
        assert (isinstance(self._recoveryThresholdInterval, int))
        self.display_parameters()

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

    def _check_percents(self) -> None:
        """Check the sum of percents inputted for each instrument is equal to the general percents in the parameter.

        :return: None
        :rtype: None
        """
        stockPercent = 0.0
        bondPercent = 0.0
        for instr in self._instrs:
            if instr.instrType == InstrType.Stock:
                stockPercent += instr.percent
            else:
                bondPercent += instr.percent

        # use np.isclose to avoid float precises calculation problem
        if not isclose(stockPercent, self._stockPercent):
            raise ValueError("The sum of stocks ({:.2%}) unequal to the given percent of stock ({:.2%}).".format(
                stockPercent, self._stockPercent))
        if not isclose(bondPercent, self._bondPercent):
            raise ValueError("The sum of bonds ({:.2%}) unequal to the given percent of bond ({:.2%}).".format(
                bondPercent, self._bondPercent))

    def display_instruments(self) -> None:
        """Display instruments information.

        Example:
        +---------------+-----------+-----------------+--------------+
        |   InstrName   | InstrCode |    InstrType    | InstrPercent |
        +---------------+-----------+-----------------+--------------+
        |  中欧新蓝筹A  | 166002.OF | InstrType.Stock |    15.00%    |
        | 中欧消费主题A | 002621.OF | InstrType.Stock |    10.00%    |
        |    中欧成长   | 166006.OF | InstrType.Stock |    15.00%    |
        | 中欧医疗健康A | 003095.OF | InstrType.Stock |    30.00%    |
        |    中欧强债   | 166008.SZ |  InstrType.Bond |    30.00%    |
        +---------------+-----------+-----------------+--------------+

        :return: None
        :rtype: None
        """
        tb = pt.PrettyTable()
        tb.field_names = ["InstrName", "InstrCode", "InstrType", "InstrPercent"]
        for instr in self._instrs:
            tb.add_row([instr.name, instr.code, instr.instrType, "{:.2%}".format(instr.percent)])
        print(tb)

    def display_parameters(self) -> None:
        """Display portfolio information.

        Example:
        +----------------------------------+----------+
        |            Parameter             |  Value   |
        +----------------------------------+----------+
        |          Stock Percent           |  70.00%  |
        |           Bond Percent           |  30.00%  |
        |         Initial Balance          | $1000000 |
        |     Alarm Threshold Percent      |  15.00%  |
        |    Recovery Threshold Percent    |  8.00%   |
        | Recovery Threshold Time Interval | 90 days  |
        +----------------------------------+----------+

        :return: None
        :rtype: None
        """
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
    def plot(series: pd.Series, begIndex: dt.datetime = None, endIndex: dt.datetime = None, label: str = None) -> None:
        """With given time series data with dt.datetime index, plot corresponding curves.

        A static method.

        :param series: time series data with dt.datetime index
        :type series: pd.Series
        :param begIndex: the start point for part of data if exists
        :type begIndex: dt.datetime
        :param endIndex: the end point for part of data if exists
        :type endIndex: dt.datetime
        :param label: label for the curve
        :type label: str
        :return: None
        :rtype: None
        """
        plt.plot(series[begIndex:endIndex], label=label)

    @staticmethod
    def cal_max_drawdown(series: pd.Series) -> (dt.datetime, dt.datetime, float):
        """Calculate max drawdown in given pd.Series.

        A static method.
        Calculate max drawdown in the whole time series, to evaluate the performance of the portfolio.
        Reference: https://blog.csdn.net/tz_zs/article/details/80335238

        :param series: time series data with dt.datetime index
        :type series: pd.Series
        :return: begIndex: the start index of the drawdown,
                endIndex: the end index of the drawdown,
                maxDrawdown: the calculation of the max drawdown
        :rtype: dt.datetime, dt.datetime, float
        """
        endIndex = np.argmax(np.maximum.accumulate(series) - series)
        begIndex = np.argmax(series[:endIndex])
        maxDrawdown = series[begIndex] - series[endIndex]
        return begIndex, endIndex, maxDrawdown

    def alarm_drawdown_index(self, series: pd.Series, index: dt.datetime = None):
        """Find out the index when the pnl reaches the alarm threshold of the portfolio and need to cut the positions.

        If the portfolio will not reach the alarm drawdown threshold any more, this method returns False.

        :param series: time series data with dt.datetime index
        :type series: pd.Series
        :param index: if the portfolio has been recovered, the alarm drawdown should be re-calculated
        :type index: dt.datetime
        :return: a time index for given pd.Series, current drawdown before the changing day
        :rtype: dt.datetime if index exists else False, float if index exists else False
        """
        temp = series.loc[index:]
        tempSeries = temp[(np.maximum.accumulate(temp) - temp) >= self._alarmThreshold]
        try:
            tempIndex = tempSeries.index[0]
            tempPrevIndex = temp.index[np.argwhere(temp.index == tempIndex) - 1][0]
            return tempIndex, (np.maximum.accumulate(temp) - temp)[tempPrevIndex][0]
        except IndexError:
            print("The portfolio will not reach the alarm drawdown threshold any more.")
            return False, False

    def recovery_index(self, series: pd.Series, index: dt.datetime):
        """Find out when the portfolio can recovered to the previous positions.

        Only when the portfolio has been cut off, this function should be called, and the index param is compulsory.
        If the portfolio will not reach the recovery threshold any more, this method returns False.

        :param series: time series data with dt.datetime index
        :type series: pd.Series
        :param index: the start time to calculate the recovery period
        :type index: dt.datetime
        :return: a time index for given pd.Series
        :rtype: dt.datetime if index exists else False
        """
        temp = series.loc[index:]
        tempSeries = temp[(temp > temp.iloc[0] + self._recoveryThreshold) & (
                temp.index >= index + dt.timedelta(days=self._recoveryThresholdInterval))]
        try:
            tempIndex = tempSeries.index[0]
            return tempIndex, (temp[tempIndex] - temp.iloc[0])
        except IndexError:
            print("The portfolio will not reach the recovery threshold any more.")
            return False, False

    def update_pnl(self, index: dt.datetime = None) -> (pd.Series, pd.Series):
        """Calculate the profit and loss for given data.

        This method should be called firstly to calculate plain pnl without any position change.
        After that, for each time the basic parameters changes, this function should be called again with given index.

        :param index: when the positions should be changed, the start time index
        :type index: dt.datetime
        :return: deep copy of two pnl series
        :rtype: pd.Series, pd.Series
        """
        if index is None:
            balance = self._initialBalance
            for instr in self._instrs:
                self._df.loc[:, "{}_ret".format(instr.name)] = self._df.loc[:, "{}_nav".format(instr.name)] / \
                                                               self._df.iloc[0]["{}_nav".format(instr.name)] - 1.0
                self._df.loc[:, "{}_value".format(instr.name)] = balance * instr.percent * (
                        self._df.loc[:, "{}_ret".format(instr.name)] + 1.0)
        else:
            # TODO: The use of prevIdx may include future function
            prevIdx = self._df.index[np.argwhere(self._df.index == index) - 1][0]
            balance = self._df.loc[prevIdx, "PnL"].values[
                0]  # Note: without .values[0], it will return a pd.Series and cause error
            for instr in self._instrs:
                self._df.loc[index:, "{}_ret".format(instr.name)] = self._df.loc[index:, "{}_nav".format(
                    instr.name)] / self._df.loc[index]["{}_nav".format(instr.name)] - 1.0
                self._df.loc[index:, "{}_value".format(instr.name)] = balance * instr.percent * (
                        self._df.loc[index:, "{}_ret".format(instr.name)] + 1.0)
        self._df.loc[:, "PnL"] = self._df.loc[:, [item for item in self._df.columns if item.endswith('value')]].sum(
            axis=1)
        self._df.loc[:, "TotRet"] = self._df.loc[:, "PnL"] / self._initialBalance - 1.0
        return deepcopy(self._df.PnL), deepcopy(self._df.TotRet)

    def analysis(self) -> None:
        """Generate analysis of portfolio management.

        This method only works for the final version of the portfolio (after all position changes).

        :return: None
        :rtype: None
        """
        series = self._df.TotRet
        tb = pt.PrettyTable()
        tb.field_names = ["Indicator", "Result"]
        totReturn = series[-1]
        holdingTradingPeriod = len(series)
        annualReturn = totReturn / holdingTradingPeriod * 244.0
        holdingPeriod = (series.index[-1] - series.index[0]).days
        begIndex, endIndex, maxDrawdown = obj.cal_max_drawdown(series)
        tb.add_row(["Total Holding Period", "{:.0f}".format(holdingPeriod)])
        tb.add_row(["Total Trading Days", "{:.0f}".format(holdingTradingPeriod)])
        tb.add_row(["Accumulative Rate of Return", "{:.2%}".format(totReturn)])
        tb.add_row(["Annually Rate of Return", "{:.2%}".format(annualReturn)])
        tb.add_row(["Max Drawdown", "{:.2%}".format(maxDrawdown)])
        tb.add_row(["Drawdown Start Time", "{}".format(begIndex.strftime("%Y-%m-%d"))])
        tb.add_row(["Drawdown End Time", "{}".format(endIndex.strftime("%Y-%m-%d"))])
        print(tb)


if __name__ == "__main__":
    path = input("Enter the path of raw data: ")
    assert os.path.isfile(path)
    obj = Portfolio(path)
    pnl, ret = obj.update_pnl()
    plt.figure(figsize=(18, 10))
    plt.title("Portfolio Manager")
    obj.plot(pnl, label="Naive Portfolio")
    begIndexOrigin, endIndexOrigin, maxDrawdownOrigin = obj.cal_max_drawdown(ret)
    print("Naive Portfolio Max Drawdown: {:.2%}".format(maxDrawdownOrigin))
    obj.plot(pnl, begIndexOrigin, endIndexOrigin, "Naive Drawdown")
    table = pt.PrettyTable()
    table.field_names = ["Datetime", "Stock Positions", "Bond Positions", "Scenario"]
    table.add_row(
        [ret.index[0].strftime("%Y-%m-%d"), "{:.2%}".format(obj.stockPercent), "{:.2%}".format(obj.bondPercent),
         "Initialization"])
    simulation = bool(int(input("Simulation? (1 for Yes, 0 for No): ")))
    if simulation:
        restartIndex = None
        while simulation:
            # start from cutting down
            restartIndex, drawdown = obj.alarm_drawdown_index(ret, restartIndex)
            if restartIndex:
                print("-" * 5, "Cutting Down", "-" * 5)
                obj.set_percent()
                pnl, ret = obj.update_pnl(restartIndex)
                table.add_row(
                    [restartIndex.strftime("%Y-%m-%d"), "{:.2%}".format(obj.stockPercent), "{:.2%}".format(obj.bondPercent),
                     "Reach alarm drawdown threshold. The drawdown rate is {:.2%}".format(drawdown)])
            else:
                break
            restartIndex, recovery = obj.recovery_index(ret, restartIndex)
            # recovery is paired with cutting down, if any one of both is invalid, the WHILE loop ends.
            if restartIndex:
                print("-" * 5, "Recovery", "-" * 5)
                obj.set_percent()
                pnl, ret = obj.update_pnl(restartIndex)
                table.add_row(
                    [restartIndex.strftime("%Y-%m-%d"), "{:.2%}".format(obj.stockPercent), "{:.2%}".format(obj.bondPercent),
                     "Reach recovery threshold. The recovery rate is {:.2%}".format(recovery)])
            else:
                break
        obj.plot(pnl, label="Updated Portfolio")
        begIndexFinal, endIndexFinal, maxDrawdownFinal = obj.cal_max_drawdown(ret)
        obj.plot(pnl, begIndexFinal, endIndexFinal, "Updated Drawdown")
        plt.annotate("Drawdown starts", xy=(begIndexFinal, pnl[begIndexFinal]),
                     xytext=(begIndexFinal, pnl[begIndexFinal] + 200000.0),
                     arrowprops=dict(arrowstyle='->'))
        plt.annotate("Drawdown ends", xy=(endIndexFinal, pnl[endIndexFinal]),
                     xytext=(endIndexFinal - 100.0, pnl[endIndexFinal] - 200000.0),
                     arrowprops=dict(arrowstyle='->'))
        print("*" * 50, "Final Result", "*" * 50)
        print("Naive Portfolio Max Drawdown: {:.2%}".format(maxDrawdownOrigin))
        print("Updated Portfolio Max Drawdown: {:.2%}".format(maxDrawdownFinal))

    print(table)
    obj.analysis()
    plt.legend(loc="best")
    saveFig = bool(int(input("Save the figure? (1 for Yes, 0 for No): ")))
    if saveFig:
        figName = input("Enter the figure name: ")
        plt.savefig("{}.png".format(figName))
    plt.show()
