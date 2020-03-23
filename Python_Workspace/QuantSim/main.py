#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
Main entrance of programme.
"""

import re
import datetime as dt
from tqdm import tqdm
import prettytable
import strategy.strategy as stg
import quotation.quotation as qt
import broker.broker as bk
import portfolio.portfolio as pf
import utility.pnl as pnl


class QuantSim(object):
    def __init__(self, symbols: list, startDate: str, endDate: str, dividendAdjustment: str, strategy: stg.Strategy,
                 portfolio: pf.Portfolio, freq: str = 'D', commission: float = 7e-4, slippage: float = 0.0015):
        self._strategy = strategy
        print("Strategy initialized.")
        self._portfolio = portfolio
        print("Portfolio initialized.")
        self.__initialValue = self._portfolio.check_value()

        self._dividendAdjustment = dividendAdjustment
        self._commission = commission
        self._slippage = slippage
        self._freq = freq
        self._symbols = symbols if isinstance(symbols, list) else [symbols]

        def date_test(value):
            patternDate = re.compile(r"\d{4}-?\d{2}-?\d{2}")
            if patternDate.match(value) is not None:
                if len(value) == 8:
                    value = '-'.join((value[0:4], value[4:6], value[6:8]))
                date = value
                return date
            else:
                raise ValueError("Input date should be in format 'yyyymmdd' or 'yyyy-mm-dd'")

        self._startDate = date_test(startDate)
        self._endDate = date_test(endDate)

        if self._freq[0:1].upper() == 'D':
            self._quotation = qt.QuotationDailyBar(self._symbols, self._startDate, self._endDate,
                                                   self._dividendAdjustment)
            pushData = self._quotation.push_data()
        elif self._freq.startswith(("5", "15", "30", "60")):
            self._quotation = qt.QuotationMinuteBar(self._symbols, self._startDate, self._endDate,
                                                    self._dividendAdjustment, self._freq)
            pushData = self._quotation.push_data()
        else:
            raise RuntimeError("Now only support tick or 5/15/30/60 minutes or daily data.")
        print("Quotation is online.")

        self._broker = bk.Broker(symbols=self._symbols, startDate=self._startDate, endDate=self._endDate,
                                 freq=self._freq, data=pushData, commission=self._commission, slippage=self._slippage)
        print("Broker is online.")
        self._strategy.set_broker(self._broker)
        self._strategy.set_portfolio(self._portfolio)
        self.__pnl = []

    @property
    def freq(self):
        return self._freq

    @freq.setter
    def freq(self, value: str):
        self._freq = value

    @property
    def commission(self):
        return self._commission

    @commission.setter
    def commission(self, value: float):
        self._commission = value

    @property
    def slippage(self):
        return self._slippage

    @slippage.setter
    def slippage(self, value: float):
        self._slippage = value

    def backtesting(self):
        for bar in tqdm(self._quotation.push_bars(), total=len(self._quotation.push_data())):
            self._portfolio.check_positions()
            if self._freq[0:1].upper() == "D" or bar.datetime.time() == dt.time(9, 30):
                self._portfolio.reset_available_sell()
            self._strategy.execute(bar)
            self.__pnl.append(self._portfolio.check_value())

    def report(self):
        totalPosition = self._portfolio.positions
        strategyReport = self._strategy.report()
        portfolioReport = self._portfolio.report()

        strategyTable = prettytable.PrettyTable()
        strategyTable.field_names = ["Order ID", "Order Time", "Symbol", "Order Type", "Commission Fee", "Order Price",
                                     "Order Status", "Order Size"]
        for data in strategyReport:
            strategyTable.add_row(
                [data["Order ID"], data["Order Time"], data["Symbol"], data["Order Type"], data["Commission Fee"],
                 data["Order Price"], data["Order Status"], data["Order Size"]])

        portfolioTable = prettytable.PrettyTable()
        portfolioTable.field_names = ["Symbol", "Status", "Current Position", "Cash Change"]
        tempPortfolioReport = [portfolioReport[i:i + 2] for i in range(0, len(portfolioReport), 2)]
        for data in tempPortfolioReport:
            symbol = data[0].split(':')[0]
            status = data[0].split(':')[1].split('.')[0]
            status = status if "cancelled" in status else "Transaction succeed."
            position = data[0].split('.')[1].split(' ')[-1]
            change = data[1].split(':')[-1]
            portfolioTable.add_row([symbol, status, position, change])

        totalTable = prettytable.PrettyTable()
        totalTable.field_names = ["Instrument", "Position", "Order Costs", "Value"]
        totalTable.add_row(["Cash", totalPosition["Cash"], 0, totalPosition["Cash"]])
        stocks = totalPosition["Stock"]
        for key in stocks.keys():
            position = stocks[key][0]
            cost = stocks[key][1]
            value = stocks[key][0] * stocks[key][2]
            totalTable.add_row([key, position, cost, "{:.2f}".format(value)])

        print("Total Portfolio positions at the end of backtesting: ")
        print(totalTable)
        print("The strategy gives orders: ")
        print(strategyTable)
        print("The executions: ")
        print(portfolioTable)

    def analyse(self):
        pnlTable = prettytable.PrettyTable()
        pnlTable.field_names = ["Field", "Data"]
        pnlTable.add_row(['Start', self._startDate])
        pnlTable.add_row(['End', self._endDate])
        pnlTable.add_row(['Initial Balance', self.__initialValue])
        pnlTable.add_row(['End Balance', self._portfolio.check_value()])
        pnlTable.add_row(['Total Return', "{:.2%}".format(self._portfolio.check_value() / self.__initialValue - 1)])
        pnlTable.add_row(['Total PnL', self._portfolio.check_value() - self.__initialValue])
        pnlTable.add_row(['Net Return', "{:.2%}".format(
            (self._portfolio.check_value() - self._portfolio.fees) / self.__initialValue - 1)])
        pnlTable.add_row(['Net PnL', self._portfolio.check_value() - self.__initialValue - self._portfolio.fees])
        profit = pnl.PeriodReturns(self.__initialValue, self.__pnl)
        sharpe = profit.calculate_sharpe()
        sortino = profit.calculate_sortino()
        pnlTable.add_row(['Sharpe Ratio', "{:.2f}".format(sharpe)])
        pnlTable.add_row(['Sortino Ratio', "{:.2f}".format(sortino)])
        print(pnlTable)

        profit.plot_pnl()
