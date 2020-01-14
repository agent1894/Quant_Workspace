# C++ Primer Plus 6th Edition by Stephen Prata (Pearson)

- [C++ Primer Plus 6th Edition by Stephen Prata (Pearson)](#c-primer-plus-6th-edition-by-stephen-prata-pearson)
  - [Chapter2 开始学习C++](#chapter2-%e5%bc%80%e5%a7%8b%e5%ad%a6%e4%b9%a0c)
    - [Section 4 函数](#section-4-%e5%87%bd%e6%95%b0)
  - [Chapter3 处理数据](#chapter3-%e5%a4%84%e7%90%86%e6%95%b0%e6%8d%ae)
    - [Section1 简单变量](#section1-%e7%ae%80%e5%8d%95%e5%8f%98%e9%87%8f)
    - [Section2 `const`限定符](#section2-const%e9%99%90%e5%ae%9a%e7%ac%a6)
    - [Section3 浮点数](#section3-%e6%b5%ae%e7%82%b9%e6%95%b0)
    - [Section4 C++算术运算符](#section4-c%e7%ae%97%e6%9c%af%e8%bf%90%e7%ae%97%e7%ac%a6)
  - [Chapter4 复合类型](#chapter4-%e5%a4%8d%e5%90%88%e7%b1%bb%e5%9e%8b)
    - [Section1 数组](#section1-%e6%95%b0%e7%bb%84)
    - [Section2 字符串](#section2-%e5%ad%97%e7%ac%a6%e4%b8%b2)
    - [Section3 `string`类简介](#section3-string%e7%b1%bb%e7%ae%80%e4%bb%8b)
    - [Section4 结构简介](#section4-%e7%bb%93%e6%9e%84%e7%ae%80%e4%bb%8b)
    - [Section5 共用体](#section5-%e5%85%b1%e7%94%a8%e4%bd%93)
    - [Section6 枚举](#section6-%e6%9e%9a%e4%b8%be)
    - [Section7 指针和自由存储空间](#section7-%e6%8c%87%e9%92%88%e5%92%8c%e8%87%aa%e7%94%b1%e5%ad%98%e5%82%a8%e7%a9%ba%e9%97%b4)
    - [Section8 指针、数组和指针算数](#section8-%e6%8c%87%e9%92%88%e6%95%b0%e7%bb%84%e5%92%8c%e6%8c%87%e9%92%88%e7%ae%97%e6%95%b0)
    - [Section10 数组的替代品](#section10-%e6%95%b0%e7%bb%84%e7%9a%84%e6%9b%bf%e4%bb%a3%e5%93%81)
  - [Chapter5 循环和关系表达式](#chapter5-%e5%be%aa%e7%8e%af%e5%92%8c%e5%85%b3%e7%b3%bb%e8%a1%a8%e8%be%be%e5%bc%8f)
    - [Section1 `for`循环](#section1-for%e5%be%aa%e7%8e%af)
    - [Section2 `while`循环](#section2-while%e5%be%aa%e7%8e%af)
    - [Section3 `do while`循环](#section3-do-while%e5%be%aa%e7%8e%af)
    - [Section4 基于范围的`for`循环（C++11）](#section4-%e5%9f%ba%e4%ba%8e%e8%8c%83%e5%9b%b4%e7%9a%84for%e5%be%aa%e7%8e%afc11)
    - [Section5 循环和文本输入](#section5-%e5%be%aa%e7%8e%af%e5%92%8c%e6%96%87%e6%9c%ac%e8%be%93%e5%85%a5)
    - [Section6 嵌套循环和二维数组](#section6-%e5%b5%8c%e5%a5%97%e5%be%aa%e7%8e%af%e5%92%8c%e4%ba%8c%e7%bb%b4%e6%95%b0%e7%bb%84)
  - [Chapter6 分支语句和逻辑运算符](#chapter6-%e5%88%86%e6%94%af%e8%af%ad%e5%8f%a5%e5%92%8c%e9%80%bb%e8%be%91%e8%bf%90%e7%ae%97%e7%ac%a6)
    - [Section1 `if`语句](#section1-if%e8%af%ad%e5%8f%a5)
    - [Section2 逻辑表达式](#section2-%e9%80%bb%e8%be%91%e8%a1%a8%e8%be%be%e5%bc%8f)
    - [Section3 字符函数库`cctype`](#section3-%e5%ad%97%e7%ac%a6%e5%87%bd%e6%95%b0%e5%ba%93cctype)
    - [Section4 `?:`运算符](#section4-%e8%bf%90%e7%ae%97%e7%ac%a6)
    - [Section5 `switch`语句](#section5-switch%e8%af%ad%e5%8f%a5)
    - [Section6 `break`和`continue`语句](#section6-break%e5%92%8ccontinue%e8%af%ad%e5%8f%a5)
    - [Seciton7 读取数字的循环](#seciton7-%e8%af%bb%e5%8f%96%e6%95%b0%e5%ad%97%e7%9a%84%e5%be%aa%e7%8e%af)
    - [Section8 简单文件输入/输出](#section8-%e7%ae%80%e5%8d%95%e6%96%87%e4%bb%b6%e8%be%93%e5%85%a5%e8%be%93%e5%87%ba)
  - [Chapter7 函数——C++的编程模块](#chapter7-%e5%87%bd%e6%95%b0c%e7%9a%84%e7%bc%96%e7%a8%8b%e6%a8%a1%e5%9d%97)
    - [Section1 复习函数的基本知识](#section1-%e5%a4%8d%e4%b9%a0%e5%87%bd%e6%95%b0%e7%9a%84%e5%9f%ba%e6%9c%ac%e7%9f%a5%e8%af%86)
    - [Section2 函数参数和按值传递](#section2-%e5%87%bd%e6%95%b0%e5%8f%82%e6%95%b0%e5%92%8c%e6%8c%89%e5%80%bc%e4%bc%a0%e9%80%92)
    - [Section3 函数和数组](#section3-%e5%87%bd%e6%95%b0%e5%92%8c%e6%95%b0%e7%bb%84)
    - [Section4 函数和二维数组](#section4-%e5%87%bd%e6%95%b0%e5%92%8c%e4%ba%8c%e7%bb%b4%e6%95%b0%e7%bb%84)
    - [Section5 函数和C-风格字符串](#section5-%e5%87%bd%e6%95%b0%e5%92%8cc-%e9%a3%8e%e6%a0%bc%e5%ad%97%e7%ac%a6%e4%b8%b2)
    - [Section6 函数和结构](#section6-%e5%87%bd%e6%95%b0%e5%92%8c%e7%bb%93%e6%9e%84)
    - [Section9 递归](#section9-%e9%80%92%e5%bd%92)
    - [Section10 函数指针](#section10-%e5%87%bd%e6%95%b0%e6%8c%87%e9%92%88)
  - [Chapter8 函数探幽](#chapter8-%e5%87%bd%e6%95%b0%e6%8e%a2%e5%b9%bd)
    - [Section1 C++内联函数](#section1-c%e5%86%85%e8%81%94%e5%87%bd%e6%95%b0)
    - [Section2 引用变量](#section2-%e5%bc%95%e7%94%a8%e5%8f%98%e9%87%8f)
    - [Section3 默认参数](#section3-%e9%bb%98%e8%ae%a4%e5%8f%82%e6%95%b0)
    - [Section4 函数重载](#section4-%e5%87%bd%e6%95%b0%e9%87%8d%e8%bd%bd)
    - [Seciton5 函数模板](#seciton5-%e5%87%bd%e6%95%b0%e6%a8%a1%e6%9d%bf)
  - [Chapter9 内存模型和名称空间](#chapter9-%e5%86%85%e5%ad%98%e6%a8%a1%e5%9e%8b%e5%92%8c%e5%90%8d%e7%a7%b0%e7%a9%ba%e9%97%b4)
    - [Section1 单独编译](#section1-%e5%8d%95%e7%8b%ac%e7%bc%96%e8%af%91)
    - [Section2 存储持续性、作用域和链接性](#section2-%e5%ad%98%e5%82%a8%e6%8c%81%e7%bb%ad%e6%80%a7%e4%bd%9c%e7%94%a8%e5%9f%9f%e5%92%8c%e9%93%be%e6%8e%a5%e6%80%a7)
    - [Section3 名称空间](#section3-%e5%90%8d%e7%a7%b0%e7%a9%ba%e9%97%b4)
  - [Chapter10 对象和类](#chapter10-%e5%af%b9%e8%b1%a1%e5%92%8c%e7%b1%bb)
    - [Section1 过程性编程和面向对象编程](#section1-%e8%bf%87%e7%a8%8b%e6%80%a7%e7%bc%96%e7%a8%8b%e5%92%8c%e9%9d%a2%e5%90%91%e5%af%b9%e8%b1%a1%e7%bc%96%e7%a8%8b)
    - [Section2 抽象和类](#section2-%e6%8a%bd%e8%b1%a1%e5%92%8c%e7%b1%bb)
    - [Section3 类的构造函数和析构函数](#section3-%e7%b1%bb%e7%9a%84%e6%9e%84%e9%80%a0%e5%87%bd%e6%95%b0%e5%92%8c%e6%9e%90%e6%9e%84%e5%87%bd%e6%95%b0)
    - [Section4 `this`指针](#section4-this%e6%8c%87%e9%92%88)
    - [Section5 对象数组](#section5-%e5%af%b9%e8%b1%a1%e6%95%b0%e7%bb%84)
    - [Section6 类作用域](#section6-%e7%b1%bb%e4%bd%9c%e7%94%a8%e5%9f%9f)
    - [Section7 抽象数据类型](#section7-%e6%8a%bd%e8%b1%a1%e6%95%b0%e6%8d%ae%e7%b1%bb%e5%9e%8b)
  - [Chapter11 使用类](#chapter11-%e4%bd%bf%e7%94%a8%e7%b1%bb)
    - [Section1 运算符重载](#section1-%e8%bf%90%e7%ae%97%e7%ac%a6%e9%87%8d%e8%bd%bd)
    - [Section2 计算时间：一个运算符重载示例](#section2-%e8%ae%a1%e7%ae%97%e6%97%b6%e9%97%b4%e4%b8%80%e4%b8%aa%e8%bf%90%e7%ae%97%e7%ac%a6%e9%87%8d%e8%bd%bd%e7%a4%ba%e4%be%8b)

## Chapter2 开始学习C++

### Section 4 函数

- **C++程序中应当为程序中使用的每个函数提供原型 (Function Prototype)。**
  - 由于在使用函数前，C++编译器必须知道函数的参数类型和返回值类型，因此需要使用函数原型语句显性地声明。函数原型之于函数相当于变量声明之于变量。
  - 应在首次使用函数之前提供其原型。通常的做法是把原型放到`main()`函数定义的前面。
  - 如果没有函数原型放在`main()`函数前为编译器提供必要的信息，则必须将整个函数的定义语句放在`main()`函数前。实际上这两种方式各有利弊。如果将`main()`函数放在最后，则需要对整个C++程序中使用的函数组织正确的顺序。在一个程序中包含许多函数，同时这些函数又调用其他函数的情况下，使用函数原型无疑是更好的选择。（书中也是这样讲解的，完全没有提及第二种方法）

- `main()`函数中`return 0`的作用：
  - 计算机的操作系统可以看做调用程序，因此`main()`的返回值不是返回给程序中的其他部分，而是返回给操作系统。操作系统测试程序的返回值（通常被称为退出值），退出值为0则认为程序成功，非0则认为程序存在问题。

## Chapter3 处理数据

### Section1 简单变量

- 对类型名使用`sizeof`运算符时，应将名称放在括号中，但是对变量名使用`sizeof`运算符则括号可加可不加。
- `<climits>`中的符号常量，实际就是将如`INT_MIN`, `INT_MAX`用对应的数值替换，使用的是`#define`，便于C和C++同时使用。
- C++本身并不提供自动防止超出整型限制的功能，需要使用头文件`<climits>`。
- `unsigned`是无符号变体，可以增加变量能够储存的最大值，但是仅适用于非负数据。如`short`保存-32768到32767，但是`unsigned short`可以保存0-65535。
- C++中，**单引号用于字符，双引号用于字符串**。

### Section2 `const`限定符

- `const`定义常量时，常量名推荐使用全部大写，同时不要使用`#define`进行定义，因为`const`可以对常量作用域有更好的限制。

### Section3 浮点数

- **`float`只保证6位精度，超过6位会导致精度丢失，浮点常量在默认情况下为`double`类型。**

### Section4 C++算术运算符

- 5种基本的C++算术运算符：
  - `+` 加法运算。
  - `-` 减法运算。
  - `*` 乘法运算。
  - `/` 除法运算。如果分子分母均为整数，则结果为整数。
  - `%` 求模运算。分子分母必须为整型，如果运用于浮点数则会导致编译错误。
- C++会自动执行多种类型转换：
  - 初始化和赋值时进行的转换：

    在将一种类型的值赋给另一种类型时，值将被转换为接收变量的类型。在将值赋给取值范围更大的类型时通常不会带来问题（最多会导致效率问题），但是相反的情况下会带来一定的问题，如将`long`赋值给`float`会降低精度，将浮点数赋值给整型会丢失小数部分。

  - C++11中，以`{}`方式进行初始化：

    使用`{}`进行的初始化称为列表初始化(list-initialization)，这种方式对类型转换的要求更为严格，即缩窄(narrowing)操作是不被允许的。

  - 表达式中的转换：
    - 自动转换：即类型出现时便进行转换。
  
      在计算表达式时，C++将`bool`, `char`, `unsigned char`, `signed char`和`short`转换为`int`。这些转换被称为整型提升(integral promotion)

    - 不同类型同时出现在表达式中时进行转换：

      1. 如果有一个操作数的类型是`long double`，则将另一个操作数转换为`long double`。
      2. 否则，如果有一个操作数的类型是`double`，则将另一个操作数转换为`double`。
      3. 否则，如果有一个操作数的类型是`float`，则将另一个操作数转换为`float`。
      4. 否则，说明操作数都是整型，执行整形提升。
      5. 如果操作数都是`signed`或者都是`unsigned`，将低级别提升为高级别类型。
      6. 如果操作数一个是`signed`一个是`unsigned`，且`unsigned`操作数级别高于`signed`操作数，则将有符号操作数转换为无符号操作数所属的类型。
      7. 否则，如果有符号类型可表示无符号类型的所有可能值，则将无符号操作数转换为有符号操作数所属的类型。
      8. 否则，均转换为有符号类型的无符号版本。

    - 强制类型转换：

      ```C++
      (typeName) value // converts value to typeName type, C style
      typename (value) // converts value to typeName type, C++ style
      ```

      此外，C++还引入4个强制类型转换运算符，这种方式的使用要求更为严格。语法为：

      ```C++
      static_cast<typeName> (value) // converts value to typeName type
      ```

## Chapter4 复合类型

### Section1 数组

- 只有在定义数组时才能使用`{}`数组初始化，此后就不能使用，用时也不能将一个数组赋值给另一个数组。

### Section2 字符串

- `cin`的基础特性中，会识别输入的第一个单词，随后在结尾处加入空白。因此，后续输入的内容会被放入输入队列中，这会直接影响下一次输入时的状态。
- 在Chapter2 Section3中遇到的`cin.get()`的问题，在此得到解决。即不定义`char array`时，`cin.get()`仅会读取一个字符，而使用`cin.get(name, ArSize)`时，编译器会读取一个字符串放入数组中。

### Section3 `string`类简介

- `<cstring>`头文件提供了标准C语言库的字符串函数，用来处理字符数组。而`<string>`头文件则定义了`string`类。

### Section4 结构简介

- *结构中的位字段（4.4.6）存疑*

### Section5 共用体

- 共用体 (union) 可以存储多个数据结构，但是在任一时刻只能存储一种数据结构。这种互斥的方式可以节省内存。
- 共用体衍生出匿名共用体 (anonymous union)，匿名共用体直接取消了名称，这样这个共用体的所有成员存放在内存的相同地址处，显然，每次只能有一个成员是共用体的成员。

### Section6 枚举

- 枚举提供了另一种创建符号常量的方式。例如：

  ```C++
  enum spectrum {red, orange, yellow, green, blue, violet, indigo, ultraviolet};
  ```

  这条语句使`spectrum`称为新类型的名称，`spectrum`被称为枚举(enumeration)；将`red, orange, yellow`等作为符号常量，对应整数值0-7，这些常量被称为枚举量(enumerator)。
- 默认情况下会将整数值赋给枚举量，也可以显式地指定整数值来覆盖默认值。
- 可以使用枚举名来声明这种类型的变量：

  ```C++
  spectrum band; // band is a variable of type spectrum
  ```

- 在不进行强制类型装换的情况下，只能将定义枚举时使用的枚举量赋给这种枚举的变量：

  ```C++
  band = blue; // valid, blue is an enumerator
  band = 2000; // invalid, 2000 is not an enumerator
  ```

  因此，`spectrum`变量受到限制，只有8个可能的值。
- 对于枚举，只定义了赋值运算符，没有为枚举定义算术运算：

  ```C++
  band = orange; // valid
  ++band; // not valid
  band = orange + red; // not valid, but a little tricky
  ```

- 枚举量是整型，可被提升为`int`类型，但`int`类型不能自动转换为枚举类型。

  ```C++
  int color = blue; // valid, spectrum type promoted to int
  band = 3; // invalid, int not converted to spectrum
  color = 3 + red; // valid, red converted to int
  ```

- 如果`int`值是有效的，则可以通过强制类型转换，将它赋给枚举变量；如果对一个不适当的值进行强制类型转换，则会出现不确定的结果。

  ```C++
  band = spectrum(3); // typecast 3 to type spectrum
  band = spectrum(40003); // undefined
  ```

- 可以使用赋值运算符显式的设置枚举量的值：

  ```C++
  enum bits{one = 1, two = 2, four = 4, eight = 8};
  ```

  指定的值必须是整数，也可以只显式的定义其中一些枚举量的值：

  ```C++
  enum bigstep{first, second = 100, third};
  ```

  在这里，`first`在默认情况下为0，没有被初始化的枚举量的值将比其前面的枚举量大1，因此`third`的值为101。

  也可以创建多个值相同的枚举量：

  ```C++
  enum {zero, null = 0, one, numero_uno = 1};
  ```

### Section7 指针和自由存储空间

- **指针是一个变量，指向的是其储存值的地址。**
- **一定要在对指针应用解除引用运算符`*`之前，将指针初始化为一个确定的，适当的地址。**
- 使用`delete`释放内存，但是不会删除指针本身。**一定要配对使用`new`和`delete`，否则将会发生内存泄漏**，也就是说被分配的内存再也无法使用。如果内存泄漏严重，则程序将由于不断寻找更多内存而终止。
- 不要对`delete`过的内存再次`delete`，这样会导致不确定的后果。同时，不能用`delete`释放声明变量时获得的内存。

  ```C++
  int * ps = new int; // ok
  delete ps; // ok
  delete ps; // not ok for now
  int jugs = 5; // ok
  int * pi = &jugs; // ok
  delete pi; // not allowed, memory not allocated by new
  ```

- 如果通过声明来创建数组，则程序被编译时会为数组分配内存。无论程序最终是否使用数组，都会占用已声明的内存。在编译时给数组分配内存被成为静态联编(static binding)。但使用`new`时，如果在运行阶段需要数组，则创建它，如果不需要，则不创建。还可在程序运行时选择数组的长度。这种方法为成为动态联编(dynamic binding)。
- 使用`new`和`delete`时，应遵循以下规则：
  1. 不要使用`delete`来释放不是`new`分配的内存
  2. 不要使用`delete`释放同一个内存两次
  3. 如果使用`new[]`为数组分配内存，则应使用`delete[]`来释放
  4. 如果使用`new`为实体分配内存，则应使用`delete`来释放
  5. 对空指针使用`delete`是安全的
- 数组名和指针间的根本差别在于：数组名的值是不能修改的，但是指针是一个变量，因此可以修改指针的值。

  ```C++
  p3 = p3 + 1; // okay for pointers, wrong for array names
  ```

### Section8 指针、数组和指针算数

- 指针小结
  1. 声明指针

      ```C++
      typeName * pointerName;
      typeName * pointerName;
      typeName * pointerName;
      typeName * pointerName;
      typeName * pointerName;
      typeName * pointerName;
      typeName * pointerName;
      // for example:
      double * pn; // pn can point to a double value
      char * pc; // pc can point to a char value
      ```

  2. 给指针赋值应将内存地址赋给指针，可以对变量名应用`&`运算符，来获得被命名的内存的地址，`new`运算符返回未命名的内存地址

      ```C++
      double * pn; // pn can point to a double value
      double * pa; // pa can point to a double value
      char * pc; // pc can point to a char value
      double bubble = 3.2;
      pn = &bubble; // assign address of bubble to pn
      pc = new char; // assign address of newly allocated char memory to pc
      pa = new double[30]; // assign address of 1st element of array of 30 double to pa
      ```

  3. 对指针解除引用意味着获得指针指向的值。对指针应用解除引用或间接值运算符`*`来解除引用。因此，如果像上面的例子一样，`pn`是指向bubble的指针，则`*pn`是指向的值。

      ```C++
      cout << *pn; // print the value of bubble
      *pc = 'S'; // place 's' into the memory location whose address is pc
      ```

  4. 区分指针和指针所指向的值。如果`pt`是指向`int`的指针，则`*pt`不是指向`int`的指针，而是完全等同于一个`int`类型的变量。`pt`才是指针。

      ```C++
      int * pt = new int; // asssigns an address to the pointer pt
      *pt = 5; // store the value 5 at that address
      ```

  5. 多数情况下，C++将数组名视为数组的第一个元素的地址。一种例外的情况是，将`sizeof`运算符用于数组名时，此时将返回整个数组的长度（单位为字节）。

      ```C++
      int tacos[10]; // now tacos is the same as &tacos[0]
      ```

  6. 指针算数。C++允许将指针和整数相加，加1的结果等于原来的地址值加上指向的对象占用的总字节数。还可以将一个指针减去另一个指针，获得两个指针的差。后一种运算将得到一个整数，仅当两个指针指向同一个数组（也可以指向超出结尾的一个位置）时，这种运算才有意义：这将得到两个元素的间隔。

      ```C++
      int tacos[10] = {5, 2, 8, 4, 1, 2, 2, 3, 6, 8};
      int * pt = tacos; // suppose pt and tacos are the address 3000
      pt = pt + 1; // now pt is 3004 if a int is 4 bytes
      int *pe = &tacos[9]; // pe is 3036 if an int is 4 bytes
      pe = pe - 1; // now pe is 3032, the address of tacos[8]
      int diff = pe - pt; // diff is 7, the separation betweent tacos[8] and tacos[1]
      ```

  7. 数组的动态联编和静态联编。使用数组声明来创建数组时，将采用静态联编，即数组的长度在编译时设置；使用`new[]`运算符创建数组时，将采用动态联编（动态数组），即将在运行时为数组分配空间，其长度也将在运行时设置。使用完这种数组后，应使用`delete[]`释放其内存。

      ```C++
      int tacos[10]; // static binding, size fixed at compile time
      int size;
      cin >> size;
      cin >> size;
      cin >> size;
      cin >> size;
      cin >> size;
      cin >> size;
      cin >> size;
      int * pz = new int [size]; // dynamic binding, size set at run time

      ...

      delete [] pz; // free memory when finished
      ```

  8. 数组表示法和指针表示法。使用方括号数组表示法等同于对指针的解除引用。数组名和指针变量都是如此，因此对于指针和数组名，既可以使用指针表示法，也可以使用数组表示法。

      ```C++
      // tacos[0] means *tacos means the value at address tacos
      // tacos[3] means *(tacos + 3) means the value at address tacos + 3
      int * pt = new int [10]; // pt points to block of 10 ints
      *pt = 5; // set element number 0 to 5
      pt[0] = 6; // reset element number 0 to 6
      pt[9] = 44; // set tenth element (element number 9) to 44
      int coats[10];
      *(coats + 4) = 12; // set coats[4] to 12
      ```

- *指针与字符串（未完全理解）*：
  1. 在将字符串读入程序时，应使用已分配的内存地址。该地址可以是数组名，也可以是使用`new`初始化过的指针。
  2. **应使用`strcpy()`或`strncpy()`，而不是使用赋值运算符来将字符串赋给数组。**
- 在运行时创建数组优于在编译时创建数组，对于结构也是如此
- **当创建动态结构时，不能将成员运算符句点用于结构名，因为这个结构没有名称，只知道对应的地址。如果结构标识符是结构名，则使用句点运算符，如果标识符是指向结构的指针，则使用箭头成员运算符`->`**。如果`ps`是一个指针，指向一个结构`struct`，那么`ps->member`即为指向`struct`的member成员。

### Section10 数组的替代品

- vector

  ```C++
  #include <vector>

  ...

  using namespace std; // create a zero-size array of int
  int n;
  cin >> n;
  vector<double> vd(n); // create an array of n doubles
  // vector<typeName> vt(n_elem);
  ```

- array

  ```C++
  #include<array>

  ...

  using namespace std;
  array<int, 5> ai; // create array object of 5 ints
  array<double ,4> ad = {1.2, 2.1, 3.43, 4.3};
  // array<typeName, n_elem> arr;
  ```

## Chapter5 循环和关系表达式

### Section1 `for`循环

- for循环的组成：循环只进行一次初始化；test-expression（测试表达式）决定循环体是否被执行，通常，这个表达式是关系表达式，即对两个值进行比较；**update-expression（更新表达式）在每轮循环结束时执行，此时循环体已经执行完毕**。通常，它用来对跟踪循环轮次的变量的值进行增减。

  ```C++
  for (initialization; test-expression; update-expression)
    body
  ```

- C++常用的方式是，在for和括号之间加上一个空格，而省略函数名与括号之间的空格。
- `cout`在显示`bool`值之前将其转换为`int`，但`cout.setf(ios::boolalpha)`函数调用设置了一个标记，该标记命令`cout`显示`true`和`false`，而不是1和0。
- `++x`和`x++`并不相同。`x++`意味着使用x的当前值计算表达式，然后将x的值加一；而`++x`的意思是先将x的值加一，然后使用新的值计算表达式。

  ```C++
  int x = 5;
  int y = ++x; // change x, then assign to y, y is 6, x is 6

  int z = 5;
  int y = z++; // assign to y, then change z, y is 5, z is 6
  ```

- 副作用(side effect)和顺序点(sequence point)
  1. 副作用是指在计算表达式时对某些东西（如存储在变量中的值）进行了修改
  2. 顺序点是指程序执行过程中的一个点，在这里，进入下一步之前将确保对所有的副作用都进行了评估。在C++中，语句中的分号就是一个顺序点，这意味着程序处理下一条语句之前，赋值运算符、递增运算符和递减运算符执行的所有修改都必须完成。
  3. 显然如果变量被用于某些目的，如用作函数参数或给变量赋值，使用前缀格式`++x`和后缀格式`x++`的结果将不同。然而，如果递增表达式的值没有被使用，情况则有所不同。在如下例子中，尽管在逻辑上，使用前缀格式和后缀格式没有任何区别，表达式的值没有使用，因此只存在副作用，而将x加一和n减一的副作用将在程序进入下一步之前完成，前缀格式和后缀格式的最终效果相同。然而，尽管使用前缀格式和后缀格式对程序的行为没有影响，但是执行速度上会有细微的差别。对于一个类来说，前缀函数将值加一然后返回，而后缀函数首先复制一个副本，将其加一，然后将复制的副本返回。因此，对于类而言，前缀版本的效率比后缀版本高。

      ```C++
      x++;
      // 和
      ++x;

      for (n = lim; n > 0; --n)

      ...;

      // 和
      for (n = lim; n > 0; n--)

      ...;
      ```

- 运算符的优先级相同时，以从右到左的方式进行结合。**后缀运算符的优先级高于前缀运算符**。
- `{}`语句块允许把两条或更多条语句放到按C++句法只能放一条语句的地方，逗号运算符对表达式完成同样的任务，允许将两个表达式放到C++句法只允许放一个表达式的地方。同时，C++为逗号运算符提供了额外的两个特性：首先确保先计算第一个表达式，然后计算第二个表达式，（换句话说，逗号运算符式一个是顺序点）。因此，形如以下的代码是安全的。其次，逗号表达式的值是第二部分的值。

  ```C++
  i = 20, j = 2 * i // i set to 20, then j set to 40, the expression is 40
  ```

- 比较C-字符串，应当使用C-风格字符串库中的`strcmp()`函数来比较。该函数接受两个字符串地址作为参数，这意味着参数可以是指针、字符串常量或字符串数组名。如果两个字符串相同，该函数将返回零；如果第一个字符串按字母顺序排在第二个字符串之前，则`strcmp()`将返回一个负数值；如果第一个字符串按字母顺序排在第二个字符串之后，则`strcmp()`将返回一个正数值。注意此处字符是根据字符的系统编码进行比较的。如果使用ASCII码时，所有大写字母的编码都比小写字母小，所以大写字母将位于小写字母之前，同时这也意味着大小写是敏感的。

### Section2 `while`循环

- `while`循环是没有初始化和更新部分的`for`循环，它只有测试条件和循环体。

  ```C++
  while (test-condition)
    body
  ```

- 标点符号的使用要特别注意。分号结束一个语句，而`for`或`while`为一个完整的语句，下面提供了一个错误的示例。由于错误的使用了分号，会导致花括号内的代码位于循环后，永远不会被执行，构成了一个死循环。

  ```C++
  i = 0;
  while (name[i] != '\0'); // problem semicolon
  {
    cout << name[i] << endl;
    i++;
  }
  cout << "Done" << endl;
  ```

- 延迟循环：使用头文件`<ctime>`实现，其中定义了符号常量`CLOCKS_PER_SEC`，该常量等于每秒钟包含的系统时间单位数。因此，将系统时间（函数`clock()`）除以这个值，可以得到秒数，或将秒数乘以这个值，可以得到以系统时间单位为单位的时间。同时`<ctime>`将`clock_t`作为`clock()`返回类型的别名，因此可以将变量声明为`clock_t`类型，从而避免不同的系统或编译器对`clock()`函数返回值的类型的差异。
- 类型别名：C++为类型建立别名的方式有两种，一种是使用预处理器`#define`，这种方式书中并不推荐，包括在定义`const`常量时。另一种则是使用C++（和C）的关键字`typedef`来创建别名。`typedef`不会创建新类型，而只是为已有的类型建立一个新名称。`typedef`的通用格式为：

  ```C++
  typedef typeName aliasName;
  ```

### Section3 `do while`循环

- `do while`循环不同于`for`循环和`while`循环，`do while`时出口条件(exit condition)循环，即这种循环将**首先执行循环体，在判定测试表达式，因此这样的循环通常至少执行一次**。其语法结构为：

  ```C++
  do
    body
  while (test_expression);
  ```

### Section4 基于范围的`for`循环（C++11）

- 基于范围(range-based)的`for`循环是C++11新增的新特性，使对数组的每个元素执行相同操作的循环成为可能。
- 会在模板容器类中做详细讨论

### Section5 循环和文本输入

- `cin`在读取`char`值时，会忽略空格和换行符，因此显示时不会显示空格，也不会对空格进行计数。
- 为了修正上述问题，会使用`cin.get(char)`函数，成员函数`cin.get(char)`读取输入中的下一个字符（即使是空格），并将其赋值给变量。
- **函数重载是C++的特性，允许创建多个同名函数，条件是参数列表不同**。在书中的案例中，`cin.get(name, ArSize)`会使编译器找到使用`char*`和`int`作为参数的`cin.get()`的版本；如果使用`cin.get(ch)`，则编译器将使用接受一个`char`参数的版本；如果没有提供参数，则编译器将使用不接受任何参数的`cin.get()`的版本。
- 检测文件尾(EOF)作为一种功能更加强大的技术，可以更好的协同输入和操作系统。
  1. 操作系统支持重定向，因此程序可以从文件而非键盘获取输入，常用的重定向符为`<`
  2. 操作系统同样支持通过键盘模拟文件尾。在Unix中为\<CTRL\>+\<D\>，在Windows和Linux中通常是\<CTRL\>+\<Z\>+\<ENTER\>

  如果变成环境支持EOF，则可以使用键盘输入模拟EOF。如果检测到EOF，`cin.eof()`或`cin.fail()`会返回`bool`值`true`，否则返回`false`。（`cin.fail()`比`cin.eof()`可用于更多的实现中。）

### Section6 嵌套循环和二维数组

- C++没有提供二维数组类型。

## Chapter6 分支语句和逻辑运算符

### Section1 `if`语句

- 从语法上看，整个if else结构被视为一条语句。
- if else if else结构，看似是一种新的结构，实际上是由于C++的自由格式允许将这些元素排列成便于阅读的格式。它只是一个if else被包含在另一个if else中。

### Section2 逻辑表达式

- 逻辑运算符：
  1. `OR: ||`
  2. `AND: &&`
  3. `NOT: !`
- C++规定，`||`和`&&`运算符是个顺序点(sequence point)，也就是说，先修改左侧的值，再对右侧的值进行判定（C++11的说法是，运算符左边的子表达式先于右边的子表达式）。举例如下：

  ```C++
  i++ < 6||i == j
  ```

  假设原来的值为10，则在对i和j进行比较时，i的值将为11。
- 取值范围测试的每一部分都使用`AND`运算符将两个完整的关系表达式组合起来，**不要使用数学符号**。

  ```C++
  if (age > 17 && age < 35) // OK
  if (17 < age < 35) // Don't do this!
  ```

  **编译器不会捕获这种错误，因为这是有效的C++语法。**`<`运算符从左向右结合，因此上述表达式的含义为：

  ```C++
  if ( (17 < age) < 35)
  ```

  **但`17 < age`的值要么为`true(1)`，要么为`false(0)`。不管是哪种情况，表达式`17 < age`的值都小于35，因此整个测试的结果总是true!**
- C++逻辑`OR(||)`和逻辑`AND(&&)`运算符的优先级都低于关系运算符，但是`NOT(!)`运算符的优先级高于所有的关系运算符和算术运算符，但是**逻辑`AND`运算符的优先级高于逻辑`OR`运算符**。
- C++可以使用`and or not`替代`&& || !`。

### Section3 字符函数库`cctype`

- `<cctype>`类库提供了对分析字符串更好的方式。

### Section4 `?:`运算符

- `?:`运算符类似于Python中的三元表达式。

### Section5 `switch`语句

- `switch`语句的通用格式：

  ```C++
  switch (integer-expression)
  {
    case label1 : statement(s)
    case label2 : statement(s)

    ...

    default : statement(s)
  }
  ```

- **integer expression 必须是一个结果为整数值的表达式，每个标签都必须是整数常量表达式。最常见的标签是`int`或`char`常量，也可以是枚举量。**
- **C++中的`case`标签只是行标签，而不是选项之间的界线。当程序跳到switch中特定代码行后，将依次执行之后的所有语句，除非有明确的其他知识。程序不会在执行到下一个`case`处自动停止，要让程序执行完以组特定语句后停止，必须使用`break`语句。**
- `switch`中的每一个`case`标签都必须是一个单独的值，且必须是整数（包括`char`），因此`switch`无法处理浮点测试。
- 如果所有的选项都可以用整数常量来标识，则可以使用`switch`语句或`if else`语句。如果既可以使用`if else if`语句，也可以使用`switch`语句，则当选项不少于3个时，应使用`switch`语句（代码长度和执行速度上，`switch`语句效率更高）。

### Section6 `break`和`continue`语句

- `continue`跳过循环体剩余的部分，开始新一轮循环。
- `break`跳过循环的剩余部分，到达下一条语句。
- `continue`语句会跳过循环体的剩余部分，但不会跳过循环的更新表达式。

### Seciton7 读取数字的循环

- 输入错误和EOF都会导致`cin`返回`false`，这给使用非数字输入结束读取数字循环提供了方法。
- 需要使用`cin.clear()`对输入进行重置。

### Section8 简单文件输入/输出

- 文件输出和控制台输出非常类似：
  - 控制台输出(`cout`)：
    - 必须包含头文件`<iostream>`
    - 头文件`<iostream>`定义了一个用于处理输出的`ostream`类
    - 头文件`<iostream>`声明了一个名为`cout`的`ostream`变量（对象）
    - 使用命名空间`std::`
  - 文件输出：
    - 必须包含头文件`<fstream>`
    - 头文件`<fstream>`定义了一个用于处理输出的`ofstream`类
    - 需要声明一个或多个`ofstream`变量（对象）
    - 使用命名空间`std::`
    - 需要将`ofstream`对象与文件关联，方法之一是使用`open()`方法
    - 使用完文件后应使用方法`close()`将其关闭
  - 需要注意的是，`iostream`提供了预先定义好名为`cout`的`ostream`对象，但是在文件输出时，必须自己声明`ofstream`对象。
  - **打开已有的文件以接受输出时，默认将原文件清空。**
- 文件输入和控制台输入的关系与文件输出和控制台输出的关系非常类似。
  - `<cstdlib>`头文件定义了一个用于同操作系统通信的参数值`EXIT_FAILURE`。
  - 由于方法`good()`指出读取输入的操作是否成功，因此，应该在执行读取输入的操作后立刻使用`good()`进行测试。在`sumafile.cpp`中，使用的方法是先放置一条输入语句，然后在循环的末尾在放置另一条输入语句，即：

    ```C++
    // standard file-reading loop design
    inFile >> value; // get first value
    while (inFile.good()) // while input good and not at EOF
    {
        // loop body goes here
        inFile >> value; // get next value
    }
    ```

    但是实际上，表达式`inFile>>value`的结果为`inFile`，而在需要一个`bool`值的情况下，`inFile`的结果为`inFile.good()`，即`true` or `false`。因此，上述代码可以精简为：

    ```C++
    // abbreviated file-reading loop design
    // omit pre-loop input
    while (inFile >> value) // read and test for success
    {
        // loop body goes here
        // omit end-of-loop input
    }
    ```

## Chapter7 函数——C++的编程模块

### Section1 复习函数的基本知识

- 要使用C++函数，必须满足：
  - 提供函数定义
  - 提供函数原型
  - 调用函数
- C++对于返回值的类型有一定的限制：不能是数组，但可以是其他任何类型。
- 函数原型是一条语句，因此必须以分号结束。在函数原型中不必提供变量名，有类型列表就足够了。
- 在编译阶段进行的原型化被称为静态类型检查(static type checking)。静态类型检查可以捕获许多在运行阶段难以捕获的错误。

### Section2 函数参数和按值传递

- 用于接收传递值的变量被称为形参，C++标准又称为参量(parameter)，传递给函数的值被称为实参，C++标准又称为参数(argument)。
- 7.4 lotto.cpp中，计算中奖概率使用了组合$C_n^m=\frac{A_n^m}{m!}=\frac{n!}{m!(n-m)!}$。书中提出，这种计算不应当先计算出所有的分母，所有的分子，然后相除，因为这回导致计算过程中的中间值过大，应当每次计算一组分母除以分子，然后将所有中间值相乘，即$\frac{10}{2}\times\frac{9}{1}$好于$\frac{10\times9}{2\times1}$。

### Section3 函数和数组

- **当且仅当在函数头或函数原型中，`int * arr` 和 `int arr []`有相同的含义，都表示`arr`是一个`int`指针**。

  ```C++
  arr[i] == *(ar + i) // values in two notations
  &arr[i] == ar + i // addresses in two notations
  ```

- **如果需要将数组类型和元素数量告诉数组处理函数，必须通过两个不同的参数来传递，而不能使用方括号表示法传递数组长度。**

  ```C++
  void fillArray(int arr[], int size); // prototype
  void fillArray(int arr[size]); // NO -- bad prototype
  ```

- 使用普通参数时，由于C++按值传递数据，并且函数使用数据的副本，因此传递的参数能够得到自动保护不被修改，但是，在接受数组名的函数中，使用的是原始数据，因此，对传入参数的保护就显得比较重要。在函数头声明形参时使用`const`可以起到这个效果。注意，这里的`const`不代表传入的参数必须是常量，只是说在这个函数中，这个参数不能被修改。
- 指针和`const`：有两种方式将`const`关键字用于指针
  - **指针指向一个常量对象**，这样可以防止使用该指针来修改所指向的值。
  - **将指针本身声明为常量**，这样可以防止改变指针指向的位置。

  首先声明一个指向常量的指针`pt`：

  ```C++
  int age = 39;
  const int * pt = &age;
  ```

  该声明指出`pt`指向一个`const int`（例中为39）（写作`(const int)* pt`可能更好理解），因此**不能使用`pt`来修改这个值**。换句话说，**`*pt`的值为`const`，不能被修改。**

  ```C++
  *pt += 1; // INVALID because pt points to a const int
  cin >> *pt; // INVALID for the same reason
  ```

  但是，`pt`的声明不意味着它指向的值是常量，只是意味着对`pt`而言，这个值是常量。因此，可以通过修改`age`变量来修改`age`的值，但是不能通过`pt`指针来修改`age`的值。

  ```C++
  *pt = 20; // INVALID because pt points to a const int
  age = 20; // VALID because age is not declared to be const
  ```

  到此为止，已经讨论了将常规变量的地址赋给常规指针，上例则将常规变量的地址赋给指向`const`的指针。显然，还有两种可能，将`const`变量的地址赋给指向`const`的指针和将`const`变量的地址赋给常规指针。前一种可行而后一种不可行。

  ```C++
  const float g_earth = 9.80;
  const float * pe = &g_earth; // VALID

  const float g_moon = 1.63;
  float * pm = &g_moon; // INVALID
  ```

  前一种情况表明无论是通过变量还是通过指针都不能修改变量的值。后一种不被允许的原因在于：如果可以通过指针修改变量的值，那就和变量本身`const`冲突。

### Section4 函数和二维数组

- 如果将二维数组作为函数的参数，首先需要记住数组名被视为地址，因此，相应的形参是一个指针。
- **注意**

  ```C++
  int (*ar2)[4]; // 指向4个int组成数组的指针
  int *ar2 [4]; // 4个指向int指针组成的数组， 其实写成int* ar2 [4];会更好理解。int*说明ar2是指针
  ```

  *同样，在使用`const`时仍有困惑*

### Section5 函数和C-风格字符串

- C-风格字符串由一系列字符组成，以空值字符结尾。
- 将字符串作为参数时意味传递的是地址。其中有三种表示字符串的方式：
  - `char`数组
  - 用引号括起的字符串常量（也称字符串字面值）
  - 被设置为字符串的地址的`char`指针
  
  但是这三种方法的类型都是`char`指针（即`char*`）。也就是说，虽然将字符串作为参数传递，但是实际上传递的是字符串第一个字符的地址。这意味着字符串函数原型应当将其表示字符串的形参声明为`char*`类型。
- C-风格字符串和常规`char`数组的一个重要区别在于：字符串有内置的结束字符(`\0`)，即包含字符，但不以空值字符结尾的`char`数组只是数组，而不是字符串。

  ```C++
    // 7.9 strgfun.cpp
    char* wail = "ululate"; // wail points to string. 会收到编译器警告，ISO C++ 禁止string常量转换
  ```

### Section6 函数和结构

- 通常来说，使用结构编程时，像处理基本类型一样处理结构即可，即将结构作为参数传递，并在需要时将结构用返回值使用。按值传递会在函数中使用原始结构的副本。但是这种按值传递会有一个缺点：当结构很大时，复制结构会增加内存的需求，降低运行速度。因此，也可以使用传递结构的地址，然后使用指针访问结构的内容。C++提供按引用传递，这个在后面章节进行讨论。

### Section9 递归

- 如果递归函数调用自己，则被调用的函数也将调用自己，从而无限循环下去，除非代码中包含终止调用链的内容。

  ```C++
  void recurs(argumentlist)
  {
    statement1;
    if (test)
      recurs(arguments);
    statements2;
  }
  ```

  在这个递归函数中，只要if语句为`true`，每个`recurs()`调用都将执行statements1，然后再调用`recurs()`，而不会执行statements2.当if为`false`时，当前调用将执行statements2，然后程序控制权将返回调用它的`recurs()`，再执行statements2。因此，statements1会**按函数调用的顺序执行n次，而statements2将以与函数调用相反的顺序执行n次。**

### Section10 函数指针

- 获取函数的地址：使用函数名，并不跟参数即可。

  ```C++
  process(think); // passes address of think() to process()
  thought(think()); // passes return value of think() to thought()
  ```

- 声明函数指针：声明应指定函数的返回类型以及函数的特征标（参数列表），即声明应像函数原型那样指出有关函数的信息。**通常，要声明指向特定类型的函数的指针，可以首先编写这种函数的原型，然后用`(*pf)`替换函数名，这样`pf`就是这类函数的指针。这里要额外注意运算符的优先级，必须在声明中使用括号将`*pf`括起。`*pf(int)`意味着`pf()`是一个返回指针的函数，而`(*pf)(int)`意味着`pf`是一个指向函数的指针。**

  ```C++
  double (*pf)(int); // pf points to a function that returns double
  double *pf(int); // pf() a function that returns a pointer-to-double
  ```

## Chapter8 函数探幽

### Section1 C++内联函数

- 对于常规函数，C++执行到函数调用指令时，程序将在函数调用后立刻储存该指令的内存地址，并将函数参数复制到堆栈，跳转至标记函数起点的内存单元，执行函数代码，如果有的话将返回值放入寄存器中，然后调回到地址被保存的指令处继续执行。这种在内存中反复跳跃的过程会产生一定的开销。对于内联函数，程序则无需跳转至另一个位置执行代码，再跳转回来，而是直接使用对应的函数代码替换了函数调用。因此，内联函数的运行速度比常规函数略快，但是会产生额外的内存消耗。
- 使用内联函数需要在函数声明前加关键字`inline`，或在函数定义前加关键字`inline`。
- 通常的做法是省略函数原型，将整个函数（函数头和所有函数代码）放在原先函数原型的位置。
- **内联函数不能递归**。

### Section2 引用变量

- 引用变量会和原始变量使用相同的值和内存单元。
- 引用变量使用`&`进行创建，此处`&`不代表地址运算符，而是类型标识符的一部分。
- **必须在声明引用变量时进行初始化。**
- 在按值传递的函数中，实参可以选择多种类型，但是如果将类似的参数传递给接受引用参数的函数，编译器将会进行更严格的限制。以书中8.5为例：

  ```C++
  double cube(double a);
  double refcube(double &ra);
  // 按值传递
  double z = cube(x + 2.0); // evaluate x + 2.0, pass value
  z = cube(8.0); // pass the value 8.0
  int k = 10;
  z = cube(k); // convert value of k to double, pass value
  double yo[3] = {2.2, 3.3, 4.4};
  z = cube(yo[2]); // pass the value 4.4
  // 接受引用参数的函数
  double z = refcube(x + 3.0); // should not compile
  x + 3.0 = 5.0; // nonsensical
  ```

  显然，refcube接受ra作为一个变量的引用，那么实参应该是该变量，而不是一个表达式`x + 3.0`。

- 如果实参与引用参数不匹配，C++将生成临时变量。在当前，仅当参数为`const`引用时，C++才允许这种操作。
- 当引用参数是`const`，则编译器将在两种情况下生成临时变量：
  - 实参的类型正确，但不是左值
    - 可被引用的数据对象都是左值。如变量、数组元素、结构成员、引用和解除引用的指针等
    - 非左值包括字面变量和包含多项的表达式
    - 常规变量属于可修改的左值，而`const`变量属于不可修改的左值
  - 实参的类型不正确，但可以转换为正确的类型
- C++11新增了右值引用(rvalue reference)，这种引用使用`&&`指向右值。
- 在示例8.6中：

  ```C++
  accumulate(dup, five) = four;
  ```

  这条语句将值赋给函数调用是可行的。因为`accumulate()`的返回值是一个引用。如果`accumulate()`按值返回，则不能通过编译。由于返回值是指向dup的引用，因此，这段代码等效于：

  ```C++
  accumulate(dup, five); // add five's data to dup
  dup = four; // overwrite the contents of dup with the contents of four
  ```

- 传统的返回机制与按值传递函数参数类似：计算`return`后的表达式，并将结果返回给调用函数。也就是说，这个值被复制到一个临时位置，然后调用程序使用这个值。而在返回引用中，会使用不同的机制：

  ```C++
  dup = accumulate(team, five);
  ```

  如果`accumulate()`返回一个结构而不是指向结构的引用，则会把整个结构复制到一个临时位置，然后将这个拷贝复制给dup，但在返回引用时，直接将team复制到dup，提高了效率。因此，**返回引用的函数实际上是被引用的变量的别名**。
- 在返回引用时注意变量的作用空间，避免返回函数终止时不再存在的内存单元的引用。同样，也应当避免返回指向临时变量的指针。为避免这种情况，示例8.6中返回了一个作为参数传递给函数的引用。作为参数的引用将指向调用函数使用的数据，因此返回的引用也将指向这些数据。另一种方法是用`new`来分配新的存储空间，用`new`分配内存空间后，返回指向该内存空间的指针。同样，可以使用引用完成类似的工作：

  ```C++
  const free_throws & clone(free_throws & ft)
  {
    free_throws * pt;
    *pt = ft; // copy info
    return *pt; // return reference to copy
  }
  ```

  在这段代码中，指针`pt`指向无名结构`free_throws`，因此`*pt`就是该结构，但是函数声明表示函数会返回结构的引用，因此，可以这样使用该函数：

  ```C++
  free_throws & jolly = clone(three);
  ```

  这使得jolly成为新结构的应用。但是，这种方法隐藏的对`new`的调用，因此会容易导致忘记使用`delete`释放内存。
- 示例8.7中：

  ```C++
  const string & version2 (string & s1, const string & s2)
  {
    s1 = s2 + s1 + s2;
    return s1;
  }
  ```

  这里，s1作为一个非`const`值作为`const string`返回是合理且安全的。

- 对象、继承和引用：

  - 派生类继承基类的方法，可以使用基类的特性。
  - 基类引用可以指向派生类对象，而无需进行强制类型转换。因此，可以定义一个接受基类引用最为参数的函数，调用该函数时，可以将基类对象作为参数，也可以将派生类对象作为参数。

- 何时使用引用参数：

  使用引用参数的主要原因有两个：

  - 程序员能够修改调用函数中的数据对象。
  - 通过传递引用而不是整个数据对象可以提高程序的运行速度。

  当数据对象较大时第二个原因更为重要。但是同时，这也是使用指针参数的原因。那么什么时候使用引用，什么时候使用指针，什么时候按值传递呢？书中给出了一些指导原则：
  
  - 对于使用传递的值而不作修改的函数：
    - 如果数据对象很小，如内置数据类型或小型结构，则按值传递。
    - 如果数据对象是数组，则使用指针。**因为这是唯一的选择，并将指针声明为指向`const`的指针**。
    - 如果数据对象是较大的结构，则使用`const`指针或`const`引用以提高程序效率。这样可以节省复制结构所需的时间和空间。
    - 如果数据对象是类对象，则使用`const`引用。类设计的语义常常要求使用引用，这是C++新增这项特性的原因。因此，传递类对象参数的标准方式是按引用传递。
  - 对于修改调用函数中数据的函数：
    - 如果数据对象是内置数据类型，则使用指针。如果看到诸如`fixit(&x)`这样的代码（其中x是int），则显然该函数将修改x。
    - 如果数据对象是数组，则**只能使用指针**。
    - 如果数据对象是结构，则使用引用或指针。
    - 如果数据对象是类对象，则使用引用。

### Section3 默认参数

- 设置默认参数需要通过函数原型。

### Section4 函数重载

- 函数多态和函数重载表示相同的含义。多态是指函数可以有多种形式，重载是指可以有多个同名的函数，因此对名称进行了重载。
- 函数重载的关键是函数的参数列表，也称函数特征标(function signature)。如果两个函数的参数数目和类型相同，同时参数的排列顺序也相同，则特征标相同，此时变量名是无关紧要的。C++允许定义名称相同的函数，条件是特征标不同。因此可以定义一组如下的`print()`函数：

  ```C++
  void print(const char * str, int width); // #1
  void print(double d, int width); // #2
  void print(long l, int width); // #3
  void print(int i, int width); // #4
  void print(const char * str); // #5
  ```
  
  此时使用`print()`函数时，编译器将根据所采取的用法使用有相应特征标的原型：
  
  ```C++
  print("Pancakes", 15); // use #1
  print("Syrup"); // use #5
  print(1990.0, 10); // use #2
  print(1999, 12); // use #4
  print(1999L, 15); // use #3
  ```

  使用被重载的函数时，需要在函数调用中使用正确的参数类型，因此，对于下面的语句：

  ```C++
  unsigned int year = 3210;
  print(year, 6); // ambiguous call
  ```

  `print()`调用和任何原型均不匹配。没有匹配的原型的情况下，C++将尝试使用标准类型转换强制进行匹配。如果#2是`print()`的唯一原型，则函数调用`print(year, 6)`时将尝试把year转换为`double`类型，但是由于有3个将数字作为第一个参数的原型，因此有三种转换year的方式，因此C++将拒绝这种调用并给出报错。

  特例：一些看起来不同的特征标是不能共存的，例如如下两个原型：

  ```C++
  double cube(double x);
  double cube(double & x);
  ```

  这种情况下看似可以使用函数重载，但是实际上，假设如下代码`cout << cube(x);`中，参数x与两个原型都匹配，因此编译器无法确定使用那种原型。因此，编译器在检查函数特征标时，将**把类型引用和类型本身使用同一个特征标**。

  匹配函数时，会区分`const`和非`const`变量（对照英文版此处有错译）。例如：
  
  ```C++
  void dribble(char * bits); // overloaded
  void dribble(const char * cbits); // overloaded
  void dabble(char * bits); // not overloaded
  void drivel(const char * bits); // not overloaded
  
  const char p1[20] = "How's the weather?";
  char p2[20] = "How's the business?";
  dribble(p1); // dribble(const char *);
  dribble(p2); // dribble(char *);
  dabble(p1); // no match
  dabble(p2); // dabble(char *);
  drivel(p1); // drivel(const char *);
  drivel(p2); // drivel(const char *);
  ```

  `dribble()`有两个函数原型，一个用于`const`指针，一个用于常规指针。编译器将根据实参是否为`const`选择使用的原型。`dabble()`（对照英文版此处有错译）只与带非`const`参数的调用匹配，而`drivel()`可以与带`const`或非`const`参数的调用匹配。原因在于将非`const`值赋给`const`变量是合法的，但反之是非法的。

  **是特征标而不是函数类型使得可以对函数进行重载**。例如：

  ```C++
  long gronk(int n, float m); // same signatures,
  double gronl(int n, float m); // hence not allowed
  ```

  返回的类型可以不同，但是特征标也必须不同：

  ```C++
  long gronk(int n, float m); // different signatures,
  double gronl(float n, float m); // hence allowed
  ```

- *重载引用参数暂未理解*
- 避免滥用函数重载。仅当函数基本上执行相同的任务，但使用不同形式的数据时，才应当采用函数重载。
- 名称修饰(name decoration)或名称矫正(name mangling)是编译器在编译时根据函数原型中指定的形参类型对每个函数名加密，从而让C++跟踪每个重载函数。

### Seciton5 函数模板

- 函数模板是C++的新增特性。函数模板是通用的函数描述，使用泛型来定义函数，其中的泛型可用具体的类型（如`int`或`double`）替换。通过将类型作为参数传递给模板，可使编译器生成该类型的函数。由于模板允许以泛型而非具体类型编写程序，因此也被称为通用编程。由于类型是用参数表示，因此模板特性也被称为参数化类型(parameterized types)。
- 在编写函数时，如果需要不同类型数据实现相同的任务，同时使用函数重载过于繁琐时，即需要多个将同一种算法用于不同类型的函数，使用函数模板会是更好的选择。
- 函数模板允许以任意类型的方式来定义函数，例如可以定义如下模板：

  ```C++
  template <typename AnyType>
  void Swap(AnyType &a, AnyType &b)
  {
    AnyType temp;
    temp = a;
    a = b;
    b = temp;
  }
  ```

  第一行建立模板，并将类型命名为`AnyType`。**关键字`template`和`typename`是必须的，同时必须使用尖括号**。

- 在历史版本中，关键字`typename`被用`class`替代。这两种表示方法是完全等价的。
- 在需要对多个不同类型使用同一种算法的函数时，可以使用模板，但是同样有一些情况，并非所有的类型都使用相同的算法。为了满足这种需求，可以想重载常规函数定义那样重载模板定义。和常规重载一样，被重载的模板的函数特征标必须不同。
- 模板函数同样存在局限性，因为某些数据类型并不能正确处理。例如定义了比较运算符`>`或`<`，但是如果数据类型是数组，由于数组名为对应的地址，因此实际上比较运算符比较的是数组的地址，从而可能带来不可预知的结果。同样，赋值运算符`=`不能运用于结构，乘法运算符`*`不能运用于数组、指针、结构等，都会带来类似的问题。
- 当需要为特定类型提供具体化的模板定义时，可以使用显式具体化(explicit specialization)这种方法。
- 显式具体化方法：
  - 对于给定的函数名，可以有非模板函数，模板函数和显示具体化模板函数以及他们的重载版本。
  - 显示具体化的原型和定义应以`template <>`开头，并通过名称来指出类型。
  - 具体化模板函数优先于常规模板函数，非模板函数优先于具体化和常规模板函数。
- 使用函数模板本身不会生成函数定义，当编译器使用模板为特定类型生成函数定义时，会得到模板实例(instantiation)，实例化过的模板才是函数定义。
- 编译器根据提供的类型参数（如`int`，`double`等）对模板进行实例化，从而生成函数定义，这种方式被称为隐式实例化(implicit instantiation)。

  现在C++还允许显式实例化(explicit instantiation)。即直接命令编译器创建特定类型的实例，如`Swap<int>()`，其语法是在声明时用尖括号指示类型，并在声明前加上关键字`template`：
  
  ```C++
  template void Swap<int>(int, int); // explicit instantiation
  ```

  在这个声明下，编译器将直接使用`Swap()`模板生成一个使用`int`类型的实例。
- **显式实例化(explicit instantiation)和显式具体化(explicit specialization)的区别**

  ```C++
  template void Swap<int>(int, int); // explicit instantiation

  template <> void Swap<int>(int &, int &); // explicit specialization
  ```

  显式具体化(explicit specialization)声明在关键字`template`后包含尖括号`<>`，而显式实例化(explicit instantiation)没有。

  显式具体化(explicit specialization)是指，当面对指定的类型时，不要使用常规模板生成函数定义，而是使用专门为该指定类型显式定义的函数定义；而显式实例化(explicit instantiation)是要求编译器根据指定的类型生成模板。
- **警告：试图在同一个文件中使用同一种类型的显式实例和显式具体化将出错。**
- 还可以通过在程序中使用函数创建显式实例化，例如：

  ```C++
  template <typename T>
  T Add<T a, T b> // pass by value
  {
    return a + b;
  }

  ...

  int m = 6;
  double x = 10.2;
  cout << Add<double>(x, m) << endl; // explicit instantiation
  ```

  在上例中，由于模板要求两个传入的参数类型相同，因此模板和函数调用不匹配，但通过使用`Add<double>(x, m)`从而强制为`double`类型实例化，从而将参数m从`int`强制转换为`double`，以便与函数`Add<double>(double, double)`的参数匹配。

  但是如果对pass by reference使用这种方式则不可行，因为引用无法指向另一种格式。
- Specialization总结：

  ```C++

  ...

  template <typename T>
  void Swap(T &, T &); // template prototype

  template <> void Swap<job>(job &, job &); // explicit specialization for job

  int main(void)
  {
    template void Swap<char>(char &, char &); // explicit instantiation for char
    short a, b;

    ...

    Swap(a, b); // implicit template instantiation for short

    job n, m;

    ...

    Swap(n, m); // use explicit specialization for job

    char g, h;

    ...

    Swap(g, h); // use explicit template instantiation for char

    ...

  }
  ```

  编译器看到`char`的显式实例化后，将使用模板定义生成`Swap()`的`char`版本，对于其他`Swap()`调用，编译器根据函数调用中实际使用的参数生成对应的版本。

  当调用`Swap(a, b)`时，生成`Swap()`的`short`版本；当调用`Swap(n, m)`时，使用为`job`类型提供的独立定义（显式具体化，explicit specialization）；当调用`Swap(g, h)`时，使用已经显式实例化时生成的模板具体化。
- 当出现函数重载、函数模板和函数模板重载时，C++需要使用一种策略来决定为函数调用使用哪一个函数定义，这个过程称为重载解析(overloading resolution)。简单来说，这个过程有如下三步：

  1. 创建候选函数列表，包含与被调用函数名称相同的函数和模板函数。
  2. 使用候选函数列表创建可行函数列表。
  3. 确定是否有最佳的可行函数，如果有则使用，否则报错。

  举例如下，当函数只有一个参数时：

  ```C++
  may('B'); // actual argument is type char
  ```

  首先编译器先选择所有名称为`may()`的函数和函数模板，然后寻找可以用一个参数调用的函数。以下函数均符合要求：

  ```C++
  void may(int); // #1
  float may(float, float = 3); // #2
  void may(char); // #3
  char * may(const char *); // #4
  char may(const char &); // #5
  template<typename T> void may(const T &); // #6
  template<typename T> void may(T *); // #7
  ```

  其中，#4和#7不符合，因为整型不能被隐式转换为指针，剩下的4个函数和一个模板具体化后都可以使用。

  随后，编译器将选择最佳可行函数。选择顺序为：

  1. 完全匹配，但常规函数优先于函数模板。
  2. 提升转换（例如`char`和`short`自动转换为`int`，`float`自动转换为`double`）。
  3. 标准转换（例如`int`转换为`char`，`long`转换为`double`）。
  4. 用户定义的转换，如类声明中定义的转换。

  所以，#1优于#2，因为`char`到`int`是提升转换，而`char`到`float`是标准转换。#3，#5，#6都优于#1和#2，因为能够完全匹配。#3和#5优于#6因为#6是模板。#3和#5都能完全匹配，通常来说这表示出现了问题，但是仍然存在例外：在进行完全匹配时，C++允许某些“无关紧要的转换”（`Type`表示任意类型）：
  
  | **从实参 From an Actual Argument** | **到形参 To a Formal Argument**   |
  |:-------------------------------:|:------------------------------:|
  | Type | Type &|
  | Type & | Type|
  | Type \[\] | \* Type |
  | Type \(argument\-list\) | Type \(\*\) \(argument\-list\) |
  | Type | const Type |
  | Type | volatile Type |
  | Type \* | const Type |
  | Type \* | volatile Type \* |

  因此，假设如下函数代码：

  ```C++
  struct blot
  {
    int a;
    char b[10];
  };

  blot ink = {25, "spots"};

  ...

  recycle(ink);
  ```

  对应以下原型都能完全匹配：

  ```C++
  void recycle(blot); // #1 blot-to-blot
  void recycle(const blot); // #2 blot-to-(const blot)
  void recycle(blot &); // #3 blot-to-(blot &)
  void recycle(const blot &); // #4 blot-to-(const blot &)
  ```

  通常来说，如果有多个匹配的原型，编译器无法完成重载解析过程，但是如果多个匹配的函数仍有优先顺序时，重载解析可以实现。如指向非const数据的指针和引用优先与非const指针和引用参数匹配，在`recycle()`中体现为选择函数#3，因为`ink`没有被声明为`const`；然而，`const`和非`const`的区别只适用于指针和引用指向的数据，因此如果只定义了#1和#2，则会出现错误。另一种情况是非模板函数优先于模板函数（包括显式具体化），如果两个完全匹配的函数都是模板函数，则较具体的模板函数优先，即显式具体化优先于隐式具体化。举例如下：

  ```C++
  struct blot
  {
    int a;
    char b[10];
  };

  template <typename Type> void recycle (Type t); // template
  template <> void recycle<blot> (blot & t); //specialization for blot

  ...

  blot ink = {25, "spots"};

  ...

  recycle(ink); // use specialization
  ```

  需要注意的是，所谓“最具体(most specialized)”并不意味着显式具体化，而是在编译器推断时需要进行的类型转换最少，如以下两个模板：

  ```C++
  template <typename Type> void recycle (Type t); // #1
  template <typename Type> void recycle (Type * t); // #2
  ```

  如果程序中的调用使用如下代码：

  ```C++
  struct blot
  {
    int a;
    char b[10];
  };

  blot ink = {25, "spots"};

  ...

  recycle(&ink); // address of a structure
  ```

  在这个调用中，`recycle(&ink)`都能与#1和#2模板匹配，在与#1匹配时，`Type`被解释为`blot*`，在与#2匹配时，`Type`被解释为`ink`。在这种情况下，#2被认为是更具体的，因为#2已经显式指出函数参数是指向`Type`的指针，因此更加具体。

  以上规则被称为函数模板的部分排序规则(partial ordering rules)，和显式实例化一样，是C++98新增的特性。

  此外，还可以通过编写合适的函数调用，使编译器选择用户希望使用的函数或函数模板。程序8.15有详细的示例。

- 因为使用模板时不确定模板实例化时所使用的类型，因此会导致模板中一些类型无法得到确定：

  - ```C++
    template<typename T1, typename T2>
    void ft(T1 x, T2 y)
    {

      ...

      ?type? xpy = x + y;

      ...

    }
    ```

    在这个案例中，由于由于不知道`ft()`如何使用，因此也就无法确定`xpy`的类型，在C++11前，无法声明`xpy`的类型。

    C++11后，新增了关键字`decltype`从而解决了上述问题：

    ```C++
    int x;
    decltype(x) y; // make y the same type as x

    decltype(x + y) xpy; // make xpy the same type as x + y
    xpy = x + y;
    // same as
    decltype(x + y) xpy = x + y;
    ```

    因此模板函数`ft()`可以重写为：

    ```C++
    template<typename T1, typename T2>
    void ft(T1 x, T2 y)
    {

      ...

      decltype (x + y) xpy = x + y;

      ...

    }
    ```

    通用声明为:

    ```C++
    decltype(expression) var;
    ```

    对于`decltype`确定类型，编译器需要通过如下几步进行核对：

    1. 如果`expression`是没有用括号括起的标识符，则`var`类型与标识符类型相同，包括`const`等限定符：

        ```C++
          double x = 5.5;
          double y = 7.9;
          double &rx = x;
          const double * pd;
          decltype(x) w; // w is type double
          decltype(rx) u = y; // u is type double &
          decltype(pd) v; // v is type const double *
        ```

    2. 如果`expression`是一个函数调用，则`var`类型与函数返回值相同：

        ```C++
        long indeed(int);
        decltype (indeed(3)) m; // m is type long
        ```

        （书中说明`m`的类型是`int`，但是根据上下文，应该是`long`）
    3. 如果`expression`是一个左值，则`var`是指向其类型的引用：

        ```C++
        double xx = 4.4;
        decltype((xx)) r2 = xx; // r2 is double &
        decltype(xx) w = xx; // w is double (Stage 1 match)
        ```

    4. 如果以上都不匹配，则`var`类型与`expression`类型相同：

        ```C++
        int j = 3;
        int &k = j;
        int &n = j;
        decltype(j+6) i1; // i1 type int
        decltype(100L) i2; // i2 type long
        decltype(k+n) i3; // i3 type int
        ```

  - 另外，还有一种情况是`decltype`无法解决的，例如：

    ```C++
    template<typename T1, typename T2>
    ?type? gt(T1 x, T2 y)
    {

      ...

      return x + y;
    }
    ```

    同样，`x + y`的类型无法预知，同时，`decltype(x + y)`作为返回值也是无效的，因为参数`x y`并还未被声明，`decltype`必须在声明参数后才能使用。因此，C++新增了一种语法。举例，对于如下原型：

    ```C++
    double h(int x, float y);
    ```

    新增语法可以如下编写：

    ```C++
    auto h(int x, float y) -> double;
    ```

    这将返回类型移动到参数声明后面。`->`被称为后置返回类型(trailing return type)，`auto`是一个占位符，表示后置返回类型提供的类型。这种方法也可以用于函数定义：

    ```C++
    auto h(int x, float y) -> double
    {
      /*
      function body
      */;
    }
    ```

    通过这种方式，结合`decltype`便可以给上例中`gt()`指定返回类型，即：

    ```C++
    template<typename T1, typename T2>
    auto gt(T1 x, T2 y) -> decltype(x + y)
    {

      ...

      return x + y;
    }
    ```

## Chapter9 内存模型和名称空间

### Section1 单独编译

- 推荐的设计模式为，将程序分为三部分：

  1. 头文件：包含结构声明和使用这些结构的函数的原型
  2. 源代码文件：包含与结构有关的函数的代码
  3. 源代码文件：包含调用与结构相关的函数的代码

- 不要在头文件中写完整的函数定义，这样当一个程序的多个文件都包含这个头文���时，会导致同一个函数重复定义产生错误。通常来说，头文件中一般包含：

  - 函数原型
  - 使用`#define`或`const`定义的符号常量
  - 结构声明
  - 类声明
  - 模板声明
  - 内联函数

- 在包含自定义的头文件时，使用`""`而非`<>`，因为编译器对尖括号内的头文件会在系统文件中查找，而在双引号内会优先查找工作目录，没有后再查找标准位置。
- **注意，不要使用`#include`包含源代码文件，这样会导致多重声明。**
- 为避免多次包含同一个头文件，C++使用预处理器编译指令`#ifndef`，即(if not defined)，这样，编译器将查看`#ifndef`和`endif`之间的内容。

### Section2 存储持续性、作用域和链接性

- C++使用四种不同的方案存储数据，区别在于数据留存在内存中的时间：
  - 自动存储持续性：在函数定义中声明的变量（包括函数参数）的存储持续性为自动的。他们在程序开始执行其所有的函数或代码块时被创建，在执行完函数或代码块时，他们使用的内存被释放。
  - 静态存储持续性：在函数定义外定义的变量和使用关键字`static`定义的变量的存储持续性都为静态。他们在程序整个运行过程中存在。
  - 线程存储持续性(C++11)：使用关键字`thread_local`声明的变量，其生命周期与所属的线程一样。
  - 动态存储持续性：用`new`运算符分配的内存将一直存在，直到使用`delete`运算符将其释放或程序结束为止。这种内存的存储持续性为动态，有时被称为自由存储(free store)或堆(heap)。

- 作用域(scope)描述了名称在多大范围内可见。链接性(linkage)描述了名称如何在不同单元间共享。
- 在默认情况下，在函数中声明的函数参数和变量的**存储持续性为自动，作用域为局部，没有链接性。**
- 可以使用任何在声明时其值为已知的表达式来初始化自动变量。
- 由于自动变量的数目随函数的开始和结束而增减，因此程序必须在运行时对自动变量进行管理。常用的方法是留出一段内存，并将其视为栈，以管理变量的增减。

  程序使用两个指针来跟踪栈，一个指针指向栈底（即栈开始的位置），另一个指针指向栈顶（即下一个可用内存单元）。
- 寄存器变量由关键字`register`标识，会使用CPU寄存器来存储自动变量：

  ```C++
  register int count_fast; // request for a register variable
  ```

  在C++11后，这种方式的用法已经基本退化。

- C++为静态持续变量提供了3种链接性：
  - 外部链接性，可在其他文件中访问。必须在代码块外部声明。
  - 内部链接性，只能在当前文件中访问。必须在代码块外部声明，并使用`static`限定符。
  - 无链接性，只能在当前函数或代码块中访问。必须在代码块内部声明，并使用`static`限定符。

  ```C++
  ...

  int global = 1000; // static duration, external linkage
  static int one_file = 50; // static druation, internal linkage
  int main()
  {

    ...

  }
  void funct1(int n)
  {
    static int count = 0; // static duration, no linkage
    int llama = 0;

    ...

  }
  void funct2(int q)
  {

    ...

  }
  ```

  在上例中，`global`, `one_file`和`count`都是静态持续变量，在整个程序执行期间都存在。`count`作用域为局部，没有链接性，因此只能在`funct1()`函数中使用。与自动变量`llama`不同的是，即使`funct1()`函数没有被执行，`count`变量同样留在内存中。

  如果没有显式地初始化静态变量，编译器将全部设置为0。这种变量被称为零初始化(zero-initialized)。

  | **存储描述** | **持续性** | **作用域** | **链接性** | **声明** |
  |:----------------:|:------:|:------:|:------:|:----------------------------------:|
  | 自动 | 自动 | 代码块 | 无 | 代码块中 |
  | 寄存器 | 自动 | 代码块 | 无 | 代码块中，使用关键字`register' |
  | 静态，无链接性 | 静态 | 代码块 | 无 | 代码块中，使用关键字`static` |
  | 静态，外部链接性 | 静态 | 文件 | 外部 | 不在任何函数内 |
  | 静态，内部链接性 | 静态 | 文件 | 内部 | 不在任何函数内，使用关键字`static` |

  除了默认使用的零初始化外，也可以进行表达式初始化和动态初始化。零初始化和表达式初始化会在编译时初始化变量，动态初始化则在编译后初始化。
- 链接性为外部的变量通常称为外部变量，存储持续性为静态，作用域为整个文件，也称为全局变量。
  - 单定义规则(One Definition Rule, ODR)是指，变量只能有一次定义。但是C++同时规定，每个使用外部变量的文件都必须声明。为了避免和ODR冲突，C++提供了两种变量声明：一种是定义声明(defining declaration)或简称为定义(definition)，给变量分配存储空间；另一种是引用声明(referencing declaration)或简称为声明(declaration)，不给变量分配存储空间，因为这是对已有变量的引用。
  
    引用声明使用关键字`extern`且不进行初始化，否则声明为定义，并分配存储空间。
  
    如果要在多个文件中使用外部变量，只需在一个文件中包含该变量的定义（单定义规则），但在使用该变量的所有其他文件中，都必须使用关键字`extern`声明：

    ```C++
    // file01.cpp
    extern int cats = 20; // definition because of initialization
    int dogs = 22; // also a definition
    int fleas; // also a definition

    ...

    // file02.cpp
    // use cats and dogs from file01.cpp
    extern int cats; // not definitions because they use
    extern int dogs; // extern and have no initialization

    ...

    // file98.cpp
    // use cast, dogs and fleas from file01.cpp
    extern int cats;
    extern int dogs;
    extern int fleas;

    ...
    ```

    在上例中，所有文件都使用了`file01.cpp`中定义的变量`cats`和`dogs`。但`file02.cpp`没有重新声明变量`fleas`因此无法使用这个变量。

    在`file01.cpp1`中，`extern`关键字并不是必须的，但是在引用这个变量的另一个文件中，必须要有`extern`关键字。

  - 在程序9.6中，使用了作用域解析运算符(`::`)，放在变量名前时，该运算符表示使用变量的全局版本。
  
- 将`static`限定符用于作用域为整个文件的变量时，该变量的链接性将为内部的，同时会覆盖同名的全局定义。
- 将`static`限定符用于在代码块中定义的变量，则创建无链接性的局部变量。尽管这个变量只在该代码块中可用，但它在该代码块不处于活动状态时仍然存在。因此在两次函数调用之间，静态局部变量的值将保持不变。
- 被称为存储说明符(storage class specifier)或cv-限定符(cv-qualifier)的C++关键字提供了有关存储的信息。
- 存储说明符：`register`, `static`, `extern`, `thread_local`(C++11), `mutable`。
- cv-限定符：`const`, `volatile`。`volatile`限定符表明即使程序代码没有修改内存单元，其值也可能发生变化。*主要用于优化，未完全理解。*
- `mutable`指出，即使结构或类变量为const，其某个成员也可以被修改。
- 在默认情况下，全局变量的链接性是外部的，但是`const`全局变量的链接性是内部的。这种方式可以避免当常量放在头文件中时，多个文件对同时对头文件的引用导致的单定义规则报错。同时，内部链接性保证了每个文件都有自己的一组常量，而非所有文件共享一组常量。如果希望某个常量的链接性是外部的，则可以使用`extern`关键字来覆盖默认的内部链接性：

  ```C++
  extern const int states = 50; // definition with external linkage
  ```

  在这种情况下，必须在所有使用该常量的文件中使用`extern`关键字来声明。注意这和常规外部变量不同。常规外部变量定义时不需要使用`extern`关键字，而是在使用该变量的其他文件中使用`extern`。

  另外由于单个`const`在多个文件之间共享，因此**只有一个文件可以对其进行初始化。**

- C++不允许在一个函数中定义另一个函数。因此，所有函数的存储持续性都为静态。
- 函数同样有链接性，默认情况下函数链接性为外部，即可在文件中共享。也可以使用`static`将函数链接性设置为内部，使之只能在一个文件中使用。
- 除以上几种链接性以外，还有一种所谓语言链接性(languange linking)，主要实现不同语言不同编译器如何对函数名进行翻译并链接的行为。
- 已介绍过的为变量分配内存的方案并不适用于使用C++运算符`new`分配的内存，这种内存被称为动态内存。动态内存由运算符`new`和`delete`控制，而不是由作用域和链接性规则控制。因此，可以在一个函数中分配动态内存，而在另一个函数中将其释放。与自动内存不同，动态内存不是LIFO，其分配和释放的顺序要取决于`new`和`delete`在何时以何种方式被使用。
  - 可以直接使用`new`运算符进行初始化，在C++11中，可以使用大括号的列表初始化初始化常规结构或数组，例如：

    ```C++
    struct where
    {
      double x;
      double y;
      double z;
    };

    where * one = new where {2.5, 5.3, 7.2}; // C++11
    int * ar = new int [4] (2, 4, 6, 7); // C++11
    ```

    同样，C++11中也可以将列表初始化用于单值变量：

    ```C++
    int * pi = new int {6}; // *pi set to 6
    double * pd = new double {99.99}; // *pd set to 99.99
    ```

  - 当`new`请求内存失败时，会引发异常`std::bad_alloc`。
  - 运算符`new`和`new []`分别调用以下函数：

    ```C++
    void * operator new(std::size_t); // used by new
    void * operator new[] (std::size_t); // used by new[]
    ```

    这些函数被称为分配函数(alloction function)，位于全局名称空间中，对应的有`delete`和`delete[]`调用的释放函数(deallocation function)。
  - 通常`new`负责在堆(heap)中找到一个满足要求的内存块，但`new`运算符还有另一种变体，被称为定位(placement)`new`运算符，可以指定要使用的位置，便于进行设置内存管理，处理需要通过特定地址进行访问的硬件或在特定位置创建对象。

    要使用定位`new`特性，首先需要包含头文件`<new>`，提供了定位`new`运算符的原型，然后将`new`运算符用于提供了所需地址的参数，例如：

    ```C++
    #include <new>
    struct chaff
    {
      char dross[20];
      int slag;
    };
    char buffer1[50];
    char buffer2[500];
    int main()
    {
      chaff * p1, * p2;
      int * p3, * p4;
      // first, the regular forms of new
      p1 = new chaff; // place structure in heap
      p3 = new int[20]; // place int array in heap
      // now, the two forms of placement new
      p2 = new (buffer1) chaff; // place structure in buffer1
      p4 = new (buffer2) int[20]; // place int array in buffer2
    }
    ```

    上例中使用了两个数组给定位`new`运算符提供内存空间。即从`buffer1`中分配空间给`chaff`，从`buffer2`中分配空间给一个包含20个元素的`int`数组。

    *定位`new`运算符暂时未完全理解。*

### Section3 名称空间

- 声明区域(declaration region)指可以在其中进行声明的区域。当在函数外声明全局变量时，变量的声明区域为其声明所在的文件；当在函数内声明变量时，声明区域为其声明所在的代码块。
- 潜在作用域(potential scope)指变量从声明点开始到声明区域的结尾。
- 变量并非在其潜在作用域的全部范围内可见，例如变量常常会被另一个嵌套在声明区域中声明的同名变量隐藏。比如在函数中声明的局部变量（其声明区域为整个函数）会隐藏同一个文件中声明的全局变量（其声明区域为整个文件）。
- 在C++新增的特性中，可以通过定义一种新的声明区域来创建命名的名称空间。一个名称空间中的名称不会与另一个名称空间中的相同名称发生冲突，同时允许程序的其他部分使用该名称空间中声明的东西。
- 名称空间可以是全局的，也可以位于另一个名称空间中，但不能位于代码块中。因此，在默认情况下，在名称空间中声明的名称的链接性为外部的，除非引用了常量。
- 除了用户定义的名称空间外，还存在另一个名称空间——全局名称空间(global namespace)，对应于文件级声明区域，因此所谓的全局变量可以描述为位于全局名称空间中。
- 任何名称空间中的名称都不会与其他名称空间中的名称发生冲突。
- 作用域解析运算符`::`可以访问给定名称空间的名称。未被装饰的名称称为未限定名称(unqualified name)，包含名称空间的名称称为限定名称(qualified name)。
- C++提供了两种机制来简化对名称空间中名称的使用，可以不用每次都通过作用域解析运算符`::`使用名称空间来限定名称。

  1. `using`声明是特定的标识符可用。
  2. `using`编译指令使整个名称空间可用。

- `using`声明由被限定的名称和它前面的关键字`using`组成。`using`声将特定的名称添加到它所属的声明区域中：

  ```C++
  namespace Jill
  {
    double bucket(double n) // function definition
      {

        ...

      }
    double fetch; // variable declaration
    struct Hill
    {

      ...

    }; // structure declaration
  }
  char fetch;

  int main()
  {
    using Jill:fetch; // put getch into local namespace
    double fetch; // Error! Already have a local fetch
    cin >> fetch; // read a value into Jill::fetch
    cin >> ::fetch; // read a value into global fetch

    ...

  }
  ```

  在上例中，由于`using`声明将名称添加到局部声明区域中，因此这个示例避免了将另一个局部变量也命名为`fetch`，同时，和其他局部变量一样，`fetch`将覆盖同名的全局变量。

- 在函数外使用`using`声明时，将把名称添加到全局名称空间中：

  ```C++
  void other();
  namespace Jill
  {
    double bucket(double n)
    {

      ...

    }
    double fetch;
    struct Hill
    {

      ...

    };
  }
  using Jill::fetch; // put fetch into global namespace

  int main()
  {
    cin >> fetch; // read a value into Jill:fetch
    other()

    ...

  }

  void other()
  {
    cout << fetch; // display Jill::fetch

    ...

  }
  ```

- `using`声明使一个名称可用，而`using`编译指令使所有的名称都可用。`using`编译指令由名称空间名和它前面的关键字`using namespace`组成，它使名称空间中所有名称都可用，而不需要使用作用域解析运算符`::`。

  ```C++
  using namespace Jack; // make all the names in Jack available
  ```

  在全局声明区域中使用`using`编译指令，将使该名称空间的名称全局可用：

  ```C++
  #include <iostream>
  using namespace std; // places names in namespace std make names available globally
  ```

  在函数中使用`using`编译指令，将使其中的名称在该函数中可用：

  ```C++
  int main()
  {
    using namespace Jack; // make names available in main()

    ...

  }
  ```

- 如果使用作用域解析运算符，不会存在二义性，如：

  ```C++
  jack::pal = 3;
  jill::pal = 10;
  ```

  但如果使用`using`声明，情况将发生变化：

  ```C++
  using jack::pal;
  using jill::pal;
  pal = 4; // which one? now have a conflict
  ```

  编译器将阻止这种声明，因为会导致二义性。

- 使用`using`编译指令导入一个名称空间中所有的名称与使用多个`using`声明是不一样的，而更像是大量使用作用域解析运算符。使用`using`声明时，就如同声明了相应的名称，如果这个名称在函数中已经声明，则不能用`using`声明导入相同的名称。但在使用`using`编译指令时，将进行名称解析，就像在包含`using`声明和名称空间本身的最小声明区域中声明名称一样。在全局的名称空间中，如果使用`using`编译指令导入一个已经在函数中声明的名称，则局部名称将隐藏名称空间名，但仍然可以使用作用域解析运算符：

  ```C++
  namespace Jill
  {
    double bucket(double n)
    {

      ...

    }
    double fetch;
    struct Hill
    {

      ...

    };
  }
  char fetch; // global namespace
  
  int main()
  {
    using namespace Jill; // import all namespace names
    Hill Thrill; // create a type Jill::Hill structure
    double water = bucket(2); // use Jill::bucket()
    double fetch; // not an error; hides Jill::fetch
    cin >> fetch; // read a value into the local fetch
    cin >> ::fetch; // read a value into global fetch
    cin >> Jill::fetch; // read a value into Jill::fetch

    ...

  }

  int foom()
  {
    Hill top; // ERROR
    Jill::Hill crest; //valid
  }
  ```

  在上例中，在函数`main()`中，名称`Jill::fetch`被放在局部名称空间中，但作用域不是局部的，因此不会覆盖全局的`fetch`，然而，局部声明的`fetch`将隐藏`Jill::fetch`和全局`fetch`，但是如果使用作用域解析运算符，则后两个`fetch`变量都是可用的。对比使用`using`声明的例子，可以更加直观地理解其中的区别。

  尽管**函数中的`using`编译指令将名称空间的名称视为在函数之外声明**的，但是不会使该文件中的其他函数能够使用这些名称。上例中，`foom()`函数即不能使用未限定的标识符`Hill`。

- **假设名称空间和声明区域定义了相同的名称，如果试图使用`using`声明将名称空间的名称导入该声明区域，则这两个名称会发生冲突，从而出错；如果使用`using`编译指令将该名称空间的名称导入该声明区域，则局部版本将隐藏名称空间版本。**

  一般来说，使用`using`声明比使用`using`编译指令更加安全，因为`using`声明只导入指定的名称，如果这个名称和局部名称发生冲突，则编译器将给出提示；而使用`using`编译指令会导入所有名称，包括可能并不需要的名称，如果与局部名称发生冲突，则局部名称将覆盖名称空间版本，同时编译器并不会给出警告。

- 名称空间声明可以进行嵌套：

  ```C++
  namespace elements
  {
    namespace fire
    {
      int flame;

      ...

    }
    float water;
  }
  ```

  这里，`flame`指的是`element::fire::flame`，同样。也可以使用`using`编译指令使内部名称可用：

  ```C++
  using namespace elements::fire;
  ```

  名称空间中也可以使用`using`编译指令和`using`声明：

  ```C++
  namespace myth
  {
    using Jill::fetch;
    using namespace elements;
    using std::cout;
    using std::cin;
  }
  ```

  此时如果需要访问`Jill::fetch`，由于`Jill::fetch`位于名称空间`myth`中，因此可以这样访问：

  ```C++
  std::cin >> myth::fetch;
  ```

  同样，`fetch`也位于`Jill`名称空间中，因此仍然可以使用`Jill::fetch`：

  ```C++
  std::cout << Jill::fetch; // display value read into myth::fetch
  ```

  如果没有冲突的局部变量，也可以写为：

  ```C++
  using namespace myth;
  cin >> fetch; // readlly std::cin and Jill::fetch
  ```

  同时，上例中使用的`using`编译指令也被进行了传递，即：

  ```C++
  using namespace myth;
  ```

  等价于：

  ```C++
  using namespace myth;
  using namespace elements;
  ```

- 名称空间可以创建别名，例如：

  ```C++
  namespace my_very_favourite_things {...};
  namespace mvft = my_very_favourite_thins; // alias  
  ```

  从而可以简化对嵌套名称的使用：

  ```C++
  namespace MEF = myth::elements::fire;
  using MEF::flame;
  ```

- 可以通过省略名称空间的名称来创建未命名的名称空间：

  ```C++
  namespace // unnamed namespace
  {
    int ice;
    int bandycoot;
  }
  ```

  这种声明方法的潜在作用域为从该声明点到该声明区域的末尾。由于未命名的名称空间没有名称，因此无法显式地使用`using`编译指令或`using`声明来使其可以在其他位置使用，因此，可以理解为提供了链接性为内部的静态变量的替代品。举例如下：

  ```C++
  static int counts; // static storage, internal linkage
  int other();
  int main();
  {

    ...

  }
  
  int other();
  {

    ...

  }
  ```

  可以采用名称空间方法为：

  ```C++
  namespace
  {
    int counts; // static storage, internal linkage
  }
  int other();
  int main();
  {

    ...

  }

  int other();
  {

    ...

  }
  ```

- 名称空间的指导原则：

  - 使用在已命名的名称空间中声明的变量，而不是使用外部全局变量。
  - 使用在已命名的名称空间中声明的变量，而不是使用静态全局变量。
  - 如果开发了一个函数库或类库，将其放在一个名称空间中。
  - 仅将编译指令`using`作为一种将旧代码转换为使用名称空间的权宜之计。
  - 不要在头文件中使用`using`编译指令。
  - 导入名称时，首选使用作用域解析运算符`::`或`using`声明的方法。
  - 对于`using`声明，首选将其作用域设置为局部而不是全局。

## Chapter10 对象和类

- OOP的重要特性：
  - 抽象
  - 封装和数据隐藏
  - 多态
  - 继承
  - 代码的可重用性

### Section1 过程性编程和面向对象编程

- 采用OOP编程时，首先考虑数据，不仅要考虑如何表示数据，还要考虑如何使用数据。从用户的角度考虑对象——描述对象所需的数据以及描述用户与数据交互所需的操作。完成对接口的描述后，需要确定如何实现接口和数据存储。最后使用新的设计方案创建出程序。

### Section2 抽象和类

- 类规范由两个部分组成：
  - 类声明： 以数据成员的方式描述数据部分，以成员函数（被称为方法）的方式描述公有接口。
  - 类方法定义：描述如何实现类成员函数。
- 接口是一个公共框架，供两个系统交互时使用。对于类，我们说公共接口。在这里，公共(public)是使用类的程序，交互系统由类对象组成，而接口由编写类的人提供的方法组成。接口让程序员能够编写与类对象交互的代码，从而让程序能够使用类对象。要使用某个类，必须了解其公共接口，要编写类，必须创建公共接口。
- C++程序员通常将接口（类定义）放在头文件中，将实现（类方法的代码）放在源代码文件中。
- 类设计尽可能将公有接口与实现细节分开。公有接口表示设计的抽象组件，将实现细节放在一起并将它们与抽象分开被称为封装。数据隐藏（将数据放在类的私有部分中）是一种封装，将实现的细节隐藏在私有部分中也是一种封装。
- 无论类成员是数据成员还是成员函数，都可以在类的公有部分或私有部分中声明。但由于隐藏数据是OOP的主要目标之一，因此数据项通常放在私有部分，组成类接口的成员函数放在公有部分，否则就无法从程序中调用这些函数。
- **不必在类声明中使用关键字`private`，因为这是类对象的默认访问控制。**
- 客户/服务器模型：
  - 客户是使用类的程序，类声明（包括类方法）构成了服务器，它是程序可以使用的资源。客户只能通过以公有方式定义的接口使用服务器，这意味着客户唯一的责任是了解该接口。服务器的责任是确保服务器根据该接口可靠并准确的执行。服务器设计人员只能修改类设计的实现细节，而不能修改接口。这样程序员独立地对客户和服务器进行改进，对服务器的修改不会对客户的行为产生意外的影响。

### Section3 类的构造函数和析构函数

- 类构造函数可以在创建类对象时对其进行初始化。**构造函数没有声明类型。**
- **成员名和参数名**：
  - 如果试图将类成员名称用作构造函数的参数名，例如：

    ```C++
    // NO!
    Stock::Stock(const string& company, long shares, double share_val)
    {

      ...

    }
    ```

    这种方式是错误的。构造函数的参数表示的不是类成员，而是赋给类成员的值。因此，**参数名不能与类成员相同**，否则最终的代码将会是这样的：

    ```C++
    shares = shares;
    ```

    为避免这种混乱，一种常见的做法是在数据成员名中使用`m_`前缀，例如：

    ```C++
    class Stock
    {
    private:
      string m_company;
      long m_shares;

      ...

    }
    ```

    更常见的做法是，在成员名中使用后缀`_`：

    ```C++
    class Stock
    {
    private:
      string company_;
      long shares_;

      ...

    }
    ```

    无论哪种方法，都可在公有接口中在参数名中包含company和shares。

- C++提供了两种使用构造函数进行初始化对象的方法：
  - 显式地调用构造函数：

    ```C++
    Stock food = Stock("World Cabbage", 250, 1.25);
    ```

  - 隐式地调用构造函数：

    ```C++
    Stock garment("Furry Mason", 50, 2.5);
    ```

  每次创建类对象，甚至使用`new`动态分配内存时，C++都使用类构造函数，例如：

  ```C++
  Stock* pstock = new Stock("Electroshock Games", 18, 19.0);
  ```

  当没有提供构造函数时，C++会自动提供默认构造函数，但是不初始化其成员。一旦为类定义了构造函数后，就必须为它提供默认构造函数，否则声明会出错。

  在设计类时，通常应提供对所有类成员做隐式初始化的默认构造函数。

- 析构函数会在对象过期时完成清理工作。如果构造函数使用`new`来分配内存，则析构函数将使用`delete`来释放内存。
- 析构函数的名称为在类名前加`~`，和构造函数一样，析构函数也没有返回值和声明类型，同时析构函数没有参数。

  通常不应在代码中显式地调用析构函数。如果创建的是静态存储类对象，则其析构函数将在程序结束时自动被调用；如果创建的是自动存储类对象，则其析构函数将在程序执行完代码块时自动被调用；如果对象是通过`new`创建的，则它将驻留在栈内存或堆内存（自由存储区）中，当使用`delete`释放内存时，其析构函数将自动被调用。
- 由于在类对象过期时析构函数将自动被调用，因此必须有一个析构函数。如果没有提供析构函数，则编译器将隐式地声明一个默认析构函数，并在发现导致对象被删除的代码后，提供默认析构函数的定义。
- 在默认情况下，将一个对象赋给同类型的另一个对象时，C++将源对象的每个数据成员的内容复制到目标对象中相应的数据成员中。
- 当应用构造函数至已存在对象时，构造函数会创建一个新的临时的对象，将内容复制到已存在对象中，然后编译器调用析构函数，以删除临时对象。
- 自动变量被存放于栈中，因此最后创建的对象将最先被删除。
- 根据编译器的不同，初始化创建有指定值的对象，可能会创建临时对象，可能不会，因此可能会调用析构函数，也可能不会；而在赋值语句中使用构造函数则总会在赋值前创建一个临时对象，相应的也会调用析构函数。如果既可以通过初始化，也可以通过赋值来设置对象的值，则应采用初始化的方式，这种方式的效率更高。
- C++11中，支持使用列表初始化语法，只要用大括号括起即可。
- 当出现如下情况时：

  ```C++
  const Stock land = Stock("Kludgehorn Properties");
  land.show();
  ```

  编译器将拒绝第二行。因为`show()`的代码无法确保调用对象不被修改（因为是`const`）。在之前会在函数声明中将参数声明为`const`引用或指向`const`的指针，但是在这里，`show()`不提供任何参数，而且使用的对象是由方法调用提供的，因此需要使用另一种语法保证函数不会修改调用对象。解决方法是将`const`关键字放在函数的括号后面，即`show()`的声明更新为：

  ```C++
  void show() const; // promises not to change invoking object
  ```

  函数定义的开头则为：

  ```C++
  void stock::show() const // promises not to change invoking object
  ```

  以这种方式声明和定义的类函数被称为`const`成员函数，只要类方法不修改调用对象，就应将其声明为`const`。

- 构造函数和析构函数小结：
  - 构造函数是一种特殊的类成员函数，在创建类对象时被调用。
  - 构造函数的名称和类名相同，但通过函数重载，可以创建多个同名的构造函数，条件是每个函数的特征标都不同。
  - 构造函数没有声明类型。
  - 构造函数用于初始化类对象的成员，初始化应与构造函数的参数列表匹配。例如，`Bozo`类的构造函数原型为：

    ```C++
    Bozo(const char* fname, const char* lname); // constructor prototype
    ```

    则可以用来初始化新对象：

    ```C++
    Bozo bozetta = Bozo("Bozetta", "Biggens"); // primary form
    Bozo fufu("Fufu", "O'Dweeb"); // short form
    Bozo* pc = new Bozo("Popo", "Le Peu"); // dynamic object
    // C++11
    Bozo boztta = {"Bozetta", "Biggens"};
    Bozo fufu{"Fufu", "O'Dweeb"};
    Bozo* pc = new Bozo{"Popo", "Le Peu"};
    ```

  - 如果构造函数只有一个参数，则将对象初始化为一个与参数的类型相同的值时，该构造函数将被调用。例如，`Bozo`类的构造函数原型为：

    ```C++
    Bozo(int age);
    ```

    则可以初始化对象：

    ```C++
    Bozo dribble = Bozo(44); // primary form
    Bozo roon(66); // secondary form
    Bozo tubby = 32; // special form for one-argument constructors
    ```

    其中第三种是一个特性，**接受一个参数的构造函数允许使用赋值语法将对象初始化为一个值**：

    ```C++
    Classname object = value;
    ```

    这种特性可能导致问题，因此后续将提到如何关闭这项特性。

  - 默认构造函数没有参数，如果创建对象时没有进行显式初始化，则将调用默认构造函数。如果程序中没有提供任何构造函数，则编译器会为程序定义一个默认构造函数，否则必须自己提供默认构造函数。默认构造函数可以没有任何参数，如果有，则必须给所有参数都提供默认值。
  - 当对象被删除时，程序将调用析构函数。每个类都只能有一个析构函数。
  - 析构函数没有返回类型，也没有参数，其名称为类名称前加上`~`。
  - **如果构造函数使用了`new`，则必须提供使用`delete`的析构函数**。

### Section4 `this`指针

- 当需要在函数调用中返回对象本身，可以使用`this`指针。`this`指针指向用来调用成员函数的对象，`this`被作为隐藏参数传递给方法。一般来说，所有的类方法都将`this`指针设置为调用它的对象的地址。
- 每个成员函数（包括构造函数和析构函数）都有一个`this`指针。`this`指针指向调用对象。如果方法需要引用整个调用对象，则可以使用表达式`*this`。在函数的括号后面使用`const`限定符将`this`限定为`const`，这样将不能使用`this`来修改对象的值。

  然而，要返回的并不是`this`，因为`this`是对象的地址，对象本身是`*this`（将解除引用运算符`*`用于指针，将得到指针指向的值）。

### Section5 对象数组

- 声明对象数组的方法与声明标准类型数组相同。
- 当程序创建未被显式初始化的类对象时，总是调用默认构造函数。声明对象数组要求类要么没有显式地定义任何构造函数，那将使用不执行任何操作的隐式默认构造函数，要么定义了一个显式默认构造函数。
- 可以用构造函数来初始化数组。在这种情况下，必须为每个元素调用构造函数。

### Section6 类作用域

- 类作用域意味着不能从外部直接访问类的成员，即使要调用公有成员函数，也必须通过对象。
- 在定义成员函数时，必须使用作用域解析运算符。
- 在类中直接声明一个常量是不可行的，因为声明类只是描述了对象的形式，并没有创建对象：

  ```C++
  class Bakery
  {
    private:
      const int Months = 12; // declare a constant? FAILS
      double costs[Months];

      ...

  }
  ```

  要实现这个目标，通常有两种做法：
  - 在类中声明一个枚举。在类声明中声明的枚举的作用域为整个类，因此可以用枚举为整型常量提供作用域为整个类的符号名称。即：

    ```C++
    class Bakery
    {
      private:
        enum {Months = 12};
        double costs[Months];

        ...

    }
    ```

  - 另一种方式是使用关键字`static`：

    ```C++
    class Bakery
    {
      private:
        static const int Months = 12;
        double costs[Months];

        ...

    }
    ```

- 在传统枚举中，不同枚举定义中的枚举量可能发生冲突，例如：

  ```C++
  enum egg{Small, Medium, Large, Jumbo};
  enum t_shirt{Small, Medium, Large, Jumbo};
  ```

  这将无法通过编译，因为处于相同的作用域中会导致冲突。

  C++11提供了一种新的枚举，其枚举作用域为类，其声明类似于：

  ```C++
  enum class egg {Small, Medium, Large, Jumbo};
  enum class t_shirt{Small, Medium, Large, Xlarge};
  ```

  需要使用枚举名来限定枚举量：

  ```C++
  egg choice = egg::Large; // the Large enumerator of the egg enum
  t_shirt Floyd = t_shirt::Large; // the Large enumerator of the t_shirt enum
  ```

### Section7 抽象数据类型

- 抽象数据类型(abstract data type, ADT)可以用类来很好的实现。所谓抽象数据类型，即以一种通用的方式描述数据类型，而不引入语言或实现细节。
- 例如，栈就是一种管理变量的抽象数据类型。根据栈的特征，可以由可对它执行的操作来描述：
  - 可创建空栈。
  - 可将数据项添加到栈顶（压入）。
  - 可从栈顶删除数据项（弹出）。
  - 可查看栈是否填满。
  - 可查看栈是否为空。

  将上述描述转换为类声明，使用公有成员函数提供栈操作的接口，使用私有数据成员存储栈数据。

## Chapter11 使用类

### Section1 运算符重载

- 运算符重载是一种形式的C++多态。
- 要重载运算符，需使用被称为运算符函数的特殊函数形式，格式如下：

  ```C++
  operator op(argument-list)
  ```

  其中`op`必须是有效的C++运算符。例如`operator+()`重载`+`运算符，`operator*()`重载`*`运算符。

### Section2 计算时间：一个运算符重载示例

- 再次重申使用引用作为参数和返回值的注意点：不要返回指向局部变量或临时变量的引用。函数执行完毕后，局部变量和临时变量将消失，引用将指向不存在的数据。
- 运算符重载中，编译器将根据操作数的类型来确定如何操作：

  ```C++
  int a, b, c;
  Time A, B, C;
  c = a + b; // use int addition
  C = A + B; // use addition as defined for Time objects
  ```
