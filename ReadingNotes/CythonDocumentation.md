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

Cython同样可以很简单的调用C标准库的函数，只需要使用`from libc.stdlib cimport`即可，这种方式同样可以导入C++标准库。

同时，Cython也提供了C数学库的声明，可以直接调用：

```Python
from libc.math cimport sin

cdef double f(double x):
    return sin(x * x)
```

在某些环境下，`libc.math`可能没有创建动态链接，因此需要配置动态库。同时，对于一些没有默认提供声明的C/C++代码，需要自行声明。在这里文档讲述的比较模糊，查找资料后详细分析如下：

首先，需要对静态库和动态库有一个基本的理解，静态库的代码在编译过程中被直接载入可执行文件，因此速度快，体积大；动态库则在可执行文件运行时才被载入，在编译过程中仅作为引用，因此体积小，速度慢。

先试着使用C++写一个简单的函数：

```C++
// Filename: userFunc.h
double addSquare(double x, double y);
void sayHello();
void sayBye();

// Filename: userFunc.cpp
#include <iostream>
#include "userFunc.h"

double addSquare(double x, double y)
{
    return x * x + y * y;
}

void sayHello()
{
    std::cout << "Hello World!" << std::endl;
}

void sayBye()
{
    std::cout << "Bye!" << std::endl;
}
// Filename: main.cpp
#include "userFunc.h"
#include <iostream>

int main()
{
    sayHello();
    double x, y;
    std::cout << "Enter x: ";
    std::cin >> x;
    std::cout << "Enter y: ";
    std::cin >> y;
    double result = addSquare(x, y);
    std::cout << "The sum of x^2 and y^2 is: " << result << std::endl;
    sayBye();

    return 0;
}
```

这个程序当然可以简单的直接编译链接并生成可执行文件：

```Bash
$ g++ userFunc.cpp main.cpp -o main_simple.bin
$ ./main_simple.bin
Hello World!
Enter x: 2
Enter y: 5
The sum of x^2 and y^2 is: 29
Bye!
$ rm main_simple.bin
```

但是如果需要将源码生成动态链接，则不能这样操作，而应该先进行单独编译：

```Bash
g++ -fPIC -shared userFunc.cpp -o libuserFunc.so
```

在这里，`-fPIC`表示生成与位置无关代码，`-shared`表示制作动态库，如果不加上则无法进行链接。所谓与位置无关的代码（PIC: Position Independent Code）是指产生的代码不包含对函数和变量具体内存位置的引用，因为编译动态库的当下是不知道使用这段代码的程序会将其链接至哪一段内存空间。

需要注意的是，无论动态库还是静态库，都有命名规范，即以`lib`为前缀，紧接库名，如果是静态库则扩展名为`.a`，如果是动态库则扩展名为`.so`。

创建完成动态库后，就可以链接动态库并生成可执行文件：

```Bash
$ g++ main.cpp -L . -I . -l userFunc -o execute.bin
$ ./execute.bin
./execute.bin: error while loading shared libraries: libuserFunc.so: cannot open shared object file: No such file or directory
```

链接时，`-L`指出动态库的路径，`-L .`即说明动态库路径可能在当前目录下，`-I`指出头文件的路径，同样`-I .`说明头文件路径可能在当前目录下，`-l`指出动态库名称，注意需要去掉前缀的`lib`和扩展名`.so`。

当成功生成可执行文件`execute.bin`后，运行时发现报错，显示并没有这个库。此时可以使用`ldd`命令查看某个可执行文件所链接的动态库：

```Bash
$ ldd execute.bin
linux-vdso.so.1 (0x00007ffffeeb9000)
libuserFunc.so => not found
libstdc++.so.6 => /lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007fc8206b0000)
libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fc8204b0000)
libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007fc820361000)
/lib64/ld-linux-x86-64.so.2 (0x00007fc8208b5000)
libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007fc820340000)
```

发现确实是`libuserFunc.so`这个库没有找到。导致这个问题的原因在于，程序在执行时，会查找需要的动态库文件，如果找到则载入动态库，否则报错。系统内动态库默认搜索路径为`/usr/lib/`和`/lib`，显然，最简单的方式是将刚刚生成的动态库移动到该目录下。但是由于这个操作需要`sudo`权限且风险较大，因此不推荐使用这种方式。

除此以外，编译器会查找环境变量`LD_LIBRARY_PATH`所指定的目录，因此，将当前路径加入这个环境变量即可解决这个问题：

```Bash
export LD_LIBRARY_PATH=$(pwd)
```

这种方法只在当前终端下有效，如果希望永久有效，将其写入`.bashrc`中。

另一种方式是将`.so`文件的绝对路径追加如`/etc/ld.so.conf`文件中并使用`sudo ldconfig -v`更新，但是同样需要`sudo`权限。

最后一种方式是直接在编译时指定所需要的查找路径，在编译时加入参数`-Wl,-rpath=.`即可完成这个任务，同时不需要修改环境变量：

```Bash
$ g++ main.cpp -L . -I . -l userFunc -Wl,-rpath=. -o execute.bin
$ ./execute.bin
Hello World!
Enter x: 2
Enter y: 3
The sum of x^2 and y^2 is: 13
Bye!
```

需要特别注意的是，`-Wl,-rpath=.`中间没有空格，后面没有`,`，如果不小心加入逗号，会出现`/usr/bin/ld: cannot find : No such file or directory`报错。

理解了以上的内容之后，便可以使用Cython编译自己的C/C++程序：

```Python
# Filename: user.pyx
# distutils:language = c++

cdef extern from "userFunc.h":
    cpdef double addSquare(double x, double y)
```

`setup.up`相当于`makefile`，指导Cython的编译过程，因此内容为：

