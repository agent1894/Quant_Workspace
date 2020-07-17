# distutiles: extra_compile_args = -fopenmp
# distutiles: extra_link_args = -fopenmp
# cython: profile = True
# distutils:language = c++

cdef extern from "userFunc.h":
    cpdef double addSquare(double x, double y)
