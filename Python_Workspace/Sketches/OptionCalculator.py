#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
This Module Contains Black-Scholes-Merton Calculations of
Prices and Greeks for Options.
'''

import numpy as np
from scipy.stats import norm
import datetime as dt
import warnings
warnings.filterwarnings('ignore')


class Option(object):
    ''' Defines a basic option for further calculation.
    Attributes:
        The following items are compulsory.
        setDate & expDate or t: annualized time interval.
        S0: underlying price.
        K: strike price.
        optionType: Call or Put.
        r: risk-free interest rate.
        vol: volatility.
        div: dividends.
    '''
    def __init__(self,
                 setDate=dt.date.today(),
                 expDate=dt.date.today(),
                 t=None,
                 S0=1,
                 K=1,
                 optionType='C',
                 r=0.05,
                 vol=0.3,
                 div=0):
        ''' Inits the Option class.
        In Python 3.x, all inputs are typed as string, thus the format
        cast is necessary.
        '''
        self.optionType = optionType[0].upper()
        self.K = float(K)
        self.r = float(r)
        self.vol = float(vol)
        self.setDate = setDate
        self.expDate = expDate
        self.div = float(div)

        if t:  # when directly input the days to expire
            self.t = float(t) / 252.0
        else:
            self.t = self.__calculate_t()
        if self.t == 0:  # case in expiration date
            self.t = 0.000001
        self.S0 = float(S0)  # self.S0 = float(S0)*np.exp(self.r*self.t)

    def __calculate_t(self):
        ''' Calculate the time interval when using the start/end date.

        This private method calculates the days to expire under different types
        of date parameters.
        '''
        if type(self.setDate) != dt.date and type(self.setDate) != dt.datetime:
            self.setDate = self.dateFormat(self.setDate)
        if type(self.expDate) != dt.date and type(self.expDate) != dt.datetime:
            self.expDate = self.dateFormat(self.expDate)
        # calculate the days to expire
        return (self.expDate - self.setDate).days / 252.0

    def dateFormat(self, inputDate):
        ''' Proper date inputs.

        This method transforms the input date into proper date format.
        '''
        inputDate = str(inputDate)
        if len(inputDate) == 8:
            if inputDate >= '19000101' and inputDate <= '20991231':
                year = inputDate[0:4]
                month = inputDate[4:6]
                day = inputDate[6:8]
            else:
                raise TypeError('Inappropriate Datetime Format')
        elif len(inputDate) == 10:
            year = inputDate[0:4]
            month = inputDate[5:7]
            day = inputDate[8:10]
        else:
            raise TypeError('Inappropriate Datetime Format')
        return dt.datetime.strptime(year + month + day, '%Y%m%d')


class OptionPriceCalculator(Option):
    ''' Inheritance class from base class Option for price calculation.

    There are two common approaches to calculate the option price:
    Black-Scholes-Merton model formula or Monte-Carlo simulation.
    This class realizes two approaches and gives comparisons.
    '''
    def getOptionPriceBSM(self):
        d1 = (np.log(self.S0 / self.K) +
              (self.r + self.div + 0.5 * self.vol**2) * self.t) / (self.vol * np.sqrt(self.t))
        d2 = d1 - self.vol * np.sqrt(self.t)
        if self.optionType == 'C':
            BSMPrice = norm.cdf(d1) * self.S0 - self.K * np.exp(-self.r * self.t) * norm.cdf(d2)
        elif self.optionType == 'P':
            BSMPrice = self.K * np.exp(-self.r * self.t) * norm.cdf(-d2) - norm.cdf(-d1) * self.S0
        else:
            raise TypeError('Inappropriate Option Type')
        return BSMPrice

    def getOptionPriceMonteCarlo(self, n=10000000):
        ''' The default simulation times is 10000000.

        Using array can save CPU time rather than for-loops.
        The calculation of ndarray returns a list of lists.
        '''
        z = np.random.randn(1, n)  # type(z) is np.ndarray
        st = self.S0 * np.exp((self.r - 0.5 * self.vol**2) * self.t + self.vol * np.sqrt(self.t) * z)[0]
        if self.optionType == 'C':
            value = st - self.K
        elif self.optionType == 'P':
            value = self.K - st
        else:
            raise TypeError('Inappropriate Option Type')
        MCPrice = np.exp(-self.r * self.t) * np.mean([max(value, 0) for value in value])
        return MCPrice

    def getOptionPrice(self):
        BSMPrice = self.getOptionPriceBSM()
        MCPrice = self.getOptionPriceMonteCarlo()
        print('-' * 20 + 'Calculate the option price' + '-' * 20)
        print('The Black-Scholes-Merton option price is: {:.2f}'.format(BSMPrice))
        print('The Monte-Carlo simulation option price is: {:.2f}'.format(MCPrice))


class OptionGreeksCalculator(Option):
    ''' Inheritance class from base class Option for Greeks calculation.

    Generally, the Greeks can not use the explicit formula to calculate
    except Delta. Therefore, the common approach for Greeks calculation
    is by differential method to find the approximate solution.
    '''
    def __init__(self,
                 setDate=dt.date.today(),
                 expDate=dt.date.today(),
                 t=None,
                 S0=1,
                 K=1,
                 optionType='C',
                 r=0.05,
                 vol=0.3,
                 div=0):
        super(OptionGreeksCalculator, self).__init__(setDate=setDate,
                                                     expDate=expDate,
                                                     t=t,
                                                     S0=S0,
                                                     K=K,
                                                     optionType=optionType,
                                                     r=r,
                                                     vol=vol,
                                                     div=div)
        preOption = OptionPriceCalculator(S0=self.S0,
                                          K=self.K,
                                          r=self.r,
                                          t=self.t * 252,
                                          vol=self.vol,
                                          optionType=self.optionType)
        self.prePrice = preOption.getOptionPriceBSM()

    def getOptionDelta(self):
        '''stock price changes ds, the option price changes delta ds'''
        d1 = (np.log(self.S0 / self.K) + (self.r + 0.5 * self.vol**2) * self.t) / (self.vol * np.sqrt(self.t))
        if self.optionType == 'C':
            delta = norm.cdf(d1)
        else:
            delta = -norm.cdf(-d1)
        return delta

    def getOptionGamma(self, ds=0.00001):
        '''stock price changes ds, the option delta changes gamma ds'''
        preDelta = self.getOptionDelta()
        postOption = OptionGreeksCalculator(
            S0=self.S0 + ds,
            K=self.K,
            r=self.r,
            t=self.t * 252,  # annualize t
            vol=self.vol,
            optionType=self.optionType)
        postDelta = postOption.getOptionDelta()
        gamma = (postDelta - preDelta) / ds
        return gamma

    def getOptionTheta(self, dt=1.0):
        postOption = OptionPriceCalculator(S0=self.S0,
                                           K=self.K,
                                           r=self.r,
                                           t=self.t * 252 - dt,
                                           vol=self.vol,
                                           optionType=self.optionType)
        postPrice = postOption.getOptionPriceBSM()
        '''
        Usually, theta is calculated based on a day-time.
        Therefore, the result of theta needs to divided by trading days.
        When others keeps constant, with one day passes,
        the option value changes theta
        '''
        theta = (postPrice - self.prePrice) / dt
        return theta

    def getOptionVega(self, dvol=0.00001):
        postOption = OptionPriceCalculator(S0=self.S0,
                                           K=self.K,
                                           r=self.r,
                                           t=self.t * 252,
                                           vol=self.vol + dvol,
                                           optionType=self.optionType)
        postPrice = postOption.getOptionPriceBSM()
        '''
        When implied vol changes 1% (0.01),
        the option value changes 0.01 * vega
        '''
        vega = (postPrice - self.prePrice) / dvol
        return vega

    def getOptionRho(self, dr=0.00001):
        postOption = OptionPriceCalculator(S0=self.S0,
                                           K=self.K,
                                           r=self.r + dr,
                                           t=self.t * 252,
                                           vol=self.vol,
                                           optionType=self.optionType)
        postPrice = postOption.getOptionPriceBSM()
        '''
        When interest rate changes 1% (0.01),
        the option value changes 0.01 * rho
        '''
        rho = (postPrice - self.prePrice) / dr
        return rho

    def getOptionGreeks(self):
        delta = self.getOptionDelta()
        gamma = self.getOptionGamma()
        theta = self.getOptionTheta()
        vega = self.getOptionVega()
        rho = self.getOptionRho()
        print('-' * 20 + 'Calculate the option greeks' + '-' * 20)
        print('Delta: {:.4f}'.format(delta))
        print('Gamma: {:.4f}'.format(gamma))
        print('Theta: {:.4f}'.format(theta))
        print('Vega:  {:.4f}'.format(vega))
        print('Rho:   {:.4f}'.format(rho))


class OptionImpliedVolCalculator(Option):
    ''' Inheritance class from base class Option for
    implied volatility calculation.

    There are two common approaches to calculate the implied volatility:
    Newton-Raphson method and bisection method.
    This class realizes two approaches and gives comparisons.
    '''
    def __init__(self,
                 setDate=dt.date.today(),
                 expDate=dt.date.today(),
                 t=None,
                 S0=1,
                 K=1,
                 optionType='C',
                 r=0.05,
                 vol=0.3,
                 div=0,
                 price=np.nan):
        super(OptionImpliedVolCalculator, self).__init__(setDate=setDate,
                                                         expDate=expDate,
                                                         t=t,
                                                         S0=S0,
                                                         K=K,
                                                         optionType=optionType,
                                                         r=r,
                                                         vol=vol,
                                                         div=div)
        self.price = float(price)

    def getImpliedVolNewton(self):
        ''' Newton-Raphson method needs to use the first-order derivative
        for option's volatility which is exactly the Vega of the option.'''
        price = self.price
        vol = 0.5
        n = 1
        t = self.t * 252
        priceGuess = 0.0
        while abs(price - priceGuess) > 0.0000001 and n < 100:
            priceGuess = OptionPriceCalculator(setDate=self.setDate,
                                               expDate=self.expDate,
                                               t=t,
                                               S0=self.S0,
                                               K=self.K,
                                               optionType=self.optionType,
                                               r=self.r,
                                               div=self.div,
                                               vol=vol).getOptionPriceBSM()
            vol = vol - (priceGuess - price) / OptionGreeksCalculator(setDate=self.setDate,
                                                                      expDate=self.expDate,
                                                                      t=t,
                                                                      S0=self.S0,
                                                                      K=self.K,
                                                                      optionType=self.optionType,
                                                                      r=self.r,
                                                                      div=self.div,
                                                                      vol=vol).getOptionVega()
            n += 1
        print('*' * 20 + ' Newton-Raphson method ' + '*' * 20)
        print('Iteration: {}'.format(n))
        print('Accuracy： {:.2e}'.format(price - priceGuess))
        print('The implied volatility is：{:.2%}'.format(vol))
        return vol

    def getImpliedVolBisection(self):
        price = self.price
        vol = 0.5
        volLow = 0.0
        volHigh = 1.0
        n = 1
        t = self.t * 252
        priceGuess = 0.0
        while abs(price - priceGuess) > 0.0000001 and n < 100:
            priceGuess = OptionPriceCalculator(setDate=self.setDate,
                                               expDate=self.expDate,
                                               t=t,
                                               S0=self.S0,
                                               K=self.K,
                                               optionType=self.optionType,
                                               r=self.r,
                                               div=self.div,
                                               vol=vol).getOptionPriceBSM()
            if priceGuess > price:
                volHigh = vol
            else:
                volLow = vol
            vol = (volHigh + volLow) / 2.0
            n += 1
        print('*' * 20 + ' Bisection method ' + '*' * 20)
        print('Iteration: {}'.format(n))
        print('Accuracy： {:.2e}'.format(price - priceGuess))
        print('The implied volatility is：{:.2%}'.format(vol))
        return vol

    def getOptionImpliedVol(self):
        print('-' * 20 + 'Calculate the option implied vol' + '-' * 20)
        self.getImpliedVolNewton()
        self.getImpliedVolBisection()


