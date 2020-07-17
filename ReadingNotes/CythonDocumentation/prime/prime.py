#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Filename     :prime_origin.py
@Author       :Arthur Zhan
@Init Time    :2020/06/16
"""


def primes_1(num):
    i = 2
    lst = []
    while len(lst) < num:
        if 2 > i // 2 + 1:
            limit = i
        else:
            limit = i // 2 + 1
        for d in range(2, limit):
            if i % d == 0:
                break
        else:
            lst.append(i)
        i += 1
    return lst


def primes_2(num):  # According to documentation's example
    i = 2
    lst = []
    while len(lst) < num:
        for d in lst:
            if i % d == 0:
                break
        else:
            lst.append(i)
        i += 1
    return lst
