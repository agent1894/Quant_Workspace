#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import prettytable


class Report(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self._report = list()
        self._table = prettytable.PrettyTable()

    @abstractmethod
    def parse_report(self):
        raise NotImplementedError("Should implement parse_report().")

    @abstractmethod
    def append_report(self, report):
        raise NotImplementedError("Should implement append_report().")

    @abstractmethod
    def print_report(self):
        raise NotImplementedError("Should implement print_report().")


class Order(Report):
    def __init__(self):
        super(Order, self).__init__()

    def append_report(self, report):
        self._report.append(report)

    def parse_report(self):
        self._table.field_name = ["Order ID", "Symbol", "Order Time", "Order Type", "Order Status", "Completion Time",
                                  "Order Price", "Order Size", "Commission Fees"]

    def print_report(self):
        print(self._report)


class Execute(Report):
    def __init__(self):
        super(Execute, self).__init__()

    def append_report(self, report):
        self._report.append(report)

    def parse_report(self):
        self._table.field_name = []

    def print_report(self):
        print(self._report)
