# -*- coding: utf-8 -*-
import numpy as np
import datetime as dt


# Q1
def fib(n):
    '''
    用递归的方法求解斐波那契数列的第n项的值
    输入：int
    输出：int
    '''
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# Q2
def maxDrawDown(r):
    '''
    计算一个收益序列的最大回撤率, 要求时间复杂度为 O(n).

    如果收益序列r = [r_1,r_2, ... ], 那么对应的净值序列为 [1+r_1, (1+r_1)*(1+r_2), (1+r_1)*(1+r_2)*(1+r_3), ... ]
    最大回撤率定义见 https://baike.baidu.com/item/%E6%9C%80%E5%A4%A7%E5%9B%9E%E6%92%A4%E7%8E%87/3645063?fr=aladdin

    输入：收益序列, np.array, shape = (1,).
    输出：float
    '''
    series = np.cumprod([x + 1 for x in r])
    endIndex = np.argmax(np.maximum.accumulate(series) - series)
    begIndex = np.argmax(series[:endIndex])
    maxDrawdown = series[begIndex] - series[endIndex]
    return maxDrawdown


# Q3
class TimeConvert(object):
    '''
    将HHMMSS.mmm类型的真实时间（time）与分阶段的交易时间（tk）互转, 交易总时长为上午93000.000 – 113000.000 下午130000.000 – 150000.000,
    要求每3秒为一个tk值且向后对齐, 例如93000.000对应的tk为0, 93003.000对应的tk为1, 那么93000.000到93003.000中的所有时间(不包括93000.000)都对应1,
    93000.000以前的时刻为集合竞价阶段, 也全部对应为0.
    反过来, 输入tk值0则返回真实时间93000.000, 输入1则返回93003.000.
    注意几个重要时点：113000.000对应2400, 130000.000对应2401, 150000.000对应4801. time超过150000.0000的直接报错, tk小于0或大于4801也报错.
    '''
    def __init__(self):
        self.__morningStart = dt.datetime.strptime("093000.001", "%H%M%S.%f")
        self.__afternoonStart = dt.datetime.strptime("130000.001", "%H%M%S.%f")

    def time_to_tk(self, time):
        '''
        输入: float
        输出: int
        '''
        assert time <= 150000, 'wrong input'
        assert '.' in str(time), 'wrong input'  # to satisfy time format
        if time <= 93000.000:
            return 0
        tsTime = dt.datetime.strptime(str(time), "%H%M%S.%f")
        if time < 113000.000:
            delta = tsTime - self.__morningStart
            return delta.seconds // 3 + 1
        elif 113000.000 <= time < 130000.000:
            return 2400
        else:
            delta = tsTime - self.__afternoonStart
            return delta.seconds // 3 + 2401

    def tk_to_time(self, tk):
        '''
        输入: int
        输出: float
        '''
        assert 0 <= tk <= 4801, 'wrong input'
        if tk <= 2400:
            return float(
                dt.datetime.strftime(dt.datetime(2020, 5, 19, 9, 30, 0) + dt.timedelta(seconds=tk * 3), "%H%M%S.%f"))
        else:
            return float(
                dt.datetime.strftime(
                    dt.datetime(2020, 5, 19, 9, 30, 0) + dt.timedelta(seconds=(tk + 1799) * 3), "%H%M%S.%f"))


# Q4
def recordTransform(record_table, n_code=100):
    '''
    将实时记录(record_table) 转化为矩阵类型且时刻对齐的记录表(compressed_table).
    实时记录有3列, 分别为真实交易时间(time),代码(code),数值(value), 每一行代表一条记录, 时间为升序排列(从92500.00开始直到150000.000为止), 代码乱序(代码固定由0到n_code-1, n_code=100)
    对齐的记录表为分阶段交易时间(tk)*代码(code)的2维数组, 其中位置为(t,c)的元素表示t-1至t时刻代码为c的实时记录最新数值, 若对应时间内没有数值则用np.nan表示。

    例: 时间为从92500.00开始到93012.000为止, 代码为0到4 (n_code=5) 的实时记录
        record_table = np.array([[92602.012,3,20],
                                 [93002.312,4,23],
                                 [93003.122,1,45],
                                 [93004.932,1,48],
                                 [93006.120,2,27],
                                 [93006.120,2,30],
                                 [93006.156,1,48],
                                 [93006.234,0,73],
                                 [93009.000,1,33],
                                 [93009.412,4,12]]
                                )
        转化结果
        compressed_table =  np.array([[np.nan, np.nan, np.nan, 20   , np.nan],
                                     [np.nan, np.nan, np.nan, np.nan, 23    ],
                                     [np.nan, 48    , np.nan, np.nan, np.nan],
                                     [73    , 33    , 30    , np.nan, np.nan],
                                     [np.nan, np.nan, np.nan, 12    , np.nan]])

    输入: np.array, shape = (n,3), 行数n任意
    输出: np.array, shape = (4802,n_code)

    (可利用Q3实现的类)
    '''
    result = np.full((4802, n_code), np.nan)
    obj = TimeConvert()
    record_table[:, 0] = list(map(obj.time_to_tk, record_table[:, 0]))
    for i in range(len(record_table)):
        idx = int(record_table[i, 0])
        code = int(record_table[i, 1])
        val = record_table[i, 2]
        result[idx, code] = val

    return result
