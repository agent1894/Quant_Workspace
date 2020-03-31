# Intermediate Python by @yasoob

本书已开源[GitHub](https://github.com/yasoob/intermediatePython)

译者：老高 @spawnris 刘宇 @liuyu 明源 @muxueqz 大牙 @suqi 蒋委员长  @jiedo，译本已开源[GitHub](https://github.com/eastlakeside/interpy-zh)

使用Python 3编程环境。

读后感受：本书适合对Python有一定基础知识的读者补充一些进阶性的技巧。这些技巧通常是不常见的，甚至是没有之前没有想过的。本书每一章节都比较短小，优点是同样篇幅下涉及的知识概念较多，但是同样导致深度不足，讲解不够细致，很多示例没有连贯的逻辑，需要读者额外查阅相关资料进行理解。综上，是一本不错的小品级书籍，适当阅读即可。对于我个人而言，关于`__slots__`，容器，自省，协程和函数缓存的内容是我之前没有了解过的新知识。

- [Intermediate Python by @yasoob](#intermediate-python-by-yasoob)
  - [`*args`和`**kwargs`](#args%e5%92%8ckwargs)
  - [调试(Debugging)](#%e8%b0%83%e8%af%95debugging)
  - [生成器(Generators)](#%e7%94%9f%e6%88%90%e5%99%a8generators)
  - [`Map`, `Filter`和`Reduce`](#map-filter%e5%92%8creduce)
  - [`set`数据结构](#set%e6%95%b0%e6%8d%ae%e7%bb%93%e6%9e%84)
  - [三元运算符](#%e4%b8%89%e5%85%83%e8%bf%90%e7%ae%97%e7%ac%a6)
  - [装饰器](#%e8%a3%85%e9%a5%b0%e5%99%a8)
  - [`Global`和`Return`](#global%e5%92%8creturn)
  - [对象变动(Mutation)](#%e5%af%b9%e8%b1%a1%e5%8f%98%e5%8a%a8mutation)
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

关于装饰器的案例，书中给出两个示范，分别是使用装饰器进行授权验证(authorization)：

```Python
from functools import wraps

def requires_auth(f):

    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            authenticate()
        return f(*args, **kwargs)

    return decorated
```

日志记录(logging)：

```Python
from functools import wraps

def logit(func):

    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return with_logging

@logit
def addition_func(x):
   """Do some math."""
   return x + x


result = addition_func(4)
# Output: addition_func was called
```

装饰器同样可以接收参数，这需要再对函数进行一层包装。相关思路需要仔细理解闭包的原理。

不带有参数的装饰器实际接收了被装饰的函数对象作为参数，如果需要对装饰器传入参数，则需要通过再外一层函数来接收参数。根据函数嵌套的概念，需要先执行外部函数，然后执行内部函数。书中同样使用记录日志的程序作为示例：

```Python
from functools import wraps

def logit(logfile='out.log'):

    def logging_decorator(func):

        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile，并写入内容
            with open(logfile, 'a') as opened_file:
                # 现在将日志打到指定的logfile
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)

        return wrapped_function

    return logging_decorator

@logit()
def myfunc1():
    pass

myfunc1()
# Output: myfunc1 was called
# 现在一个叫做 out.log 的文件出现了，里面的内容就是上面的字符串

@logit(logfile='func2.log')
def myfunc2():
    pass

myfunc2()
# Output: myfunc2 was called
# 现在一个叫做 func2.log 的文件出现了，里面的内容就是上面的字符串
```

除了使用函数以外，类也可以用来构建装饰器，即类装饰器。使用类装饰器需要实现`__init__`方法和`__call__`方法，`__init__`方法接收被装饰函数，`__call__`方法添加装饰器需要实现的功能。

一个类如果没有实现`__call__`方法， 则不能直接执行，会抛出异常。但是如果实现了`__call__`方法，则可以直接调用：

```Python
In [15]: class Demo(object):
    ...:     def __init__(self):
    ...:         pass

In [16]: demo = Demo()

In [17]: demo()
TypeError: 'Demo' object is not callable

In [18]: class Demo(object):
    ...:     def __init__(self):
    ...:         pass
    ...:     def __call__(self):
    ...:         print("Now this class is callable.")

In [19]: demo = Demo()

In [20]: demo()
Now this class is callable.
```

理解了类中`__call__`方法则可以理解类装饰器的原理。同样以记录日志为例，使用类装饰器：

```Python
from functools import wraps

class logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):

        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile并写入
            with open(self.logfile, 'a') as opened_file:
                # 现在将日志打到指定的文件
                opened_file.write(log_string + '\n')
            # 现在，发送一个通知
            self.notify()
            return func(*args, **kwargs)

        return wrapped_function

    def notify(self):
        # logit只打日志，不做别的
        pass
```

此时这个类装饰器`logit`已经可以像函数装饰器一样使用`@`。同时，继承了这个类的子类也能够产生装饰器的作用，同时子类也可以在`notify()`方法中实现更多的功能。

> 说说Python中的闭包[cnblogs](https://www.cnblogs.com/cicaday/p/python-closure.html)
>
> 详解Python的装饰器[cnblogs](https://www.cnblogs.com/cicaday/p/python-decorator.html)
>
> python装饰器简介---这一篇也许就够了[CSDN](https://blog.csdn.net/weixin_44014228/article/details/85268112?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task)
>
> Python装饰器的通俗理解[CSDN](https://blog.csdn.net/u013471155/article/details/68960244?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task)
>
> Python装饰器的实现和万能装饰器[CSDN](https://blog.csdn.net/weixin_43790276/article/details/90728864?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task)

## `Global`和`Return`

通常，函数内的变量的作用域仅在函数内部，但是如果使用`global`关键字，则会将变量的作用域修改为全局。这是一种不推荐的做法，因为会在全局作用域中引用太多冗余变量，造成不可控的后果。

此外需要注意的是，在函数外部定义的变量，进入函数内部如果出现同名变量，则会被内部变量所覆盖：

```Python
In [1]: globalPara = 10

In [2]: def add(x):
    ...:     globalPara += x
    ...:     print(globalPara)

In [3]: add(1)
UnboundLocalError: local variable 'globalPara' referenced before assignment
```

如果需要返回多个值，可以使用元组、列表、字典将多个变量组合，或者直接使用`return result1, result2, ...`，这是最好的方式。在任何情况下，尽量不要使用全局变量。

## 对象变动(Mutation)

Python作为解释性语言，对于每个变量的赋值，实际上是对内存块的引用。不可变性意味着当变量创建后即不能发生改变。对于可变变量，当将一个可变变量赋值给另一个变量时，新变量只是旧变量的引用，因此无论对于新旧变量的任一个进行的修改，都会同时作用于两者。

使用`id`方法可以方便的确认：

```Python
# list是可变对象
In [1]: listA = ["element 1"]

In [2]: listB = listA

In [3]: listB.append("element 2")

In [4]: listB
Out[4]: ['element 1', 'element 2']

In [5]: listA
Out[5]: ['element 1', 'element 2']

In [6]: id(listA)
Out[6]: 139640116124232

In [7]: id(listB)
Out[7]: 139640116124232
```

而对于不可变变量，由于创建后不能发生改变，因此修改会开辟新的内存区域存储这块数据。

```Python
# str是不可变对象
In [8]: strA = "element 1"

In [9]: strB = strA

In [10]: id(strA)
Out[10]: 139640116966384

In [11]: id(strB)
Out[11]: 139640116966384

In [12]: strB += " element 2"

In [13]: strA
Out[13]: 'element 1'

In [14]: strB
Out[14]: 'element 1 element 2'

In [15]: id(strA)
Out[15]: 139640116966384

In [16]: id(strB)
Out[16]: 139640107303176
```

在这里，一开始的`strA`和`strB`是指向了相同的内存地址，但是当`strB`修改时，内存为`element 2`开辟了一块空间，接着为`element1 element2`开辟了一块空间，然后将变量`strB`指向`element1 element2`，随着`element 1`和`element2`对象不再被使用，其占用的内存被Python的垃圾回收机制销毁。

此外，在Python中，`==`判断的是两个对象的值是否相等，而`is`判断的是两个对象是否指向同一个内存：

```Python
In [17]: strA = "element 1"

In [18]: strB = "element 1"

In [19]: id(strA)
Out[19]: 139640107215408

In [20]: id(strB)
Out[20]: 139640107216112

In [21]: strA == strB
Out[21]: True

In [22]: strA is strB
Out[22]: False
```

基于这个，可以理解书中所说*永远不要定义可变类型的默认参数*：

```Python
In [23]: def add_to(element, target=[]):
    ...:     target.append(element)
    ...:     return target

In [24]: add_to(1)
Out[24]: [1]

In [25]: add_to(2)
Out[25]: [1, 2]

In [26]: add_to(3)
Out[26]: [1, 2, 3]
```

此时列表不会在每次都初始化默认参数，从而可能产生不符合预期的结果。更加合理的定义应该是：

```Python
In [27]: def add_to(element, target=None):
    ...:     if target is None:
    ...:         target = []
    ...:     target.append(element)
    ...:     return target

In [28]: add_to(42)
Out[28]: [42]

In [29]: add_to(42)
Out[29]: [42]

In [30]: add_to(42)
Out[30]: [42]
```

## `__slots__`魔法

当一个类需要创建大量实例时，使用`__slots__`对需要使用的属性进行声明，可以获得更快的属性访问速度和更少的内存占用，从而提升运行效率。

由于在默认情况下，Python用一个字典来保存一个类的实例，这使得用户能够在某个类的实例中设定任意的新属性。

但是，基于哈希表的字典创建时不能预知所需要使用的内存，因此会额外分出更多的空间以保存可能扩容的属性。当一个类下出现很多实例时，为了字典预留的空间会导致不必要的内存消耗。

因此，使用`__slots__`方法，可以让Python在设置属性时不使用字典，而是只给一个固定的属性集合分配空间，从而有效节省内存使用，提升运行效率。

```Python
# 不使用__slots__
class MyClass(object):
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.set_up()

# 使用__slots__
class MyClass(object):
    __slots__ = ['name', 'identifier']
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.set_up()
```

> Python__slots__详解[cnblogs](https://www.cnblogs.com/rainfd/p/slots.html)

## 虚拟环境

使用`virtualenv`可以为每一个项目创建独立的Python环境，而不是在全局使用所有模块。

使用`conda`可以理解为使用了`pip`和`virtualenv`的结合。`pip`作为Python官方的包管理器，只能安装`PyPI`下的包，而`conda`提供了更多的第三方支持。

`conda`支持联网下载所需的Python解释器，而`virtualenv`只能创建本地含有的Python解释器虚拟环境。

## 容器(Collections)

除了常见的数据结构元组、列表、字典和集合之外，Python的`collections`模块提供了多种预先实现的容器数据类型：`namedtuple`，`deque`，`ChainMap`，`Counter`，`OrderedDict`，`defaultdict`。其中`deque`是一个双向链表结构，`namedtuple`是元组的拓展，其余的可以视作字典的拓展。在Python 3.4以上，提供了枚举结构`enum.Enum`。

> Python 容器用法整理[cnblogs](https://www.cnblogs.com/shawnChi/p/6484591.html)

- `defaultdict`

  `defaultdict`是一种字典的拓展。相较于字典，`defaultdict`不需要`key`在一开始存在。
  
  在字典中，如果访问不存在的键，会抛出`KeyError`异常，但是如果一个字典在访问不存在的键时可以获取一个默认值而不是引发异常，则在某些场景下会获得很多便利。

  `defaultdict`类类似于字典，但是需要进行初始化。这个类的初始化函数需要接受一个**类型**作为参数，确切的说是一个**工厂函数**。这个工厂函数可以是`list`，`set`，`str`，`int`等，当`key`不存在时，返回的是工厂函数的默认值。

  ```Python
  In [1]: from collections import defaultdict

  In [2]: dct = defaultdict(list)
  
  In [3]: dct
  Out[3]: defaultdict(list, {})
  
  In [4]: dct["new key1"]
  Out[4]: []
  
  In [5]: dct
  Out[5]: defaultdict(list, {'new key1': []})
  
  In [6]: dct["new key2"] = "append value1"
  
  In [7]: dct
  Out[7]: defaultdict(list, {'new key1': [], 'new key2': 'append value1'})
  
  In [8]: dct["new key3"].append("append value 2")
  
  In [9]: dct
  Out[9]:
  defaultdict(list,
              {'new key1': [],
               'new key2': 'append value1',
               'new key3': ['append value 2']})
  ```

  `defaultdict`类除了接受类型名称作为初始化函数的参数之外，还可以使用任何不带参数的可调用函数，而以该函数的返回结果作为默认值。例如：

  ```Python
  In [10]: def zero():
    ...:     return 0

  In [11]: dct = defaultdict(zero)

  In [12]: dct
  Out[12]: defaultdict(<function __main__.zero()>, {})

  In [13]: dct["new key1"]
  Out[13]: 0

  In [14]: dct
  Out[14]: defaultdict(<function __main__.zero()>, {'new key1': 0})
  ```

  > python中defaultdict方法的使用[CSDN](https://blog.csdn.net/real_ray/article/details/17919289)

- `counter`
  
  `counter`是一个计数器，可以认为是一个key-int字典。通过接收一个可迭代对象、映射或关键字参数进行实例化。根据键值返回对应的统计次数：

  ```Python
  In [15]: from collections import Counter

  In [16]: c = Counter("gallahad")
  
  In [17]: c
  Out[17]: Counter({'a': 3, 'd': 1, 'g': 1, 'h': 1, 'l': 2})

  In [18]: c['x']
  Out[18]: 0
  ```

  `counter`提供了多种方法进行键值的修改操作。

  > Python Counter()计数工具[cnblogs](https://www.cnblogs.com/nisen/p/6052895.html)
  >
  > Python标准库——collections模块的Counter类[Pythoner](http://www.pythoner.com/205.html)

- `deque`

  `deque`是一个双端队列或双向链表，可以在队列的开头或结尾添加或删除元素。但是这个容器不支持切片操作，因此无法用于替换、截取、排序等操作。

- `namedtuple`

  `namedtuple`和普通元组一样，是一个不可变的列表。如果需要获取元组中的数据，需要使用下标索引，但是`namedtuple`将其转变为一个有名称的容器，甚至可以理解为是一种简单的结构体，从而可以不使用整数索引而使用具体名称来访问其中的元素。创建一个`namedtuple`需要提供元组的名称和对应的字段名称：

  ```Python
  In [19]: from collections import namedtuple

  In [20]: Program = namedtuple("Program", "Name, BeginYear, Version")

  In [21]: py = Program(Name="Python", BeginYear=1989, Version="3.7")
  
  In [22]: py
  Out[22]: Program(Name='Python', BeginYear=1989, Version='3.7')
  
  In [23]: py.Name
  Out[23]: 'Python'
  
  In [24]: py.BeginYear
  Out[24]: 1989
  
  In [25]: py.Version
  Out[25]: '3.7'

  In [26]: py[0]
  Out[26]: 'Python'

  In [27]: py[1]
  Out[27]: 1989

  In [28]: py[2]
  Out[28]: '3.7'
  ```

  由此可见，`namedtuple`既可以使用属性来访问对应的值，也可以像普通元组一样使用下标索引访问。同时，由于`namedtuple`可以直接访问属性的特性，使得其成为一个自描述的结构，非常适合用于存储表条目。

  由于`namedtuple`同样是元组，因此试图修改其属性值是非法的：

  ```Python
  In [29]: py.BeginYear = 2020
  AttributeError: can't set attribute
  ```

  `namedtuple`支持的一些内建方法提供了诸如从转换为字典或使用可迭代对象建立`namedtuple`的功能。

- `enum.Enum`

  在Python 3.4之后，提供了枚举类的标准库`enum`，从而使用户可以使用枚举类型。

  在没有枚举类型提供之前，要实现类似枚举的效果通常是创建一个字典或类来实现，但是这带来了可以被修改的隐患，因此引入了枚举类型：

  ```Python
  In [32]: from enum import Enum

  In [33]: class Color(Enum):
      ...:     red = 1
      ...:     green = 2
      ...:     blue = 3
  
  In [34]: Color.red
  Out[34]: <Color.red: 1>
  
  In [36]: Color(1)
  Out[36]: <Color.red: 1>
  
  In [37]: Color['red']
  Out[37]: <Color.red: 1>
  
  In [35]: type(Color.red)
  Out[35]: <enum 'Color'>
  ```

  枚举类型可以通过多种方式访问，不可实例化，不可更改。**成员名无法重复，成员值允许相同，相同成员值的情况下，第二个及以后的成员名被视作第一个成员名的别名**。

  > Python 的枚举类型[segmentfault](https://segmentfault.com/a/1190000017327003)
  >
  > Python——枚举（enum）[cnblogs](https://www.cnblogs.com/-beyond/p/9777329.html)

## 枚举(Enumerate)

枚举函数和上一节中的枚举类型不是一个概念。枚举函数(`enumerate()`)是用来遍历数据并构成一个序列的函数，通常在`for-loop`中使用：

```Python
my_list = ['apple', 'banana', 'grapes', 'pear']
for counter, value in enumerate(my_list, start=1):  # 下标从1开始
    print(counter, value)

# output:
(1, 'apple')
(2, 'banana')
(3, 'grapes')
(4, 'pear')
```

## 对象自省

对象自省可以帮助用户更好的理解Python中的任一对象。

- `dir`
  
  `dir`返回一个列表，会列出一个对象所拥有的所有的属性的方法，例如：

  ```Python
  In [1]: dir(set)
  Out[1]:
  ['__and__',
   '__class__',
   '__contains__',
   '__delattr__',
   '__dir__',
   '__doc__',
   '__eq__',
   '__format__',
   '__ge__',
   '__getattribute__',
   '__gt__',
   '__hash__',
   '__iand__',
   '__init__',
   '__ior__',
   '__isub__',
   '__iter__',
   '__ixor__',
   '__le__',
   '__len__',
   '__lt__',
   '__ne__',
   '__new__',
   '__or__',
   '__rand__',
   '__reduce__',
   '__reduce_ex__',
   '__repr__',
   '__ror__',
   '__rsub__',
   '__rxor__',
   '__setattr__',
   '__sizeof__',
   '__str__',
   '__sub__',
   '__subclasshook__',
   '__xor__',
   'add',
   'clear',
   'copy',
   'difference',
   'difference_update',
   'discard',
   'intersection',
   'intersection_update',
   'isdisjoint',
   'issubset',
   'issuperset',
   'pop',
   'remove',
   'symmetric_difference',
   'symmetric_difference_update',
   'union',
   'update']
  ```

- `type`和`id`
  
  `type`返回对象类型，而`id`返回对象在内存中的唯一标识符。`id`在判断两个对象是否指向同一个内存地址时非常有用，可以结合`is`理解，而`==`无法做类似的判断：

  ```Python
  In [2]: str1 = "test string"

  In [3]: str2 = "test string"
  
  In [4]: str1 == str2
  Out[4]: True
  
  In [5]: str1 is str2
  Out[5]: False
  
  In [6]: id(str1)
  Out[6]: 140410587911344
  
  In [7]: id(str2)
  Out[7]: 140410587575920
  ```

此外还有`inspect`模块，可以用以获取对象的信息。

## 推导式(Comprehension)

推导式又称解析式，是Python的独有特性，可以通过一种数据序列构建另一种数据序列。Python支持三种推导式，分别是列表推导式，字典推导式和集合推导式。

列表推导式的通常语法为

```Python
variable = [out_exp for variable in input_list if conditions]
```

当出现多层循环嵌套时，`out_exp`是最下一层，每一个`for`依次**从外向内嵌套**：

```Python
In [1]: lst = [x * y for x in range(1, 5) if x > 2 for y in range(1, 4) if y < 3]

In [2]: list(lst)
Out[2]: [3, 6, 4, 8]
```

等价于：

```Python
In [3]: lst = []
   ...: for x in range(1, 5):
   ...:     if x > 2:
   ...:         for y in range(1, 4):
   ...:             if y < 3:
   ...:                 lst.append(x * y)

In [4]: lst
Out[4]: [3, 6, 4, 8]
```

> python 循环高级用法[cnblogs](https://www.cnblogs.com/bonelee/p/8545263.html)

字典推导式和集合推导式都使用类似的方式，需要注意的是**没有元组推导式**，如果用`()`替代`[]`或`{}`会产生一个生成器，而在Python3之后，使用列表推导式也会得到一个生成器。

## 异常

最常用的异常捕捉是`try/except`从句，将可能触发异常的代码放在`try`语句块里，处理异常的代码放在`except`语句块里。

除了这种方式外，异常处理可以同时处理多种异常，一种是将所有可能发生的异常放在一个元组里：

```Python
try:
    file = open('test.txt', 'rb')
except (IOError, EOFError) as e:
    print("An error occurred. {}".format(e.args[-1]))
```

或者在每个`except`块中处理单独的异常：

```Python
try:
    file = open('test.txt', 'rb')
except EOFError as e:
    print("An EOF error occurred.")
    raise e
except IOError as e:
    print("An error occurred.")
    raise e
```

或者直接捕获所有可能的异常：

```Python
try:
    file = open('test.txt', 'rb')
except Exception:
    raise
```

如果使用`try/except/finally`从句，则程序会在主程序代码或异常处理代码运行完成后，运行`finally`从句，即无论异常是否触发，`finally`语句块中的代码都会被执行。

在此之外，还可以加上`else`构成`try/except/else/finally`从句。这样可以保证只有在`try`语句块中的代码才会进行异常捕获，如果有异常出现在`else`中，则不会被捕获后进入`except`语句块。`else`只会在`try`没有异常的情况下执行。

因此，在`try/except/else/finally`从句中，首先执行`try`，如果没有异常则执行`else`，如果出现异常则执行`except`，最后无论如何都会执行`finally`。

## `lambda`表达式

`lambda`表达式定义了一个匿名函数，只会在定义时使用一次。使用匿名函数并不会带来效率的提高，只会使代码更加简洁。如果在使用匿名函数和定义函数之间进行取舍，需要考虑的是函数的复杂程度，重用性和可读性。

## 一行式

书中所谓的一行式，实际是在terminal中执行Python的一些简单命令或执行简单的脚本，

在终端下使用`python -h`可以看到Python解释器支持的一些参数选项，例如：

```Bash
$ python3 -h
usage: python3 [option] ... [-c cmd | -m mod | file | -] [arg] ...
Options and arguments (and corresponding environment variables):
-b     : issue warnings about str(bytes_instance), str(bytearray_instance)
         and comparing bytes/bytearray with str. (-bb: issue errors)
-B     : don't write .py[co] files on import; also PYTHONDONTWRITEBYTECODE=x
-c cmd : program passed in as string (terminates option list)
-d     : debug output from parser; also PYTHONDEBUG=x
-E     : ignore PYTHON* environment variables (such as PYTHONPATH)
-h     : print this help message and exit (also --help)
-i     : inspect interactively after running script; forces a prompt even
         if stdin does not appear to be a terminal; also PYTHONINSPECT=x
-I     : isolate Python from the user's environment (implies -E and -s)
-m mod : run library module as a script (terminates option list)
-O     : optimize generated bytecode slightly; also PYTHONOPTIMIZE=x
-OO    : remove doc-strings in addition to the -O optimizations
-q     : don't print version and copyright messages on interactive startup
-s     : don't add user site directory to sys.path; also PYTHONNOUSERSITE
-S     : don't imply 'import site' on initialization
-u     : unbuffered binary stdout and stderr, stdin always buffered;
         also PYTHONUNBUFFERED=x
         see man page for details on internal buffering relating to '-u'
-v     : verbose (trace import statements); also PYTHONVERBOSE=x
         can be supplied multiple times to increase verbosity
-V     : print the Python version number and exit (also --version)
-W arg : warning control; arg is action:message:category:module:lineno
         also PYTHONWARNINGS=arg
-x     : skip first line of source, allowing use of non-Unix forms of #!cmd
-X opt : set implementation-specific option
file   : program read from script file
-      : program read from stdin (default; interactive mode if a tty)
arg ...: arguments passed to program in sys.argv[1:]
```

## `For` - `Else`

`else`是`for`循环中的一个可选的额外分支，并不常用，甚至并不推荐使用。

在常用的`for`循环中，每次执行一次循环直到循环结束，如果需要跳出循环，则使用`break`跳出循环不再执行，或使用`continue`跳出当前循环并执行下一次循环，或在函数中使用`return`直接返回结果。

`else`在这个情况下提供了一个分支，即：**当且只当循环全部结束时，执行`else`内的程序**。只有正常退出循环时，`else`内的会被执行，如果使用`break`退出循环，则`else`不执行。这是使用`else`打印素数的一个示例：

```Python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print( n, 'equals', x, '*', n/x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
```

注意在这里，由于`continue`没有中断循环的继续，只是跳过了某次循环，因此当循环结束时仍然算正常退出循环，`else`仍然会被执行：

```Python
In [1]: for i in "pyxxxxthon":
   ...:     if i == 'x':
   ...:         continue
   ...:     print(i)
   ...: else:
   ...:     print("loop exited")
p
y
t
h
o
n
loop exited
```

## 使用C拓展

CPython支持Python对C的调用。

`ctypes`模块是最简单的Python对C调用的方式。`ctypes`模块提供了和C语言兼容了数据类型和函数来加载`.so`(Linux)或`.dll`(Windows)文件，同时在调用时不需要对源文件做任何修改。

这里使用书中的示例：

```C
//sample C file to add 2 numbers - int and floats

#include <stdio.h>

int add_int(int, int);
float add_float(float, float);

int add_int(int num1, int num2)
{
    return num1 + num2;
}

float add_float(float num1, float num2)
{
    return num1 + num2;
}
```

将C文件编译为`.so`（Windows下为`.dll`）文件：

```Bash
gcc -shared -Wl,-soname,adder -o adder.so -fPIC add.c
```

然后在Python代码中进行调用：

```Python
from ctypes import *

#load the shared object file
adder = CDLL('./adder.so')

#Find sum of integers
res_int = adder.add_int(4,5)
print ("Sum of 4 and 5 = " + str(res_int))

#Find sum of floats
a = c_float(5.5)
b = c_float(4.1)

add_float = adder.add_float
add_float.restype = c_float
print ("Sum of 5.5 and 4.1 = ", str(add_float(a, b)))
```

这是一种最基本的方式。

第二种方式为SWIG(Simplified Wrapper and Interface Generator)。这种方式需要编写额外的接口文件作为入口。通常不会采用这种方式，因为过于复杂，除非编写的C/C++代码需要被多种语言调用时才会使用。

最后最常用的是`Python/C API`，不仅简单而且可以在C中操作Python对象。

使用这种方法需要用特定的方式编写C代码，以供Python对代码进行调用。Python对象被一种`PyObject`的结构体描述，并在`Python.h`头文件中提供了操作函数。大部分的Python原生对象的基础函数和操作在`Python.h`头文件中都有。

当编写完成后，只需要在Python中像导入包一样使用`import`即可，例如：

```Python
# Though it looks like an ordinary python import, the addList module is implemented in C
import addList

l = [1,2,3,4,5]
print "Sum of List - " + str(l) + " = " +  str(addList.add(l))
```

关于C代码的编写和编译在书中有较为详细的解释。

## `open`函数

使用`open`打开文件，首先需要保证打开的文件句柄能够正常关闭。要完成这个任务，不能简单地直接使用形如`f.close()`的语句，因为有可能会在关闭前由于异常的引发而导致`f.close()`不被调用。因此，一种方式是使用`try/except/finally`，在`finally`中关闭文件，或者使用上下文管理器`with`保证其正常关闭。

`open`使用的文件打开模式需要正确确定。通常，读取使用`r`，读取并写入使用`r+`，覆盖使用`w`，追加使用`a`。确定正确的模式非常重要，因为如果选择错误的打开模式，可能会直接引发报错。

例如，如果打开一个`.jpg`文件，使用`r+`就会抛出异常。因为`.jpg`并不是一个文本文件，应该使用二进制模式(`'b'`)打开，得到一个字节串，而不是使用文本模式(`'t'`)打开从而得到一个字符串。因此，打开`.jpg`文件的正确模式应该是`rb`。

最后，由于编码方式的不同，打开文件最好指定编码如`UTF-8`或`GBK`等，否则可能会导致不可预知的读取错误。

## 目标Python2+3

为了兼容Python2+和Python3+，除了开发两套代码之外，可以使用一些技巧使其尽可能的兼容。

第一中方法是导入`__future__`模块，可以在Python2中使用Python3的功能。

例如如果需要在Python2.5中导入Python2.6开始支持的上下文管理器特性：

```Python
from __future__ import with_statement
```

在Python3中`print`成为一个函数，而在Python2中是一个关键字，如果需要使用其作为函数，也可以类似的导入：

```Python
from __future__ import print_function
```

第二种方式是使用模块别名：

```Python
try:
    import urllib.request as urllib_request  # for Python 3
except ImportError:
    import urllib2 as urllib_request  # for Python 2
```

如果需要在Python2的代码确保不使用已经被Python3移除的功能，从而保证兼容性，可以使用如下方式：

```Python
from future.builtins.disabled import *

apply()
# Output: NameError: obsolete Python 2 builtin apply is disabled
```

此外也可以使用非官方支持的库为Python2提供Python3的功能。

## 协程

协程(Coroutine)和多线程不同，协程是程序自身控制程序间的调度，因此不存在线程切换的开销，同时不受到GIL的影响。对于IO密集型任务，协程可以提供非常高的执行效率，而对于CPU密集型，可以使用多进程加协程的方式。

在Python中，对于协程的支持通过生成器(Generators)实现，协程是遵循某些规则的生成器。

当使用`yield`关键字创建一个生成器后，`yield`不仅可以用来传递数据，同时也能接收数据。实际上，在初学生成器时，将`yield`理解为`return`是很片面的。因为在`yield`中，程序并没有终止，只是暂停在了当时所在的位置，因此，`yield`不仅可以放在函数结尾，也可以放在函数中间，在执行`__next__()`方法时，从上一次`yield`停止的位置继续执行。

这里推荐使用参考文章中的案例：

> 理解Python的协程(Coroutine)[简书](https://www.jianshu.com/p/84df78d3225a)

```Python
In [1]: def test():
   ...:     print("generator starts")
   ...:     n = 1
   ...:     while True:
   ...:         yield_expression_value = yield n
   ...:         print("yield_expression_value = {}".format(yield_expression_value))
   ...:         n += 1

In [2]: generator = test()

In [3]: print(type(generator))
<class 'generator'>

In [4]: next_result = generator.__next__()
generator starts

In [5]: print("next_result = {}".format(next_result))
next_result = 1

In [6]: send_result = generator.send(100)
yield_expression_value = 100

In [7]: print("send_result = {}".format(send_result))
send_result = 2
```

如果要启动生成器，需要先调用`__next__()`或`send(None)`，这将会让程序执行到`yield`所在的位置。在这个例子中，程序首先打印`generator starts`，然后将`n`对应的值传给`next_result`，从这里开始，生成器被暂停，直到下次获得调用。

当使用`send()`向生成器传入一个值后，生成器恢复执行，从`yield_expression_value`出开始，接收到传入的值`100`，然后继续执行直到再次遇到`yield`为止。

这种程序主动调配，中断并切换执行的方式，体现了协程的特点。随后给出的生产者-消费者模式的案例更好的说明了这个过程：

```Python

```

## 函数缓存

## 上下文管理器
