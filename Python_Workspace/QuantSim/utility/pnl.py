#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


class PeriodReturns(object):
    def __init__(self, initialValue: float, returns: list):
        self._pnl = returns
        self._returns = []
        for i in range(1, len(returns)):
            self._returns.append(returns[i] / returns[i - 1] - 1)

    def calculate_sharpe(self):
        return np.mean(self._returns) / np.std(self._returns) * np.sqrt(252)

    def calculate_sortino(self):
        negative = [x for x in self._returns if x < 0]
        return np.mean(self._returns) / np.std(negative) * np.sqrt(252)

    def plot_pnl(self):
        plt.plot(self._pnl)
        plt.show()
