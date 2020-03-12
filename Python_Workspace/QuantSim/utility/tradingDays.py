#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import datetime as dt
import pandas as pd

holidaysCH = {
    dt.date(2020, 1, 1),  # New Year
    dt.date(2020, 1, 24),  # Chinese New Year
    dt.date(2020, 1, 25),  # Chinese New Year
    dt.date(2020, 1, 26),  # Chinese New Year
    dt.date(2020, 1, 27),  # Chinese New Year
    dt.date(2020, 1, 28),  # Chinese New Year
    dt.date(2020, 1, 29),  # Chinese New Year
    dt.date(2020, 1, 30),  # Chinese New Year
    dt.date(2020, 1, 31),  # Chinese New Year (COVID-19)
    dt.date(2020, 2, 1),  # Chinese New Year
    dt.date(2020, 2, 2),  # Chinese New Year
    dt.date(2020, 4, 4),  # Qingming Festival
    dt.date(2020, 4, 5),  # Qingming Festival
    dt.date(2020, 4, 6),  # Qingming Festival
    dt.date(2020, 5, 1),  # Labor Day
    dt.date(2020, 5, 2),  # Labor Day
    dt.date(2020, 5, 3),  # Labor Day
    dt.date(2020, 5, 4),  # Labor Day
    dt.date(2020, 5, 5),  # Labor Day
    dt.date(2020, 6, 25),  # Dragon boat Festival
    dt.date(2020, 6, 26),  # Dragon boat Festival
    dt.date(2020, 6, 27),  # Dragon boat Festival
    dt.date(2020, 10, 1),  # National Day
    dt.date(2020, 10, 2),  # National Day
    dt.date(2020, 10, 3),  # National Day
    dt.date(2020, 10, 4),  # National Day
    dt.date(2020, 10, 5),  # National Day
    dt.date(2020, 10, 6),  # National Day
    dt.date(2020, 10, 7),  # National Day
    dt.date(2020, 10, 8),  # Mid-autumn Festival
    dt.date(2018, 12, 30),  # New Year
    dt.date(2018, 12, 31),  # New Year
    dt.date(2019, 1, 1),  # New Year
    dt.date(2019, 2, 4),  # Chinese New Year
    dt.date(2019, 2, 5),  # Chinese New Year
    dt.date(2019, 2, 6),  # Chinese New Year
    dt.date(2019, 2, 7),  # Chinese New Year
    dt.date(2019, 2, 8),  # Chinese New Year
    dt.date(2019, 2, 9),  # Chinese New Year
    dt.date(2019, 2, 10),  # Chinese New Year
    dt.date(2019, 4, 5),  # Qingming Festival
    dt.date(2019, 4, 6),  # Qingming Festival
    dt.date(2019, 4, 7),  # Qingming Festival
    dt.date(2019, 5, 1),  # Labor Day
    dt.date(2019, 5, 2),  # Labor Day
    dt.date(2019, 5, 3),  # Labor Day
    dt.date(2019, 5, 4),  # Labor Day
    dt.date(2019, 6, 7),  # Dragon boat Festival
    dt.date(2019, 6, 8),  # Dragon boat Festival
    dt.date(2019, 6, 9),  # Dragon boat Festival
    dt.date(2019, 9, 13),  # Mid-autumn Festival
    dt.date(2019, 9, 14),  # Mid-autumn Festival
    dt.date(2019, 9, 15),  # Mid-autumn Festival
    dt.date(2019, 10, 1),  # National Day
    dt.date(2019, 10, 2),  # National Day
    dt.date(2019, 10, 3),  # National Day
    dt.date(2019, 10, 4),  # National Day
    dt.date(2019, 10, 5),  # National Day
    dt.date(2019, 10, 6),  # National Day
    dt.date(2019, 10, 7),  # National Day
    dt.date(2018, 1, 1),  # New Year
    dt.date(2018, 2, 15),  # Chinese New Year
    dt.date(2018, 2, 16),  # Chinese New Year
    dt.date(2018, 2, 17),  # Chinese New Year
    dt.date(2018, 2, 18),  # Chinese New Year
    dt.date(2018, 2, 19),  # Chinese New Year
    dt.date(2018, 2, 20),  # Chinese New Year
    dt.date(2018, 2, 21),  # Chinese New Year
    dt.date(2018, 4, 5),  # Qingming Festival
    dt.date(2018, 4, 6),  # Qingming Festival
    dt.date(2018, 4, 7),  # Qingming Festival
    dt.date(2018, 4, 29),  # Labor Day
    dt.date(2018, 4, 30),  # Labor Day
    dt.date(2018, 5, 1),  # Labor Day
    dt.date(2018, 6, 16),  # Dragon boat Festival
    dt.date(2018, 6, 17),  # Dragon boat Festival
    dt.date(2018, 6, 18),  # Dragon boat Festival
    dt.date(2018, 9, 22),  # Mid-autumn Festival
    dt.date(2018, 9, 23),  # Mid-autumn Festival
    dt.date(2018, 9, 24),  # Mid-autumn Festival
    dt.date(2018, 10, 1),  # National Day
    dt.date(2018, 10, 2),  # National Day
    dt.date(2018, 10, 3),  # National Day
    dt.date(2018, 10, 4),  # National Day
    dt.date(2018, 10, 5),  # National Day
    dt.date(2018, 10, 6),  # National Day
    dt.date(2018, 10, 7),  # National Day
    dt.date(2017, 1, 1),  # New Year
    dt.date(2017, 1, 2),  # New Year
    dt.date(2017, 1, 27),  # Chinese New Year
    dt.date(2017, 1, 28),  # Chinese New Year
    dt.date(2017, 1, 29),  # Chinese New Year
    dt.date(2017, 1, 30),  # Chinese New Year
    dt.date(2017, 1, 31),  # Chinese New Year
    dt.date(2017, 2, 1),  # Chinese New Year
    dt.date(2017, 2, 2),  # Chinese New Year
    dt.date(2017, 4, 2),  # Qingming Festival
    dt.date(2017, 4, 3),  # Qingming Festival
    dt.date(2017, 4, 4),  # Qingming Festival
    dt.date(2017, 4, 29),  # Labor Day
    dt.date(2017, 4, 30),  # Labor Day
    dt.date(2017, 5, 1),  # Labor Day
    dt.date(2017, 5, 28),  # Dragon boat Festival
    dt.date(2017, 5, 29),  # Dragon boat Festival
    dt.date(2017, 5, 30),  # Dragon boat Festival
    dt.date(2017, 10, 1),  # National Day
    dt.date(2017, 10, 2),  # National Day
    dt.date(2017, 10, 3),  # National Day
    dt.date(2017, 10, 4),  # Mid-autumn Festival
    dt.date(2017, 10, 5),  # National Day
    dt.date(2017, 10, 6),  # National Day
    dt.date(2017, 10, 7),  # National Day
    dt.date(2017, 10, 8),  # National Day
    dt.date(2016, 1, 1),  # New Year
    dt.date(2016, 1, 2),  # New Year
    dt.date(2016, 1, 3),  # New Year
    dt.date(2016, 2, 7),  # Chinese New Year
    dt.date(2016, 2, 8),  # Chinese New Year
    dt.date(2016, 2, 9),  # Chinese New Year
    dt.date(2016, 2, 10),  # Chinese New Year
    dt.date(2016, 2, 11),  # Chinese New Year
    dt.date(2016, 2, 12),  # Chinese New Year
    dt.date(2016, 2, 13),  # Chinese New Year
    dt.date(2016, 4, 2),  # Qingming Festival
    dt.date(2016, 4, 3),  # Qingming Festival
    dt.date(2016, 4, 4),  # Qingming Festival
    dt.date(2016, 4, 30),  # Labor Day
    dt.date(2016, 5, 1),  # Labor Day
    dt.date(2016, 5, 2),  # Labor Day
    dt.date(2016, 6, 9),  # Dragon boat Festival
    dt.date(2016, 6, 10),  # Dragon boat Festival
    dt.date(2017, 6, 11),  # Dragon boat Festival
    dt.date(2017, 9, 15),  # Mid-autumn Festival
    dt.date(2017, 9, 16),  # Mid-autumn Festival
    dt.date(2017, 9, 17),  # Mid-autumn Festival
    dt.date(2017, 10, 1),  # National Day
    dt.date(2017, 10, 2),  # National Day
    dt.date(2017, 10, 3),  # National Day
    dt.date(2017, 10, 4),  # National Day
    dt.date(2017, 10, 5),  # National Day
    dt.date(2017, 10, 6),  # National Day
    dt.date(2017, 10, 7),  # National Day
    dt.date(2016, 1, 1),  # New Year
    dt.date(2016, 1, 2),  # New Year
    dt.date(2016, 1, 3),  # New Year
    dt.date(2016, 2, 7),  # Chinese New Year
    dt.date(2016, 2, 8),  # Chinese New Year
    dt.date(2016, 2, 9),  # Chinese New Year
    dt.date(2016, 2, 10),  # Chinese New Year
    dt.date(2016, 2, 11),  # Chinese New Year
    dt.date(2016, 2, 12),  # Chinese New Year
    dt.date(2016, 2, 13),  # Chinese New Year
    dt.date(2016, 4, 2),  # Qingming Festival
    dt.date(2016, 4, 3),  # Qingming Festival
    dt.date(2016, 4, 4),  # Qingming Festival
    dt.date(2016, 4, 30),  # Labor Day
    dt.date(2016, 5, 1),  # Labor Day
    dt.date(2016, 5, 2),  # Labor Day
    dt.date(2016, 6, 9),  # Dragon boat Festival
    dt.date(2016, 6, 10),  # Dragon boat Festival
    dt.date(2016, 6, 11),  # Dragon boat Festival
    dt.date(2016, 9, 15),  # Mid-autumn Festival
    dt.date(2016, 9, 16),  # Mid-autumn Festival
    dt.date(2016, 9, 17),  # Mid-autumn Festival
    dt.date(2016, 10, 1),  # National Day
    dt.date(2016, 10, 2),  # National Day
    dt.date(2016, 10, 3),  # National Day
    dt.date(2016, 10, 4),  # National Day
    dt.date(2016, 10, 5),  # National Day
    dt.date(2016, 10, 6),  # National Day
    dt.date(2016, 10, 7),  # National Day
    dt.date(2015, 1, 1),  # New Year
    dt.date(2015, 1, 2),  # New Year
    dt.date(2015, 1, 3),  # New Year
    dt.date(2015, 2, 18),  # Chinese New Year
    dt.date(2015, 2, 19),  # Chinese New Year
    dt.date(2015, 2, 20),  # Chinese New Year
    dt.date(2015, 2, 21),  # Chinese New Year
    dt.date(2015, 2, 22),  # Chinese New Year
    dt.date(2015, 2, 23),  # Chinese New Year
    dt.date(2015, 2, 24),  # Chinese New Year
    dt.date(2015, 4, 5),  # Qingming Festival
    dt.date(2015, 4, 6),  # Qingming Festival
    dt.date(2015, 4, 7),  # Qingming Festival
    dt.date(2015, 5, 1),  # Labor Day
    dt.date(2015, 5, 2),  # Labor Day
    dt.date(2015, 5, 3),  # Labor Day
    dt.date(2015, 6, 20),  # Dragon boat Festival
    dt.date(2015, 6, 21),  # Dragon boat Festival
    dt.date(2015, 6, 22),  # Dragon boat Festival
    dt.date(2015, 9, 3),  # 70th Anniversary of Anti-Fascist Victory
    dt.date(2015, 9, 4),  # 70th Anniversary of Anti-Fascist Victory
    dt.date(2015, 9, 5),  # 70th Anniversary of Anti-Fascist Victory
    dt.date(2015, 9, 27),  # Mid-autumn Festival
    dt.date(2015, 10, 1),  # National Day
    dt.date(2015, 10, 2),  # National Day
    dt.date(2015, 10, 3),  # National Day
    dt.date(2015, 10, 4),  # National Day
    dt.date(2015, 10, 5),  # National Day
    dt.date(2015, 10, 6),  # National Day
    dt.date(2015, 10, 7),  # National Day
    dt.date(2014, 1, 1),  # New Year
    dt.date(2014, 1, 31),  # Chinese New Year
    dt.date(2014, 2, 1),  # Chinese New Year
    dt.date(2014, 2, 2),  # Chinese New Year
    dt.date(2014, 2, 3),  # Chinese New Year
    dt.date(2014, 2, 4),  # Chinese New Year
    dt.date(2014, 2, 5),  # Chinese New Year
    dt.date(2014, 2, 6),  # Chinese New Year
    dt.date(2014, 4, 7),  # Qingming Festival
    dt.date(2014, 5, 1),  # Labor Day
    dt.date(2014, 5, 2),  # Labor Day
    dt.date(2014, 5, 3),  # Labor Day
    dt.date(2014, 6, 2),  # Dragon boat Festival
    dt.date(2014, 9, 8),  # Mid-autumn Festival
    dt.date(2014, 10, 1),  # National Day
    dt.date(2014, 10, 2),  # National Day
    dt.date(2014, 10, 3),  # National Day
    dt.date(2014, 10, 4),  # National Day
    dt.date(2014, 10, 5),  # National Day
    dt.date(2014, 10, 6),  # National Day
    dt.date(2014, 10, 7),  # National Day
    dt.date(2013, 1, 1),  # New Year
    dt.date(2013, 1, 2),  # New Year
    dt.date(2013, 1, 3),  # New Year
    dt.date(2013, 2, 9),  # Chinese New Year
    dt.date(2013, 2, 10),  # Chinese New Year
    dt.date(2013, 2, 11),  # Chinese New Year
    dt.date(2013, 2, 12),  # Chinese New Year
    dt.date(2013, 2, 13),  # Chinese New Year
    dt.date(2013, 2, 14),  # Chinese New Year
    dt.date(2013, 2, 15),  # Chinese New Year
    dt.date(2013, 4, 4),  # Qingming Festival
    dt.date(2013, 4, 5),  # Qingming Festival
    dt.date(2013, 4, 6),  # Qingming Festival
    dt.date(2013, 4, 29),  # Labor Day
    dt.date(2013, 4, 30),  # Labor Day
    dt.date(2013, 5, 1),  # Labor Day
    dt.date(2013, 6, 10),  # Dragon boat Festival
    dt.date(2013, 6, 11),  # Dragon boat Festival
    dt.date(2013, 6, 12),  # Dragon boat Festival
    dt.date(2013, 9, 19),  # Mid-autumn Festival
    dt.date(2013, 9, 20),  # Mid-autumn Festival
    dt.date(2013, 9, 21),  # Mid-autumn Festival
    dt.date(2013, 10, 1),  # National Day
    dt.date(2013, 10, 2),  # Mid-autumn Festival
    dt.date(2013, 10, 3),  # Mid-autumn Festival
    dt.date(2013, 10, 4),  # Mid-autumn Festival
    dt.date(2013, 10, 5),  # Mid-autumn Festival
    dt.date(2013, 10, 6),  # Mid-autumn Festival
    dt.date(2013, 10, 7),  # Mid-autumn Festival
}


class Trading(object):
    def __init__(self, startDate: str, endDate: str, freq: str):
        self._startDate = startDate
        self._endDate = endDate
        self._freq = freq

    def trade_datetimes(self) -> pd.Series:
        dates = pd.date_range(start=self._startDate, end=self._endDate, freq=self._freq)
        dates = {date.strftime("%Y-%m-%d") for date in dates if date.weekday() not in (5, 6)}
        dates = [dt.datetime.strptime(update, "%Y-%m-%d") for update in
                 dates - {date.strftime("%Y-%m-%d") for date in holidaysCH}]
        if self._freq.capitalize()[0:1] == 'D':
            return pd.Series(dates).sort_values().reset_index(drop=True)
        else:
            dates = [date for date in dates if
                     dt.time(9, 30) < date.time() <= dt.time(11, 30) or dt.time(13, 0) < date.time() <= dt.time(15, 0)]
            return pd.Series(dates).sort_values().reset_index(drop=True)

    # TODO: add tick data trading time
