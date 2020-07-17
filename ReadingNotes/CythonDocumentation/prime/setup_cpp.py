from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize("prime_cython_cpp.pyx"))
