#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import numpy as np
import pandas as pd
import quotation.quotation as qt
import broker.broker as bk
import portfolio.portfolio as pf


class Strategy(object):
    __metaclass__ = ABCMeta

    def __init__(self, symbols: list, portfolio: pf.Portfolio):
        pass

    @abstractmethod
    def calculate_signals(self):
        raise NotImplementedError("Should implement calculate_signals().")

    @abstractmethod
    def execution(self):
        raise NotImplementedError("Should implement execution().")
