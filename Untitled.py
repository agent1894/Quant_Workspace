#!/usr/bin/env python
# coding: utf-8


#YBB计算函数
from math import fabs,exp,log
import numpy as np
import pandas as pd
test=pd.read_csv('000001.csv')

elapse = 0.0000001

def ybb_Equal(a, b): 
    return fabs(a-b) <= elapse or a==b


def ybb_Greater(a, b): 
    return a - b > elapse


def ybb_Smaller(a, b): 
    return b - a > elapse


def ybb_GreaterOrEqual(a, b): 
    return ybb_Greater(a, b) or ybb_Equal(a, b)


def ybb_SmallerOrEqual(a, b): 
    return ybb_Smaller(a, b) or ybb_Equal(a, b)


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

ybb_outReal_extend_2

len(ybb_outReal_extend_2)



length=21
test=pd.read_csv('000001.csv')
test=test[['date_','open_t','close_']]
test['current_value']=test['close_'].shift(length)
test['current_temp']=test['close_'].shift(length-1)
test['roll21_max']=test['current_temp'].rolling(length).max()
test['roll21_min']=test['current_temp'].rolling(length).min()
test['roll11_max']=test['current_temp'].shift(length//2).rolling(length//2+1).max()
test['roll11_min']=test['current_temp'].shift(length//2).rolling(length//2+1).min()
test['roll10_max']=test['current_temp'].rolling(length//2).max()
test['roll10_min']=test['current_temp'].rolling(length//2).min()
test['n3']=test.apply(lambda x:(max(x['current_temp'],x['roll21_max'])-min(x['current_temp'],x['roll21_min']))/length,axis=1)
test['n2']=test.apply(lambda x:(max(x['current_temp'],x['roll11_max'])-min(x['current_temp'],x['roll11_min']))/length*2,axis=1)
test['n1']=test.apply(lambda x:(max(x['current_temp'],x['roll10_max'])-min(x['current_temp'],x['roll10_min']))/length*2,axis=1)
test['alpha']=test.apply(lambda x:np.exp(-4.6*((np.log(x['n1']+x['n2'])-np.log(x['n3']))/np.log(2)-1)) if x['n1']>0 and x['n2']>0 and x['n3']>0 else np.nan,axis=1)
test['current_adj']=test['alpha']*test['close_']+test['current_value']*(1-test['alpha'])
test['current_adj'].iloc[0:41]=test['close_'].iloc[0:41]
test['indicator']=test.apply(lambda x:x['current_adj']/x['open_t']-1 if x['open_t']!=0 else 0,axis=1)
test['indicator']