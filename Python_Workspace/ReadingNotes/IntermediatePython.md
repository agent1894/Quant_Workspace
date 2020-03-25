# Intermediate Python by @yasoob

本书已开源[GitHub](https://github.com/yasoob/intermediatePython)

译者：老高 @spawnris 刘宇 @liuyu 明源 @muxueqz 大牙 @suqi 蒋委员长  @jiedo，译本已开源[GitHub](https://github.com/eastlakeside/interpy-zh)

- [Intermediate Python by @yasoob](#intermediate-python-by-yasoob)
  - [`*args`和`**kwargs`](#args%e5%92%8ckwargs)
  - [调试(Debugging)](#%e8%b0%83%e8%af%95debugging)
  - [生成器(Generators)](#%e7%94%9f%e6%88%90%e5%99%a8generators)
  - [`Map`, `Filter`和`Reduce`](#map-filter%e5%92%8creduce)
  - [`set`数据结构](#set%e6%95%b0%e6%8d%ae%e7%bb%93%e6%9e%84)
  - [三元运算符](#%e4%b8%89%e5%85%83%e8%bf%90%e7%ae%97%e7%ac%a6)
  - [装饰器](#%e8%a3%85%e9%a5%b0%e5%99%a8)
  - [`Global`和`Return`](#global%e5%92%8creturn)
  - [对象变动`Mutation`](#%e5%af%b9%e8%b1%a1%e5%8f%98%e5%8a%a8mutation)
  - [`__slots__`魔法](#slots%e9%ad%94%e6%b3%95)
  - [虚拟环境](#%e8%99%9a%e6%8b%9f%e7%8e%af%e5%a2%83)
  - [容器(Collections)](#%e5%ae%b9%e5%99%a8collections)
  - [枚举(Enumerate)](#%e6%9e%9a%e4%b8%beenumerate)
  - [对象自省](#%e5%af%b9%e8%b1%a1%e8%87%aa%e7%9c%81)
  - [推导式(Comprehension)](#%e6%8e%a8%e5%af%bc%e5%bc%8fcomprehension)
  - [异常](#%e5%bc%82%e5%b8%b8)
  - [`lambda`表达式](#lambda%e8%a1%a8%e8%be%be%e5%bc%8f)
  - [一行式](#%e4%b8%80%e8%a1%8c%e5%bc%8f)
  - [`For` - `Else`](#for---else)
  - [使用C拓展](#%e4%bd%bf%e7%94%a8c%e6%8b%93%e5%b1%95)
  - [`open`函数](#open%e5%87%bd%e6%95%b0)
  - [目标Python2+3](#%e7%9b%ae%e6%a0%87python23)
  - [协程](#%e5%8d%8f%e7%a8%8b)
  - [函数缓存](#%e5%87%bd%e6%95%b0%e7%bc%93%e5%ad%98)
  - [上下文管理器](#%e4%b8%8a%e4%b8%8b%e6%96%87%e7%ae%a1%e7%90%86%e5%99%a8)

## `*args`和`**kwargs`

`*args`和`**kwargs`都是在函数定义中传入不定长参数。在这其中，只有`*`是必须的，args和kwargs只是约定俗成的写法。`*args`传入非键值对的参数，生成的`args`是一个**元组**，而`**kwargs`是将不定长度的键值对作为参数传入函数，尽管处理的是键值对，但是并不是说明传入的是一个字典，相反，生成的`kwargs`才是一个字典：

```Python
In [1]: def kwargs(**kwargs):
   ...:     print(type(kwargs))
   ...:     for arg in kwargs:
   ...:         print("key: ", arg, "value: ",kwargs[arg])

In [2]: kwargs(arg1=0, arg2="Hello World", arg3=list("string"))
<class 'dict'>
key:  arg2 value:  Hello World
key:  arg3 value:  ['s', 't', 'r', 'i', 'n', 'g']
key:  arg1 value:  0
```

另一个可行的用法是使用`*args`和`**kwargs`给函数传递参数，而非在函数定义中使用：

```Python
In [3]: def test_args_kwargs(arg1, arg2, arg3):
   ...:     print("arg1: ", arg1)
   ...:     print("arg2: ", arg2)
   ...:     print("arg3: ", arg3)

In [4]: args = ("two", 3, 5)

In [5]: test_args_kwargs(*args)
arg1:  two
arg2:  3
arg3:  5

In [6]: kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}

In [7]: test_args_kwargs(**kwargs)
arg1:  5
arg2:  two
arg3:  3
```

无论是在函数定义中，还是在函数中使用， 应当使用的顺序是：`some_func(fargs, *args, **kwargs)`。

## 调试(Debugging)

尽管现在有成熟的IDE支持调试等功能，但是传统的pdb(Python debugger)调试仍然需要了解。

在命令行可以直接调用pdb：

```Bash
python -m pdb mu_script.py
```

但是更常见的方式是在脚本内部运行：

```Python
In [1]: import pdb

In [2]: def make_bread():
    ...:     pdb.set_trace()
    ...:     return "I don't have time"

In [3]: print(make_bread())
> <ipython-input-10-8ed93f9d8af5>(3)make_bread()
-> return "I don't have time"
(Pdb) c
I don't have time
```

这种方式会直接进入调试模式。一些常见的命令需要了解：

- `c`：继续执行
- `w`：显示当前执行代码上下文
- `a`：打印当前参数列表
- `s`：单步进入(`s`tep)
- `n`：单步跳过(`n`ext)

## 生成器(Generators)

了解生成器需要能够区分可迭代对象(iterable)，迭代器(iteration)。

简单来说，所有实现了返回**迭代器**的`__iter__`方法的对象或者定义了支持下标索引的`__getitem__`方法的就是**可迭代对象**，而定义了`__iter__`和`__next__`（Python2使用`next`）方法的对象就是**迭代器**。迭代器的`__iter__`返回其自身`self`，`__next__`提供了返回迭代器下一个值的方法，并在结尾处抛出`StopIteration`异常。获取迭代器的下一个方法可以使用`next(Iterator)`方法或`Iterator.__next__()`方法。

因此，**迭代器一定是可迭代对象**，因为迭代器一定有`__iter__`方法。由于可迭代对象可能只实现了`__getitem__`方法，所以可迭代对象不一定是迭代器。实际上，迭代器是可迭代对象的子类。例如，`str`是可迭代对象，但是并不是一个迭代器：

```Python
In [1]: string = "This is a string."

In [2]: next(string)
TypeError: 'str' object is not an iterator
```

但是可以使用内置函数`iter()`，根据一个可迭代对象返回迭代器对象：

```Python
In [3]: string_iter = iter(string)

In [4]: next(string_iter)
Out[4]: 'T'

In [5]: next(string_iter)
Out[5]: 'h'

In [6]: next(string_iter)
Out[6]: 'i'

In [7]: next(string_iter)
Out[7]: 's'
```

生成器是一种特殊的迭代器。对于生成器，只能对其迭代一次。在生成器中，并不会将函数的结果一次性全部产出，相反，则会保留当时的状态，并在下一次运行时继续。需要通过遍历来使用生成器，一般用`for`进行循环，或者将其传入任何支持迭代的函数中，也可以使用`next()`方法逐一获取其中的元素。

创建生成器最简单的方式是在列表推导式中将`[]`改为`()`，即生成器表达式，但是更为常用的方式是在函数定义中使用`yield`关键字，即生成器函数。例如：

```Python
In [8]: def generator(n):
   ...:     i = 0
   ...:     while i < n:
   ...:         yield i * 2 + 1
   ...:         i += 1

In [9]: obj = generator(10)

In [10]: for item in obj:
   ...:     print(item)
1
3
5
7
9
11
13
15
17
19
```

在生成器函数中，函数会在`yield`关键字处暂停并返回值，在下一次迭代开始时从yield下继续进行。这种方式没有将所有的结果一次性导入内存中，而是在程序运行的过程中生成结果，从而可以有效的节省资源。

注意，由于生成器只能迭代一次，因此，如果试图再次使用之前的对象，会直接抛出`StopIteration`异常。由于`for`循环会自动捕捉`StopIteration`异常并停止调用`next()`，因此如果试图再次使用`for`循环不会得到任何结果。

```Python
In [11]: next(obj)
StopIteration:
```

> Python3中yield理解与使用（一遍就懂系列，绝不反驳）[CSDN](https://blog.csdn.net/u011318077/article/details/93749143?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task)
>
> python 生成器和迭代器有这篇就够了 [CSDN](https://blog.csdn.net/weixin_30416497/article/details/99356788?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task)

检查一个对象是否是可迭代对象或迭代器，需要导入`collections`库：

```Python
In [12]: from collections import Iterator, Iterable

In [13]: isinstance(string, Iterator)
Out[13]: False

In [14]: isinstance(string, Iterable)
Out[14]: True

In [15]: isinstance(string_iter, Iterator)
Out[15]: True

In [16]: isinstance(string_iter, Iterable)
Out[16]: True
```

## `Map`, `Filter`和`Reduce`

`map`，`filter`，`reduce`主要用来处理函数式编程相关的操作。

`map`将函数映射至输入的一个可迭代对象后返回，其基本格式为：

```Python
map(function_to_apply, list_of_inputs)
```

通常会使用匿名函数`lambda`配合`map`，甚至可迭代对象可以是函数的列表：

```Python
In [1]: def multiply(x):
    ...:     return x * x

In [2]: def add(x):
    ...:     return x + x

In [3]: funcs = [multiply, add]

In [4]: for i in range(5):
    ...:     value = map(lambda x: x(i), funcs)
    ...:     print(list(value))
[0, 0]
[1, 2]
[4, 4]
[9, 6]
[16, 8]
```

`filter`使用和`map`相同的格式，会对传入可迭代对象的元素进行过滤，并返回所有符合要求的元素。这里`filter`类似于`for`循环，但是由于是内置函数，所以有更好的性能。

```Python
In [5]: number_list = range(-5, 5)

In [6]: less_than_zero = filter(lambda x: x < 0, number_list)

In [7]: print(list(less_than_zero))
[-5, -4, -3, -2, -1]
```

由于Python3中`map`，`filter`会返回迭代器，因此需要使用`list`进行转换。

Python3中将`reduce`从内置函数中移除，如果需要使用必须导入：

```Python
In [8]: from functools import reduce
```

> [廖雪峰](https://www.liaoxuefeng.com/wiki/1016959663602400/1017329367486080) `reduce`会把一个函数作用在一个序列上，这个函数必须接受两个参数，然后`reduce`把结果继续和序列的下一个元素做累积计算，其效果就是：`reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)`

## `set`数据结构

`set`是一种无序不重复的数据结构。

创建空集合必须使用`set()`而不能使用`{}`，大括号创建的是一个字典。

使用`set_x.intersecton(set_y)`可以得出两个集合的交集，使用`set_x.difference(set_y)`可以得出两个集合的差集，也可以用`set_x & set_y`计算交集，`set_x | set_y`计算并集，`set_x - set_y`计算差集。

## 三元运算符

常用的三元表达式为 `condition_is_true if condition else condition_is_false`。

还有一种元组条件表达式：`(if_test_is_false, if_test_is_true)[test]`

这种方式较为晦涩，且性能较弱，不推荐使用。

## 装饰器

装饰器可以在不修改原有函数的基础上，增加或改变函数的功能。由于在python中一切皆对象，函数本身也可以赋值给一个变量。同时，由于函数内部可以嵌套函数，因此在函数内部定义另一个函数或返回一个函数，都是合法的。

在外部函数调用内部函数时，返回时使用`return inner_function()`则会在返回时调用内部函数，而使用`return inner_function`则会返回函数本身，此时这个函数可以被传递至其他地方，或赋值给别的变量而不去执行。

对于装饰器来说，装饰器接收一个函数作为参数，其返回值也是一个函数对象。

在没有`@`语法糖时，装饰器需要通过如下方式实现：

```Python
In [1]: def decorator(func):
    ...:
    ...:     def wrapper():
    ...:         print("Before func()")
    ...:         func()
    ...:         print("After func()")
    ...:
    ...:     return wrapper

In [2]: def function_requiring_decoration():
    ...:     print("The function requiring decoration")

In [3]: function_requiring_decoration()
The function requiring decoration

In [4]: new_function = decorator(function_requiring_decoration)

In [5]: new_function()
Before func()
The function requiring decoration
After func()
```

在这个例子中，装饰器对传入的函数进行了封装，并返回了装饰器函数本身。使用`@`语法糖之后，代码实现为：

```Python
In [6]: @decorator
    ...: def function_requiring_decoration():
    ...:     """This function is under a decorator"""
    ...:     print("The function requiring decoration")

In [7]: function_requiring_decoration()
Before func()
The function requiring decoration
After func()
```

在这里使用一个例子讨论装饰器的工作机制。当使用`__name__`打印被装饰函数的函数名时，显示的是装饰器的函数名：

```Python
In [8]: print(function_requiring_decoration.__name__)
wrapper
```

这种情况是不符合预期的。原因在于使用装饰器之后会对被装饰函数的名称和注释文档进行覆盖。因此，如果需要解决这个问题，需要导入`functools.wraps`：

```Python
In [9]: from functools import wraps

In [10]: def new_decorator(func):
    ...:
    ...:     @wraps(func)
    ...:     def wrapper():
    ...:         print("Before func()")
    ...:         func()
    ...:         print("After func()")
    ...:
    ...:     return wrapper

In [11]: @new_decorator
    ...: def function_requiring_decoration():
    ...:     """This function is under a decorator"""
    ...:     print("The function requiring decoration")

In [12]: function_requiring_decoration()
Before func()
The function requiring decoration
After func()

In [13]: print(function_requiring_decoration.__name__)
function_requiring_decoration

In [14]: print(function_requiring_decoration.__doc__)
This function is under a decorator
```

`@wraps`接受一个函数进行装饰，会使用传入函数的名称，注释文档，参数列表等。

因此，一个装饰器的应用模板应该为：

```Python
from functools import wraps

def decorator_name(f):

    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)

    return decorated

@decorator_name
def func():
    return("Function is running")

can_run = True
print(func())
# Output: Function is running

can_run = False
print(func())
# Output: Function will not run
```

> [说说Python中的闭包](https://www.cnblogs.com/cicaday/p/python-closure.html)
>
> [详解Python的装饰器](https://www.cnblogs.com/cicaday/p/python-decorator.html)
>
> [Python中装饰器超详细讲解,看不懂尽管来砍我!](https://blog.csdn.net/weixin_44014228/article/details/85268112?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task)
>
> [Python装饰器的实现和万能装饰器](https://blog.csdn.net/weixin_43790276/article/details/90728864?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task)

## `Global`和`Return`

## 对象变动`Mutation`

## `__slots__`魔法

## 虚拟环境

## 容器(Collections)

## 枚举(Enumerate)

## 对象自省

## 推导式(Comprehension)

## 异常

## `lambda`表达式

## 一行式

## `For` - `Else`

## 使用C拓展

## `open`函数

## 目标Python2+3

## 协程

## 函数缓存

## 上下文管理器
