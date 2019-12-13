# Python and HDF5 by Andrew Collette (O'Reilly)

- [Python and HDF5 by Andrew Collette (O'Reilly)](#python-and-hdf5-by-andrew-collette-oreilly)
  - [Chapter1. Introduction](#chapter1-introduction)
  - [Chapter2. Getting Started](#chapter2-getting-started)
    - [Your First HDF5 File](#your-first-hdf5-file)
      - [File Drivers](#file-drivers)
  - [Chapter3. Working with Datasets](#chapter3-working-with-datasets)
    - [Dataset Basics](#dataset-basics)
      - [Type and Shape](#type-and-shape)
      - [Reading and Writing](#reading-and-writing)
      - [Creating Empty Datasets](#creating-empty-datasets)
      - [Saving Space with Explicit Storage Types](#saving-space-with-explicit-storage-types)
      - [Automatic Type Conversion and Direct Reads](#automatic-type-conversion-and-direct-reads)
      - [Reading with astype](#reading-with-astype)
      - [Reshaping an Existing Array](#reshaping-an-existing-array)
      - [Fill Values](#fill-values)
    - [Reading and Writing Data](#reading-and-writing-data)
      - [Using Slicing Effectively](#using-slicing-effectively)
      - [Start-Stop-Step Indexing](#start-stop-step-indexing)
      - [Multidimensional and Scalar Slicing](#multidimensional-and-scalar-slicing)
      - [Boolean Indexing](#boolean-indexing)
      - [Coordinate Lists](#coordinate-lists)
      - [Automatic Broadcasting](#automatic-broadcasting)
      - [Reading Directly into an Existing Array](#reading-directly-into-an-existing-array)
      - [A Note on Data Types](#a-note-on-data-types)
    - [Resizing Datasets](#resizing-datasets)
      - [Creating Resizable Datasets](#creating-resizable-datasets)
      - [Data Shuffling with resize](#data-shuffling-with-resize)
      - [When and How to Use resize](#when-and-how-to-use-resize)

## Chapter1. Introduction

HDF5即Hierarchical Data Format version 5, 是一种全新的分层数据格式。在数据使用量日益增大的当前，HDF5格式会在数据的读写和分析上获得广泛的使用。

HDF5结构化，“自描述”的数据结构和Python的结合非常自然，目前较为成熟并得到广泛应用的是h5py和PyTables库。

书中提出HDF5的“杀手级特性”，即：HDF5使用组(groups)和属性(attributes)以分层结构组织。组类似于文件管理系统中的文件夹，将相关的数据集(datasets)储存在一起。属性则将描述性的元数据(descriptive metadata)直接和描述的数据相关联，使用户可以非常直接的看到数据的相关信息，以对数据有一个整体的认识。

HDF5的另一个特性是可以使用类似于NumPy array的切片功能。这使得HDF5在海量数据的I/O上获得很大的优势。真实数据保留在硬盘中，通过切片，只有必要的数据才会被读取到内存中，因此极大地提升了性能和效率。同时，HDF5可以允许用户控制存储空间的分配。创建一个全新的数据集不会占用任何存储空间，只有当确实有数据写入时才会分配空间。

HDF5在存储*具有相同类型的大型数值数组，有任意元数据作为标签的分层组织的数据模型*时有显著的优势。如果用户需要增强多表间的数据关联，或希望对数据使用JOINs方法，仍应当选取传统的关系型数据库。同样，对于小型的一维数据集，使用如CSV等文本格式储存会更加合理。因此，当用户不需要数据间具有强关系特性，需求高性能表现，部分I/O，分层组织结构和任意元数据时，HDF5会是非常好的工具。

HDF5数据模型有三种基本元素：数据集(datasets)，将数值型数据存于硬盘中的类数组型对象；组(groups)，分层保存数据集和其他组；属性(attributes)，直接对应数据集和组的用户自定义的元数据。

## Chapter2. Getting Started

在提到性能问题时，作者指出，尽管HDF5通常出现在大数据集应用的场景中，但是本书不会过多讨论优化和基准问题。作为用户，只需要合理调用API，将性能问题交给HDF5即可。

建议：

- 除非有显著的性能问题，不要优化任何东西。
- 尽量使用API提供的特性。
- 优先进行算法(algorithmic)层面的优化。
- 确保使用的是正确的数据类型，特别是浮点数的精度问题。
- 在成熟的社区中提问和寻找答案。

### Your First HDF5 File

使用h5py操作HDF5文件和Python操作文件非常类似。h5py的`File`对象提供了创建数据集和组的功能。类似于Python操作文件，File对象同样提供`.mode`属性。

```Python
f = h5py.File("name.hdf5", "w")   # New file overwriting any existing file
f = h5py.File("name.hdf5", "r")   # Open read-only (must exist)
f = h5py.File("name.hdf5", "r+")  # Open read-write (must exist)
f = h5py.File("name.hdf5", "a")   # Open read-write (create if doesn't exist)
```

此外，HDF5提供了额外的模式以避免覆盖已存在的文件。

```Python
f = h5py.File("name.hdf5", "w-")  # Create a new file, but fail if a file of the same name already exists
```

#### File Drivers

File drivers用于处理将HDF5文件的地址空间映射到磁盘的机制。通常来说用户不需要考虑这个设置，使用默认值即可。书中给出几种选项作为概览：

- core driver

  Core driver将文件完全保存在内存中，同时提供`backing_store`选项，选择`True`将在文件关闭时保存。

- family driver
  
  当需要将文件拆分为子文件时使用。这个特性主要用来适应文件系统无法处理2GB以上大小文件时。

- mpio driver

  mpio driver是Parallel HDF5的核心，会在后续章节进行讨论。

## Chapter3. Working with Datasets

### Dataset Basics

通过以下简单的代码就可以创建一个HDF5文件，同时将一个NumPy array保存到my dataset数据集中。

```Python
In [1]: import numpy as np

In [2]: import h5py

In [3]: f = h5py.File("testfile.hdf5")

In [4]: arr = np.ones((5,2))

In [5]: f["my dataset"] = arr

In [6]: dset = f["my dataset"]

In [7]: dset
Out[7]: <HDF5 dataset "my dataset": shape (5, 2), type "<f8">
```

#### Type and Shape

`Dataset`对象在创建时确定类型，且不能被修改。`Dataset`通常使用标准NumPy `dtype`对象。

```Python
In [8]: dset.dtype
Out[8]: dtype('<f8')

In [9]: dset.shape
Out[9]: (5, 2)
```

`Dataset`对象同样在创建时确定形状，但是可以被修改。

#### Reading and Writing

读取dataset和切片操作会返回一个NumPy array。

```Python
In [10]: out = dset[...]

In [11]: out
Out[11]:
array([[1., 1.],
       [1., 1.],
       [1., 1.],
       [1., 1.],
       [1., 1.]])

In [12]: type(out)
Out[12]: numpy.ndarray
```

在这个过程中，h5py将选取数据集中被切片的部分并读取HDF5数据，因此，切片操作会直接读写硬盘。

```Python
In [13]: dset[1:4,1] = 2.0

In [14]: dset[...]
Out[14]:
array([[1., 1.],
       [1., 2.],
       [1., 2.],
       [1., 2.],
       [1., 1.]])
```

同样，切片赋值也是可行的。

#### Creating Empty Datasets

创建数据集并不需要事先已有NumPy array的存在。`File`对象的`create_dataset`方法允许根据类型和大小创建空数据集（甚至只需要大小，不需要类型。此时默认类型为`np.float32`单精度浮点数）。

```Python
In [15]: dset = f.create_dataset("test1", (10, 10))

In [16]: dset
Out[16]: <HDF5 dataset "test1": shape (10, 10), type "<f4">

In [17]: dset = f.create_dataset("test2", (10, 10), dtype=np.complex64)

In [18]: dset
Out[18]: <HDF5 dataset "test2": shape (10, 10), type "<c8">
```

HDF5会只分配当前写入数据所需要的空间。书中给出如下例子：如果需要创建一个可以容纳4 gigabytes的一维数据集，可以通过如下方式：

```Python
In [19]: dset = f.create_dataset("big dataset", (1024**3,), dtype=np.float32)

In [20]: dset[0:1024] = np.arange(1024)

In [21]: f.flush()

In [22]: !ls -lh testfile.hdf5
-rw-rw-r-- 1 1024 users 4.1G 12月 11 18:05 testfile.hdf5
```

但是，实际发现此时硬盘空间已经真实消耗4G，并未实现书中的示例。查阅资料后发现，应使用如下代码：

```Python
In [23]: !rm testfile.hdf5

In [24]: f = h5py.File("testfile.hdf5")

In [25]: dset = f.create_dataset("big dataset", (1024**3,), dtype=np.float32, chunks=True)

In [26]: f.flush()

In [27]: !ls -lh testfile.hdf5
-rw-rw-r-- 1 1024 users 1.4K 12月 11 18:06 testfile.hdf5
```

此时验证无误。

参考如下：
> "Size on disk of a partly filled HDF5 dataset" [StackOverFlow](https://stackoverflow.com/questions/45145389/size-on-disk-of-a-partly-filled-hdf5-dataset?r=SearchResults)

#### Saving Space with Explicit Storage Types

由于HDF5可以接受基本上所有的NumPy类型，在没有显式指定保存格式时，`create_dataset`方法会自行推断保存格式。因此，当能够明确数据保存格式时，显式地指定格式可以节省磁盘空间和I/O时间。

通常，为了保证计算精度会使用8位双精度浮点数(NumPy dtype float64)进行内存中的计算。但是在数据保存时，常用的方法是使用4位单精度浮点数(NumPy dtype float32)进行保存。

```Python
In [28]: bigdata = np.ones((100,1000))

In [29]: bigdata.dtype
Out[29]: dtype('float64')

In [30]: bigdata.shape
Out[30]: (100, 1000)
```

显然直接保存时使用的是双精度浮点数，但同样可以指定使用单精度浮点数进行保存。改变保存方法后空间占用节省了一半。

```Python
In [31]: with h5py.File('big1.hdf5','w') as f1:
    ...:     f1['big'] = bigdata

In [32]: !ls -lh big1.hdf5
-rwxrwxrwx 1 1024 users 784K 12月 11 18:14 big1.hdf5

In [33]: with h5py.File('big2.hdf5','w') as f2:
    ...:     f2.create_dataset('big', data=bigdata, dtype=np.float32)

In [34]: !ls -lh big2.hdf5
-rwxrwxrwx 1 1024 users 393K 12月 11 18:15 big2.hdf5
```

但是需要注意的是，一旦指定保存格式后，读取的数据也会变成指定保存的格式。

```Python
In [35]: f1 = h5py.File("big1.hdf5")

In [36]: f2 = h5py.File("big2.hdf5")

In [37]: f1['big'].dtype
Out[37]: dtype('<f8')

In [38]: f2['big'].dtype
Out[38]: dtype('<f4')
```

#### Automatic Type Conversion and Direct Reads

在内存中的双精度向硬盘中的单精度存储时，用户不需要考虑格式转换的问题，HDF5库会自行完成格式转换。但是，当需要从硬盘中储存的单精度读入内存并使用双精度进行运算时，则会带来一定的格式问题。如果数据量极大，显然不能同时在内存中读入单精度数据后再在内存中转换为双精度。

面对这个问题的最佳解决方案为直接向预先分配好正确格式的NumPy array中读入硬盘数据。

```Python
In [39]: dset = f2['big']

In [40]: dset.dtype
Out[40]: dtype('<f4')

In [41]: dset.shape
Out[41]: (100, 1000)
```

读取上节中保存的数据，为单精度浮点数。

```Python
In [42]: big_out = np.empty((100, 1000), dtype=np.float64)  

In [43]: dset.read_direct(big_out)  

In [44]: big_out.dtype
Out[44]: dtype('float64')

In [45]: big_out[0,0]
Out[45]: 1.0
```

创建双精度浮点数的空数组（`np.empty`不像`np.ones`或`np.zeros`，不需要事先初始化数组），将数据直接读入，可以看到HDF5填充了空数组，并使用了给定的格式。

#### Reading with astype

做格式转换时不一定每次都创建空数组然后读入。使用`Dataset.astype`上下文管理器同样可以起到类似的功能。

```Python
In [46]: with dset.astype('float64'):
    ...:     out = dset[0,:]

In [47]: out.dtype
Out[47]: dtype('float64')
```

当使用HDF5自动类型转换时，需要记住以下几点：

- 转换仅限于数值型之间，如整型和浮点型、不同精度浮点型之间的转换，HDF5不支持字符型和数值型之间的转换。
- 当从高精度向低精度转换时，HDF5会对数据进行截断。

  ```Python
    In [48]: f.create_dataset('x', data=1e256, dtype=np.float64)
    Out[48]: <HDF5 dataset "x": shape (), type "<f8">

    In [49]: print(f['x'][...])
    1e+256

    In [50]: f.create_dataset('y', data=1e256, dtype=np.float32)
    Out[50]: <HDF5 dataset "y": shape (), type "<f4">

    In [51]: print(f['y'][...])
    inf
  ```

  在这个过程中，HDF5不会做任何提示，因此建议随时注意使用的数据类型。

#### Reshaping an Existing Array

只要总元素数量一致，HDF5支持写入和原始NumPy array形状不同的数据，同时不会有任何性能损耗。

```Python
In [52]: imagedata = np.random.rand(100, 480, 640)

In [53]: imagedata.shape
Out[53]: (100, 480, 640)

In [54]: f.create_dataset('newshape', data=imagedata, shape=(100, 2, 240, 640))
Out[54]: <HDF5 dataset "newshape": shape (100, 2, 240, 640), type "<f8">
```

#### Fill Values

当创建新数据集时，默认会使用0填充数据集：

```Python
In [55]: dset = f.create_dataset('empty', (2,2), dtype=np.int32)

In [56]: dset[...]
Out[56]:
array([[0, 0],
       [0, 0]], dtype=int32)
```

但是同样，也可以选择不同的默认值对数据集进行填充，如-1或NaN等，使用`fillvalue`参数即可。填充的数值只有当数据被读取的时候才会被处理，因此并不会占用额外的存储空间。但是一旦在创建数据集时被确定，则不能被更改，即该数据集所有的空值都会以创建数据集时定义的值填充，除非空值被写入其他值，`fillvalue`同样会作为数据集的属性被记录。

```Python
In [57]: dset = f.create_dataset('filled', (2,2), dtype=np.int32, fillvalue=42)

In [58]: dset[...]
Out[58]:
array([[42, 42],
       [42, 42]], dtype=int32)

In [59]: dset.fillvalue
Out[59]: 42
```

### Reading and Writing Data

#### Using Slicing Effectively

```Python
In [60]: dset = f2['big']

In [61]: dset
Out[61]: <HDF5 dataset "big": shape (100, 1000), type "<f4">

In [62]: out = dset[0:10, 20:70]

In [63]: out.shape
Out[63]: (10, 50)
```

在进行切片操作时，h5py进行了如下操作：

1. 确定目标数据的大小，在这里是(10, 50)
2. 创建一个符合目标大小的empty NumPy array
3. HDF5选出数据集中需要的部分
4. HDF5将数据复制到空NumPy array中
5. 返回新填充的数组

由此可见，在每一次进行切片操作时，HDF5都会先确定切片大小，创建空数组，选择数据集范围，然后才会开始读取数据。因此，提升数据读取性能的关键一步就是**选择合理的切片大小**。

```Python
# Check for negative values and clip to 0

# Case 1
for ix in xrange(100):
    for iy in xrange(1000):
        val = deset[ix,iy]            # Read one element
        if val < 0: dset[ix, iy] = 0  # Clip to 0 if needed

# Case 2
for ix in xrange(100):
    val = dset[ix,:]  # Read one row
    val[val < 0] = 0  # Clip negative values to 0
    dset[ix,:] = val  # Write row back out
```

在上例中，从(100, 1000)的数据集进行切片，方法2会有更好的效率。因为方法1会进行100000次切片而方法2只进行了100次切片。

尽管方法1中在内存中进行了NumPy arrays的切片，但是一旦在HDF5的机制下会降低性能。

HDF5写入数据和读入数据类似，会先确定数据的大小，确认数据集是否可以进行处理。然后在数据集中选定合适的大小进行写入。因此，一次一个元素、或一次很少的元素写入会极大地降低处理性能。

#### Start-Stop-Step Indexing

h5py使用和NumPy几乎相同的切片方式，包括含有步长的切片。

```Python
In [64]: dset = f.create_dataset('range', data=np.arange(10))

In [65]: dset[...]
Out[65]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

In [66]: dset[4]
Out[66]: 4

In [67]: dset[4:8]
Out[67]: array([4, 5, 6, 7])

In [68]: dset[4:8:2]
Out[68]: array([4, 6])

In [69]: dset[:]
Out[69]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

In [70]: dset[4:-1]
Out[70]: array([4, 5, 6, 7, 8])
```

但是，NumPy中的一些技巧并不被HDF5支持，如使用步长-1进行数组倒序的操作，在NumPy中是可行的而HDF5数据集中会报错，因为步长必须大于等于1。

```Python
In [71]: a
Out[71]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

In [72]: a[::-1]
Out[72]: array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

In [73]: dset[::-1]
ValueError: Step must be >= 1 (got -1)
```

#### Multidimensional and Scalar Slicing

HDF5使用`...`进行切片，在Python中被称为`Ellipsis`，对无需指定的轴进行全选。

```Python
In [74]: dset = f.create_dataset('4d', shape=(100, 80, 50, 20))

In [75]: dset[0,...,0].shape
Out[75]: (80, 50)

In [76]: dset[...].shape
Out[76]: (100, 80, 50, 20)
```

一种较为特殊的情况是所谓的标量(scalar)数据。在NumPy中有两种方式储存一个元素的数据。

第一种方式是一个大小为(1,)的一维数组，这种结构可以通过切片或者索引获取数据。

```Python
In [77]: dset = f.create_dataset('1d', shape=(1,), data=42)

In [78]: dset.shape
Out[78]: (1,)

In [79]: dset[0]
Out[79]: 42

In [80]: dset[...]
Out[80]: array([42])
```

这种方式下，使用`Ellipsis`会返回一个元素的数组，而使用索引会直接返回这个元素本身。

第二种方式大小为()，是一个空元组。这种方式不能通过索引获取数据。

```Python
In [81]: dset = f.create_dataset('0d', data=42)

In [82]: dset.shape
Out[82]: ()

In [83]: dset[0]
ValueError: Illegal slicing argument for scalar dataspace

In [84]: dset[...]
Out[84]: array(42)
```

在这种方式下，使用`Ellipsis`同样会返回一个数组，在这里是一个标量数组(scalar array)。

如果在这种方式下同样想获得元素本身，而不是一个NumPy array，可以使用一种看似比较奇怪的方式获取：

```Python
In [85]: dset[()]
Out[85]: 42
```

因此：

1. `Ellipsis`始终会以NumPy array的形式给出数据集所有的数据
2. 使用空元组(empty tuple"()")也会给出数据集中所有的元素，当一维或更高维时，同样给出数组结构，当0D时，给出标量元素。
3. 在一些历史代码中会见到类似`.value`的形式，这种方式完全等价于`dataset[()]`，在后续h5py的版本中将不会再支持。

#### Boolean Indexing

HDF5同样支持使用布尔值进行索引。

```Python
In [86]: data = np.random.random(10)*2 - 1

In [87]: data
Out[87]:
array([-0.39438298, -0.5841106 , -0.85382983,  0.48593953,  0.73904431,
        0.91193146, -0.30166953,  0.54883998,  0.04091559,  0.21349258])

In [88]: dset = f.create_dataset('random', data=data)

In [89]: dset[data<0] = 0

In [90]: dset[...]
Out[90]:
array([0.        , 0.        , 0.        , 0.48593953, 0.73904431,
       0.91193146, 0.        , 0.54883998, 0.04091559, 0.21349258])

In [91]: dset[data<0] = -1 * data[data<0]

In [92]: dset[...]
Out[92]:
array([0.39438298, 0.5841106 , 0.85382983, 0.48593953, 0.73904431,
       0.91193146, 0.30166953, 0.54883998, 0.04091559, 0.21349258])
```

在这个过程中，先对data进行布尔值判断，随后HDF5将布尔值转化为数据集中的坐标进行赋值读取等操作。这种方式带来两个结果：

1. 对于有很多`True`值的极大的索引表达式，在Python端修改数据后再写入数据集会更快。
2. 表达式右侧的值要么是一个标量，要么是一个完全等同于选出数据大小的数组。尽管看似比较复杂，但是实际上当符合条件数据很少时，这是一种非常有效的更新数据的方式。

需要注意的是，在上例中始终是选择data进行布尔运算，选择data进行赋值，因此dset本身没有被覆盖。也可以使用类似于Pandas DataFrame的赋值方式，则会直接覆盖dset本身。

```Python
In [93]: dset[dset<0] = 0
TypeError: unorderable types: Dataset() < int()

In [94]: dset[dset[...]>0.5] = 0

In [95]: dset[...]
Out[95]:
array([0.39438298, 0.        , 0.        , 0.48593953, 0.        ,
       0.        , 0.30166953, 0.        , 0.04091559, 0.21349258])
```

#### Coordinate Lists

h5py还从NumPy中使用了一些其他的特性，如使用列表进行切片的功能。

```Python
In [96]: dset = f['range']

In [97]: dset[...]
Out[97]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

In [98]: dset[[1,2,7]]
Out[98]: array([1, 2, 7])
```

但是h5py仍然和NumPy有一些不同，主要在于：

1. 一次只能对一根轴上进行列表切片
2. 不能使用重复的列表元素
3. 列表中的索引必须严格递增

#### Automatic Broadcasting

在之前的代码中，使用过`dset[data<0] = 0`这样的代码，这种表达式使用了类似NumPy中的广播(broadcasting)操作。这种操作能够极大地提升性能。

```Python
In [99]: dset = f2['big']

In [100]: dset.shape
Out[100]: (100, 1000)

'''alternative method:

data = dset[0,:]
for idx in xrange(100):
    dset[idx,:] = data
'''

In [101]: dset[:,:] = dset[0,:]
```

在例子中，如果需要复制第0行数据并填充剩下的所有行，尽管可以使用循环赋值，但是这样会进行之前所说的多次切片的行为，而且需要保证边际条件准确无误。使用广播则完全没有这方面的问题，同时在性能上也能有很好的提升。

表达式右侧是(1000,)的数组，左侧是(100, 1000)的数组，由于最后一个维度相同，因此h5py会自动将所有100行的索引全部重复赋值。这种操作只进行了一次切片，剩余的操作会在将数据写入硬盘时完成。

#### Reading Directly into an Existing Array

回到将HDF5数据直接填入数组中并进行自动格式转换的操作。之前已展示过将float32数据读入float64数组中：

```Python
In [102]: dset.dtype
Out[102]: dtype('<f4')

In [103]: out = np.empty((100, 1000), dtype=np.float64)

In [104]: dset.read_direct(out)
```

但是这种方法需要一次性读入所有数据。实际上，还有更加实用的方法。如果需要读第1行所有数据`dset[0,:]`然后将其存入数组第51行`out[50,:]`，可以使用`source_sel`和`dest_sel`关键字，对应*source selection*和*destination selection*。

```Python
In [105]: dset.read_direct(out, source_sel=np.s_[0,:], dest_sel=np.s_[50,:])
```

其中比较奇怪的部分是参数中的`np.s_`，这对out进行了切片操作，返回了一个`NumPy slice`对象。

此外，输出的数组不需要和数据集大小相同，例如求均值，常规做法为：

```Python
In [121]: out = dset[:,0:50]

In [122]: out.shape
Out[122]: (100, 50)

In [123]: means = out.mean(axis=1)

In [124]: means.shape
Out[124]: (100,)
```

使用`read_direct`的做法为：

```Python
In [125]: out = np.empty((100,50), dtype=np.float32)

In [126]: dset.read_direct(out, np.s_[:,0:50])  # dset_sel can be omitted

In [127]: means = out.mean(axis=1)
```

#### A Note on Data Types

### Resizing Datasets

#### Creating Resizable Datasets

#### Data Shuffling with resize

#### When and How to Use resize
