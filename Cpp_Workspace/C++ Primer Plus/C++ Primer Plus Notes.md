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
- **如果结构标识符是结构名，则使用句点运算符，如果标识符是指向结构的指针，则使用箭头运算符。**

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