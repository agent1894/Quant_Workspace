from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

ext_modules = [
    Extension(
        name='userFunc_cython_cpp',
        sources=['userFunc_cython_cpp.pyx'],
        include_dirs=['.'],  # gcc -I
        library_dirs=['.'],  # gcc -L
        libraries=['userFunc'],  # gcc -l
        language='c++',
        extra_link_args=['-Wl,-rpath=.'])
]

setup(ext_modules=cythonize(ext_modules))
