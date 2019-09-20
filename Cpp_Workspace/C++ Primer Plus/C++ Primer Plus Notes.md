- [C++ Primer Plus (6th Edition) Notes](#c-primer-plus-6th-edition-notes)
  - [Chapter2](#chapter2)
    - [Section 3](#section-3)
    - [Section 4](#section-4)
  - [Chapter3](#chapter3)
    - [Section1](#section1)

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
- unsigned是无符号变体，可以增加变量能够储存的最大值，但是仅适用于非负数据。如short保存-32768到32767，但是unsigned short可以保存0-65535。