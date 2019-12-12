# Grokking Algorithms by Aditya Bhargava

- [Grokking Algorithms by Aditya Bhargava](#grokking-algorithms-by-aditya-bhargava)
  - [算法简介](#%e7%ae%97%e6%b3%95%e7%ae%80%e4%bb%8b)
    - [算法复杂度](#%e7%ae%97%e6%b3%95%e5%a4%8d%e6%9d%82%e5%ba%a6)
    - [二分查找（Binary Search）](#%e4%ba%8c%e5%88%86%e6%9f%a5%e6%89%bebinary-search)
  - [选择排序（Selection Sort）](#%e9%80%89%e6%8b%a9%e6%8e%92%e5%ba%8fselection-sort)
    - [数据结构：数组与链表](#%e6%95%b0%e6%8d%ae%e7%bb%93%e6%9e%84%e6%95%b0%e7%bb%84%e4%b8%8e%e9%93%be%e8%a1%a8)
    - [选择排序](#%e9%80%89%e6%8b%a9%e6%8e%92%e5%ba%8f)
  - [递归](#%e9%80%92%e5%bd%92)
    - [基线条件和递归条件](#%e5%9f%ba%e7%ba%bf%e6%9d%a1%e4%bb%b6%e5%92%8c%e9%80%92%e5%bd%92%e6%9d%a1%e4%bb%b6)
    - [栈](#%e6%a0%88)
  - [快速排序（Quick Sort）](#%e5%bf%ab%e9%80%9f%e6%8e%92%e5%ba%8fquick-sort)
    - [分治法与递归](#%e5%88%86%e6%b2%bb%e6%b3%95%e4%b8%8e%e9%80%92%e5%bd%92)
    - [快速排序](#%e5%bf%ab%e9%80%9f%e6%8e%92%e5%ba%8f)
  - [散列表（哈希表，Hash Table）](#%e6%95%a3%e5%88%97%e8%a1%a8%e5%93%88%e5%b8%8c%e8%a1%a8hash-table)
  - [广度优先搜索（Breadth-First-Search, BFS）](#%e5%b9%bf%e5%ba%a6%e4%bc%98%e5%85%88%e6%90%9c%e7%b4%a2breadth-first-search-bfs)
    - [图（Graph）](#%e5%9b%begraph)
    - [广度优先搜索](#%e5%b9%bf%e5%ba%a6%e4%bc%98%e5%85%88%e6%90%9c%e7%b4%a2)
    - [队列](#%e9%98%9f%e5%88%97)
    - [BFS实现](#bfs%e5%ae%9e%e7%8e%b0)
  - [狄克斯特拉算法（Dijkstra's Algorithm）](#%e7%8b%84%e5%85%8b%e6%96%af%e7%89%b9%e6%8b%89%e7%ae%97%e6%b3%95dijkstras-algorithm)
  - [贪婪算法（Greedy Algorithm）](#%e8%b4%aa%e5%a9%aa%e7%ae%97%e6%b3%95greedy-algorithm)
    - [NP](#np)
      - [P问题](#p%e9%97%ae%e9%a2%98)
      - [NP问题](#np%e9%97%ae%e9%a2%98)
      - [NPC问题](#npc%e9%97%ae%e9%a2%98)
      - [NPH问题](#nph%e9%97%ae%e9%a2%98)
  - [动态规划（Dynamic Programming）](#%e5%8a%a8%e6%80%81%e8%a7%84%e5%88%92dynamic-programming)
    - [背包问题](#%e8%83%8c%e5%8c%85%e9%97%ae%e9%a2%98)
  - [K最邻近算法（K-Nearest Neighbours, KNN）](#k%e6%9c%80%e9%82%bb%e8%bf%91%e7%ae%97%e6%b3%95k-nearest-neighbours-knn)
  - [接下来如何做……](#%e6%8e%a5%e4%b8%8b%e6%9d%a5%e5%a6%82%e4%bd%95%e5%81%9a)
  - [Reference](#reference)

## 算法简介

### 算法复杂度

大$O$表示法指出了最差情况下算法的运行时间，即算法运行时间的上限。

### 二分查找（Binary Search）

算法复杂度 $O(\log n)$，前提条件必须在已排序数组中使用。

```Python
In [1]: import numpy as np

In [2]: def binary_search(array, item):
   ...:     low = 0
   ...:     high = len(array) - 1
   ...:     while low < high - 1:
   ...:         mid = (low+high) // 2
   ...:         if item == array[mid]:
   ...:             print('The Index of the Item is: {}'.format(mid))
   ...:             return
   ...:         elif item < array[mid]:
   ...:             high = mid
   ...:         else:
   ...:             low = mid
   ...:     print('No Such Item in the Array.')

In [3]: binary_search(list(range(100)), 10)
The Index of the Item is: 10
```

## 选择排序（Selection Sort）

### 数据结构：数组与链表

- 数组在内存中是相连的，如果添加新元素时内存对数组预留的空间不足，则需要重新分配内存并重新安排数组。
- 链表中的元素存放在内存的任意位置，每个链表记录下个元素在内存中的位置。

- 读取：
数组$O(1)$，链表$O(n)$
- 插入：
数组$O(n)$，链表$O(1)$
- 删除：
数组$O(n)$，链表$O(1)$

### 选择排序

算法复杂度$O(n^2)$

```Python
In [4]: def find_smallest(array):
   ...:     smallest_index = 0
   ...:     for i in range(len(array)):
   ...:         if array[i] < array[smallest_index]:
   ...:             smallest_index = i
   ...:     return smallest_index

In [5]: def selection_sort(array):  # 实现选择排序
   ...:     sorted_list = []
   ...:     for i in range(len(array)):
   ...:         sorted_list.append(array.pop(find_smallest(array)))
   ...:     return sorted_list

In [6]: selection_sort([9, 3, 0, 5, 7, 8, 1, 4, 2, 6])
Out[6]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## 递归

### 基线条件和递归条件

递归函数自己调用自己，为避免无限循环，每个递归函数都有两部分，基线条件(base case)和递归条件(recursive case)。

- 递归条件指函数调用自己
- 基线条件指函数不再调用自己

### 栈

栈也是一种数据结构，遵循后进先出（LIFO）原则。栈有两种基本操作：进栈（push, 压栈）和出栈（pop）。调用栈是用来控制一系列子程序的栈，用于储存多个函数的栈称为调用栈。每调用一个程序，系统就会对这个程序分配一块内存，然后依次堆叠。当一个程序调用结束后，栈顶的内存块被弹出，从而返回到上一个程序。在调用另一个函数时，当前函数暂停，所有变量储存在内存中。

## 快速排序（Quick Sort）

### 分治法与递归

```Python
In [7]: def recursion_sum(array):  # 使用递归的方式求列表元素和
   ...:     if len(array) == 0:
   ...:         return 0
   ...:     else:
   ...:         return array[0] + recursion_sum(array[1:])

In [8]: recursion_sum([2, 4, 6])
Out[8]: 12

In [9]: def recursion_count(array):  # 使用递归方式求列表元素数
   ...:     if len(array) == 0:
   ...:         return 0
   ...:     else:
   ...:         return 1+recursion_count(array[1:])

In [10]: recursion_count(list(range(10)))
Out[10]: 10

In [11]: def recursion_max(list):  # 使用递归方式求列表最大元素
    ...:     if len(list) == 2:
    ...:         return list[0] if list[0] > list[1] else list[1]
    ...:     sub_max = recursion_max_book(list[1:])
    ...:     return list[0] if list[0] > sub_max else sub_max
In [12]: print(recursion_max([-11, 5, 2, 4, -8, 9, 3, 10]))
10
```

### 快速排序

算法平均复杂度$O(n\log n)$，最坏复杂度$O(n^2)$

```Python
In [13]: def quick_sort(array):   # 使用分治与递归实现快速排序
    ...:     if len(array) < 2:
    ...:         return array
    ...:     else:
    ...:         pivot = array[0]
    ...:         small_list = []
    ...:         large_list = []
    ...:         for i in array[1:]:
    ...:             if i <= pivot:
    ...:                 small_list.append(i)
    ...:             else:
    ...:                 large_list.append(i)
    ...:         return quick_sort(small_list)+[pivot]+quick_sort(large_list)

In [14]: print(quick_sort([-11, 5, 2, 4, -8, 9, 3, 10]))
[-11, -8, 2, 3, 4, 5, 9, 10]

In [15]: def quick_sort_book(array):   # 使用分治与递归实现快速排序（书中答案）
    ...:     if len(array) < 2:
    ...:         return array
    ...:     else:
    ...:         pivot = array[0]
    ...:         less = [i for i in array[1:] if i <= pivot]  # 使用列表推导式简化代码
    ...:         greater = [i for i in array[1:] if i > pivot]
    ...:         return quick_sort_book(less) + [pivot] + quick_sort_book(greater)

In [16]: print(quick_sort_book([-11, 5, 2, 4, -8, 9, 3, 10]))
[-11, -8, 2, 3, 4, 5, 9, 10]
```

尽管使用大$O$表示复杂度时不同算法的大$O$可能相同，但是实际上，大$O$忽略了算法所需的固定时间量（*常量*）的部分。因此，有时候常量的影响会比较大。例如简单查找的复杂度为$O(n)$，而二分查找的复杂度为$O(\log n)$，因此常量$c$的影响无关紧要，但是尽管快速排序和归并排序的平均算法复杂度均为$O(n\log n)$，由于快速排序的常量$c$较小，因此很多时候快速排序的速度更快。

计算复杂度时，可以先看平均情况下/最坏情况下，调用栈的高度$O()$，再看每层调用栈的时间$O()$，最后计算得出整体的算法时间复杂度。

## 散列表（哈希表，Hash Table）

散列表使用散列函数（哈希函数）将输入映射为一个数字，通过数字标定数组的索引，从而提高查找效率。

- 散列函数要满足一致性，相同的输入要能产出相同的结果。
- 如果不同的输入产出了相同的结果，则称为散列冲突，也称为哈希碰撞。显然，如果要存放10个数，分配10000个内存空间，碰撞的概率会非常低，但是造成了系统资源的浪费。
因此，理想的散列函数的基础要求是简单易于计算，同时要能够在尽量小的空间上均匀分布产出的结果，同时尽量减少散列冲突的可能。*注意：散列冲突是无法避免的，因为输出的数量是给定的，而输入的数量是无限的，因此冲突是必然发生的。*

散列表的应用：

- 用来查找
- 防止重复（因为只能有唯一的键值）
- 用来缓存

由于散列冲突不可避免，因此需要考虑如何解决散列冲突的问题。很常见的解决方法是先根据散列函数生成数组，每个散列函数指向这个数组的头部，后续一旦出现多个键值指向同一个位置的散列冲突，则在对应的数组后创建一个链表用以追加元素。但是这带来的问题是如果链表很长，则查询效率会大幅下降。*一个好的散列函数会避免产生过长的链表。*

最差情况下，散列表的复杂度为$O(n)$，即链表（但是内存消耗更大）。

填装因子=散列表包含的元素数/位置总数
显然填充因子要小于等于1，因为一旦超过1则必然发生碰撞。理想的填充因子是0.7，一旦大于0.7则需要调整散列表的长度。

## 广度优先搜索（Breadth-First-Search, BFS）

### 图（Graph）

无论是数组、链表还是栈，都是一种线性的数据结构，而图(Graph)则是一种较为复杂的非线性数据结构。

图由节点（vertex/vertice）和边（edge/edges）组成。边如果有方向则为有向图，用\<\>表示，而没有方向的称为无向图，用()表示。

如果边上有一定的权重，则图又可以分为有权图和无权图（无权图每边权重为1）。

如果图上的所有点都有路径相连，则称为连通图，否则称为非连通图。

### 广度优先搜索

广度优先搜索解决两类问题：

- 是否存在节点A-B的路径
- 节点A-B的最短路径是什么
*只有按照顺序搜索时，才能保证找到的路径是最短路径。因此需要引入队列（queue）保证数据的顺序。*

### 队列

队列同样是一种数据结构，和栈不同的是先进先出（FIFO），先入队的数据将优先出队。

队列可以用数组或者链表实现，用数组实现的叫顺序队列，用链表实现的叫链式队列。

Python可以直接创建一个双端队列。

```Python
In [17]: from collections import deque

In [18]: new_queue = deque()
```

### BFS实现

注意一旦图为有向图，且两个节点之间互相连接，则搜索队列会导致无限循环。因此，需要建立已搜索池。每次执行搜索前进行判断，如果不在搜索池中，则搜索后加入，如果在搜索池中，则不进行搜索。

书中算法的搜索池是使用列表构成的，考虑到去重的问题，个人认为可以使用集合（set）进行处理。

由于BFS需要寻找所有可能节点的路径，因此时间复杂度为$O(|V|+|E|)$，其中$|V|$是节点的数目，$|E|$是边的数目。

```Python
In [19]: def search(name):
    ...:     search_queue = deque()
    ...:     # graph是一个图，通过散列表实现，每一个键值name映射对应所有的节点的列表。因此，graph[name]是一个数组，记录了name对应的所有节点
    ...:     search_queue += graph[name]
    ...:     # searched=[] #书中使用列表记录
    ...:     searched = set()
    ...:     while search_queue:
    ...:         person = search_queue.popleft()
    ...:         if person not in searched:  # 如果不在搜索池中则进行搜索
    ...:             if match_the_condition(person):  # 判断是否符合搜索条件
    ...:                 print(person + 'matched')
    ...:                 return True
    ...:             else:
    ...:                 search_queue += graph(person)  # 将所有与此人相关的节点加入队列
    ...:                 searched.add(person)  # 将此人加入已搜索
    ...:     return False
```

## 狄克斯特拉算法（Dijkstra's Algorithm）

由于BFS仅仅找出了段数最短的路径，而如果每条边有一定的权重，则段数最短的路径并不代表总权重最小的路径。因此，可以使用狄克斯特拉算法（Dijkstra's Algorithm）。狄克斯特拉算法使用了广度优先搜索解决有向图的最短路径问题。

一旦图存在环，则狄克斯特拉算法无效。需要注意的是，无向图本身就是环。因此，狄克斯特拉算法仅适用于有向无环图（Directed Acyclic Graph, DAG）

Dijkstra's Algorithm的时间复杂度为$O(|V|^2)$，其中$|V|$是节点的数目。

如果存在负权边，由于Dijkstra's Algorithm认为所有已处理的节点均为最小开销节点，因此一旦存在负权边，则该算法无法找到最小开销路径，算法失效。

面对负权边情况，要找出最小权重路径，需要使用贝尔曼-福特算法（Bellman-Ford Algorithm）

*狄克斯特拉算法的关键理念：选择并处理图中最便宜的节点，并确保到达该节点没有更便宜的路径。*

1. 从权重最小节点开始，计算到达其他节点的开销。所有未知到达时间的节点使用$\infty$表示。
2. 从该节点出发，每到达一个节点，如果到达节点的开销小于当前值，则更新到达节点的开销，并更新新的父节点，同时将当前节点标记为已处理。
3. 找到最低开销后，根据父节点选择总权重最小的路径。

```Python
In [20]: graph = {}   # 建立图及对应的路径权重

In [21]: graph['0'] = {'1': 5, '2': 2}  

In [22]: graph['1'] = {'3': 4, '4': 2}

In [23]: graph['2'] = {'1': 8, '4': 7}

In [24]: graph['3'] = {'4': 6, '5': 3}  

In [25]: graph['4'] = {'5': 1}

In [26]: graph['5'] = {}  

In [27]: costs = {'1': 5, '2': 2., '3': np.infty, '4': np.infty, '5': np.infty}  # 建立目前已知的节点开销

In [28]: parents = {'1': '0', '2': '0', '3': None, '4': None, '5': None}  # 建立父节点

In [29]: proceed = set()  # 建立已处理节点池

In [30]: def find_lowest_cost_node(costs):  # 寻找当前最低开销节点
    ...:     lowest = np.infty
    ...:     lowest_node = None
    ...:     for index in costs:
    ...:         cost = costs[index]
    ...:         if cost < lowest and index not in proceed:  # 剔除已处理节点
    ...:             lowest = cost
    ...:             lowest_node = index
    ...:     return lowest_node

In [31]: node = find_lowest_cost_node(costs)  # 从一开始的最小节点开始查找

In [32]: while node:  # 如果还有最小节点存在
    ...:     cost = costs[node]  # 计算该节点的开销
    ...:     neighbour = graph[node]  # 找出该节点通向的子节点
    ...:     for key in neighbour.keys():  # 遍历所有的子节点
    ...:         # 如果通过当前最小节点到达所产生的开销，小于子节点开销，则更新子节点开销，同时更新父节点
    ...:         new_cost = cost + neighbour[key]
    ...:         if new_cost < costs[key]:
    ...:             costs[key] = new_cost
    ...:             parents[key] = node
    ...:     proceed.add(node)  # 遍历完成，将该节点加入已处理节点池
    ...:     node = find_lowest_cost_node(costs)


In [33]: path = []  # 记录最短路径

In [34]: def get_path(node):
    ...:     path.append(node)
    ...:     if node in parents:
    ...:         node = parents[node]
    ...:         get_path(node)
    ...:     return path[::-1]

In [35]: print(costs['5'])
8

In [36]: print(get_path('5'))
['0', '1', '4', '5']
```

## 贪婪算法（Greedy Algorithm）

贪婪算法在于每一步都选取当前状态下的局部最优解，从而希望通过局部最优解得到全局最优解。

但是对于大部分问题，贪婪算法通常不能找到全局最优解，因为没有对所有可能的路径全部尝试而过早做出决定，从而偏离最优解。但是贪婪算法作为一种近似算法（approximation algorithm），因为其高效性和对所求答案较为接近的特性，可以用作辅助算法或者直接解决一些要求结果不是特别精确的问题。

判断近似算法优劣的标准：

- 速度有多快
- 得到的近似解与最优解的接近程度

Dijkstra's Algorithm就结合了BFS和贪婪算法，BFS本身也采用了贪婪算法

### NP

关于P问题，NP问题，NPH问题，NPC问题，有比较详细的总结，给出参考如下：
> [什么是P问题、NP问题和NPC问题](http://www.matrix67.com/blog/archives/105)
>
> [P、NP、NPC、NPH问题的区别和联系](https://www.cnblogs.com/sench/p/10165376.html)
>
> [什么是P、NP、NPC、NP-Hard问题](https://hujichn.github.io/2016/07/14/%E4%BB%80%E4%B9%88%E6%98%AFP%E3%80%81NP%E3%80%81NPC%E3%80%81NP-Hard%E9%97%AE%E9%A2%98/)

#### P问题

P问题（Polynomial Problem，多项式问题），即在多项式时间（Polynomial Time）内可解的问题即为P问题。

时间复杂度为$O(1), O(n^k), O(\log n)$等都称为多项式级的时间复杂度，而另一种如$O(n!), O(a^n)$则被称为非多项式级的。显然，非多项式级的时间复杂度在数据量上升时会有巨大的时间消耗，从而导致即使使用计算机也无法解决。

因此，如果一个问题可以找到一个能在多项式的时间里解决它的算法，那么这个问题就属于P问题。

#### NP问题

相对于P问题，NP问题（Non-deterministic Polynomial Problem，非确定性多项式问题）意为在多项式时间内可以验证某一个解的问题。

简单来说，当一个问题求解其所有结果并不可能，但是可以轻易验证某一个猜测的结果的正确性的问题，就被称为NP问题。

并非所有的问题都是NP问题，一个非常好的例子为：Hamilton回路问题中，验证某个路线是否通过所有的节点非常容易，因此是NP问题，但是如果问题换为某一个图是否不存在Hamilton回路，则不是NP问题。因为找出一个不存在的结果并不能证明整个图都不存在Hamilton回路，而要验证这个结果，需要遍历所有的可能性，而遍历过程是非多项式级的。

显然，所有的P问题都是NP问题，即能多项式地解决一个问题，必然能多项式地验证这个问题的某个解。难处在于，是否所有的NP问题都是P问题？即，$NP=P?$

#### NPC问题

NPC问题（Non-deterministic Polynomial Complete Problem，NP完全问题）是一种特殊的NP问题。需要同时满足两个条件：

1. 是NP问题
2. 所有的NP问题都可以在多项式时间内约化至该问题
随着NP问题不断的约化，最终可以找到一个复杂度最高的问题，即NPC问题。一旦NPC问题得以解决，则所有的NP问题都可以得到解决。

特别的是，NPC问题不止一个。一旦证明存在一个多项式级算法可以解决NPC问题，则能够证明$P=NP$。而目前所有的NPC问题都没有找到多项式级的算法，因此目前倾向于$P\neq NP$。

#### NPH问题

NPH问题放宽了限制条件，只需要满足NPC问题的第二个条件，不需要满足第一条，即NPH问题不一定是NP问题。NPH问题由于条件更加宽泛，因此可能比NPC问题更难以解决。

需要注意的是，有时易于解决的问题和NP完全问题非常接近。

例如：当需要找到从A点到B点的最短路径可以采用Dijkstra's Algorithm，但是一旦限定需要经过的路径点，则问题转变为旅行商问题（Travelling Salesman Problem, TSP），TSP是NP完全问题。

## 动态规划（Dynamic Programming）

动态规划是一个比较难以理解的概念。看完书上和网上的一些相关资料以后，也只能说理解了一个大概。在这里先简单整理一下目前的收获以备日后查漏补缺。

目前的理解可能会有错漏，回看的时候需要仔细判断和思考。

参考资料：
> [什么是动态规划(Dynamic Programming)？动态规划的意义是什么？](https://www.zhihu.com/question/23995189)
>
> [五大常用算法之二：动态规划算法](https://www.cnblogs.com/steven_oyj/archive/2010/05/22/1741374.html)
>
> [算法-动态规划 Dynamic Programming--从菜鸟到老鸟](https://blog.csdn.net/u013309870/article/details/75193592)
>
> [五大常用算法——分治法，动态规划，回溯法，分支界限法，贪心算法](https://blog.csdn.net/u013630349/article/details/51565383)
>
> [分治法，动态规划及贪心算法感悟](https://hxrs.iteye.com/blog/1055478)

相关例题的讲解可参考：
> [常见的动态规划问题分析与求解](https://www.cnblogs.com/wuyuegb2312/p/3281264.html)
>
> [字符串相似度算法——Levenshtein Distance算法](https://www.cnblogs.com/xiaoyulong/p/8846745.html)

首先，动态规划（DP）和分治策略等并不是互斥的。同样，动态规划和贪心算法也不是互斥的。事实上，广义来说，动态规划也是利用了分治的思想，贪心算法也可以称得上是动态规划的特殊形式。

动态规划的基本思想是和分治法类似的，都是将待求解的问题分解为若干个子问题，通过依次解决各子问题，得到最后一个子问题的解就是初始问题的解。

在这个层面上看，似乎动态规划和分治法没有什么区别。但是如果每个子问题是有重叠的，即这个子问题得到的解会在后面的子问题中重复被用到，那么如果使用分治法，则会在每次重复计算子问题，导致时间复杂度和空间复杂度都提高。这时如果保存上一个子问题的结果，则会大大改善算法效率。因此，动态规划与分治法的最大区别在于：*适合于用动态规划法求解的问题，经分解后得到的子问题往往不是互相独立的（即下一个子阶段的求解是建立在上一个子阶段的解的基础上，进行进一步的求解）*，即：

- 动态规划的子问题重叠
- 分治法的子问题独立

> 《算法导论》
>
> 动态规划要求其子问题既要独立又要重叠，这看上去似乎有些奇怪。虽然这两点要求听起来可能矛盾的，但它们描述了两种不同的概念，而不是同一个问题的两个方面。如果同一个问题的两个子问题不共享资源，则它们就是独立的。对两个子问题俩说，如果它们确实是相同的子问题，只是作为不同问题的子问题出现的话，是重叠的，则它们是重叠的。

能采用动态规划求解的问题通常有三个特性：

1. 最优化原理：如果问题的最优解所包含的子问题的解也是最优的，就称该问题具有最优子结构，即满足最优化原理。
2. 无后效性：即某阶段状态一旦确定，就不受这个状态以后决策的影响。也就是说，某状态以后的过程不会影响以前的状态，只与当前状态有关。
3. 有重叠子问题：即子问题之间是不独立的，一个子问题在下一阶段决策中可能被多次使用到。*（该性质并不是动态规划适用的必要条件，但是如果没有这条性质，动态规划算法同其他算法相比就不具备优势）*同样的，如果子问题并非相互独立，尽管仍然可以使用分治法，但是分治法要做许多不必要的工作，重复地解公共的子问题，因此一般用动态规划法较好。

一个较好的总结如下（来自知乎）：

- 每个阶段只有一个状态 -> 递推
- 每个阶段的最优状态都是由上一个阶段的最优状态得到的 -> 贪心
- 每个阶段的最优状态是由之前所有阶段的状态的组合得到的 -> 搜索
- 每个阶段的最优状态可以从之前某个阶段的某个或某些状态直接得到而不管之前这个状态是如何得到的 -> 动态规划

### 背包问题

面对背包问题，如果使用排列组合进行暴力搜索，显然时间复杂度达到了$O(2^n)$，而使用贪婪算法，则无法达成最优解。因此需引入动态规划。

需要注意的是：背包问题是NP完全问题，但是使用动态规划，可以得到一个伪多项式时间的算法。

书中给出了较为直观的理解背包问题的方法，即使用网格。在使用网格理解背包问题时，需要注意如下几点：

1. 行的排列顺序变化不会影响结果
2. 子问题的单位越小，网格的粒度也要越细
3. 动态规划只能够解决拿或不拿的背包问题，不存在拿一部分的情况
4. 如果每个子问题*相互依赖*，则动态规划无法解决

略去背包问题代码复现，最长公共子序列问题。

## K最邻近算法（K-Nearest Neighbours, KNN）

KNN算法是一种非常容易理解的分类算法。

简而言之，KNN算法的逻辑为：

给定一个已经做好分类和特征值提取的数据集，当有一个新样本进入时，计算新样本到数据集内每个样本的距离，选择距离最小的K个样本（即KNN中K的来源），这K个样本的多数属于哪个分类，则新样本也被认为属于这个分类。

KNN算法实现的难点在于：

1. K值的选择。太小容易读入噪音，太大则失去了训练好的数据集的信息。可以从$\sqrt{N}$开始，N为样本容量。
2. 距离的度量方式。最简单的方式是使用欧几里得距离（Euclidean Distance），但是有很多其他的方式，如余弦相似度（Cosine Similarity）等。
3. 特征的归一化。即统一量纲。

## 接下来如何做……

全书最后一节，主要举例了一些后续可以深入学习研究的算法，在此仅做列举：

1. 树
2. 反向索引（Inverted Index）
3. 傅里叶变换（Fourier Transform）
4. 并行算法（Parallel Computing）
5. MapReduce
6. 布隆过滤器（Bloom Filter）和HyperLogLog
7. SHA算法
8. 局部敏感的散列算法
9. Diffie-Hellman 密钥交换
10. 线性规划

## Reference

> [VISUALGO](https://visualgo.net/en)
