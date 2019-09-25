- [C++ Primer Plus (6th Edition) Notes](#c-primer-plus-6th-edition-notes)
  - [Chapter2](#chapter2)
    - [Section 3](#section-3)
    - [Section 4](#section-4)
  - [Chapter3](#chapter3)
    - [Section1](#section1)
    - [Section2](#section2)
    - [Section3](#section3)
  - [Chapter4](#chapter4)
    - [Section1](#section1-1)
    - [Section2](#section2-1)
    - [Section4](#section4)
    - [Section5](#section5)

# C++ Primer Plus (6th Edition) Notes
## Chapter2
- C++ 中必须使用双引号，使用单引号会无法通过编译。
### Section 3
- cin:
cin和cin.get()等存在区别，cin.get()无法读取数字，如果使用cin.get()并在terminal中输入int等会出现数值错误。
### Section 4
- **C++程序中应当为程序中使用的每个函数提供原型 (Function Prototype)。**
  - 由于在使用函数前，C++编译器必须知道函数的参数类型和返回值类型，因此需要使用函数原型语句显性地声明。函数原型之于函数相当于变量声明之于变量。
  - 应在首次使用函数之前提供其原型。通常的做法是把原型放到 main() 函数定义的前面。
  - 如果没有函数原型放在 main() 函数前为编译器提供必要的信息，则必须将整个函数的定义语句放在 main() 函数前。实际上这两种方式各有利弊。如果将 main() 函数放在最后，则需要对整个C++程序中使用的函数组织正确的顺序。在一个程序中包含许多函数，同时这些函数又调用其他函数的情况下，使用函数原型无疑是更好的选择。（书中也是这样讲解的，完全没有提及第二种方法）

- main() 函数中 return 0 的作用：
  - 计算机的操作系统可以看做调用程序，因此 main() 的返回值不是返回给程序中的其他部分，而是返回给操作系统。操作系统测试程序的返回值（通常被称为退出值），退出值为0则认为程序成功，非0则认为程序存在问题。

## Chapter3
### Section1
- 对类型名使用sizeof运算符时，应将名称放在括号中，但是对变量名使用sizeof运算符则括号可加可不加。
- \<climits\>中的符号常量，实际就是将如INT_MIN, INT_MAX用对应的数值替换，使用的是\#define，便于C和C++同时使用。
- C++本身并不提供自动防止超出整型限制的功能，需要使用头文件\<climits\>。
- unsigned是无符号变体，可以增加变量能够储存的最大值，但是仅适用于非负数据。如short保存-32768到32767，但是unsigned short可以保存0-65535。
- C++中，单引号用于*字符*，双引号用于*字符串*。
### Section2
- const定义常量时，常量名推荐使用全部大写，同时不要使用\#define进行定义，因为const可以对常量作用域有更好的限制。
### Section3
- **float只保证6位精度，超过6位会导致精度丢失，浮点常量在默认情况下为double类型。**

## Chapter4
### Section1
- 只有在定义数组时才能使用\{\}数组初始化，此后就不能使用，用时也不能将一个数组赋值给另一个数组。
### Section2
- cin的基础特性中，会识别输入的第一个单词，随后在结尾处加入空白。因此，后续输入的内容会被放入输入队列中，这会直接影响下一次输入时的状态。
  - 在Chapter2 Section3中遇到的cin.get()的问题，在此得到解决。即不定义char array时，cin.get()仅会读取一个字符，而使用cin.get(name, ArSize)时，编译器会读取一个字符串放入数组中。
- \<cstring\>头文件提供了标准C语言库的字符串函数，用来处理字符数组。而\<string\>头文件则定义了string类。
### Section4
- 结构中的位字段（4.4.6）存疑
### Section5
- 共用体 (union) 可以存储多个数据结构，但是在任一时刻只能存储一种数据结构。这种互斥的方式可以节省内存。
- 共用体衍生出匿名共用体 (anonymous union)，匿名共用体直接取消了名称，这样这个共用体的所有成员存放在内存的相同地址处，显然，每次只能有一个成员是共用体的成员。