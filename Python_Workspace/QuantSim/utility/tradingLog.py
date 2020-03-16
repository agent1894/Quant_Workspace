#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Report(object):
    __metaclass__ = ABCMeta

    def __init__(self, report: dict):
        self._report = report

    @abstractmethod
    def parse_report(self):
        pass


class Order(Report):
    def __init__(self, report: dict):
        super(Order, self).__init__(report=report)

    def parse_report(self):
        pass


class Execute(Report):
    def __init__(self, report: dict):
        super(Execute, self).__init__(report=report)

    def parse_report(self):
        pass


class Portfolio(Report):
    def __init__(self, report: dict):
        super(Portfolio, self).__init__(report=report)

    def parse_report(self):
        pass
