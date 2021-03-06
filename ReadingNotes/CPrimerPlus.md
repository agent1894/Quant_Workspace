# C Primer Plus 6th Edition by Stephen Prata (Pearson)

- [C Primer Plus 6th Edition by Stephen Prata (Pearson)](#c-primer-plus-6th-edition-by-stephen-prata-pearson)
  - [Chapter1 初识C语言](#chapter1-初识c语言)
    - [Section8 编程机制](#section8-编程机制)
  - [Chapter2 C语言概述](#chapter2-c语言概述)
    - [Section2 示例解释](#section2-示例解释)
  - [Chapter3 数据和C](#chapter3-数据和c)
    - [Section3 数据：数据类型关键字](#section3-数据数据类型关键字)
    - [Section4 C语言基本数据类型](#section4-c语言基本数据类型)
  - [Chapter4 字符串和格式化输出](#chapter4-字符串和格式化输出)
    - [Section2 字符串简介](#section2-字符串简介)
    - [Section3 常量和C预处理器](#section3-常量和c预处理器)
    - [Section4 `printf()`和`scanf()`](#section4-printf和scanf)
  - [Chapter5 运算符、表达式和语句](#chapter5-运算符表达式和语句)
    - [Section2 基本运算符](#section2-基本运算符)
    - [Section3 其他运算符](#section3-其他运算符)
    - [Section4 表达式和语句](#section4-表达式和语句)
    - [Section5 类型转换](#section5-类型转换)
    - [Section6 带参数的函数](#section6-带参数的函数)
  - [Chapter6 C控制语句：循环](#chapter6-c控制语句循环)
    - [Section2 `while`语句](#section2-while语句)
    - [Section3 用关系运算符和表达式比较大小](#section3-用关系运算符和表达式比较大小)
    - [Section6 `for`循环](#section6-for循环)
    - [Section6 其他赋值运算符：`+=, -=, *=, /=, %=`](#section6-其他赋值运算符-----)
    - [Section7 逗号运算符](#section7-逗号运算符)
    - [Section9 如何选择循环](#section9-如何选择循环)
  - [Chapter7 C控制语句：分支和跳转](#chapter7-c控制语句分支和跳转)
    - [Section2 `if else`语句](#section2-if-else语句)
    - [Section3 逻辑运算符](#section3-逻辑运算符)
    - [Section5 条件运算符`?`](#section5-条件运算符)
    - [Section7 多重选择：`switch`和`break`](#section7-多重选择switch和break)
    - [Section8 `goto`语句](#section8-goto语句)
  - [Chapter8 字符输入/输出和输入验证](#chapter8-字符输入输出和输入验证)
    - [Section2 缓冲区](#section2-缓冲区)
    - [Section3 结束键盘输入](#section3-结束键盘输入)
    - [Section4 重定向和文件](#section4-重定向和文件)
    - [Section5 创建更友好的用户界面](#section5-创建更友好的用户界面)
  - [Chapter9 函数](#chapter9-函数)
    - [Section1 复习函数](#section1-复习函数)
    - [Section3 递归](#section3-递归)
    - [Section7 指针简介](#section7-指针简介)
  - [Chapter10 数组和指针](#chapter10-数组和指针)
    - [Section1 数组](#section1-数组)
    - [Section2 多维数组](#section2-多维数组)
    - [Section3 指针和数组](#section3-指针和数组)
    - [Section4 函数、数组和指针](#section4-函数数组和指针)
    - [Section5 指针操作](#section5-指针操作)
    - [Section6 保护数组中的数据](#section6-保护数组中的数据)
    - [Section7 指针和多维数组](#section7-指针和多维数组)
    - [Section8 变长数组（VLA）](#section8-变长数组vla)
    - [Section9 复合字面量](#section9-复合字面量)
    - [补充：`const`和指针](#补充const和指针)
  - [Chapter11 字符串和字符串函数](#chapter11-字符串和字符串函数)
    - [Section1 字符串和字符串函数](#section1-字符串和字符串函数)
    - [Section2 字符串输入](#section2-字符串输入)
    - [Section3 字符串输出](#section3-字符串输出)
    - [Section4 自定义输入/输出函数](#section4-自定义输入输出函数)
    - [Section5 字符串函数](#section5-字符串函数)
    - [Section6 字符串示例：字符串排序](#section6-字符串示例字符串排序)
    - [Section7 `ctype.h`字符函数和字符串](#section7-ctypeh字符函数和字符串)
    - [Section8 命令行参数](#section8-命令行参数)
    - [Section9 把字符串转换为数字](#section9-把字符串转换为数字)
  - [Chapter12 存储类别、链接和内存管理](#chapter12-存储类别链接和内存管理)
  - [Chapter13 文件输入/输出](#chapter13-文件输入输出)
  - [Chapter14 结构和其他数据形式](#chapter14-结构和其他数据形式)
  - [Chapter15 位操作](#chapter15-位操作)
  - [Chapter16 C预处理器和C库](#chapter16-c预处理器和c库)
  - [Chapter17 高级数据表示](#chapter17-高级数据表示)

## Chapter1 初识C语言

### Section8 编程机制

- 编译器将源代码转换成中间代码，链接器将中间代码和其他代码合并，生成可执行文件。C使用这种分而治之的方法方便对程序进行模块化，可以独立编译单独的模块，稍后再用链接器合并已编译的模块。
- 链接器还将编写的程序和预编译的库代码合并。
- 中间代码有多种形式，最普遍的形式为将源代码转换为机器语言代码，并把结果放在目标代码文件（或简称目标文件中）。目标代码文件不能直接运行，因为只包含编译器翻译的源代码。
  - 目标代码文件缺失启动代码(startup code)，启动代码充当程序和操作系统之间的接口，不同系统的启动代码不同。
  - 目标文件代码缺失库函数。
- 链接器的作用是将编写的目标代码，系统的标准启动代码和库代码合并为文件，即可执行文件。对于库代码，链接器只会把程序中要用到的库函数代码提取出来。

## Chapter2 C语言概述

### Section2 示例解释

- 声明变量的4个理由：
  
  - 所有变量放在一处，便于查找和理解程序的用途。
  - 促使在编程开始前进行合理计划。
  - 有助于发现隐藏在程序中的小错误。
  - 如果实现未声明变量，C程序将无法通过编译。

- C99之前标准要求所有声明置于块的顶部，C99允许在需要时声明。
- C语言提供6种基本语句：
  
  - 标号语句
  - 复合语句
  - 表达式语句
  - 选择语句
  - 迭代语句
  - 跳转语句

- C语言通过赋值运算符而不是赋值语句完成赋值操作。根据C标准，C语言没有所谓的“赋值语句”，所谓的“赋值语句”实际上是表达式语句。

## Chapter3 数据和C

### Section3 数据：数据类型关键字

- 截至C99标准，共有12个基本类型关键字：`int, long, short, unsigned, char, float, double, signed, void, _Bool, _Complex, _Imaginary`。
- `char`类型也可以表示较小的整数。
- `_Bool`类型表示布尔值`true`或`false`。
- `_Complex, _Imaginary`分别表示复数和虚数。

### Section4 C语言基本数据类型

- 当整数超出相应类型的取值范围后，会出现溢出行为。当超过最大值时，`unsigned int`类型变量从`0`开始，而`int`类型变量从`-2147483648`开始。**注意**，当出现溢出行为时，系统**不会**通知用户，同时溢出行为是未定义行为(Undefined Behaviour)。
- 在C语言中，用单引号括起来的单个字符被称为字符常量(character constant)，如果使用双引号，则编译器认为这个字符是一个字符串。
- 字符是以数值形式存储的，所以也可以使用数字代码值来赋值，如`char grade = 65;`。
- `printf`函数中的转换说明决定了数据的显示方式，而不是存储方式。
- C语言使用指数记数法（e记数法）表示浮点数。
- C标准规定，`float`类型必须至少能表示6位有效数字，且取值范围至少是$10^{-37}\sim10^{37}$。`double`类型和`float`类型的最小取值范围相同，但至少保证10位有效数字。`long double`比`double`可以满足更高的精度要求，但是C只保证`long double`类型至少与`double`类型的精度相同。
- 通常，系统存储一个浮点数`float`需要占用32位，其中8位用于表示指数，剩下24位用于表示非指数部分（也叫做尾数或有效数）及其符号。
- 浮点值的上溢(overflow)和下溢(underflow)：
  
  - 当计算导致数值过大，超过当前类型能表达的范围时，就会发生上溢。如下例：

    ```C
    float toobig = 3.4E38 * 100.0f;
    printf("%e\n", toobig);

    // inf
    ```

    这种行为在过去是未定义的，现在会给一个表示无穷大的特定值，`printf()`显示该值为`inf`或`infinity`。
  - 当计算处理一个很小的数时，情况会更为复杂。因为`float`类型以指数和尾数存储，如果一个数，指数部分已经为最小值，占用了全部可用位，当其除以2时，理论来说会继续减小指数部分。但是由于指数部分已经占用了所有可能位，因此计算机只能将尾数部分的位向右移，空出1个二进制位并丢弃最后一个二进制数，这个过程会损失原末尾有效位上的数字，被称为下溢。

- 浮点数舍入错误：

  如下例：

  ```C
  #include <stdio.h>
  int main(void)
  {
      float a, b;

      b = 2.0e20 + 1.0;
      a = b - 2.0e20;
      printf("%f \n", a);

      return 0;
  }

  /*不同的编译器返回的结果可能为
  0.000000
  -13584010575872.000000
  4008175468544.000000
  */
  ```

  导致这个问题的原因是计算机缺少足够的小数位完成运算。由于`2.0e20`在2后有20个0，如果加1则会在第21位发生变化。如果要正确运算，程序至少要储存21位有效数字，而`float`类型只能按指数比例存储6或7位有效数字，因此计算结果是错误的。如果计算的是`2.0e4`，则不会有这个问题，因为只需要改变第5位上的数字，而`float`类型的精度可以保证这样的运算。

## Chapter4 字符串和格式化输出

### Section2 字符串简介

- 字符串常量`"x"`和字符常量`'x'`不同。区别一在于`'x'`是基本类型`char`，而`"x"`是派生类型`char`数组；区别二在于`"x"`实际上由两个字符组成：`'x'`和空字符(null character)`'\0'`。C语言用空字符标记字符串的结束。
- C中的字符串一定以空字符结束，因此意味着`char`数组的容量必须至少比待存储字符数多1。

### Section3 常量和C预处理器

- 使用预处理器定义常量，会在编译程序用定义的值替换常量，这一过程被称为编译时替换(compile-time substitution)，这样定义的常量也被称为明示常量(manifest constant)。
- 使用预处理器时，不使用`=`和`;`。

### Section4 `printf()`和`scanf()`

- `printf()`中打印`%`需要使用`%%`而不是`\%`。
- 转换说明仅把以二进制储存在计算机中的值转换为一系列字符并打印出来，并不是将原始的值替换为转换后的值。
- **注意**：在Linux64位下，`long`占8个字节，在Window32位，Windows64位，Linux32位下，`long`占4个字节。
- `float`作为`printf()`的参数时，会被转换为`double`类型，从4字节扩展为8字节。
- 使用`printf()`时，整型和浮点型同样可能存在转换不匹配的问题。如书中4.12的示例：
  
  ```C
  #include <stdio.h>
  int main(void)
  {
      float n1 = 3.0;
      double n2 = 3.0;
      long n3 = 2000000000;
      long n4 = 1234567890;

      printf("%.1e %.1e %.1e %.1e\n", n1, n2, n3, n4);
      printf("%ld %ld\n", n3, n4);
      printf("%ld %ld %ld %ld\n", n1, n2, n3, n4);

      return 0;
  }

  /* Output:
  3.0e+00 3.0e+00 -5.5e+303 3.2e-319
  2000000000 1234567890
  2000000000 1234567890 0 0
  */
  ```

  在第一行输出中，`%e`没有把整型转为浮点型。因为用`%e`转换`n3(long)`时，`%e`转换说明让`printf()`认为待转换的值为`double`类型，在系统中，`double`为8个字节，因此当查看`n3`（4个字节）时，除了读取了`n3`的4个字节，还额外读取了`n3`相邻的4个字节共8个字节，接着将8个字节的位组合解释为浮点数。

  在第三行输出中，`%ld`表明读取4个字节，但是`float`和`double`都被转换为8个字节进栈，因此导致读取错位。
  
  *但是，在Linux64下，`long`同样是8个字节，可结果仍然不对，此处存疑*。

- 如果用`scanf()`读取基本变量类型的值，在变量名前加`&`。
- 如果用`scanf()`把字符串读入字符数组中，不用加`&`。
- `scanf()`返回值为成功读取项的数量。
- 在`printf()`中可以使用`*`修饰符，在`printf()`中，如果不想预先指定字段宽度，那可以用`*`修饰符代替字符宽度，然后用参数告诉函数该`*`对应的宽度的值。
- 在`scanf()`中，把`*`放在`%`和转换字符中，会使`scanf()`跳过相应的输出项，例如`scanf("%*d %*d %d", &n);`会跳过前两个整数，把第三个整数拷贝给`n`。

## Chapter5 运算符、表达式和语句

### Section2 基本运算符

- 数据对象、左值、右值和运算符：
  
  - 赋值表达式语句的目的是把值储存到内存位置上。用于储存值的数据存储区域统称为数据对象(data object)。
  - 左值(lvalue)是C语言术语，用于标识特定数据对象的名称或表达式，因此，对象指的是实际的数据存储，而左值是用于标识或定位存储位置的标签。
  - 在早期，C的左值意味着：
    1. 指定一个对象，所以引用内存中的地址
    2. 可用在赋值运算符的左侧

    但是在标准增加了`const`限定符后，用`const`创建的变量不可修改，为此C标准新增了可修改的左值(modifiable lvalue)，用于标识可修改的对象。因此赋值运算符的左侧应该是可修改的左值。
  - 右值(rvalue)指能赋值给可修改左值的量，且本身不是左值。右值可以是常量、变量或其他可求值的表达式。

### Section3 其他运算符

- `sizeof`运算符以字节为单位返回运算对象的大小，为`size_t`类型的值。
- 递增运算符(increment operator)有两种形式，`++`出现在其作用的变量前面，称为前缀模式，`++`出现在其作用的变量后面，称为后缀模式。两种模式的区别在于**递增行为发生的时间不同**。当单独使用递增运算符时，前后缀没有区别，如果运算符和运算对象时更复杂的表达式的一部分时，使用前后缀的效果会不同。如下例：

  ```C
  int a = 1;
  int q;

  q = 2*++a;
  // a先递增1，随后乘以2将结果赋给q，q = 4，a = 2
  q = 2*a++;
  // 先计算2乘以a，将结果赋给q，随后a递增1，q = 2，a = 2
  ```

  如果`n++`是表达式的一部分，可将其视为先使用`n`，再递增，而`++n`表示先递增`n`再使用。

- 在C语言中，编译器可以自行选择先对函数中的哪个参数求值，这样做提高了编译器的效率，但是如果在函数的参数中使用了递增运算符，就会有一些问题，例如`printf("%10d %10d\n", num, num * num++);`在这里`printf()`可能先计算`num * num++`，将`5 25`的结果打印为`6 25`，甚至可能从右往左执行，对`num++`中的`num`使用`5`，对其他两个`num`使用`6`，最后打印结果为`6 30`。
- 同样，表达式也可能会出现类似问题，例如`ans = num / 2 + 5 * (1 + num++);`也无法保证编译器先计算哪项。
- 类似的还有`y = x++ + x++;`执行这句后，`x`一定会比旧值大2，但`y`的值不确定。
- 以上均为未定义行为，为避免未定义行为，应该遵循如下规则：
  
  - **如果一个变量出现在一个函数的多个参数中，不要对该变量使用递增或递减运算符。**
  - **如果一个变量多次出现在一个表达式，不要对该变量使用递增或递减运算符。**

### Section4 表达式和语句

- C表达式的一个最重要的特性是，**每个表达式都有一个值**。有赋值运算符`=`的表达式的值与赋值运算符左侧变量的值相同。
- 副作用(side effect)是对数据对象或文件的修改。
- 序列点(sequence point)是程序执行的点，在该点上，所有的副作用都在进入下一步之前发生。即在一个语句中，赋值运算符，递增运算符和递减运算符对运算对象做的改变必须在程序执行下一条语句之前完成。
- 在C语言中，语句中的分号标记了一个序列点，任何一个完整表达式的结束也是一个序列点。
- 完整表达式(full expression)指这个表达式不是另一个更大表达式的子表达式。
- 例如如下代码：

  ```C
  while (guests++ < 10)
    printf("%d \n", guests);
  ```

  由于表达式`guests++ < 10`作为`while`循环的测试条件，是一个完整表达式，因此该表达式的结束就是一个序列点，因此C保证了在程序转至`printf()`之前发生副作用（即递增`guests`），同时使用后缀形式保证了`guests`在完成与10的比较后才进行递增。

  而如下语句：

  ```C
  y = (4 + x++) + (6 + x++);
  ```

  表达式`4 + x++`不是一个完整表达式，所以C无法保证`x`在子表达式`4 + x++`求值后立即递增`x`。这里完整表达式是整个赋值表达式语句，分号标记了序列点，所以C保证在执行下一条语句之前递增`x`两次，但不保证在对子表达式求值后递增还是对所有表达式求值后递增。

### Section5 类型转换

- 基本类型转换规则：

  1. 当类型转换出现在表达式时，会从较小类型转换为较大类型，称为升级(promotion)。其中`char`和`short`会被转换成`int`，或必要时转换成`unsigned int`。
  2. 涉及两种类型的运算，两个值会被分别转换成两种类型的更高级别。
  3. 类型的级别从高到低依次是`long double, double, float, unsigned long long, long long, unsigned long ,long ,unsigned int, int`。`short`和`char`会被升级到`int`或`unsigned int`。
  4. 在赋值表达式语句中，计算的最终结果会被转换成被赋值变量的类型，这个过程可能导致类型升级或降级(demotion)。
  5. 当作为函数参数传递时，`char`和`short`被转换成`int`，`float`被转换成`double`。

- 强制类型转换(cast)中，圆括号和它括起来的类型名构成了强制类型转换运算符(cast operator)，其通用形式是`(type)`。
  
### Section6 带参数的函数

- 声明参数旧创建了被称为形式参数(formal argument/parameter)的变量，简称形参，函数调用传递的值为实际参数(actual argument/parameter)简称实参。
- C99规定了对于actual argument或actual parameter使用术语argument（实参），对于formal argument或formal parameter使用术语parameter（形参），可以认为，形参是变量，实参是函数调用提供的值，实参被赋给相应的形参。

## Chapter6 C控制语句：循环

### Section2 `while`语句

- 循环在执行完测试条件后的第1条语句（简单语句或复合语句）后进入下一轮迭代，直到测试条件为假才会结束。
- 单独一个分号被视为一条语句，称为空语句(null statement)。
- 处理空语句更好的方式是使用`continue`语句。

### Section3 用关系运算符和表达式比较大小

- 关系运算符不能用于比较字符串。
- 比较浮点数时，尽量只使用`<`或`>`。因为浮点数的舍入误差会导致在逻辑上应该相等的两数不相等。
- C99提供了`stdbool.h`头文件，该沟文件让`bool`成为`_Bool`的别名，而且把`true`和`false`分别定义为1和0的符号常量。包含该头文件后，写出的代码可以与C++兼容，因为C++把`bool, true, false`定义为关键字。
- 关系运算符的优先级比算术运算符低，比赋值运算符高。
- 关系运算符中，`<, <=, >, >=`为高优先级，`==, !=`为低优先级。

### Section6 `for`循环

- 关键字`for`后的圆括号有三个表达式，被称为控制表达式，都是完整表达式，所以每个表达式的副作用（如递增变量）都会发生在对下一个表达式求值之前。
- 第三个表达式可以使用任何合法的表达式，无论是什么表达式，每次迭代都会更新该表达式的值。如`for (x = 1; y <= 45; y = (++x * 5) + 50)`。
- 可以省略一个或多个表达式（但是不能省略分号），只要在循环中包含能结束循环的语句即可。例如：

  ```C
  for (n = 3; ans <= 25;)
    ans = ans * n;
  ```

- 第一个表达式不一定是给变量赋初始值，也可以使用`printf()`。但是在执行循环的其他部分之前，只对第一个表达式求值一次或执行一次。例如：

  ```C
  for (printf("Keep entering numbers!\n"); num != 6; )
    scanf("%d", &num);
  ```

- 循环体中的行为可以改变循环头中的表达式。例如`for (n = 1; n < 10000; n = n + delta)`。如果循环体中有命令，可以在运行时改变`delta`的大小。
- 第一个表达式在首次循环前执行，因此可以使用类似如下代码：

  ```C
  int i, sum;

  for (i = 0, sum = 0; i < 5; ++i)
  ```

  也可以在第一个表达式中声明计数变量，例如：

  ```C
  for (int i = 0; i < 5; ++i)
  ```

  但是，如果使用类似的用法，**会出现错误**：

  ```C
  double sum;

  for (int i = 0, sum = 0; i < 5; ++i)
  ```

  因为这种方式在`for`循环体内部声明了一个`int`类型的值`sum`，而不是使用在循环体外部声明的`double`类型的`sum`，从而导致使用未初始化的值，产生不可预知的结果。

### Section6 其他赋值运算符：`+=, -=, *=, /=, %=`

- 和递增/递减运算符一样，使用组合形式的赋值运算符生成的机器代码更高效。

### Section7 逗号运算符

- 逗号运算符并不局限于在`for`循环中使用，但这是最常用的地方。
- 逗号运算符保证了被分隔的表达式从左往右求值，即逗号是一个序列点，所以逗号左侧项的所有副作用都在程序执行逗号右侧项之前发生。
- 逗号表达式的值是右侧项的值，例如`x = (y = 3, (z = ++y + 2) + 5);`中，最终将结果11赋给`x`。
- 另一例中，`houseprice = 249,500`，C编译器将其解释为一个逗号表达式，即`houseprice = 249`是逗号左侧的子表达式，`500`是右侧的子表达式。因此整个逗号表达式的值是逗号右侧表达式的值，等价于`houseprice = 249; 500;`。
- 而`houseprice = (249,500)`中，赋给`houseprice`的值是逗号右侧表达式的值，即`500`。

### Section9 如何选择循环

- 要让`for`循环看起来像`while`循环，可以省略第一个和第三个表达式，例如`for (; test;)`等价于`while (test)`。
- 一般而言，当循环涉及初始化和更新变量时，用`for`循环比较合适，而在其他情况下，使用`while`循环更好。

## Chapter7 C控制语句：分支和跳转

### Section2 `if else`语句

- `while ((ch = getchar()) != '\n')`是C特有的编程风格，将两个行为合并为一个表达式。因为赋值表达式的值是赋值运算符左侧运算对象的值，所以`ch = getchar()`的值就是`ch`的值，因此在读取`ch`的值后，测试条件相当于`ch != '\n'`。如果省略`ch = getchar()`两侧的括号，变成`while (ch = getchar() != '\n')`，因为`!=`的运算优先级比`=`高，因此先对表达式`getchar() != '\n'`求值。由于这是关系表达式，因此值为`1`或`0`，然后赋值，从而导致`ch`的值只会是`0`或`1`，而不是`getchar()`的返回值。
- 如果没有花括号，`else`与离它最近的`if`匹配。

### Section3 逻辑运算符

- C保证逻辑表达式的求值顺序是从左往右，且`&&`和`||`运算符都是序列点。因此这样的代码可以生效：`while ((c = getchar()) != ' ' && c != '\n')`。因为第一个子表达式会将读取的值赋给`c`，给第二个子表达式使用。如果没有这个机制，可能会在对`c`赋值前先对后一个子表达式求值。
- `&&`运算符可用于测试范围，但是只能使用`range >= 90 && range <= 100`的写法，而不能使用`90 <= range <= 100`。因为`<=`运算符的求值顺序为从左至右，因此编译器会把表达式解释为`(90 <= range) <= 100`。由于`90 <= range`一定为`0`或`1`，因此无论`range`的值，整个表达式恒为真。

### Section5 条件运算符`?`

- 条件运算符为C语言中唯一的三元运算符。使用条件运算符会让编译器生成更紧凑的程序代码。

### Section7 多重选择：`switch`和`break`

- 如果没有`break`语句，会从匹配标签开始执行到`switch`末尾。
- `break`语句可用于循环和`switch`语句中，但是`continue`只能用于循环中。如果`switch`语句在一个循环中，`continue`便可作为`switch`语句的一部分。这种情况下，`continue`让程序跳出循环的剩余部分，包括`switch`语句的其他部分。
- `switch`在圆括号中的测试表达式的值应该是一个整数值（包括`char`类型）。`case`标签必须是整数类型（包括`char`类型）的常量或整型常量表达式。不能用变量作为`case`标签。

### Section8 `goto`语句

- 原则上避免使用`goto`语句。
- C程序员可以接受一种`goto`的用法，即出现问题时从一组嵌套循环中跳出（而`break`只能跳出当前循环）。

## Chapter8 字符输入/输出和输入验证

### Section2 缓冲区

- 缓冲分为两类，完全缓冲I/O和行缓冲I/O。完全缓冲输入指的是当缓冲区被填满时才刷新缓冲区（内容被发送至目的地），通常出现在文件输入中。行缓冲指的是在出现换行符时刷新缓冲区，键盘输入通常是行缓冲输入。

### Section3 结束键盘输入

- 在C语言中，用`getchar()`读取文件检测到文件结尾时将返回一个特殊的值，即`EOF`(end of file)，`scanf()`函数检测到文件结尾时也返回`EOF`。
- 通常`EOF`定义在`stdio.h`文件中：`#define EOF (-1)`。因为`getchar()`的返回值介于0～127，对应标准字符集（扩展字符集对应0～255），而-1不在范围内，因此可以用于标记文件结尾。
- 使用`while ((ch = getchar()) != EOF)`时，最好用声明`int ch;`代替`char ch;`，因为`char`类型的变量只能表示0～255的无符号整数，而`EOF`的值是-1。

### Section4 重定向和文件

- 命令与重定向运算符的顺序无关，对于命令`echo_eof < mywords > savewords`，命令`echo > savewords < mywords`同样起作用。

### Section5 创建更友好的用户界面

- 缓冲输入要求用户按下Enter键发送输入，但这一动作也传送了换行符，在读取后会将换行符留在缓冲区的输入队列中。
- 和`scanf()`不同，`getchar()`不会跳过换行符，

## Chapter9 函数

### Section1 复习函数

- 函数原型(function protytype)告诉编译器函数的类型。
- 函数调用(functioin call)表示在此执行函数。
- 函数定义(function definition)明确指定了函数要做什么。
- ANSI C要求在函数定义的每个变量前都声明其类型。声明函数原型可以省略变量名。
- 形式参数是被调函数(called function)中的变量，实际参数是主调函数(calling function)赋给被调函数的具体值。

### Section3 递归

- 递归函数必须包含能让递归调用停止的语句。通常，递归函数都使用`if`或其他等价的测试条件在函数形参等于某特定值时终止递归。为此，每次递归调用的形参都要使用不同的值。
- 最简单的递归形式是把递归调用置于函数的末尾，即正好在`return`语句之前。这种形式的递归被称为**尾递归**(tail recursion)，因为递归调用在函数的末尾。尾递归是最简单的递归形式，因为相当于循环。
- 每次递归都会创建一组变量，所以递归使用的内存更多，而且每次递归调用都会把创建的一组新变量放在栈中。递归调用的数量受限于内存空间。
- 由于每次函数调用要花费一定的时间，所以递归的执行速度较慢。
- 递归在处理倒序问题时较为方便。

### Section7 指针简介

- 指针(pointer)是一个值为内存地址的变量（或数据对象）。
- 间接运算符`*`(indirection operator)也称为解引用运算符(dereferencing operator)。
- 地址运算符`&`后跟一个变量名时，`&`给出该变量的地址；地址运算符`*`后跟一个指针名或地址时，`*`给出储存在指针指向地址上的值。
- 声明指针变量时必须指定指针所指向变量的类型，因为不同变量类型占用不同的存储空间，一些指针操作要求知道操作对象的大小。
- 被调函数一般不会改变主调函数中的变量，如果要改变，应使用指针作为参数。如果希望把更多的值传回主调函数，必须使用指针。

## Chapter10 数组和指针

### Section1 数组

- 数组由数据类型相同的一系列元素组成。
- 普通变量可以使用的类型，数组元素都可以使用。
- 用以逗号分隔的值列表（用花括号括起来）对数组进行初始化。
- 使用数组前必须先初始化。如果不初始化数组，数组元素和未初始化的普通变量一样，其中储存的都是垃圾值；但是如果部分初始化数组，剩余的元素就会被初始化为0。
- 如果初始化列表的项数多于数组元素个数，编译器会将其视为错误。可以省略方括号中的数字，让编译器自动匹配数组大小和初始化列表中的项数，例如`const int days[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 31};`但是如果让编译器自动识别，则可能导致无法察觉初始化列表中的项数有误。
- C99增加了一个新特性：指定初始化器(designated initializer)。利用该特性可以初始化指定的数组元素。例如，只初始化数组的最后一个元素。对于传统的C初始化语法，必须初始化最后一个元素之前的所有元素才能初始化它，而C99规定，可以在初始化列表中使用带方括号的下标指明待初始化的元素。例如：

  ```C
  int arr[6] = {0, 0, 0, 0, 0, 212};  // 传统的语法
  int arr[6] = {[5] = 212};  // C99特性，把arr[5]初始化为212
  ```

- 下例给出了指定初始化器的两个重要特性：

  ```C
  #include <stdio.h>
  #define MONTHS 12
  int main(void)
  {
      int days[MONTHS] = {31, 28, [4] = 31, 30, 31, [1] = 29};
      int i;

      for (i = 0; i < MONTHS; i++)
          printf("%2d %d\n", i + 1, days[i]);

      return 0;
  }

  /* Output:
  1 31
  2 29
  3 0
  4 0
  5 31
  6 30
  7 31
  8 0
  9 0
  10 0
  11 0
  12 0
  */
  ```

  1. 如果指定初始化器后面有更多的值，那么后面的值将被用于初始化指定元素后面的元素。
  2. 如果再次初始化指定的元素，那么最后的初始化会取代之前的初始化。

- 如果未指定元素大小，编译器会把数组的大小设置为足够装得下初始化的值。

  ```C
  int stuff[] = {1, [6] = 23};  // 7个元素
  int stuff[] = {1, [6] = 4, 9, 10};  // 9个元素
  ```

- 编译器不会检查数组下标是否使用得当。在C标准中，使用越界下标的结果是未定义的。

### Section2 多维数组

- 一维数组下数据个数和数组大小不匹配的问题同样适用于多维数组中的每一行。如果数量不足，则被默认初始化为0，如果某一行超出则会报错，但是不会影响其他行的初始化。
- 初始化时也可省略内部的花括号，只保留最外面的一对花括号。只要保证初始化的数值个数正确，则没有任何区别。但是如果初始化的数值不够，则按照先后顺序逐行初始化，直到用完所有的值，后面没有被初始化的元素被统一初始化为0.

### Section3 指针和数组

- 数组名是数组首元素的地址。即如果`flizny`是一个数组，则`flizny == &flizny[0];`
- 在C中，指针加1指的是增加一个**存储单元**。对数组而言，意味值加1后的地址是下一个**元素**的地址，而不是下一个字节的地址。这也是为什么必须声明指针所指向的对象类型的原因之一。指针加1，指针的值递增它所指向类型的大小（以字节为单位）。
- 对于C：
  
  ```C
  dates + 2 == &date[2];  // 相同的地址
  *(dates + 2) == dates[2];  // 相同的值
  ```

- 间接运算符`*`的优先级较高，因此：

  ```C
  *dates + 2;  // dates第一个元素的值+2
  (*dates) + 2;  // dates第一个元素的值+2
  *(dates + 2);  // dates第3个元素的值
  ```

### Section4 函数、数组和指针

- 只有在函数原型或函数定义头中，才可以用`int ar[]`代替`int * ar`。`int * ar`形式和`int ar[]`形式都表示`ar`是一个指向`int`的指针。但是`int ar[]`只能用于声明形式参数。`int ar[]`提醒指针`ar`指向的不仅仅是一个`int`类型值，还是一个`int`类型数组的元素。
- 因为数组名是该数组首元素的地址，作为实际参数的数组名要求形式参数是一个与之匹配的指针。只有在这种情况下，C彩绘把`int ar[]`和`int * ar`解释成一样。由于函数原型喝一省略参数名，所以以下4种原型等价：

  ```C
  int sum(int *ar, int n);
  int sum(int *, int);
  int sum(int ar[], int n);
  int sum(int [], int);
  ```

  而在函数定义中不能省略参数名，以下2种函数定义等价：

  ```C
  int sum(int *ar, int n)
  {
      // codes
  }

  int sum(int ar[], int n)
  {
      // codes
  }
  ```

- C保证在给数组分配空间时，指向数组后面第一个位置的指针仍是有效指针，这使得书中例子所使用的`while`循环测试条件有效且简洁：

  ```C
  int sump(int *start, int *end)
  {
      int total = 0;

      while (start < end)
      {
          total += *start;
          start++;  // 让指针指向下一个元素
          /* 
          在最后一次while循环种执行完start++后，
          start的值就是end的值。
          */
      }

      return total;
  }
  ```

  循环体还可以压缩诶成一行代码：`total += *start++;`。一元运算符`*`和`++`的优先级相同，但结合律是从右往左，所以`start++`先求值，然后才是`*start`。也就是说，指针`start`先递增后指向。使用后缀形式意味着先把指针指向位置上的值加到`total`上，然后在递增指针。如果使用前缀形式`*++start`，则先递增指针，再使用指针指向位置上的值。如果使用`(*start)++`，则先使用`start`指向的值，再递增该值，而不是递增指针。这样，**指针将一直指向同一个位置，但是该位置上的值发生了变化**。下例演示了优先级的情况：

  ```C
  #include <stdio.h>
  int data[2] = {100, 200};
  int moredata[2] = {300, 400};
  int main(void)
  {
      int *p1, *p2, *p3;
  
      p1 = p2 = data;
      p3 = moredata;
      printf("  *p1 = %d,   *p2 = %d,     *p3 = %d\n", *p1, *p2, *p3);
      printf("*p1++ = %d, *++p2 = %d, (*p3)++ = %d\n", *p1++, *++p2, (*p3)++);
      printf("  *p1 = %d,   *p2 = %d,     *p3 = %d\n", *p1, *p2, *p3);

      return 0;
  }

  /* Output:
      *p1 = 100,   *p2 = 100,     *p3 = 300
    *p1++ = 100, *++p2 = 200, (*p3)++ = 300
      *p1 = 200,   *p2 = 200,     *p3 = 301
  */
  ```

  其中只有`(*p3)++`改变了数组元素的值，其他两个操作分别把`p1`和`p2`指向数组的下一个元素。

- 处理数组的函数实际上用指针作为参数。使用数组表示法和指针表示法是等价的，但指针表示法（尤其与递增运算符一起使用时）更接近机器语言，因此一些编译器在编译时能生成效率更高的代码。

### Section5 指针操作

- 以下程序演示了C提供的指针变量的8种基本操作：

  ```C
  #include <stdio.h>
  int main(void)
  {
      int urn[5] = {100, 200, 300, 400, 500};
      int *ptr1, *ptr2, *ptr3;
  
      ptr1 = urn;  // 把一个地址赋给指针
      ptr2 = &urn[2];  // 把一个地址赋给指针
  
      // 解引用指针，获得指针的地址
      printf("pointer value, dereferenced pointer, pointer address:\n");
      printf("ptr1 = %p, *ptr1 = %d, &ptr1 = %p\n", ptr1, *ptr1, &ptr1);

      // 指针加法
      ptr3 = ptr1 + 4;
      printf("\nadding an int to a pointer:\n");
      printf("ptr1 + 4 = %p, *(ptr1 + 4) = %d\n", ptr1 + 4, *(ptr1 + 4));

      // 递增指针 
      ptr1++;
      printf("\nvalues after ptr1++:\n");
      printf("ptr1 = %p, *ptr1 = %d, &ptr1 = %p\n", ptr1, *ptr1, &ptr1);

      // 递减指针
      ptr2--;
      printf("\nvalues after ptr2--:\n");
      printf("ptr2 = %p, *ptr2 = %d, &ptr2 = %p\n", ptr2, *ptr2, &ptr2);
     
      --ptr1;  // 恢复为初始值
      ++ptr2;  // 恢复为初始值
      printf("\nPointers reset to original values:\n");
      printf("ptr1 = %p, ptr2 = %p\n", ptr1, ptr2);
  
      // 一个指针减去另一个指针
      printf("\nsubtracting one pointer from another:\n");
      printf("ptr2 = %p, ptr1 = %p, ptr2 - ptr1 = %td\n", ptr2, ptr1, ptr2 - ptr1);
  
      // 一个指针减去一个整数
      printf("\nsubtracting an int from a pointer:\n");
      printf("ptr3 = %p, ptr3 - 2 = %p\n", ptr3, ptr3 - 2);
  
      return 0;
  }

  /* Output:
  pointer value, dereferenced pointer, pointer address:
  ptr1 = 0x7ffe481ce180, *ptr1 = 100, &ptr1 = 0x7ffe481ce168

  adding an int to a pointer:
  ptr1 + 4 = 0x7ffe481ce190, *(ptr1 + 4) = 500

  values after ptr1++:
  ptr1 = 0x7ffe481ce184, *ptr1 = 200, &ptr1 = 0x7ffe481ce168

  values after ptr2--:
  ptr2 = 0x7ffe481ce184, *ptr2 = 200, &ptr2 = 0x7ffe481ce170

  Pointers reset to original values:
  ptr1 = 0x7ffe481ce180, ptr2 = 0x7ffe481ce188

  subtracting one pointer from another:
  ptr2 = 0x7ffe481ce188, ptr1 = 0x7ffe481ce180, ptr2 - ptr1 = 2

  subtracting an int from a pointer:
  ptr3 = 0x7ffe481ce190, ptr3 - 2 = 0x7ffe481ce188
  */
  ```

  - 赋值：将地址赋给指针，可以用数组名，带地址运算符`&`的变量名，另一个指针进行赋值。
  - 解引用：`*`运算符给出指针指向地址上储存的值。
  - 取址：和所有变量一样，指针变量也有地址和值。上例中，`&ptr1`是指向`ptr1`的指针，而`ptr1`是指向`urn[0]`的指针。
  - 指针与整数相加：如果相加的结果超出了初始指针指向的数组范围，则计算结果是未定义的，除非正好超过数组末尾第一个位置，C保证该指针有效。
  - 递增指针：递增指向数组元素的指针可以让该指针移动至数组的下一个元素。递减指针同理。
  - 指针减去一个整数：可以使用`-`运算符从一个指针中减去一个整数。指针必须是第一个运算符对象，整数是第二个运算对象。
  - 指针求差：可以计算两个指针的差值，两个指针必须指向同一个数组的不同元素。通过求差可以计算出两个元素的距离。差值的单位与数组类型的单位相同。
  - 比较：使用关系运算符可以比较两个指针的值，前提是两个指针都指向相同类型的对象。

- 禁止解引用未初始化的指针。
- 当有：

  ```C
  int urn[3];
  int *ptr1, *ptr2;

  ptr1++;  // 有效
  urn++;  // 无效
  ```

  **不能因为之前的内容而错误的认为数组完全等同于指针**。上例中的`urn`是一个数组，指向数组首个元素的地址，但是数组是一个不可修改的左值。在C中，没有运算符可以修改数组本身（只能修改其中的元素）。

### Section6 保护数组中的数据

- 在函数原型和函数定义中声明形式参数时使用`const`，可以防止修改数组中的数据内容。在函数定义和函数原型中使用`const`并不是要求原数组是常量，而是该函数在处理数组时将其视为常量。
- 虽然用`#define`指令可以创建类似`const`的符号常量，但是`const`的使用更加灵活，可以创建`const`数组，`const`指针和指向`const`的指针：
  - `const`数组：
  
    ```C
    #define MONTHS 12
    const int days[MONTHS] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    days[9] = 44;  // 编译错误
    ```

  - 指向`const`的指针：

    ```C
    double rates[5] = {88.99, 100.12, 59.45, 183.11, 340.5};
    const double *pd = rates;  // pd指向数组的首元素

    *pd = 29.89;  // 编译错误，不允许
    pd[2] = 222.22;  // 编译错误，不允许
    rates[0] = 99.99;  // 允许，因为rates未被const限定
    pd++;  // 让pd指向rates[1]，允许
    ```

    无论使用数组表示法还是指针表示法，都不允许使用`pd`修改它所指向数据的值，因为第二行代码把`pd`指向的`double`类型的值声明为`const`，因此不能使用`pd`改变指向的值。但是`rates`并没有被声明为`const`，所以仍然可以通过`rates`修改元素的值。同时,让`pd`指向别处也是允许的。

    指向`const`的指针通常用于函数形参中，表明该函数不会使用指针改变数据。

    把`const`数据或非`const`数据的地址初始化为指向`const`的指针或为其赋值是合法的：

    ```C
    double rates[5] = {88.99, 100.12, 59.45, 183.11, 340.5};
    const double locked[4] = {0.08, 0.075, 0.0725, 0.07};
    const double * pc = rates;  // 有效
    pc = locked;  // 有效
    pc = &rates[3];  // 有效
    ```

    但是只能把非`const`数据的地址赋给普通指针：

    ```C
    double rates[5] = {88.99, 100.12, 59.45, 183.11, 340.5};
    const double locked[4] = {0.08, 0.075, 0.0725, 0.07};
    double * pnc = rates;  // 有效
    pnc = locked;  // 无效
    pnc = &rates[3];  // 有效
    ```

    显然，如果允许将`const`数据赋给普通指针，则能通过指针改变`const`数组的中的数据，这与`const`数据冲突。

    如果使用非`const`标识符的形参修改`const`数据，会导致未定义的结果。

  - `const`指针：

    可以使用`const`声明并初始化一个不能指向别处的指针，关键是`const`的位置：

    ```C
    double rates[5] = {88.99, 100.12, 59.45, 183.11, 340.5};
    double * const pc = rates;  // pc指向数组的开始
    pc = &rates[2];  // 不允许，应该该指针不能指向别处
    *pc = 92.99;  // 允许，更改rates[0]的值
    ```

    这种指针可以修改指向的值，但是只能指向初始化时设置的地址。

  - 使用`const`两次：

    创建指针时使用`const`两次，使该指针既不能更改它所指向的地址，也不能修改指向地址上的值：

    ```C
    double rates[5] = {88.99, 100.12, 59.45, 183.11, 340.5};
    const double * const pc = rates;
    pc = &rates[2];  // 不允许
    *pc = 92.99;  // 不允许
    ```

### Section7 指针和多维数组

- 给定多维数组`int zippo[4][2];`数组名`zippo`时数组首元素的地址。在这里，`zippo`的首元素是一个内含两个`int`值的数组，所以`zippo`是这个内含两个`int`值的数组的地址。
  
  - 因为`zippo`是数组首元素的地址，所以`zippo`的值和`&zippo[0]`的值相同，而`zippo[0]`本身是一个内含两个`int`的数组，所以`zippo[0]`的值和它的首元素（一个`int`）的地址相同，即`&zippo[0][0]`的值。简言之，`zippo[0]`是一个占用一个`int`大小对象的地址，而`zippo`是一个占用两个`int`大小对象的地址。由于这个整数和含两个整数的数组都开始于同一个地址，因此`zippo`和`zippo[0]`的值相同。
  - 由于`zippo`指向的对象占用两个`int`大小，而`zippo[0]`对应的对象为一个`int`，因此`zippo + 1`和`zippo[0] + 1`不同。
  - 解引用指针或在数组名后使用带下标的`[]`运算符，得到引用对象代表的值。因为`zippo[0]`是该数组首元素`zippo[0][0]`的地址，所以`*(zippo[0])`表示储存在`zippo[0][0]`上的值，即一个`int`。`*zippo`代表该数组首元素`zippo[0]`的值，但`zippo[0]`对应一个`int`类型值的地址，为`&zippo[0][0]`，所以`*zippo`为`&zippo[0][0]`。从而，`**zippo`与`*&zippo[0][0]`等价，相当于`zippo[0][0]`，即一个`int`。简言之，`zippo`是地址的地址，需要解引用两次获得原始值。地址的地址或指针的指针就是双重间接(double indirection)的例子。

- 如果需要声明一个指针变量指向一个`int`类型的二维数组，把指针声明为指向`int`类型不够，而需要指向一个内含两个`int`类型值的数组，因此声明应该为`int (*pz)[2];`其中因为`[]`的优先级高于`*`，因此需要使用括号。如果不使用括号，则`int *pax[2];`中，`pax`先与`[]`结合，然后再与`*`结合，所以`int *pax[2];`声明了一个内含两个指向`int`的指针的数组。
- 指针之间的赋值比数值类型之间的赋值严格。在数值类型中，`int`类型的值可以直接赋给`double`类型的变量，但是在指针中是不允许的。

  ```C
  int n = 5;
  double x;
  int *pl = &n;
  double *pd = &x;
  x = n;  // 隐式类型转换
  pd = pl;  // 编译错误
  ```

  对于更复杂的类型也是如此：

  ```C
  int *pt;
  int (*pa)[3];
  int ar1[2][3];
  int ar2[3][2];
  int **p2;  // 一个指向指针的指针
  
  pt = &ar1[0][0];  // 都是指向int的指针
  pt = ar1[0];  // 都是指向int的指针
  pt = ar1;  // 无效
  pa = ar1;  // 都是指向内含3个int类型元素数组的指针
  pa = ar2;  // 无效
  p2 = &pt;  // 都是指向int指针的指针
  *p2 = ar2[0];  // 都是指向int的指针
  p2 = ar2;  // 无效
  ```

- 多重解引用让人费解，例如：

  ```C
  int x = 20;
  int const y = 23;
  int *p1 = &x;
  int const *p2 = &y;
  int const **pp2;

  p1 = p2;  // 不安全 -- 把const指针赋给非const指针
  p2 = p1;  // 有效 -- 把非const指针赋给const指针
  pp2 = &p1;  // 不安全 -- 嵌套指针类型赋值
  ```

  把`const`指针赋给非`const`指针不安全，因为可以使用新指针改变`const`指针指向的数据，-执行的结果是未定义的。但是把非`const`指针赋给`const`指针是可以的，前提是只进行一级解引用。

  如果进行两级解引用，这样的赋值也不安全。例如：

  ```C
  int const **pp2;
  int *p1;
  int const n = 13;
  pp2 = &p1;  // 允许，这导致const限定符失效（但是根据第一行声明，不能通过*pp2修改所指向的内容）
  *pp2 = &n;  // 有效，都声明为const，但是会导致p1指向n（*pp2）已被修改
  *p1 = 10;  // 有效，但是将改变n的值（但是根据第三行声明，不能修改n的值）
  ```

  不安全的原因仍然为通过非`const`指针修改`const`数据，最后导致未定义的结果。

- 在函数中使用多维数组，需要正确声明函数中数组的形参。一个3行4列的二维数组可以使用如下方式声明其形参：
  - `void func(int ar[][4])`
  - `void func(int [][4])`
  - `void func(int (*ar)[4])`

  但是声明`int ar[][]`是错误的，因为编译器会把数组表示法转换为指针表示法，在编译器把`ar[1]`转换为`ar + 1`时需要知道`ar`所指的对象的大小。在`ar[][4]`中，说明`ar`指向一个内含4个`int`类型的数组，如果第二个方括号为空，则编译器无法处理相关内容。

  可以在第1个方括号中写上大小，但是**编译器会忽略该值**。

  **声明一个指向N维数组的指针时，只能省略最左边方括号中的值**。例如：`int sum4d(int ar[][12][20][30])`)，第一个方括号表示这是一个指针，其他方括号用于描述指针所指向的数据对象的类型，这样的声明等价于`int sum4d(int (*ar)[12][20][30])`，在这里，`ar`是一个指针，指向一个12\*20\*30的`int`数组。

### Section8 变长数组（VLA）

- C99新增了变长数组(variable-length array, VLA)，允许使用变量表示数组的维度。
- 变长数组有一定的限制，必须是自动存储类编，不能使用`static`或`extern`存储类表说明符，而且**不能在声明中初始化**。
- C11把变长数组作为一个可选特性，而不是必须实现的特性。
- 变长数组**不能改变大小**。这里的变长只可以在创建数组时使用变量指定数组的维度。
- C99/11标准允许在声明变长数组时使用`const`变量。该数组的定义必须是声明在块中的自动存储类别数组。
- 声明一个带二维变长数组参数的函数，需要使用如下形式：
  
  ```C
  int sum2d(int rows, int cols, int ar[rows][cols]);  // ar是一个变长数组(VLA)
  ```

  形参`rows`和`cols`用作形参`ar`的维度。因为`ar`的声明要使用`rows`和`cols`，所以在形参列表中必须在声明`ar`前声明这两个形参，因此如下原型是错误的：

  ```C
  int sum2d(int ar[rows][cols], int rows, int cols);  // 无效的顺序
  ```

  C99/C11标准规定，可以省略原型中的形参名，但这种情况下必须用星号代替省略的维度：

  ```C
  int sum2d(int, int, int ar[*][*]);  // ar是一个变长数组(VLA)，省略维度形参名
  ```

### Section9 复合字面量

- C99新增了复合字面量(compound literal)。字面量是除符号常量外的常量。
- 数组的复合字面量类似于数组初始化列表：

  ```C
  int diva[2] = {10, 20};
  (int [2]) {10, 20};  // 复合字面量
  ```

  复合字面量创建了一个和`diva`数组相同的匿名数组，去掉声明中的数组名后，留下的`int [2]`即是复合字面量的类型名。

- 复合字面量是匿名的，所以不能先创建然后再使用，而是必须在创建的时候同时使用。
- 也可以把复合字面量作为实际参数传递该带有匹配形式的函数。例如：

  ```C
  int sum(const int ar[], int n);
  ...
  int total3;
  total3 = sum((int []) {4, 4, 4, 5, 5, 5}, 6);
  ```

- 复合字面量也可以应用于多维数组，例如：

  ```C
  int (*pt2)[4];
  pt2 = (int [2][4]) {{1, 2, 3, -9}, {4, 5, 6, -8}};
  ```

- 复合字面量是提供只临时需要的值的一种手段。复合字面量具有块作用域，一旦离开复合字面量的块，程序将无法保证该字面量的存在。

### 补充：`const`和指针

在理解指针和`const`方面，有两篇很好的回答，附录于此作为参考：

- [在定义指针的时候，写成「int* p;」和「int *p;」哪个更好？](https://www.zhihu.com/question/21136956/answer/1668990148)
  
  > 推荐使用`int *p`的写法。
  >
  > 相比直接将`int*`理解为指针，上面的“运算式”写法**避免了对`*`符号理解的二义性**，即可以**永远将`*`理解为“按址取值”的一个运算符**，“`p`类型为指针”的结论由**编译器根据“`*p`为`int`类型”这个声明反推出来**。更重要的是这个理解方式可以应用到更加复杂的类型声明语句中。
  >
  > 例如典型的：`char *argv[];`，要声明的变量名`argv`按照既定的运算顺序（一元运算符优先级最高，且遵循**从右向左**的结合顺序），**先执行数组索引运算，再执行按址取值运算，最终得到`char`类型**，那么就可以反推出：**`argv[i]`为指向`char`的指针**，从而**`argv`为一个由`char`指针组成的数组**。
  >
  > 又例如：`int (*p)[N];`，**`p`在这里先执行按址取值运算，再执行数组索引运算，最终得到`int`类型**，从而反推出 **`*p`为一个长度为`N`的`int`数组，从而`p`为指向这个数组的一个指针**。

- [C++里 const int* 与 int const* 有什么区别？](https://www.zhihu.com/question/443195492/answer/1723886545)

  [Const before or const after?](https://stackoverflow.com/questions/5503352/const-before-or-const-after)

  > **const默认作用于其左边的东西，否则作用于其右边的东西**。
  >
  > 例如`const int *`，`const`只有右边有东西，所以`const`修饰`int`成为常量整型，然后`*`再作用于常量整型。所以这是 a pointer to a constant integer（指向一个整型，不可通过该指针改变其指向的内容，但可改变指针本身所指向的地址）。
  >
  > 再如`int const *`，`const`左边有东西，所以`const`作用于`int`，`*`再作用于`int const`所以这还是 a pointer to a constant integer。
  >
  > 如果`int * const`，`const`的左边是`*`，所以`const`作用于指针（不可改变指向的地址），所以这是 a constant pointer to an integer，可以通过指针改变其所指向的内容但只能指向该地址，不可指向别的地址。
  >
  > 如果`const int * const`，左边的`const`的左边没东西，右边有`int`，那么此`const`修饰`int`。右边的`const`作用于`*`使得指针本身变成`const`（不可改变指向地址），那么这个是 a constant pointer to a constant integer，不可改变指针本身所指向的地址也不可通过指针改变其指向的内容。
  >
  > 以此类推，`int const * const`仍然是 a constant pointer to a constant integer；`int const * const *`，a pointer to a constant pointer to a constant integer；`int const * const * const`，a constant pointer to a constant pointer to a constant integer。
  > 从代码可读性易维护性出发，强烈推荐把`const`写在右边，可以跟指针的作用范围很好地统一起来不至于混乱。

## Chapter11 字符串和字符串函数

### Section1 字符串和字符串函数

- `puts()`函数也属于`stdiio.h`系列的输入输出函数。但是`puts()`函数只显示字符串，而且自动在显示的字符串末尾加上换行符。
- 用双引号括起来的内容称为字符串字面量(string literal)，也叫做字符串常量(string constant)。双引号中的字符和编译器自动加入末尾的`\0`字符，都作为字符串储存在内存中。
- 在字符串内部使用双引号需要转义`\`。
- 字符串常量属于静态存储类别(static storage class)。这说明如果在函数中使用字符串常量，**该字符串只会被储存一次，在整个程序的生命周期内存在**。
- 用双引号括起来的内容被视为指向该字符串存储位置的指针。
- 在指定数组大小时，要确保数组的元素个数至少比字符串长度多1，用于容纳空字符`\0`。所有未被使用的元素都被自动初始化为`\0`。
- 字符数组名和其他数组名一样，是该数组首字母的地址。
- 可以使用数组形式和指针形式创建字符串，例如：

  ```C
  char const *pt1 = "Something is pointing at me.";
  char const ar1[] = "Something is pointing at me.";
  ```

  以上两种形式几乎相同，但是并不完全相同。

  - 数组形式`ar1[]`在内存中分配一个内含29个元素的数组（一个元素对应一个字符，再加上末尾的空字符`'\0`）。程序载入内存时，也载入了程序中的字符串，字符串储存在静态存储区(static memory)中。但是，程序在开始运行时才为该数组分配内存，此时才将字符串拷贝到数组中。此时字符串有两个副本，一个是在静态内存中的字符串字面量，一个是储存在`ar1`数组中的字符串。

    此后，编译器将数组名`ar1`识别为该数组首元素地址`&ar1[0]`的别名。**在数组形式中，`ar1`是地址常量**，不能更改`ar1`，如果改变了`ar1`则意味着改变了数组的存储位置（即地址）。可以进行类似`ar1 + 1`的操作，标识数组的下一个元素，但是不允许进行`++ar1`的操作。递增运算符只能用于可修改的左值，不能用于常量。

  - 指针形式`*pt1`也使编译器为字符串在静态存储区预留29个元素的空间。另外，一旦开始执行程序，编译器会为**指针变量`pt1`**留出一个储存位置，并把字符串的地址储存在指针变量中。该变量最初指向该字符串的首字符，但是值可以改变，因此可以使用递增运算符。
  
    字符串字面量被视为`const`数据。由于`pt1`指向这个`const`数据，所以应该把`pt1`声明为指向`const`数据的指针。如果把一个字符串字面量拷贝给一个数组，就可以随意改变数据，除非把数组名声明为`const`。经过测试，如果不将指针声明为指向`const`数据的指针，并尝试使用指针修改字符串字面量，则会通过编译，但在运行时报错。

  - 总之，**初始化数组把静态存储区的字符串拷贝到数组中，而初始化指针只把字符串的地址拷贝给指针**。如下例：

    ```C
    #define MSG "I'm special"
      
    #include <stdio.h>
    int main()
    {
        char ar[] = MSG;
        const char *pt = MSG;
        printf("address of \"I'm special\": %p \n", "I'm special");
        printf("              address ar: %p\n", ar);
        printf("              address pt: %p\n", pt);
        printf("          address of MSG: %p\n", MSG);
        printf("address of \"I'm special\": %p \n", "I'm special");

        return 0;
    }

    /* Output:
    address of "I'm special": 0x55852b51f008 
                  address ar: 0x7ffc2044882c
                  address pt: 0x55852b51f008
              address of MSG: 0x55852b51f008
    address of "I'm special": 0x55852b51f008 
    */
    ```

    上例说明：
    1. `pt`和`MSG`地址相同，而`ar`的地址不同。
    2. 虽然字符串字面里`"I'm special"`在程序的两个`printf()`函数中出现了两次，但是编译器只使用了一个存储位置，而且与`MSG`的地址相同。编译器可以把多次使用的相同的字面里存储在一处或多处，另一个编译器可能在不同的位置存储3个`"I'm special"`。
    3. 静态数据使用的内存与`ar`使用的动态内存不同。不仅值不同，特定编译器甚至使用不同的位数表示两种内存。

- 给出如下两个声明：

  ```C
  char heart[] = "I love Tillie!";
  char const *head = "I love Millie!";
  ```

  最主要的区别是，数组名`heart`是常量而指针名`head`是变量。

  在实际使用中，两者都可以使用数组表示法和指针加法：

  ```C
  // 数组表示法
  for (i = 0; i < 6; i++)
  {
      putchar(heart[i]);
  }
  putchar('\n');

  for (i = 0; i < 6; i++)
  {
      putchar(head[i]);
  }
  putchar('\n');

  // 指针加法
  for (i = 0; i < 6; i++)
  {
      putchar(*(heart + i));
  }
  putchar('\n');
  for (i = 0; i < 6; i++)
  {
      putchar(*(head + i));
  }
  putchar('\n');
  ```

  但是只有指针表示法可以使用递增操作：

  ```C
  while (*(head) != '\0)  // 在字符串末尾处停止
  {
    putchar(*(head++));  // 打印字符，指向下一个位置
  }

  可以让`head`指针指向`heart`数组的首元素，但是不能反过来：

  ```C
  head = heart;  // head现在指向数组heart
  heart = head;  // 非法构造
  ```

  这类似于`x = 3`和`3 = x`的情况。赋值运算符的左边必须是可修改的左值。此外`head = heart`不会导致`head`指向的字符串消失，只是改变了储存在`head`中的地址，但是除非保存了`"I love Millie!"`的地址，否则当`head`指向别处时，就无法访问该字符串。

  可以改变`heart`数组中元素的信息：`heart[7] = 'M'`或`*(heart + 7) = 'M'`。因为数组的元素是变量（除非被声明为`const`），但是数组名不是变量。

- 如果未使用`const`限定符的指针初始化：`char *word = "frame";` 如果使用指针修改这个字符串： `word[1] = 'l';`编译器可能允许，但是对当前的C标准来说，**这个行为是未定义的**。这样的语句可能会导致内存访问错误。因为编译器在内存中使用一个副本表示所有完全相同的字符串字面量。例如书中给出的例子：

  ```C
  char *p1 = "Klingon";
  p1[0] = 'F';
  printf("Klingon");
  printf(": Beware the %ss!\n", "Klingon");
  ```

  在书中的编译器，所有相同的字符串字面量都使用同一个地址，因此允许`p1[0]`修改字符，将影响所有使用这个字符串字面量的代码，所以打印结果会变成：`Flingon: Beware the Flingons!`。在测试中可以正常通过编译，但执行会出现异常中断。因此，建议在把指针初始化为字符串字面量时使用`const`限定符：`char const *p1 = "Klingon";`。

  如果把非`const`数组初始化为字符串字面量不会导致类似的问题，因为**数组获得的时原始字符串的副本。**

  因此，如果不修改字符串，不要用指针指向字符串字面量。

- 可以使用两种方式创建字符串数组，指向字符串的指针数组和`char`类型数组的数组。书中给出如下示例：
  
  ```C
  #include <stdio.h>
  #define SLEN 40
  #define LIM 5
  int main(void)
  {
      char const *mytalents[LIM] = {
          "Adding numbers swiftly",
          "Multiplying accurately", "Stashing data",
          "Following instructions to the letter",
          "Understanding the C language"
      };
      char yourtalents[LIM][SLEN] = {
          "Walking in a straight line",
          "Sleeping", "Watching television",
          "Mailing letters", "Reading email"
      };
      int i;

      puts("Let's compare talents.");
      printf("%-36s %-25s\n", "My Talents", "Your Talents");
      for (i = 0; i < LIM; i++)
      {
          printf("%-36s %-25s\n", mytalents[i], yourtalents[i]);
      }
      printf("\nsizeof mytalents: %zd, sizeof yourtalents: %zd\n", sizeof(mytalents), sizeof(yourtalents));

      return 0;
  }

  /* Output
  Let's compare talents.
  My Talents                           Your Talents             
  Adding numbers swiftly               Walking in a straight line
  Multiplying accurately               Sleeping                 
  Stashing data                        Watching television      
  Following instructions to the letter Mailing letters          
  Understanding the C language         Reading email            

  sizeof mytalents: 40, sizeof yourtalents: 200
  */
  ```

  使用指向字符串的指针数组`mytalents`和`char`类型数组的数组`yourtalents`差别不大：都代表5个字符串，使用一个下标时表示一个字符串，使用两个下标时表示一个字符，初始化的方式也相同。

  但是仍然有区别。`mytalents`数组是一个内含5个指针的数组，共占用了40个字节，而`yourtalents`是一个内含5个数组的数组，每个数组内含40个`char`类型的值，共占用200字节。所以，虽然`mytalents[0]`和`yourtalents[0]`都表示一个字符串，但是`mytalents`和`yourtalents`的类型并不相同。`mytalents`的指针指向初始化时所用的字符串字面量的位置，这些字符串字面量被储存在静态内存中；而`yourtalents`中的数组储存字符串字面量的副本，所以每个字符被储存了两次。此外，为字符串数组分配内存的使用率更低，因为每个元素大小必须相同，而且必须是能储存最长字符串的大小。

  因此，如果要用数组表示一系列待显示的字符串，使用指针数组，因为会比二维数组的效率高。但是，指针数组指向的字符串字面量不能更改，而二维字符数组的内容可以修改。所以如果要改变字符串或为字符串输入预留空间，不要使用指向字符串字面量的指针。

- 字符串的绝大多数操作都是通过指针完成的。书中给出如下示例：

  ```C
  #include <stdio.h>
  int main(void)
  {
      char const *mesg = "Don't be a fool!";
      char const *copy;

      copy = mesg;
      printf("%s\n", copy);
      printf("mesg = %s; &mesg = %p; value = %p\n", mesg, &mesg, mesg);
      printf("copy = %s; &copy = %p; value = %p\n", copy, &copy, copy);

      return 0;
  }

  /* Output:
  Don't be a fool!
  mesg = Don't be a fool!; &mesg = 0x7ffd05321738; value = 0x55c95505f008
  copy = Don't be a fool!; &copy = 0x7ffd05321740; value = 0x55c95505f008
  */
  ```

  通过最后的`printf()`的输出可以看出：
  1. `%s`以字符串形式输出没有问题。
  2. 指针`mesg`和`copy`分别储存在地址为`0x7ffd05321738`和`0x7ffd05321740`的内存中。
  3. 最后一项显示指针的值。指针的值就是指针存储的地址，这里`mesg`和`copy`的值都是`0x55c95505f008`，说明指向同一个位置。因此，程序并为拷贝字符串。语句`copy = mesg;`把`mesg`的值赋给`copy`，即让`copy`也指向`mesg`指向的字符串。

  这样做的好处是拷贝地址的效率高于拷贝整个数组。

### Section2 字符串输入

- 如果需要将字符串读入程序，必须预留储存该字符串的空间，因此要做的第一件事是分配空间，以储存稍后读入的字符串。类似如下的代码：

  ```C
  char *name;
  scanf("%s", name);
  ```

  因为`scanf()`要把信息拷贝至参数指定的地址上，而`name`是一个未初始化的指针，可能指向任何地方。因此在读入`name`时，`name`可能会擦写掉程序中的数据和代码，从而导致程序异常终止。

  因此最简单的方式是在声明时显式指明数组的大小，如`char name[81]`。另一种方式是使用C库函数分配内存。

- 在读取字符串时，`scanf()`和转换说明`%s`只能读取一个单词。在历史上，`gets()`函数用于读取一整行输入，直到遇到换行符，然后丢弃换行符，储存其余字符，并在字符末尾添加一个空字符使其成为一个C字符串。

  但是在更加现代的编译器中，使用`gets()`函数会出现警告，原因在于`gets()`的唯一参数是数组，无法检查数组是否装得下输入行。因为数组名会被转换成数组首元素的地址，因此`gets()`函数只知道数组的开始，而不知道数组的结尾。如果输入的字符串过长，就会导致缓冲区溢出(buffer overflow)，即多余的字符超出了指定的目标空间。如果这些多余的字符只是占用了尚未使用的内存，不会立即出现问题，如果擦写掉程序中其他的数据，则会导致程序异常终止。例如常见的报错`Segmentation fault`表明程序试图访问未分配的内存。

  C11标准废除了`gets()`函数。

- 过去使用`fgets()`代替`gets()`，C11标准新增了`gets_s()`函数也可以代替`gets()`，但是因为是`stdio.h`中的可选扩展，因此不是所有支持C11标准的编译器都支持`gets_s()`函数。
- `fgets()`函数的第二个参数指明了读入字符的最大数量，如果参数是`n`，则读入`n-1`个字符，或读到遇到的第一个换行符为止。**读入`n-1`个字符后，会在结尾添加一个空字符**，随后存入数组中。
- `fgets()`读到的换行符会储存在字符中，而不是像`gets()`丢弃换行符。
- `fgets()`函数的第三个参数指明了要读入的文件。如果读入从键盘输入的数据，则以`stdin`（标准输入）作为参数。该标识符定义在`stdio.h`中。
- 因为`fgets()`把换行符放在字符串末尾，因为通常与`fputs()`函数配对使用。`fputs()`函数的第二个参数指明要写入的文件，如果显示在显示器上，则使用`stdout`（标准输出）作为参数。`puts()`函数会在待输出字符串末尾添加一个换行符，而`fputs()`不会这么做。
- `fputs()`函数返回指向`char`的指针。如果一切顺利，函数返回的地址与传入的第一个参数相同。如果函数读到文件结尾，会返回一个特殊的指针：空指针(null pointer)。空指针保证不会指向有效的数据，所以可用于标识这种情况。
- 在书中给出的一个例子中：

  ```C
  #include <stdio.h>
  #define STLEN 10

  int main(void)
  {
      char words[STLEN];

      puts("Enter strings (empty line to quit):");
      while (fgets(words, STLEN, stdin) != NULL && words[0] != '\n')
      {
          fputs(words, stdout);
      }
      puts("Done.");

      return 0;
  }

  /* Output:
  Enter strings (empty line to quit):
  By the way, the gets() function
  By the way, the gets() function
  also retuns a null pointer if it
  also retuns a null pointer if it
  encounters end-of-file.
  encounters end-of-file.

  Done.
  */
  ```

  可以看到尽管`STLEN`被设置为10，但是程序在执行时没有受到过长输入的影响。原因是`fgets()`会读入`STLEN - 1`个字符（程序中为10-1=9个字符），所以一开始只读取了`"By the wa"`，并储存为`"By the wa\0"`，接着由`fputs()`函数打印该字符串，但是因为`fputs()`不会在结尾处增加换行符，因此没有换行，随`while`进入下一轮迭代，`fgets()`从输入中继续读取数据，直至一行的结束。

- 空字符`\0`是用于标记C字符串末尾的字符。空指针`NULL`有一个值，这个值不会与任何数据的有效地址对应。通常，函数使用它返回一个有效地址表示某些特殊情况发生，例如遇到文件末尾或未能按预期执行。空字符是整数类型，占1个字节，而空指针是指针类型，通常占4个字节。
- C11新增的`gets_s()`函数和`fgets()`类似，用一个参数限制读入的字符数。`gets_s()`与`fgets()`的区别为：

  1. `gets_s()`只从标准输入中读取数据，所以不需要第三个参数。
  2. `gets_s()`读到换行符会丢弃。
  3. 如果`gets_s()`读到最大字符数都没有读到换行符，则首先把目标数组中的首字符设置为空字符，读取并丢弃随后的输入直至读到换行符或文件结尾，然后返回空指针。接着调用依赖实现的处理函数，可能会中止或退出程序。

- 当输入与预期不符时，`gets_s()`没有`fgets()`方便灵活。因此`fgets()`通常是处理类似情况的最佳选择。
- `scanf()`和`%s`转换说明读取字符串，而`scanf()`和`gets()`或`fgets()`的区别在于如何确定字符串的末尾：`scanf()`更像是获取单词的函数。`scanf()`的典型用法是读取并转换混合数据类型为某种标准形式。
- 在`scanf()`中，`%s`转换说明使用字段宽度可以防止溢出。

### Section3 字符串输出

- 使用`puts()`只需要将字符串的地址作为参数传递即可。这个地址标识`puts()`从哪里开始输出。`puts()`在遇到空字符时会停止输出，因此必须确保有空字符，否则`puts()`会一直打印内存中的内容，直到遇到空字符为止。因此：类似`char dont[] = {'W', 'O', 'W', '!'};`不能直接使用，因为`dont`没有空字符结尾，所以不是一个字符串，
- 如果混合使用`fgets()`输入和`puts()`输出，会导致每个待显示的字符串后有两个换行符。因此需要注意`puts()`和`gets()`配对使用，`fputs()`与`fgets()`配对使用。

### Section4 自定义输入/输出函数

- 可以基于`getchar()`和`putchar()`自定义输入输出函数。例如书中给出的不自动添加换行符的`puts()`函数：

  ```C
  #include <stdio.h>
  void put1(char const *string)  // 不会改变字符串
  {
      while (*string != '\0')  // 使用while(*string)更加简洁
      {
          putchar(*string++);  // ++的优先级高于*，因此打印string指向的值，递增string本身
      }
  }
  ```

  其中形参使用的是`char const *string`，因为处理字符串，实参可以是数组名，用字符串字面量，或声明为`char *`类型的变量。用`char const *string`可以提醒用户实参不一定是数组。

### Section5 字符串函数

- ANSI C将处理字符串的函数原型放在`string.h`头文件中。
- `strlen()`函数：统计字符串的长度。书中给出一个缩短字符串的示例：

  ```C
  #include <stdio.h>
  #include <string.h>
  void fit(char *, unsigned int);

  int main(void)
  {
      char mesg [] = "Things should be as simple as possible," " but not simpler.";

      puts(mesg);
      fit(mesg, 38);
      puts(mesg);
      puts("Let's look at some more of the string.");
      puts(mesg + 39);

      return 0;
  }

  void fit(char *string, unsigned int size)
  {
      if (strlen(string) > size)
      {
          string[size] = '\0';
      }
  }

  /* Output:
  Things should be as simple as possible, but not simpler.
  Things should be as simple as possible
  Let's look at some more of the string.
   but not simpler.
  */
  ```

  可以只修改`string[size]`为空字符的原因是`puts()`只会读到空字符为止。剩余的部分留存在缓冲区中，在下一次使用`puts()`时继续输出直到原字符串最后的空字符。

- `strcat()`函数：拼接字符串，接收两个字符串作为参数，把第二个字符串的备份附加在第一个字符串的末尾，并把拼接后形成的新字符串作为第一个字符串，第二个字符串保持不变。`strcat()`函数返回第一个参数，即拼接第二个字符串后的第一个字符串的地址。
- `strncat()`函数：`strcat()`函数无法检查第一个数组是否能容纳第二个字符串。如果分配给第一个数组的空间不够，则多出的字符溢出同样会带来问题。使用`strncat()`函数，在第三个参数指定了最大添加字符数。
- `strcmp()`函数：无法直接比较两个字符串，因为这相当于比较两个指针。由于两个字符串会储存在不同的地址，因为比较指针的结果永远为假。因此比较字符串内容需要使用`strcmp()`函数，如果字符串相同则返回`0`，如果不相同，根据ASCII标准，在字母表中，如果第一个字符串在第二个字符串前，则返回负数，如果第一个字符串在第二个字符串后面，则返回正数。不同编译器可能会返回`1/-1`或字符ASCII码之差。由于`strcmp()`函数比较的是字符串不是字符，因此参数应该是字符串如`"apples"`或`"A"`，而不是字符如`'A'`。由于`char`类型实际上是整数类型，因此可以用关系运算符进行比较如`ch == 'q'`。
- `strncmp()`函数：`strcmp()`函数会一直比较到字符串的结尾，使用`strncmp()`函数可以只比较第三个参数指定的字符数。
- `strcpy()`和`strncpy()`函数
- `sprintf()`函数

### Section6 字符串示例：字符串排序

### Section7 `ctype.h`字符函数和字符串

### Section8 命令行参数

### Section9 把字符串转换为数字

## Chapter12 存储类别、链接和内存管理

## Chapter13 文件输入/输出

## Chapter14 结构和其他数据形式

## Chapter15 位操作

## Chapter16 C预处理器和C库

## Chapter17 高级数据表示
