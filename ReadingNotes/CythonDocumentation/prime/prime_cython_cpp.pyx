# distutils:language = c++
'''
@Filename     :prime_cython_cpp.pyx
@Author       :Arthur Zhan
@Init Time    :2020/06/16
'''

from libcpp.vector cimport vector

def primes(unsigned int num):
    cdef unsigned int i = 2
    cdef vector[int] lst
    cdef unsigned int lim = 0
    cdef unsigned int d
    while lst.size() < num:
        if 2 > i // 2 + 1:
            lim = i
        else:
            lim = i // 2 + 1
        for d in range(2, lim):
            if i % d == 0:
                break
        else:
            lst.push_back(i)
        i += 1
    return lst