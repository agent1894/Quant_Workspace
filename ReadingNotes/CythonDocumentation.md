# Cython 3.0 Documentation

来自Cython [GitHub](https://github.com/cython/cython)。官方文档使用.rst格式，下载源码后使用安装sphinx，使用`make html`编译后获取.html文件。

基于当前最新版本Cython 3.0a5。

- [Cython 3.0 Documentation](#cython-30-documentation)
  - [Getting Started](#getting-started)
    - [Cython - an overview](#cython---an-overview)
    - [Installing Cython](#installing-cython)
    - [Building Cython code](#building-cython-code)
    - [Faster code via static typing](#faster-code-via-static-typing)
  - [Tutorials](#tutorials)
    - [Basic Tutorial](#basic-tutorial)
    - [Calling C functions](#calling-c-functions)
    - [Using C libraries](#using-c-libraries)
    - [Extension types (aka. cdef classes)](#extension-types-aka-cdef-classes)
    - [pxd files](#pxd-files)
    - [Caveats](#caveats)
    - [Profiling](#profiling)
    - [Unicode and passing strings](#unicode-and-passing-strings)
    - [Memory Allocation](#memory-allocation)
    - [Embedding Cython modules in C/C++ applications](#embedding-cython-modules-in-cc-applications)
    - [Pure Python Mode](#pure-python-mode)
    - [Working with NumPy](#working-with-numpy)
    - [Working with Python arrays](#working-with-python-arrays)
    - [Further reading](#further-reading)
    - [Related work](#related-work)
  - [Users Guide](#users-guide)
    - [Language Basics](#language-basics)
    - [Extension Types](#extension-types)
    - [Special Methods of Extension Types](#special-methods-of-extension-types)
    - [Sharing Declarations Between Cython Modules](#sharing-declarations-between-cython-modules)
    - [Interfacing with External C Code](#interfacing-with-external-c-code)
    - [Source Files and Compilation](#source-files-and-compilation)
    - [Early Binding for Speed](#early-binding-for-speed)
    - [Using C++ in Cython](#using-c-in-cython)
    - [Fused Types (Templates)](#fused-types-templates)
    - [Porting Cython code to PyPy](#porting-cython-code-to-pypy)
    - [Migrating from Cython 0.29 to 3.0](#migrating-from-cython-029-to-30)
    - [Limitations](#limitations)
    - [Differences between Cython and Pyrex](#differences-between-cython-and-pyrex)
    - [Typed Memoryviews](#typed-memoryviews)
    - [Implementing the buffer protocol](#implementing-the-buffer-protocol)
    - [Using Parallelism](#using-parallelism)
    - [Debugging your Cython program](#debugging-your-cython-program)
    - [Cython for NumPy users](#cython-for-numpy-users)
    - [Pythran as a NumPy backend](#pythran-as-a-numpy-backend)

## Getting Started

### Cython - an overview

最常用的Python解释器为用C编写的CPython，其他有类似使用Java编写的Jython，C#编写的IronPythonn，Python自己编写的PyPy等。由于CPython使用C编写，因此可以包装很多用C编写接口的外部库。但是，对于相比C这种更接近底层的语言，对Python这类高级语言更熟悉的程序员来说，使用C编写一些接口仍然是比较麻烦的。

Cython作为Python的超集，能够提供高级、面向对象、功能性和动态编程等特性。它的主要特性是在语言中提供可选的静态类型声明，从而将源码转换为优化的C/C++代码，然后编译成Python可用的扩展模块。Cython会将Python代码转换为等效的C语言代码，使其能在CPython中运行的同时拥有C的速度。同时这种方式保留了原始的Python接口从而可以在Python中直接使用。

Cython可以编译大部分常规Python代码，同时生成的C代码可以通过静态类型声明在速度上获得极大的提升。类型声明可以起到两个作用，一是将代码从动态的Python转换为静态的C，二是直接操作外部库中定义的类型。

### Installing Cython

使用Cython必须有C编译器，通常在Linux发行版上已存在GUN C编译器（GCC）。因此只需要使用包管理器即可轻松安装：

```Bash
pip install Cython
```

### Building Cython code

不同于Python，Cython代码必须进行编译。这包含两步：

1. Cython将包含Python扩展模块的代码`.pyx`文件编译为`.c`文件。
2. `.c`文件会被C编译器编译为`.so`文件（在Windows系统上为`.pyd`）。这种文件可以直接被Python`import`使用。模块`distutils`或`setuptools`负责这部分运行。

构建Cython代码可以有以下几种方式：

- 写一个调用`distutils/setuptools`的`setup.py`脚本。这是最常用也是最推荐的方式。
- 使用`Pyximport`，像类似直接导入`.py`文件一样导入Cython的`.pyx`文件。这种方式更加简单，但是不够灵活且不能指定特定的编译选项。
- 手动使用Cython命令行程序将`.pyx`转换为`.c`，然后手动将其编译为`.so`或`.dll`文件（通常只用来调试和实验）。
- 使用Jupyter Notebook，Jupyter Notebook允许内联Cython代码，这是使用Cython最简单的方式。

现在使用Cython创建一个*Hello World*脚本，可以看出和Python脚本没有任何区别：

```Python
# Filename: hello.pyx
def say_hello_to(name):
    print("Hello, {}".format(name))
```

```Python
# Filename: setup.py
from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize("hello.pyx"))
```

然后只需要在命令行中运行：

```Bash
python3 setup.py build_ext --inplace
```

即可完成编译。此后在任何一个Python脚本中都可以使用`from hello import say_hell_to`来导入这个模块中的函数。

Cython也可以很方便的在Jupyter Notebook中进行交互使用。首先在Jupyter Notebook中加载`Cython`扩展，然后使用`%%cython`标记单元格，即可进行编译使用。

```Python
In [1]: %load_ext cython

In [2]: %%cython
   ...:
   ...: cdef int a = 0
   ...: for i in range(10):
   ...:     a += i
   ...: print(a)

45
```

由于静态类型声明是提高速度的关键，因此初学者往往会倾向于在所有地方加入类型检查。这种方式一方面降低了可读性和灵活性，甚至可能降低性能（例如加入了不必要的类型检查等），另一方面，没有在关键部分加入类型会极大的破环性能。因此，Cython提供了注释功能用以确定代码为何花费了时间。

使用`%%cython --annotate`在下方输出HTML格式的分析，白色表示这段代码转换为纯C代码，颜色越深表示可优化内容越多，即使用的Python C-API越多。同样，在`setup.py`中设置`annotate`则会在编译同目录下生成独立的HTML文件用于分析。

### Faster code via static typing

Cython作为一个Python编译器，除了一些尚未支持的特殊情况下，可以在不做任何改变的情况下编译大部分常见Python代码。但是在某些对性能有重大影响的代码处，添加静态声明可以非常好的提升性能。使用静态声明运行Cython脱离Python动态解释的特性从而产出更加高速的C代码。有时这种方式可以达到几个数量级的提升。

使用类型声明会导致源码冗长从而降低可读性，因此不鼓励在没有充分理由的情况下使用他们。

所有的C类型都可以用于类型声明，包括整型(integer)，浮点型(floating point types)，复数(complex numbers)，结构体(structs)，集合(unions)和指针(pointer)。

**类型通过`cdef`关键字声明**。

注意在Jupyter Notebook中使用Cython一定要先加载Cython模块：

```Python
In [1]: %load_ext cython
```

以下是一段纯Python代码：

```Python
In [2]: def f(x):
   ...:     return x ** 2 - x
   ...:
   ...: def integrate_f(a, b ,N):
   ...:     s = 0
   ...:     dx = (b - a) / N
   ...:     for i in range(N):
   ...:         s += f(a + i * dx)
   ...:     return s * dx

In [3]: %time integrate_f(0, 5, 100000000)
CPU times: user 18.2 s, sys: 0 ns, total: 18.2 s
Wall time: 18.2 s
Out[3]: 29.1666661666685
```

如果只是对其进行编译处理：

```Python
In [4]: %%cython
   ...:
   ...: def f_c(x):
   ...:     return x ** 2 - x
   ...:
   ...: def integrate_f_c(a, b ,N):
   ...:     s = 0
   ...:     dx = (b - a) / N
   ...:     for i in range(N):
   ...:         s += f_c(a + i * dx)
   ...:     return s * dx

In [5]: %time integrate_f_c(0, 5, 100000000)
CPU times: user 11.4 s, sys: 0 ns, total: 11.4 s
Wall time: 11.5 s
Out[5]: 29.1666661666685
```

可以看到已经有了35%左右的提升。

如果加上静态类型声明：

```Python
In [6]: %%cython
   ...:
   ...: def f_cc(double x):
   ...:     return x ** 2 - x
   ...:
   ...: def integrate_f_cc(double a, double b ,long N):
   ...:     cdef int i
   ...:     cdef double s = 0
   ...:     cdef double dx = (b - a) / N
   ...:     for i in range(N):
   ...:         s += f_cc(a + i * dx)
   ...:     return s * dx

In [7]: %time integrate_f_cc(0, 5, 100000000)
CPU times: user 3.77 s, sys: 0 ns, total: 3.77 s
Wall time: 3.79 s
Out[7]: 29.1666661666685
```

可以看到已经有超过4倍的提升。

由于在Python中进行函数调用会有很大的开销，在Cython中这样的开销会加倍，因为在函数`f_cc()`中，函数在内部和被调用时都是C语言的`double`类型，但是必须构造一个Python的`float`对象才能将其传递给Python函数进行调用。因此，Cython提供了声明C语言风格函数的语法，同样是使用`cdef`关键字声明函数：

```Python
In [8]: %%cython
   ...:
   ...: cdef double f_ccc(double x) except *:
   ...:     return x ** 2 - x
   ...:
   ...: def integrate_f_ccc(double a, double b ,long N):
   ...:     cdef int i
   ...:     cdef double s = 0
   ...:     cdef double dx = (b - a) / N
   ...:     for i in range(N):
   ...:         s += f_ccc(a + i * dx)
   ...:     return s * dx

In [9]: %time integrate_f_ccc(0, 5, 100000000)
CPU times: user 125 ms, sys: 0 ns, total: 125 ms
Wall time: 122 ms
Out[9]: 29.1666661666685
```

此时可以看到，相比原始代码加速已经超过150倍。注意在声明函数`f_ccc`时，加上了异常捕捉。文档中提供的方式为`cdef double f(double x) except? -2`，即如果返回值为-2则检查错误，同时`?`表示`-2`也可能是有效的返回值。而使用相对略慢的`except *`会更为安全。

**cdef的副作用是Python空间不再提供该函数。**

```Python
In [10]: f(5)
Out[10]: 20

In [11]: f_c(5)
Out[11]: 20

In [12]: f_cc(5)
Out[12]: 20.0

In [13]: f_ccc(5)
NameError: name 'f_ccc' is not defined
```

可以看到，调用使用`cdef`声明的函数`f_ccc()`会抛出`NameError`。

解决这个问题的方法是使用`cpdef`关键字替代`cdef`关键字。`cpdef`会创建一个Python包装器，使其可以同时对Cython和Python可见。这种方式会略微增加一定的开销。

## Tutorials

### Basic Tutorial

Cython是具有C数据类型的Python，几乎任何Python代码都是有效的Cython代码。由于参数和变量可以声明为C的数据类型，因此Python和C的值可以在代码中自由混合。即使在操作C的数据类型时，也可以使用Python的特性如`try-except`等功能。

正如前文所说，通过源码写入`.pyx`脚本，创建`setup.py`脚本进行编译，在命令行中使用`python setup.py build_ext --inplace`可以生成Linux中的`.so`文件，或Windows中的`.pyd`文件。随后就可以像使用普通Python模块一样导入。

如果模块不需要任何额外的C库或特殊的构建设置，那么使用`pyximport`模块可以在导入时直接加载`.pyx`文件，而无需使用`setup.py`：

```Python
In [1]: import pyximport

In [2]: pyximport.install()
Out[2]: (None, <pyximport.pyximport.PyxImporter at 0x7fb61b10d8e0>)

In [3]: import hello

In [4]: hello.say_hello_to('World!')
Hello, World!
```

`pyximport`模块主要用于实验性的编译，不推荐在最终构建代码时使用。

文档中使用了一个查找素数的示例：

```Python
def primes(int nb_primes):
    cdef int n, i, len_p
    cdef int p[1000]
    if nb_primes > 1000:
        nb_primes = 1000

    len_p = 0  # The current number of elements in p.
    n = 2
    while len_p < nb_primes:
        # Is n prime?
        for i in p[:len_p]:
            if n % i == 0:
                break

        # If no break occurred in the loop, we have a prime.
        else:
            p[len_p] = n
            len_p += 1
        n += 1

    # Let's return the result in a python list:
    result_as_list  = [prime for prime in p[:len_p]]
    return result_as_list
```

在这里，由于不确定数组的长度，程序在调用栈上创建了一个长度1000的数组，这并不是一个管理内存的好方式。在后续内容中会讨论动态分配数组的内容。程序使用了切片操作以避免遍历数组的全部元素，同时使用了Python的`for-else`特性。最后，由于Python无法读取C数组，因此Cython将其转换为Python数据类型，这里使用了列表解析式将C的`int`值复制进一个由Python `int`组成的列表中。当然也可以手动迭代C数组然后使用`list.append()`方法。

Cython同样可以使用C++，特别是C++标准库的一部分内容可以直接通过Cython导入。在上例中，使用C语言没有对内存进行动态分配，而在C++中，提供了`Vector`容器可以动态分配数组的大小，此外还提供了`reserve()`方法供预先知道数组大小时使用。因此，可以如下组织代码：

```Python
# distutils: language=c++
from libcpp.vector cimport vector
def primes(unsigned int nb_primes):
    cdef int n, i
    cdef vector[int] p
    p.reserve(nb_primes)  # allocate memory for 'nb_primes' elements.
    n = 2
    while p.size() &lt; nb_primes:  # size() for vectors is similar to len()
        for i in p:
            if n % i == 0:
                break
        else:
            p.push_back(n)  # push_back is similar to append()
        n += 1
    # Vectors are automatically converted to Python
    # lists when converted to Python objects.
    return p
```

基于示例，尝试自己写了Python, Cython(C++)和C++的实现如下：

```Python
# Filename: prime.py
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
    # print(lst)


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
    # print(lst)
```

```Python
# Filename: prime_cpp.pyx
from libcpp.vector cimport vector

def prime_cpp(unsigned int num):
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
    # print(lst)
```

```C++
#include <iostream>
#include <vector>
#include <chrono>

class PRIME
{
    public:
        PRIME();
        PRIME(unsigned int n);
        ~PRIME(){};
        void calculate();
        void show();
    private:
        std::vector<unsigned int> list;
        unsigned int num;
};

PRIME::PRIME(unsigned int n)
{
    num = n;
}

void PRIME::calculate()
{
    unsigned int i = 2;
    unsigned int limit;
    bool test = true;
    while (list.size() < num)
    {
        if (2 > i / 2 + 1)
        {
            limit = i;
        }
        else
        {
            limit = i / 2 + 1;
        }
        for (unsigned int d = 2; d < limit; ++d)
        {
            if (i % d == 0)
            {
                test = false;
                break;
            }
            else
            {
                test = true;
            }
        }
        if (test)
        {
            list.push_back(i);
        }
        i++;
    }
}

void PRIME::show()
{
    for (long unsigned int i = 0; i < list.size(); ++i)
    {
        std::cout << list[i] << " ";
    }
    std::cout << std::endl;
}

int main()
{
    std::cout << "Enter the numbers of primes: ";
    unsigned int num;
    std::cin >> num;
    auto start = std::chrono::system_clock::now();
    PRIME data = PRIME(num);
    data.calculate();
    // data.show();
    auto end = std::chrono::system_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    std::cout << "Time costs: " << duration.count()  << " us" << std::endl;
}
```

分别编译执行后可以看到结果如下：

原生Python代码：

```Bash
$ python3 -m timeit -s "from prime import primes_1" "primes_1(1000)"
5 loops, best of 5: 83.3 msec per loop
```

Cython代码：

```Bash
$ python3 -m timeit -s "from prime_cpp import prime_cpp" "prime_cpp(1000)"
50 loops, best of 5: 4.22 msec per loop
```

C++代码：

```Bash
$ g++ prime.cpp -o prime
$ ./prime
Enter the numbers of primes: 1000
Time costs: 4296 us
```

可以看到使用Cython加速的代码效率和C++非常接近，达到原生代码的20倍。

### Calling C functions

### Using C libraries

### Extension types (aka. cdef classes)

### pxd files

### Caveats

### Profiling

### Unicode and passing strings

### Memory Allocation

### Embedding Cython modules in C/C++ applications

### Pure Python Mode

### Working with NumPy

### Working with Python arrays

### Further reading

### Related work

## Users Guide

### Language Basics

### Extension Types

### Special Methods of Extension Types

### Sharing Declarations Between Cython Modules

### Interfacing with External C Code

### Source Files and Compilation

### Early Binding for Speed

### Using C++ in Cython

### Fused Types (Templates)

### Porting Cython code to PyPy

### Migrating from Cython 0.29 to 3.0

### Limitations

### Differences between Cython and Pyrex

### Typed Memoryviews

### Implementing the buffer protocol

### Using Parallelism

### Debugging your Cython program

### Cython for NumPy users

### Pythran as a NumPy backend