if __name__ == '__main__':
    while True:
        S0 = input('Please enter the underlying price: ')
        K = input('Please enter the strike price: ')
        optionType = input('Please enter the option type: ')
        r = input('Please enter the risk-free interest rate: ')
        div = input('Please enter the divided: ')
        dates = input('Use the start & end date? (Y/N): ')
        if dates[0].upper() == 'Y':
            setDate = input('Please enter the set date: ')
            expDate = input('Please enter the expire date: ')
        elif dates[0].upper() == 'N':
            years = input('The interval is in days or in years?')
            if years[0].upper() == 'D':
                t = float(input('Please enter the interval(days): '))
            elif years[0].upper() == 'Y':
                t = float(input('Please enter the interval(years): ')) * 252
            else:
                raise TypeError('Unsupported Time Interval')
            setDate = dt.date.today()
            expDate = dt.date.today()
        else:
            raise TypeError('Unsupported Time Interval')
        impVol = input('To calcualte the implied volatility? (Y/N): ')
        if impVol[0].upper() == 'Y':
            price = input('Please enter the option price: ')
            impVol = OptionImpliedVolCalculator(setDate=setDate,
                                                expDate=expDate,
                                                t=t,
                                                S0=S0,
                                                K=K,
                                                optionType=optionType,
                                                r=r,
                                                div=div,
                                                price=price)
            impVol.getOptionImpliedVol()
        elif impVol[0].upper() == 'N':
            vol = input('Please enter the volatility: ')
            prices = OptionPriceCalculator(setDate=setDate,
                                           expDate=expDate,
                                           t=t,
                                           S0=S0,
                                           K=K,
                                           optionType=optionType,
                                           r=r,
                                           vol=vol,
                                           div=div)
            prices.getOptionPrice()
            greeks = OptionGreeksCalculator(setDate=setDate,
                                            expDate=expDate,
                                            t=t,
                                            S0=S0,
                                            K=K,
                                            optionType=optionType,
                                            r=r,
                                            vol=vol,
                                            div=div)
            greeks.getOptionGreeks()
        else:
            raise TypeError('Unsupported Option Calculations')
        print('DONE!')
