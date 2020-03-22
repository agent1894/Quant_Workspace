#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Report(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self._report = list()

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

    def print_report(self):
        return self._report


class Execute(Report):
    def __init__(self):
        super(Execute, self).__init__()

    def append_report(self, report):
        self._report.append(report)

    def print_report(self):
        return self._report
