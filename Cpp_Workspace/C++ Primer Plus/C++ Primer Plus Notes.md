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
    - [Section6](#section6)
    - [Section7](#section7)
    - [Section8](#section8)
    - [Section10](#section10)
  - [Chapter5](#chapter5)

# C++ Primer Plus (6th Edition) Notes
## Chapter2
### Section 3
- cin:
cin和cin.get()等存在区别，cin.get()无法读取数字，如果使用cin.get()并在terminal中输入int等会出现数值错误。
### Section 4
- **C++程序中应当为程序中使用的每个函数提供原型 (Function Prototype)。**
  - 由于在使用函数前，C++编译器必须知道函数的参数类型和返回值类型，因此需要使用函数原型语句显性地声明。函数原型之于函数相当于变量声明之于变量。
  - 应在首次使用函数之前提供其原型。通常的做法是把原型放到main()函数定义的前面。
  - 如果没有函数原型放在main()函数前为编译器提供必要的信息，则必须将整个函数的定义语句放在main()函数前。实际上这两种方式各有利弊。如果将main()函数放在最后，则需要对整个C++程序中使用的函数组织正确的顺序。在一个程序中包含许多函数，同时这些函数又调用其他函数的情况下，使用函数原型无疑是更好的选择。（书中也是这样讲解的，完全没有提及第二种方法）

- main()函数中return 0的作用：
  - 计算机的操作系统可以看做调用程序，因此main()的返回值不是返回给程序中的其他部分，而是返回给操作系统。操作系统测试程序的返回值（通常被称为退出值），退出值为0则认为程序成功，非0则认为程序存在问题。

## Chapter3
### Section1
- 对类型名使用sizeof运算符时，应将名称放在括号中，但是对变量名使用sizeof运算符则括号可加可不加。
- \<climits\>中的符号常量，实际就是将如INT_MIN, INT_MAX用对应的数值替换，使用的是\#define，便于C和C++同时使用。
- C++本身并不提供自动防止超出整型限制的功能，需要使用头文件\<climits\>。
- unsigned是无符号变体，可以增加变量能够储存的最大值，但是仅适用于非负数据。如short保存-32768到32767，但是unsigned short可以保存0-65535。
- C++中，单引号用于字符，双引号用于字符串。
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
- *结构中的位字段（4.4.6）存疑*
### Section5
- 共用体 (union) 可以存储多个数据结构，但是在任一时刻只能存储一种数据结构。这种互斥的方式可以节省内存。
- 共用体衍生出匿名共用体 (anonymous union)，匿名共用体直接取消了名称，这样这个共用体的所有成员存放在内存的相同地址处，显然，每次只能有一个成员是共用体的成员。
### Section6
- *暂时还不能理解枚举的意义*
### Section7
- **指针！ 指针是一个变量，指向的是其储存值的地址！**
- **一定要在对指针应用解除引用运算符\*之前，将指针初始化为一个确定的，适当的地址！**
- 使用delete释放内存，但是不会删除指针本身。**一定要配对使用new和delete，否则将会发生内存泄漏**，也就是说被分配的内存再也无法使用。如果内存泄漏严重，则程序将由于不断寻找更多内存而终止。
- 不要对delete过的内存再次delete，这样会导致不确定的后果。同时，不能用delete释放声明变量时获得的内存。
  ```c++
  int * ps = new int; // ok
  delete ps; // ok
  delete ps; // not ok for now
  int jugs = 5; // ok
  int * pi = &jugs; // ok
  delete pi; // not allowed, memory not allocated by new
  ```
- 如果通过声明来创建数组，则程序被编译时会为数组分配内存。无论程序最终是否使用数组，都会占用已声明的内存。在编译时给数组分配内存被成为静态联编（static binding）。但使用new时，如果在运行阶段需要数组，则创建它，如果不需要，则不创建。还可在程序运行时选择数组的长度。这种方法为成为动态联编（dynamic binding）。
- 使用new和delete时，应遵循以下规则：
  1. 不要使用delete来释放不是new分配的内存
  2. 不要使用delete释放同一个内存两次
  3. 如果使用new\[\]为数组分配内存，则应使用delete\[\]来释放
  4. 如果使用new为实体分配内存，则应使用delete来释放 
  5. 对空指针使用delete是安全的
- 数组名和指针间的根本差别在于：数组名的值是不能修改的，但是指针是一个变量，因此可以修改指针的值。
  ```c++ 
  p3 = p3 + 1; // okay for pointers, wrong for array names
  ```
### Section8
- 指针小结
  1. 声明指针
    ```c++
    typeName * pointerName; 
    // for example:
    double * pn; // pn can point to a double value
    char * pc; // pc can point to a char value
    ```
  2. 给指针赋值应将内存地址赋给指针，可以对变量名应用\&运算符，来获得被命名的内存的地址，new运算符返回未命名的内存地址
    ```c++
    double * pn; // pn can point to a double value
    double * pa; // pa can point to a double value
    char * pc; // pc can point to a char value
    double bubble = 3.2;
    pn = &bubble; // assign address of bubble to pn
    pc = new char; // assign address of newly allocated char memory to pc
    pa = new double[30]; // assign address of 1st element of array of 30 double to pa
    ```
  3. 对指针解除引用意味着获得指针指向的值。对指针应用解除引用或间接值运算符\(\*\)来解除引用。因此，如果像上面的例子一样，pn是指向bubble的指针，则\*pn是指向的值。
    ```c++
    cout << *pn; // print the value of bubble
    *pc = 'S'; // place 's' into the memory location whose address is pc
    ```
  4. 区分指针和指针所指向的值。如果pt是指向int的指针，则\*pt不是指向int的指针，而是完全等同于一个int类型的变量。pt才是指针。
    ```c++
    int * pt = new int; // asssigns an address to the pointer pt
    *pt = 5; // store the value 5 at that address
    ```
  5. 多数情况下，C++将数组名视为数组的第一个元素的地址。一种例外的情况是，将sizeof运算符用于数组名时，此时将返回整个数组的长度（单位为字节）。
    ```c++
    int tacos[10]; // now tacos is the same as &tacos[0]
    ```
  6. 指针算数。C++允许将指针和整数想家，加1的结果等于原来的地址值加上指向的对象占用的总字节数。还可以将一个指针减去另一个指针，获得两个指针的差。后一种运算将得到一个整数，仅当两个指针指向同一个数组（也可以指向超出结尾的一个位置）时，这种运算才有意义：这将得到两个元素的间隔。
    ```c++
    int tacos[10] = {5,2,8,4,1,2,2,3,6,8};
    int * pt = tacos; // suppose pt and tacos are the address 3000
    pt = pt + 1; // now pt is 3004 if a int is 4 bytes
    int *pe = &tacos[9]; // pe is 3036 if an int is 4 bytes
    pe = pe - 1; // now pe is 3032, the address of tacos[8]
    int diff = pe - pt; // diff is 7, the separation betweent tacos[8] and tacos[1]
    ```
  7. 数组的动态联编和静态联编。使用数组声明来创建数组时，将采用静态联编，即数组的长度在编译时设置；使用new\[\]运算符创建数组时，将采用动态联编（动态数组），即将在运行时为数组分配空间，其长度也将在运行时设置。使用完这种数组后，应使用delete\[\]释放其内存。
    ```c++
    int tacos[10]; // static binding ,size fixed at compile time
    int size;
    cin >> size; 
    int * pz = new int [size]; // dynamic binding, size set at run time
    ...
    delete [] pz; // free memory when finished
    ```
  8. 数组表示法和指针表示法。使用方括号数组表示法等同于对指针的解除引用。数组名和指针变量都是如此，因此对于指针和数组名，既可以使用指针表示法，也可以使用数组表示法。
    ```c++
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
  1. 在将字符串读入程序时，应使用已分配的内存地址。该地址可以是数组名，也可以是使用new初始化过的指针。
  2. 应使用strcpy()或strncpy()，而不是使用赋值运算符来将字符串赋给数组。
- 在运行时创建数组优于在编译时创建数组，对于结构也是如此
- **如果结构标识符是结构名，则使用句点运算符，如果标识符是指向结构的指针，则使用箭头运算符。**
### Section10
- vector
  ```c++
  #include <vector>
  ...
  using namespace std; // create a zero-size array of int
  int n;
  cin >> n;
  vector<double> vd(n); // create an array of n doubles
  // vector<typeName> vt(n_elem);
  ```
- array 
  ```c++
  #include<array>
  ...
  using namespace std;
  array<int, 5> ai; // create array object of 5 ints
  array<double ,4> ad = {1.2, 2.1, 3.43, 4.3};
  // array<typeName, n_elem> arr;
  ```
## Chapter5