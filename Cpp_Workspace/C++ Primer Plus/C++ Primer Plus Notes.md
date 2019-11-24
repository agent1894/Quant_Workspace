- [C++ Primer Plus (6th Edition) Notes](#c-primer-plus-6th-edition-notes)
  - [Chapter2 开始学习C++](#chapter2-%e5%bc%80%e5%a7%8b%e5%ad%a6%e4%b9%a0c)
    - [Section 4 函数](#section-4-%e5%87%bd%e6%95%b0)
  - [Chapter3 处理数据](#chapter3-%e5%a4%84%e7%90%86%e6%95%b0%e6%8d%ae)
    - [Section1 简单变量](#section1-%e7%ae%80%e5%8d%95%e5%8f%98%e9%87%8f)
    - [Section2 const限定符](#section2-const%e9%99%90%e5%ae%9a%e7%ac%a6)
    - [Section3 浮点数](#section3-%e6%b5%ae%e7%82%b9%e6%95%b0)
  - [Chapter4 复合类型](#chapter4-%e5%a4%8d%e5%90%88%e7%b1%bb%e5%9e%8b)
    - [Section1 数组](#section1-%e6%95%b0%e7%bb%84)
    - [Section2 字符串](#section2-%e5%ad%97%e7%ac%a6%e4%b8%b2)
    - [Section3 string类简介](#section3-string%e7%b1%bb%e7%ae%80%e4%bb%8b)
    - [Section4 结构简介](#section4-%e7%bb%93%e6%9e%84%e7%ae%80%e4%bb%8b)
    - [Section5 共用体](#section5-%e5%85%b1%e7%94%a8%e4%bd%93)
    - [Section6 枚举](#section6-%e6%9e%9a%e4%b8%be)
    - [Section7 指针和自由存储空间](#section7-%e6%8c%87%e9%92%88%e5%92%8c%e8%87%aa%e7%94%b1%e5%ad%98%e5%82%a8%e7%a9%ba%e9%97%b4)
    - [Section8 指针、数组和指针算数](#section8-%e6%8c%87%e9%92%88%e6%95%b0%e7%bb%84%e5%92%8c%e6%8c%87%e9%92%88%e7%ae%97%e6%95%b0)
    - [Section10 数组的替代品](#section10-%e6%95%b0%e7%bb%84%e7%9a%84%e6%9b%bf%e4%bb%a3%e5%93%81)
  - [Chapter5 循环和关系表达式](#chapter5-%e5%be%aa%e7%8e%af%e5%92%8c%e5%85%b3%e7%b3%bb%e8%a1%a8%e8%be%be%e5%bc%8f)
    - [Section1 for循环](#section1-for%e5%be%aa%e7%8e%af)
    - [Section2 while循环](#section2-while%e5%be%aa%e7%8e%af)
    - [Section3 do while循环](#section3-do-while%e5%be%aa%e7%8e%af)
    - [Section4 基于范围的for循环（C++11）](#section4-%e5%9f%ba%e4%ba%8e%e8%8c%83%e5%9b%b4%e7%9a%84for%e5%be%aa%e7%8e%afc11)
    - [Section5 循环和文本输入](#section5-%e5%be%aa%e7%8e%af%e5%92%8c%e6%96%87%e6%9c%ac%e8%be%93%e5%85%a5)
    - [Section6 嵌套循环和二维数组](#section6-%e5%b5%8c%e5%a5%97%e5%be%aa%e7%8e%af%e5%92%8c%e4%ba%8c%e7%bb%b4%e6%95%b0%e7%bb%84)
  - [Chapter6 分支语句和逻辑运算符](#chapter6-%e5%88%86%e6%94%af%e8%af%ad%e5%8f%a5%e5%92%8c%e9%80%bb%e8%be%91%e8%bf%90%e7%ae%97%e7%ac%a6)
    - [Section1 if语句](#section1-if%e8%af%ad%e5%8f%a5)
    - [Section2 逻辑表达式](#section2-%e9%80%bb%e8%be%91%e8%a1%a8%e8%be%be%e5%bc%8f)
    - [Section3 字符函数库cctype](#section3-%e5%ad%97%e7%ac%a6%e5%87%bd%e6%95%b0%e5%ba%93cctype)
    - [Section4 ?:运算符](#section4-%e8%bf%90%e7%ae%97%e7%ac%a6)
    - [Section5 switch语句](#section5-switch%e8%af%ad%e5%8f%a5)
    - [Section6 break和continue语句](#section6-break%e5%92%8ccontinue%e8%af%ad%e5%8f%a5)
    - [Seciton7 读取数字的循环](#seciton7-%e8%af%bb%e5%8f%96%e6%95%b0%e5%ad%97%e7%9a%84%e5%be%aa%e7%8e%af)
    - [Section8 简单文件输入/输出](#section8-%e7%ae%80%e5%8d%95%e6%96%87%e4%bb%b6%e8%be%93%e5%85%a5%e8%be%93%e5%87%ba)
  - [Chapter7 函数——C++的编程模块](#chapter7-%e5%87%bd%e6%95%b0c%e7%9a%84%e7%bc%96%e7%a8%8b%e6%a8%a1%e5%9d%97)
    - [Section1 复习函数的基本知识](#section1-%e5%a4%8d%e4%b9%a0%e5%87%bd%e6%95%b0%e7%9a%84%e5%9f%ba%e6%9c%ac%e7%9f%a5%e8%af%86)
    - [Section2 函数参数和按值传递](#section2-%e5%87%bd%e6%95%b0%e5%8f%82%e6%95%b0%e5%92%8c%e6%8c%89%e5%80%bc%e4%bc%a0%e9%80%92)
    - [Section3 函数和数组](#section3-%e5%87%bd%e6%95%b0%e5%92%8c%e6%95%b0%e7%bb%84)
    - [Section4 函数和二维数组](#section4-%e5%87%bd%e6%95%b0%e5%92%8c%e4%ba%8c%e7%bb%b4%e6%95%b0%e7%bb%84)
    - [Section5 函数和C-风格字符串](#section5-%e5%87%bd%e6%95%b0%e5%92%8cc-%e9%a3%8e%e6%a0%bc%e5%ad%97%e7%ac%a6%e4%b8%b2)
    - [Section10 函数指针](#section10-%e5%87%bd%e6%95%b0%e6%8c%87%e9%92%88)
  - [Chapter8 函数探幽](#chapter8-%e5%87%bd%e6%95%b0%e6%8e%a2%e5%b9%bd)
    - [Section1 C++内联函数](#section1-c%e5%86%85%e8%81%94%e5%87%bd%e6%95%b0)
    - [Section2 引用变量](#section2-%e5%bc%95%e7%94%a8%e5%8f%98%e9%87%8f)

# C++ Primer Plus (6th Edition) Notes

## Chapter2 开始学习C++

### Section 4 函数
- **C++程序中应当为程序中使用的每个函数提供原型 (Function Prototype)。**
  - 由于在使用函数前，C++编译器必须知道函数的参数类型和返回值类型，因此需要使用函数原型语句显性地声明。函数原型之于函数相当于变量声明之于变量。
  - 应在首次使用函数之前提供其原型。通常的做法是把原型放到main()函数定义的前面。
  - 如果没有函数原型放在main()函数前为编译器提供必要的信息，则必须将整个函数的定义语句放在main()函数前。实际上这两种方式各有利弊。如果将main()函数放在最后，则需要对整个C++程序中使用的函数组织正确的顺序。在一个程序中包含许多函数，同时这些函数又调用其他函数的情况下，使用函数原型无疑是更好的选择。（书中也是这样讲解的，完全没有提及第二种方法）

- main()函数中return 0的作用：
  - 计算机的操作系统可以看做调用程序，因此main()的返回值不是返回给程序中的其他部分，而是返回给操作系统。操作系统测试程序的返回值（通常被称为退出值），退出值为0则认为程序成功，非0则认为程序存在问题。

## Chapter3 处理数据

### Section1 简单变量
- 对类型名使用sizeof运算符时，应将名称放在括号中，但是对变量名使用sizeof运算符则括号可加可不加。
- \<climits\>中的符号常量，实际就是将如INT_MIN, INT_MAX用对应的数值替换，使用的是\#define，便于C和C++同时使用。
- C++本身并不提供自动防止超出整型限制的功能，需要使用头文件\<climits\>。
- unsigned是无符号变体，可以增加变量能够储存的最大值，但是仅适用于非负数据。如short保存-32768到32767，但是unsigned short可以保存0-65535。
- C++中，单引号用于字符，双引号用于字符串。

### Section2 const限定符
- const定义常量时，常量名推荐使用全部大写，同时不要使用\#define进行定义，因为const可以对常量作用域有更好的限制。

### Section3 浮点数
- **float只保证6位精度，超过6位会导致精度丢失，浮点常量在默认情况下为double类型。**

## Chapter4 复合类型

### Section1 数组
- 只有在定义数组时才能使用\{\}数组初始化，此后就不能使用，用时也不能将一个数组赋值给另一个数组。

### Section2 字符串
- cin的基础特性中，会识别输入的第一个单词，随后在结尾处加入空白。因此，后续输入的内容会被放入输入队列中，这会直接影响下一次输入时的状态。
  - 在Chapter2 Section3中遇到的cin.get()的问题，在此得到解决。即不定义char array时，cin.get()仅会读取一个字符，而使用cin.get(name, ArSize)时，编译器会读取一个字符串放入数组中。

### Section3 string类简介
- \<cstring\>头文件提供了标准C语言库的字符串函数，用来处理字符数组。而\<string\>头文件则定义了string类。

### Section4 结构简介
- *结构中的位字段（4.4.6）存疑*

### Section5 共用体
- 共用体 (union) 可以存储多个数据结构，但是在任一时刻只能存储一种数据结构。这种互斥的方式可以节省内存。
- 共用体衍生出匿名共用体 (anonymous union)，匿名共用体直接取消了名称，这样这个共用体的所有成员存放在内存的相同地址处，显然，每次只能有一个成员是共用体的成员。

### Section6 枚举
- *暂时还不能理解枚举的意义*

### Section7 指针和自由存储空间
- **指针是一个变量，指向的是其储存值的地址。**
- **一定要在对指针应用解除引用运算符\*之前，将指针初始化为一个确定的，适当的地址。**
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

### Section8 指针、数组和指针算数
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
  6. 指针算数。C++允许将指针和整数相加，加1的结果等于原来的地址值加上指向的对象占用的总字节数。还可以将一个指针减去另一个指针，获得两个指针的差。后一种运算将得到一个整数，仅当两个指针指向同一个数组（也可以指向超出结尾的一个位置）时，这种运算才有意义：这将得到两个元素的间隔。
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
    int tacos[10]; // static binding, size fixed at compile time
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
- **当创建动态结构时，不能将成员运算符句点用于结构名，因为这个结构没有名称，只知道对应的地址。如果结构标识符是结构名，则使用句点运算符，如果标识符是指向结构的指针，则使用箭头成员运算符(->)。**如果ps是一个指针，指向一个结构struct，那么ps->member即为指向struct的member成员。

### Section10 数组的替代品
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

## Chapter5 循环和关系表达式

### Section1 for循环
- for循环的组成：循环只进行一次初始化；test-expression（测试表达式）决定循环体是否被执行，通常，这个表达式是关系表达式，即对两个值进行比较；**update-expression（更新表达式）在每轮循环结束时执行，此时循环体已经执行完毕**。通常，它用来对跟踪循环轮次的变量的值进行增减。
  ```c++
  for (initialization; test-expression; update-expression)
    body
  ```
- C++常用的方式是，在for和括号之间加上一个空格，而省略函数名与括号之间的空格。
- cout在显示bool值之前将其转换为int，但cout.setf(ios::boolalpha)函数调用设置了一个标记，该标记命令cout显示true和false，而不是1和0。
- ++x和x++并不相同。x++意味着使用x的当前值计算表达式，然后将x的值加一；而++x的意思是先将x的值加一，然后使用新的值计算表达式。
  ```c++
  int x = 5;
  int y = ++x; // change x, then assign to y, y is 6, x is 6

  int z = 5;
  int y = z++; // assign to y, then change z, y is 5, z is 6
  ```
- 副作用（side effect）和顺序点（sequence point）
  1. 副作用是指在计算表达式时对某些东西（如存储在变量中的值）进行了修改
  2. 顺序点是指程序执行过程中的一个点，在这里，进入下一步之前将确保对所有的副作用都进行了评估。在C++中，语句中的分号就是一个顺序点，这意味着程序处理下一条语句之前，赋值运算符、递增运算符和递减运算符执行的所有修改都必须完成。
  3. 显然如果变量被用于某些目的，如用作函数参数或给变量赋值，使用前缀格式（++x）和后缀格式（x++）的结果将不同。然而，如果递增表达式的值没有被使用，情况则有所不同。在如下例子中，尽管在逻辑上，使用前缀格式和后缀格式没有任何区别，表达式的值没有使用，因此只存在副作用，而将x加一和n减一的副作用将在程序进入下一步之前完成，前缀格式和后缀格式的最终效果相同。然而，尽管使用前缀格式和后缀格式对程序的行为没有影响，但是执行速度上会有细微的差别。对于一个类来说，前缀函数将值加一然后返回，而后缀函数首先复制一个副本，将其加一，然后将复制的副本返回。因此，对于类而言，前缀版本的效率比后缀版本高。
    ```c++
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
- \{\}语句块允许把两条或更多条语句放到按C++句法只能放一条语句的地方，逗号运算符对表达式完成同样的任务，允许将两个表达式放到C++句法只允许放一个表达式的地方。同时，C++为逗号运算符提供了额外的两个特性：首先确保先计算第一个表达式，然后计算第二个表达式，（换句话说，逗号运算符式一个是顺序点）。因此，形如以下的代码是安全的。其次，逗号表达式的值是第二部分的值。
  ```c++
  i = 20, j = 2 * i // i set to 20, then j set to 40, the expression is 40
  ```
- 比较C-字符串，应当使用C-风格字符串库中的strcmp()函数来比较。该函数接受两个字符串地址作为参数，这意味着参数可以是指针、字符串常量或字符串数组名。如果两个字符串相同，该函数将返回零；如果第一个字符串按字母顺序排在第二个字符串之前，则strcmp()将返回一个负数值；如果第一个字符串按字母顺序排在第二个字符串之后，则strcmp()将返回一个正数值。注意此处字符是根据字符的系统编码进行比较的。如果使用ASCII码时，所有大写字母的编码都比小写字母小，所以大写字母将位于小写字母之前，同时这也意味着大小写是敏感的。

### Section2 while循环
- while循环是没有初始化和更新部分的for循环，它只有测试条件和循环体。 
  ```c++
  while (test-condition)
    body
  ```
- 标点符号的使用要特别注意。分号结束一个语句，而for或while为一个完整的语句，下面提供了一个错误的示例。由于错误的使用了分号，会导致花括号内的代码位于循环后，永远不会被执行，构成了一个死循环。
  ```c++
  i = 0;
  while (name[i] != '\0'); // problem semicolon
  {
    cout << name[i] << endl;
    i++;
  }
  cout << "Done" << endl;
  ```
- 延迟循环：使用头文件\<ctime\>实现，其中定义了符号常量CLOCKS_PER_SEC，该常量等于每秒钟包含的系统时间单位数。因此，将系统时间（函数clock()）除以这个值，可以得到秒数，或将秒数乘以这个值，可以得到以系统时间单位为单位的时间。同时\<ctime\>将clock_t作为clock()返回类型的别名，因此可以将变量声明为clock_t类型，从而避免不同的系统或编译器对clock()函数返回值的类型的差异。
- 类型别名：C++为类型建立别名的方式有两种，一种是使用预处理器\#define，这种方式书中并不推荐，包括在定义const常量时（可能是为了和C的语法做出一定的区别，并体现出C++的特性？）。另一种则是使用C++（和C）的关键字typedef来创建别名。typedef不会创建新类型，而只是为已有的类型建立一个新名称。typedef的通用格式为：
  ```c++
  typedef typeName aliasName;
  ```

### Section3 do while循环
- do while循环不同于for循环和while循环，do while时出口条件（exit condition）循环，即这种循环将**首先执行循环体，在判定测试表达式，因此这样的循环通常至少执行一次**。其语法结构为：
  ```c++
  do
    body
  while (test_expression);
  ```

### Section4 基于范围的for循环（C++11）
- 基于范围（range-based）的for循环是C++11新增的新特性，使对数组的每个元素执行相同操作的循环成为可能。
- 会在模板容器类中做详细讨论

### Section5 循环和文本输入
- cin在读取char值时，会忽略空格和换行符，因此显示时不会显示空格，也不会对空格进行计数。
- 为了修正上述问题，会使用cin.get(char)函数，成员函数cin.get(char)读取输入中的下一个字符（即使是空格），并将其赋值给变量。
- **函数重载是C++的特性，允许创建多个同名函数，条件是参数列表不同**。在书中的案例中，cin.get(name, ArSize)会使编译器找到使用char*和int作为参数的cin.get()的版本；如果使用cin.get(ch)，则编译器将使用接受一个char参数的版本；如果没有提供参数，则编译器将使用不接受任何参数的cin.get()的版本。
- 检测文件尾（EOF）作为一种功能更加强大的技术，可以更好的协同输入和操作系统。
  1. 操作系统支持重定向，因此程序可以从文件而非键盘获取输入，常用的重定向符为\<
  2. 操作系统同样支持通过键盘模拟文件尾。在Unix中为\<CTRL\>+\<D\>，在Windows和Linux中通常是\<CTRL\>+\<Z\>+\<ENTER\>

  如果变成环境支持EOF，则可以使用键盘输入模拟EOF。如果检测到EOF，cin.eof()或cin.fail()会返回bool值true，否则返回false（cin.fail()比cin.eof()可用于更多的实现中）。

### Section6 嵌套循环和二维数组
- C++没有提供二维数组类型。

## Chapter6 分支语句和逻辑运算符

### Section1 if语句
- 从语法上看，整个if else结构被视为一条语句。
- if else if else结构，看似是一种新的结构，实际上是由于C++的自由格式允许将这些元素排列成便于阅读的格式。它只是一个if else被包含在另一个if else中。 

### Section2 逻辑表达式
- 逻辑运算符：
  1. OR: ||
  2. AND: &&
  3. NOT: !
- C++规定，||和&&运算符是个顺序点（sequence point），也就是说，先修改左侧的值，再对右侧的值进行判定（C++11的说法是，运算符左边的子表达式先于右边的子表达式）。举例如下：
  ```c++
  i++ < 6||i == j
  ```

  假设原来的值为10，则在对i和j进行比较时，i的值将为11。
- 取值范围测试的每一部分都使用AND运算符将两个完整的关系表达式组合起来，**不要使用数学符号** 
  ```c++
  if (age > 17 && age < 35) // OK
  if (17 < age < 35) // Don't do this!
  ```

  **编译器不会捕获这种错误，因为这是有效的C++语法。**\<运算符从左向右结合，因此上述表达式的含义为：
  ```c++
  if ( (17 < age) < 35)
  ```

  **但17\<age的值要么为true(1)，要么为false(0)。不管是那种情况，表达式17\<age的值都小于35，因此整个测试的结果总是true!**
- C++逻辑OR(||)和逻辑AND(&&)运算符的优先级都低于关系运算符，但是NOT(!)运算符的优先级高于所有的关系运算符和算术运算符，但是**逻辑AND运算符的优先级高于逻辑OR运算符**。
- C++可以使用and or not替代&& || !

### Section3 字符函数库cctype
- \<cctype\>类库提供了对分析字符串更好的方式。

### Section4 ?:运算符
- ?:运算符类似于Python中的三元表达式。

### Section5 switch语句
- switch语句的通用格式：
  ```c++
  switch (integer-expression)
  {
    case label1 : statement(s)
    case label2 : statement(s)
    ...
    default : statement(s)
  }
  ```
- **integer expression 必须是一个结果为整数值的表达式，每个标签都必须是整数常量表达式。最常见的标签是int或char常量，也可以是枚举量。**
- **C++中的case标签只是行标签，而不是选项之间的界线。当程序跳到switch中特定代码行后，将依次执行之后的所有语句，除非有明确的其他知识。程序不会在执行到下一个case处自动停止，要让程序执行完以组特定语句后停止，必须使用break语句。**
- switch中的每一个case标签都必须是一个单独的值，且必须是整数（包括char），因此switch无法处理浮点测试。
- 如果所有的选项都可以用整数常量来标识，则可以使用switch语句或if else语句。如果既可以使用if else if语句，也可以使用switch语句，则当选项不少于3个时，应使用switch语句（代码长度和执行速度上，switch语句效率更高）。 

### Section6 break和continue语句
- continue跳过循环体剩余的部分，开始新一轮循环。
- break跳过循环的剩余部分，到达下一条语句。 
- continue语句会跳过循环体的剩余部分，但不会跳过循环的更新表达式。

### Seciton7 读取数字的循环
- 输入错误和EOF都会导致cin返回false，这给使用非数字输入结束读取数字循环提供了方法。
- 需要使用cin.clear()对输入进行重置。

### Section8 简单文件输入/输出
- 文件输出和控制台输出非常类似：
  - 控制台输出（cout）：
    - 必须包含头文件iostream
    - 头文件iostream定义了一个用于处理输出的ostream类
    - 头文件iostream声明了一个名为cout的ostream变量（对象）
    - 使用命名空间std::
  - 文件输出：
    - 必须包含头文件fstream
    - 头文件fstream定义了一个用于处理输出的ofstream类
    - 需要声明一个或多个ofstream变量（对象）
    - 使用命名空间std::
    - 需要将ofstream对象与文件关联，方法之一是使用open()方法
    - 使用完文件后应使用方法close()将其关闭
  - 需要注意的是，iostream提供了预先定义好名为cout的ostream对象，但是在文件输出时，必须自己声明ofstream对象。
  - **打开已有的文件以接受输出时，默认将原文件清空。**
- 文件输入和控制台输入的关系与文件输出和控制台输出的关系非常类似。
  - cstdlib头文件定义了一个用于同操作系统通信的参数值EXIT_FAILURE。
  - 由于方法good()指出读取输入的操作是否成功，因此，应该在执行读取输入的操作后立刻使用good()进行测试。在sumafile.cpp中，使用的方法是先放置一条输入语句，然后在循环的末尾在放置另一条输入语句，即：
    ```c++
    // standard file-reading loop design
    inFile >> value; // get first value
    while (inFile.good()) // while input good and not at EOF
    {
        // loop body goes here
        inFile >> value; // get next value
    }
    ```

    但是实际上，表达式inFile>>value的结果为inFile，而在需要一个bool值的情况下，inFile的结果为inFile.good()，即true or false。因此，上述代码可以精简为：
    ```c++
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
- 在编译阶段进行的原型化被称为静态类型检查（static type checking）。静态类型检查可以捕获许多在运行阶段难以捕获的错误。

### Section2 函数参数和按值传递
- 用于接收传递值的变量被称为形参，C++标准又称为参量（parameter），传递给函数的值被称为实参，C++标准又称为参数（argument）。
- 7.4 lotto.cpp中，计算中奖概率使用了组合$C_n^m=\frac{A_n^m}{m!}=\frac{n!}{m!(n-m)!}$。书中提出，这种计算不应当先计算出所有的分母，所有的分子，然后相除，因为这回导致计算过程中的中间值过大，应当每次计算一组分母除以分子，然后将所有中间值相乘，即$\frac{10}{2}\times\frac{9}{1}$好于$\frac{10\times9}{2\times1}$。

### Section3 函数和数组
- **当且仅当在函数头或函数原型中，int \* arr 和 int arr []有相同的含义，都表示arr是一个int指针**。
  ```c++
  arr[i] == *(ar + i) // values in two notations
  &arr[i] == ar + i // addresses in two notations
  ```

- **如果需要将数组类型和元素数量告诉数组处理函数，必须通过两个不同的参数来传递，而不能使用方括号表示法传递数组长度。**
  ```c++
  void fillArray(int arr[], int size); // prototype
  void fillArray(int arr[size]); // NO -- bad prototype
  ```

- 使用普通参数时，由于C++按值传递数据，并且函数使用数据的副本，因此传递的参数能够得到自动保护不被修改，但是，在接受数组名的函数中，使用的是原始数据，因此，对传入参数的保护就显得比较重要。在函数头声明形参时使用const可以起到这个效果。注意，这里的const不代表传入的参数必须是常量，只是说在这个函数中，这个参数不能被修改。
- 指针和const：有两种方式将const关键字用于指针
  - **指针指向一个常量对象**，这样可以防止使用该指针来修改所指向的值。
  - **将指针本身声明为常量**，这样可以防止改变指针指向的位置。

  首先声明一个指向常量的指针pt：
  ```c++
  int age = 39;
  const int * pt = &age;
  ```
  该声明指出pt指向一个const int（例中为39）（写作(const int)* pt可能更好理解），因此**不能使用pt来修改这个值**。换句话说，**\*pt的值为const，不能被修改。**
  ```c++
  *pt += 1; // INVALID because pt points to a const int
  cin >> *pt; // INVALID for the same reason
  ```
  但是，pt的声明不意味着它指向的值是常量，只是意味着对pt而言，这个值是常量。因此，可以通过修改age变量来修改age的值，但是不能通过pt指针来修改age的值。
  ```c++
  *pt = 20; // INVALID because pt points to a const int
  age = 20; // VALID because age is not declared to be const
  ```
  到此为止，已经讨论了将常规变量的地址赋给常规指针，上例则将常规变量的地址赋给指向const的指针。显然，还有两种可能，将const变量的地址赋给指向const的指针和将const变量的地址赋给常规指针。前一种可行而后一种不可行。
  ```c++
  const float g_earth = 9.80;
  const float * pe = &g_earth; // VALID

  const float g_moon = 1.63;
  float * pm = &g_moon; // INVALID
  ```
  前一种情况表明无论是通过变量还是通过指针都不能修改变量的值。后一种不被允许的原因在于：如果可以通过指针修改变量的值，那就和变量本身const冲突。

### Section4 函数和二维数组
- 如果将二维数组作为函数的参数，首先需要记住数组名被视为地址，因此，相应的形参是一个指针。
- **注意**
  ```c++
  int (*ar2)[4]; // 指向4个int组成数组的指针
  int *ar2 [4]; // 4个指向int指针组成的数组， 其实写成int* ar2 [4];会更好理解。int*说明ar2是指针
  ```

  *同样，在使用const时仍有困惑*

### Section5 函数和C-风格字符串
- C-风格字符串由一系列字符组成，以空值字符结尾。
- 将字符串作为参数时意味传递的是地址。其中有三种表示字符串的方式：
  - char数组
  - 用引号括起的字符串常量（也称字符串字面值）
  - 被设置为字符串的地址的char指针
  
  但是这三种方法的类型都是char指针（即char*）。也就是说，虽然将字符串作为参数传递，但是实际上传递的是字符串第一个字符的地址。这意味着字符串函数原型应当将其表示字符串的形参声明为char*类型。
- C-风格字符串和常规char数组的一个重要区别在于：字符串有内置的结束字符（\0），即包含字符，但不以空值字符结尾的char数组只是数组，而不是字符串。
- ```c++
  // 7.9 strgfun.cpp
  char* wail = "ululate"; // wail points to string. 会收到编译器警告，ISO C++ 禁止string常量转换
  ```

### Section6 函数和结构
- 通常来说，使用结构编程时，像处理基本类型一样处理结构即可，即将结构作为参数传递，并在需要时将结构用返回值使用。按值传递会在函数中使用原始结构的副本。但是这种按值传递会有一个缺点：当结构很大时，复制结构会增加内存的需求，降低运行速度。因此，也可以使用传递结构的地址，然后使用指针访问结构的内容。C++提供按引用传递，这个在后面章节进行讨论。

### Section9 递归
- ```c++
  void recurs(argumentlist) 
  {
    statement1;
    if (test)
      recurs(arguments);
    statements2;
  }
  ```

  在这个递归函数中，只要if语句为true，每个recurs()调用都将执行statements1，然后再调用recurs()，而不会执行statements2.当if为false时，当前调用将执行statements2，然后程序控制权将返回调用它的recurs()，再执行statements2。因此，statements1会**按函数调用的顺序执行n次，而statements2将以与函数调用相反的顺序执行n次。**

### Section10 函数指针
- 获取函数的地址：使用函数名，并不跟参数即可。
  ```c++
  process(think); // passes address of think() to process()
  thought(think()); // passes return value of think() to thought()
  ```

- 声明函数指针：声明应指定函数的返回类型以及函数的特征标（参数列表），即声明应像函数原型那样指出有关函数的信息。**通常，要声明指向特定类型的函数的指针，可以首先编写这种函数的原型，然后用(\*pf)替换函数名，这样pf就是这类函数的指针。这里要额外注意运算符的优先级，必须在声明中使用括号将*pf括起。\*pf(int)意味着pf()是一个返回指针的函数，而(\*pf)(int)意味着pf是一个指向函数的指针。**
  ```c++
  double (*pf)(int); // pf points to a function that returns double
  double *pf(int); // pf() a function that returns a pointer-to-double
  ```

## Chapter8 函数探幽

### Section1 C++内联函数
- 对于常规函数，C++执行到函数调用指令时，程序将在函数调用后立刻储存该指令的内存地址，并将函数参数复制到堆栈，跳转至标记函数起点的内存单元，执行函数代码，如果有的话将返回值放入寄存器中，然后调回到地址被保存的指令处继续执行。这种在内存中反复跳跃的过程会产生一定的开销。对于内联函数，程序则无需跳转至另一个位置执行代码，再跳转回来，而是直接使用对应的函数代码替换了函数调用。因此，内联函数的运行速度比常规函数略快，但是会产生额外的内存消耗。
- 使用内联函数需要在函数声明前加关键字inline，或在函数定义前加关键字inline。
- 通常的做法是省略函数原型，将整个函数（函数头和所有函数代码）放在原先函数原型的位置。
- **内联函数不能递归**。

### Section2 引用变量
- 引用变量会和原始变量使用相同的值和内存单元。
- 引用变量使用\&进行创建，此处\&不代表地址运算符，而是类型标识符的一部分。
- **必须在声明引用变量时进行初始化。**
- 在按值传递的函数中，实参可以选择多种类型，但是如果将类似的参数传递给接受引用参数的函数，编译器将会进行更严格的限制。以书中8.5为例：
  ```c++
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

  显然，refcube接受ra作为一个变量的引用，那么实参应该是该变量，而不是一个表达式（x + 3.0）。
- 如果实参与引用参数不匹配，C++将生成临时变量。在当前，仅当参数为const引用时，C++才允许这种操作。
- 当引用参数是const，则编译器将在两种情况下生成临时变量：
  - 实参的类型正确，但不是左值
    - 可被引用的数据对象都是左值。如变量、数组元素、结构成员、引用和解除引用的指针等
    - 非左值包括字面变量和包含多项的表达式
    - 常规变量属于可修改的左值，而const变量属于不可修改的左值
  - 实参的类型不正确，但可以转换为正确的类型
  - C++11新增了右值引用（rvalue reference），这种引用使用\&\&指向右值。
  - 在示例8.6中：
    ```c++
    accumulate(dup, five) = four;
    ```

    这条语句将值赋给函数调用是可行的。因为accumulate()的返回值是一个引用。如果accumulate()按值返回，则不能通过编译。由于返回值是指向dup的引用，因此，这段代码等效于：
    ```c++
    accumulate(dup, five); // add five's data to dup
    dup = four; // overwrite the contents of dup with the contents of four
    ```
  - 传统的返回机制与按值传递函数参数类似：计算return后的表达式，并将结果返回给调用函数。也就是说，这个值被复制到一个临时位置，然后调用程序使用这个值。而在返回引用中，会使用不同的机制：
    ```c++
    dup = accumulate(team, five);
    ```

    如果accumulate()返回一个结构而不是指向结构的引用，则会把整个结构复制到一个临时位置，然后将这个拷贝复制给dup，但在返回引用时，直接将team复制到dup，提高了效率。因此，**返回引用的函数实际上是被引用的变量的别名**。
  - 在返回引用时注意变量的作用空间，避免返回函数终止时不再存在的内存单元的引用。同样，也应当避免返回指向临时变量的指针。为避免这种情况，示例8.6中返回了一个作为参数传递给函数的引用。作为参数的引用将指向调用函数使用的数据，因此返回的引用也将指向这些数据。另一种方法是用new来分配新的存储空间，用new分配内存空间后，返回指向该内存空间的指针。同样，可以使用引用完成类似的工作：
    ```c++
    const free_throws & clone(free_throws & ft)
    {
      free_throws * pt;
      *pt = ft; // copy info
      return *pt; // return reference to copy
    }
    ```

    在这段代码中，指针pt指向无名结构free_throws，因此\*pt就是该结构，但是函数声明表示函数会返回结构的引用，因此，可以这样使用该函数：
    ```c++
    free_throws & jolly = clone(three);
    ```

    这使得jolly成为新结构的应用。但是，这种方法隐藏的对new的调用，因此会容易导致忘记使用delete释放内存。