```Python
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

ext_modules = [
    Extension(
        name='generate',
        sources=['user.pyx'],
        include_dirs=['.'],  # gcc -I
        library_dirs=['.'],  # gcc -L
        libraries=['userFunc'],  # gcc -l
        language='c++',
        extra_link_args=['-Wl,-rpath=.'])
]

setup(ext_modules=cythonize(ext_modules))
```

如注释所说，`include_dirs`相当于编译时的`-I`，`library_dirs`相当于编译时的`-L`，`libraries`相当于编译时的`-l`。这里需要特别注意的是，指定动态库查找路径的参数并不是`extra_compile_args`而是**`extra_link_args`**。

因为`.pyx`脚本中使用了`cpdef`关键字，因此运行后得到的`.so`文件就可以在Python中正常使用：

```Python
>>> import generate
>>> generate.addSquare(2, 5)
29.0
```

回过来看到文档中提到的对于数学库的动态链接，此时可以明白，由于数学库的动态库名称为`libm.so`，因此当没有支持链接时，需要加入`libraries=["m"]`参数进行编译，否则会出现无法找到动态库的错误。

参考资料：

> Linux基础——gcc编译、静态库与动态库（共享库）[CSDN](https://blog.csdn.net/daidaihema/article/details/80902012)
>
> Linux下gcc生成和使用静态库和动态库详解[CSDN](https://blog.csdn.net/CSqingchen/article/details/51546784)
>
> Linux共享库和动态链接[CSDN](https://blog.csdn.net/zd845101500/article/details/95891335)
>
> cython的使用[CSDN](https://blog.csdn.net/daniel_ustc/article/details/77622895)
>
> Cython 基本用法[知乎](https://zhuanlan.zhihu.com/p/24311879?utm_medium=social&utm_source=wechat_session&from=singlemessage&isappinstalled=1)
>
> I don't understand -Wl,-rpath -Wl, [StackOverflow](https://stackoverflow.com/questions/6562403/i-dont-understand-wl-rpath-wl)
>
> /usr/bin/ld: cannot find : No such file or directory [StackOverflow](https://stackoverflow.com/questions/20616961/usr-bin-ld-cannot-find-no-such-file-or-directory)
>
> Linux动态库(.so)搜索路径[cnblogs](http://www.cnitblog.com/windone0109/archive/2008/04/23/42653.html#2108)

### Using C libraries

除了编写代码更快以外，Cython的一个主要功能就是在Python中调用外部C库。因为Cython会将代码编译为C，因此直接调用C函数非常方便。文档中举出一个案例，需要在一个FIFO的队列中存储整型数值，因为要考虑内存问题同时这个数值来自于C，因此无法在Python列表或队列中存储`int`类型，所以需要考虑C的队列实现。

在CAlg(C-algorithms)库中有相应实现，可以将其封装在Python扩展类型中。

首先确定队列的C实现API，在头文件`c-algorithms/src/queue.h`中可以看到其定义：

```C
/* queue.h */

typedef struct _Queue Queue;
typedef void *QueueValue;

Queue *queue_new(void);
void queue_free(Queue *queue);

int queue_push_head(Queue *queue, QueueValue data);
QueueValue queue_pop_head(Queue *queue);
QueueValue queue_peek_head(Queue *queue);

int queue_push_tail(Queue *queue, QueueValue data);
QueueValue queue_pop_tail(Queue *queue);
QueueValue queue_peek_tail(Queue *queue);

int queue_is_empty(Queue *queue);
```

要在Cython中使用，首先要创建`.pxd`文件并对C API重新定义。例如创建`cqueue.pxd`：

```Python
# cqueue.pxd

cdef extern from "c-algorithms/src/queue.h":
    ctypedef struct Queue:
        pass
    ctypedef void* QueueValue

    Queue* queue_new()
    void queue_free(Queue* queue)

    int queue_push_head(Queue* queue, QueueValue data)
    QueueValue  queue_pop_head(Queue* queue)
    QueueValue queue_peek_head(Queue* queue)

    int queue_push_tail(Queue* queue, QueueValue data)
    QueueValue queue_pop_tail(Queue* queue)
    QueueValue queue_peek_tail(Queue* queue)

    bint queue_is_empty(Queue* queue)
```

可以看见，`.pxd`中的声明和`.h`头文件中的声明基本是一致的，同时，也不需要提供所有头文件中的声明，只要声明代码中需要的即可。

在上述声明中需要注意的是第一行中结构体`Queue`的声明。在头文件`.h`中，`Queue`结构体是一个不透明句柄，即使用了`typedef`将实现放在`.c`源文件中，从而将结构体的实现细节进行隐藏，只有被调用的库知道具体实现。由于在Cython中的代码不需要知道结构体的内容，因此不需要对其进行声明，只需要使用一个空的定义即可。

`cdef struct Queue: pass`和`ctypedef struct Queue: pass`存在细微差别。前者在C中被因为用`struct Queue`，后者在C中被引用为`Queue`，通常后者更为常用。

另一个例外是最后一行。`queue_is_empty()`函数返回的是一个C的布尔值以表示队列是否为空。这个类型在Cython中最好使用`bint`类型表示，这在C中使用的是普通的`int`类型，但是在转换Python对象时会将其对应为Python的布尔值`True/False`。

对于每一个使用的库，都应该对应定义一个`.pxd`文件，甚至如果API很大的情况下，每个头文件都要对应一个`.pxd`文件。

如果需要使用C标准库中的文件，或直接从CPython中调用C-API函数，对于这类常见的需求，Cython附带了一组标准的`.pxd`文件。主要的包为`cpython`，`libc`和`libcpp`。NumPy还提供了一个`.pxd`文件`numpy`。

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
