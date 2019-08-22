#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#YBB计算函数
from math import fabs,exp,log
import numpy as np
import pandas as pd

elapse = 0.0000001

def ybb_equal(a, b): 
    return fabs(a-b) <= elapse or a==b


def ybb_Greater(a, b): 
    return a - b > elapse


def ybb_Smaller(a, b): 
    return b - a > elapse


def ybb_GreaterOrEqual(a, b): 
    return ybb_greater(a, b) or ybb_equal(a, b)


def ybb_SmallerOrEqual(a, b): 
    return ybb_smaller(a, b) or ybb_equal(a, b)


#3021_2_minus_c_devide_c_4h
def ybb_frama(price, length, pieces, capacity, cbar, indicator):

    outReal = 0
    if(cbar < (2 * length - 1) * pieces):
        outReal = price[cbar]

    else:
        h = 0
        l = 0
        n1 = 0
        n2 = 0
        n3 = 0
        current_value = price[cbar - length * pieces]

        for i in range(cbar - (length - 1) * pieces, cbar + pieces, pieces):
            h = price[i]
            l = price[i]
            for j in range(i - (length - 1) * pieces, i + pieces, pieces):
                if(ybb_SmallerOrEqual(h, price[j])):
                    h = price[j]
                if(ybb_GreaterOrEqual(l, price[j])):
                    l = price[j]    
               
            n3 = (h - l) / length
            h = price[i]
            l = price[i]

            for j in range(i - (length - 1) * pieces, i - length // 2 * pieces + pieces, pieces):
                if(ybb_SmallerOrEqual(h, price[j])):
                    h = price[j]
                if(ybb_GreaterOrEqual(l, price[j])):
                    l = price[j]
             
            n2 = (h - l) / length * 2

            h = price[i]
            l = price[i]

            for j in range(i - (length // 2 - 1) * pieces, i + pieces, pieces):
                if(ybb_SmallerOrEqual(h, price[j])):
                    h = price[j]
                if(ybb_GreaterOrEqual(l, price[j])):
                    l = price[j]
             
            n1 = (h - l) / length * 2

            alpha = 1.0
            if(ybb_Greater(n1, 0) and ybb_Greater(n2, 0) and ybb_Greater(n3, 0)):
                alpha = exp(-4.6 * ((log(n1 + n2) - log(n3))/log(2) - 1))
         
            if(ybb_Smaller(alpha, 0.01)):
                alpha = 0.01
         
            if(ybb_Greater(alpha, 1.0)):
                alpha = 1.0
         
            current_value = alpha * price[cbar] +(1 - alpha) * current_value
         
        outReal = current_value

    indicator.append(outReal)
    if(cbar >= capacity):
        indicator.remove(indicator[0])

def ybb_minus_c_devide_c_extend(inReal, close, capacity, cbar, indicator):
    if (ybb_Equal(close[cbar], 0)):
        outReal = 0
    else:
        if(not ybb_Equal(close[cbar], 0)):
            outReal = inReal[cbar] / close[cbar] - 1;

    indicator.append(outReal)
    if(cbar >= capacity):
        indicator.remove(indicator[0])
        
        
close_=test['close_']
open_t=test['open_t']
pieces=1
capacity=545

ybb_outReal_base_2 = []
ybb_outReal_extend_2 = []
for cbar in range(545):
    ybb_frama(close_, 21, pieces, capacity, cbar, ybb_outReal_base_2)
    ybb_minus_c_devide_c_extend(ybb_outReal_base_2, open_t, capacity, cbar, ybb_outReal_extend_2)

