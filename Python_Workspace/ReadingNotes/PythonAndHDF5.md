# Python and HDF5 by Andrew Collette (O'Reilly)

笔记中使用编程环境为：

- Python 3.7.4
- IPython 7.8.0
- NumPy 1.16.5
- h5py 2.9.0

NumPy相关内容可参考NumPy中文文档：[NumPy](https://www.numpy.org.cn/user/)

阅读进度：

- [x] Chapter1 Introduction
- [x] Chapter2 Getting Started
- [x] Chapter3 Working with Datasets
- [x] Chapter4 How Chunking and Compression Can Help You
- [x] Chapter5 Groups, Links, and Iteration: The "H" in HDF5
- [x] Chapter6 Storing Metatdata with Attributes
- [x] Chapter7 More About Types
- [x] Chapter8 Organizing Data with References, Types, and Dimension Scales
- [x] Chapter9 Concurrency: Parallel HDF5, Treading, and Multiprocessing
- [x] Chapter10 Next Steps

- [Python and HDF5 by Andrew Collette (O'Reilly)](#python-and-hdf5-by-andrew-collette-oreilly)
  - [Chapter1. Introduction](#chapter1-introduction)
    - [Python and HDF5](#python-and-hdf5)
      - [Organizing Data and Metadata](#organizing-data-and-metadata)
      - [Coping with Large Data Volumes](#coping-with-large-data-volumes)
    - [What Exactly Is HDF5](#what-exactly-is-hdf5)
      - [HDF5: The File](#hdf5-the-file)
      - [HDF5: The Library](#hdf5-the-library)
      - [HDF5: The Ecosystem](#hdf5-the-ecosystem)
  - [Chapter2. Getting Started](#chapter2-getting-started)
    - [HDF5 Basics](#hdf5-basics)
    - [Setting Up](#setting-up)
      - [Python 2 or Python 3](#python-2-or-python-3)
      - [Code Examples](#code-examples)
      - [NumPy](#numpy)
      - [HDF5 and h5py](#hdf5-and-h5py)
      - [IPython](#ipython)
      - [Timing and Optimization](#timing-and-optimization)
    - [The HDF5 Tools](#the-hdf5-tools)
      - [Command Line Tools](#command-line-tools)
    - [Your First HDF5 File](#your-first-hdf5-file)
      - [Use as a Context Manager](#use-as-a-context-manager)
      - [File Drivers](#file-drivers)
      - [The User Block](#the-user-block)
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
  - [Chapter4. How Chunking and Compression Can Help You](#chapter4-how-chunking-and-compression-can-help-you)
    - [Contiguous Storage](#contiguous-storage)
    - [Chunked Storage](#chunked-storage)
    - [Setting the Chunk Shape](#setting-the-chunk-shape)
      - [Auto-Chunking](#auto-chunking)
      - [Manually Picking a Shape](#manually-picking-a-shape)
    - [Performance Example: Resizable Datasets](#performance-example-resizable-datasets)
    - [Filters and Compression](#filters-and-compression)
      - [The Filter Pipeline](#the-filter-pipeline)
      - [Compression Filters](#compression-filters)
      - [GZIP/DEFLATE Compression](#gzipdeflate-compression)
      - [SZIP Compression](#szip-compression)
      - [LZF Compression](#lzf-compression)
      - [Performance](#performance)
    - [Other Filters](#other-filters)
      - [SHUFFLE Filter](#shuffle-filter)
      - [FLETCHER32 Filter](#fletcher32-filter)
    - [Third-Party Filters](#third-party-filters)
  - [Chapter5. Groups, Links, and Iteration: The "H" in HDF5](#chapter5-groups-links-and-iteration-the-%22h%22-in-hdf5)
    - [The Root Group and Subgroups](#the-root-group-and-subgroups)
    - [Group Basics](#group-basics)
      - [Dictionary-Style Access](#dictionary-style-access)
      - [Special Properties](#special-properties)
    - [Working with Links](#working-with-links)
      - [Hard Links](#hard-links)
      - [Free Space and Repacking](#free-space-and-repacking)
      - [Soft Links](#soft-links)
      - [External Links](#external-links)
      - [A Note on Object Names](#a-note-on-object-names)
      - [Using get to Determine Object Types](#using-get-to-determine-object-types)
      - [Using require to Simplify Your Application](#using-require-to-simplify-your-application)
    - [Iteration and Containership](#iteration-and-containership)
      - [How Groups Are Actually Stored](#how-groups-are-actually-stored)
      - [Dictionary-Style Iteration](#dictionary-style-iteration)
      - [Containership Testing](#containership-testing)
    - [Multilevel Iteration with the Visitor Pattern](#multilevel-iteration-with-the-visitor-pattern)
      - [Visit by Name](#visit-by-name)
      - [Multiple Links and visit](#multiple-links-and-visit)
      - [Visiting Items](#visiting-items)
      - [Canceling Iteration: A Simple Search Mechanism](#canceling-iteration-a-simple-search-mechanism)
    - [Copying Objects](#copying-objects)
      - [Single-File Copying](#single-file-copying)
    - [Object Comparison and Hashing](#object-comparison-and-hashing)
  - [Chapter6. Storing Metadata with Attributes](#chapter6-storing-metadata-with-attributes)
    - [Attribute Basics](#attribute-basics)
      - [Type Guessing](#type-guessing)
      - [Strings and File Compatibility](#strings-and-file-compatibility)
      - [Python Objects](#python-objects)
      - [Explicit Typing](#explicit-typing)
  - [Chapter7. More About Types](#chapter7-more-about-types)
    - [The HDF5 Type System](#the-hdf5-type-system)
    - [Integers and Floats](#integers-and-floats)
    - [Fixed-Length Strings](#fixed-length-strings)
    - [Variable-Length Strings](#variable-length-strings)
      - [The vlen String Data Type](#the-vlen-string-data-type)
      - [Working with vlen String Datasets](#working-with-vlen-string-datasets)
      - [Byte Versus Unicode Strings](#byte-versus-unicode-strings)
      - [Using Unicode String](#using-unicode-string)
      - [Don't Store Binary Data in Strings](#dont-store-binary-data-in-strings)
      - [Future-Proofing Your Python 2 Application](#future-proofing-your-python-2-application)
    - [Compound Types](#compound-types)
    - [Complex Numbers](#complex-numbers)
    - [Enumerated Types](#enumerated-types)
    - [Booleans](#booleans)
    - [The array Type](#the-array-type)
    - [Opaque Types](#opaque-types)
    - [Dates and Times](#dates-and-times)
  - [Chapter8. Organizing Data with References, Types, and Dimension Scales](#chapter8-organizing-data-with-references-types-and-dimension-scales)
    - [Object References](#object-references)
      - [Creating and Resolving References](#creating-and-resolving-references)
      - [References as "Unbreakable" Links](#references-as-%22unbreakable%22-links)
      - [References as Data](#references-as-data)
    - [Region References](#region-references)
      - [Creating Region References and Reading](#creating-region-references-and-reading)
      - [Fancy Indexing](#fancy-indexing)
      - [Finding Datasets with Region References](#finding-datasets-with-region-references)
    - [Named Types](#named-types)
      - [The Datatype Object](#the-datatype-object)
      - [Linking to Named Types](#linking-to-named-types)
      - [Managing Named Types](#managing-named-types)
    - [Dimension Scales](#dimension-scales)
      - [Creating Dimension Scales](#creating-dimension-scales)
      - [Attaching Scales to a Dataset](#attaching-scales-to-a-dataset)
  - [Chapter9. Concurrency: Parallel HDF5, Threading, and Multiprocessing](#chapter9-concurrency-parallel-hdf5-threading-and-multiprocessing)
    - [Python Parallel Basics](#python-parallel-basics)
    - [Threading](#threading)
    - [Multiprocessing](#multiprocessing)
    - [MPI and Parallel HDF5](#mpi-and-parallel-hdf5)

## Chapter1. Introduction

### Python and HDF5

HDF5即Hierarchical Data Format version 5, 是一种全新的分层数据格式。在数据使用量日益增大的当前，HDF5格式会在数据的读写和分析上获得广泛的使用。

HDF5结构化，“自描述”的数据结构和Python的结合非常自然，目前较为成熟并得到广泛应用的是`h5py`和`PyTables`库。

#### Organizing Data and Metadata

在这节中会使用一个简单的案例讲解HDF5的特性在应用层面的作用。具体的细节会在后续章节中进行讨论，在此仅作为对HDF5的一个初步认识。

假设有一个`NumPy array`表示从一场实验中获取的数据：

```Python
In [1]: import numpy as np

In [2]: temperature = np.random.random(1024)

In [3]: temperature
Out[3]:
array([0.28831224, 0.3274355 , 0.49401725, ..., 0.90799347, 0.03337086,
       0.34579398])
```

假设这些数据点是由一个每十秒采集一次温度的气象站所记录。为了使数据便于理解，需要记录下采样间隔，即"delta-T"。在Python中可以使用一个变量记录：

```Python
In [4]: dt = 10.0
```

数据采集在一个指定时间点开始，这个时间点也需要记录，而且需要知道这些数据来源于15号气象站：

```Python
In [5]: start_time = 1375204299  # in Unix time

In [6]: station = 15
```

使用NumPy内建函数`np.savez`可以将这些数据保存至硬盘。这个函数将以`NumPy array`保存数据，并将相关名称打包至一个ZIP文件，然后使用`np.load`可以再次读取文件：

```Python
In [7]: np.savez("weather.npz", data=temperature, start_time=start_time, station=station)

In [8]: out = np.load("weather.npz")

In [9]: out["data"]
Out[9]:
array([0.28831224, 0.3274355 , 0.49401725, ..., 0.90799347, 0.03337086,
       0.34579398])

In [10]: out["start_time"]
Out[10]: array(1375204299)

In [11]: out["station"]
Out[11]: array(15)
```

目前来看NumPy可以胜任这些任务，但是如果一个气象站中有多个数据：

```Python
In [12]: wind = np.random.random(2048)

In [13]: dt_wind = 5.0  # Wind sampled every 5 seconds
```

甚至有不止一个气象站。在这种情况下，如何命名，是否使用多个文件保存，将给用户带来一些麻烦。

而使用HDF5对数据进行存储：

```Python
In [14]: import h5py

In [15]: f = h5py.File("weather.hdf5")

In [16]: f["/15/temperature"] = temperature

In [17]: f["/15/temperature"].attrs["dt"] = 10.0

In [18]: f["/15/temperature"].attrs["start_time"] = 1375204299

In [19]: f["/15/wind"] = wind

In [20]: f["/15/wind"].attrs["dt"] = 5.0

...

In [...]: f["/20/temperature"] = temperature_from_station_20

...

# and so on
```

这个案例指出HDF5的“杀手级特性”，即：HDF5使用组(groups)和属性(attributes)以分层结构组织。组类似于文件管理系统中的文件夹，将相关的数据集(datasets)储存在一起。在上述案例中，来自同一个气象站的温度和风速数据可以直接保存在相同的组下，如`"/15", "/20"`等。属性则将描述性的元数据(descriptive metadata)**直接和描述的数据相关联**，使用户可以非常直接的看到数据的相关信息，以对数据有一个整体的认识。

```Python
In [21]: dataset = f["/15/temperature"]

In [22]: for key, value in dataset.attrs.items():
    ...:     print("%s: %s" % (key, value))
dt: 10.0
start_time: 1375204299
```

#### Coping with Large Data Volumes

作为高级胶水语言，Python越来越多地用于大型数据集的快速可视化和整合以编译语言如C或FORTRAN运行的大规模计算。现在处理高达数百gigabytes甚至terabytes的数据集已经非常常见，HDF5本身可以处理exabytes数据。

通常来说，直接将大型数据集全部载入到内存中是不现实的。HDF5的一大优势在于对数据的部分提取和I/O。仍以上例来说，这个称作`dataset`的对象是一个HDF5数据集的代号，它支持类数组的切片操作。

```Python
In [23]: dataset = f["/15/temperature"]

In [24]: dataset[0:10]
Out[24]:
array([0.28831224, 0.3274355 , 0.49401725, 0.07706269, 0.29467911,
       0.43153889, 0.0636959 , 0.80148648, 0.68665553, 0.30635717])

In [25]: dataset[0:10:2]
Out[25]: array([0.28831224, 0.49401725, 0.29467911, 0.0636959 , 0.68665553])

```

使用这种类似于`NumPy array`的切片功能使得HDF5在海量数据的I/O上获得很大的优势。真实数据保留在硬盘中，通过切片，只有必要的数据才会被读取到内存中，因此极大地提升了性能和效率。

HDF5的另一优势在于可以允许用户控制存储空间的分配。除了元数据外，创建一个全新的数据集不会占用任何存储空间，只有当确实有数据写入时才会分配空间。例如可以在任何电脑上创建一个2-terabyte大小的数据集：

```Python
In [31]: big_dataset = f.create_dataset("big", shape=(1024, 1024, 1024, 512), dtype="float32", chunks)
```

由于没有任何空间被分配，因此整个数据集的全部空间都是对用户可用的，可以在数据集的任何地方写入数据，只有写入数据的部分才会占用磁盘空间：

```Python
In [32]: big_dataset[244, 678, 23, 36] = 42.0
```

实际上，在这里当使用`f.close()`关闭文件后，会发现已有2TB的空间被占用，关于如何解决这个问题参见第三章Creating Empty Datasets。

当空间非常重要时，甚至可以进行基于dataset-by-dataset的压缩：

```Python
In [33]: compressed_dataset = f.create_dataset("comp", shape=(1024,), dtype="int32", compression="gzip")

In [34]: compressed_dataset[:] = np.arange(1024)

In [35]: compressed_dataset[:]
Out[35]: array([   0,    1,    2, ..., 1021, 1022, 1023])
```

### What Exactly Is HDF5

HDF5在存储**具有相同类型的大型数值数组，有任意元数据作为标签的分层组织的数据模型**时有显著的优势。如果用户需要增强多表间的数据关联，或希望对数据使用JOINs方法，仍应当选取传统的关系型数据库。同样，对于小型的一维数据集，使用如CSV等文本格式储存会更加合理。因此，当用户不需要数据间具有强关系特性，需求高性能表现，部分I/O，分层组织结构和任意元数据时，HDF5会是非常好的工具。

所以当需要定义HDF5时，可以认为它包含三个部分：

- 一种文件规范和相关的数据模型。
- 一个可以从C, C++, Java, Python等提供具有API访问权限的标准库。
- 一个由使用HDF5的客户端程序和类似MATLAB, IDL和Python等分析平台共同构成的软件生态系统。

#### HDF5: The File

在上文的例子中，已经可以看到HDF5的三种基本元素：数据集(`datasets`)，将数值型数据存于硬盘中的类数组型对象；组(`groups`)，分层保存数据集和其他组；属性(`attributes`)，可附加到数据集和组的用户自定义的元数据。

通过这些基本的抽象，用户可以构建特定的应用格式，以适合需要解决的问题的方式组织数据。在上例中，使用组对应每个气象站，用不同的数据集对应实验数据，用属性保存关于数据集的其他信息。在此基础上，HDF5作为处理跨平台的数据问题，类似和其他成员分享数据就变成非常简单的基于操作组、数据集和数据属性以获得结果的问题。因为所有的文件都是“自描述”的，因此即使时确认应用格式也不需要从文件中获取数据，只要通过文件浏览其内容即可：

```Python
In [36]: f.keys()
Out[36]: <KeysViewHDF5 ['15', 'comp']>

In [37]: f["/15"].keys()
Out[37]: <KeysViewHDF5 ['temperature', 'wind']>
```

#### HDF5: The Library

人们说的HDF5通常指用C编写，带有C++和Java的附加绑定的库。最流行的两个Python接口`PyTables`和`h5py`都是被设计使用HDF Group提供的C语言库。HDF5是主动维护的，并且注重向后兼容。

#### HDF5: The Ecosystem

HDF5几乎支持所有平台，具有非常完善的生态。

## Chapter2. Getting Started

### HDF5 Basics

HDF5的组织方式从上到下分为三层：

- 使用HDF5的软件层：

  - User code
  - Middleware: h5py, PyTables, IDL, MATLAB, ...

  大部分的用户代码，包括Python的包`h5py`和`PyTables`都位于此层，使用了原生C的API（HDF5本身用C编写）。C API，及其之上的Python代码，都是设计来处理HDF5数据模型中的三个公共抽象：数据集、组和属性。

- HDF5库内部层：

  - C API
  - Public abstractions: datasets, groups, attributes
  - Internal data structures: B-trees to index groups, "chunk" dataset storage, etc
  - 1-D file "address space"
  - Low-level drivers

  HDF5使用多种内部数据结构来表示数据集、组和属性。例如组使用B树对其条目进行索引，从而使检索和创建组成员的速度非常快，即使有大量对象存储在组中也一样。通常只有涉及性能考虑时才会需要关心这些数据结构。例如当使用分块存储时，了解数据在磁盘上的实际组织方式非常重要。

  后两层与数据如何访问磁盘有关。HDF5对象都位于一维逻辑地址中，但在这层和磁盘上实际字节中有额外的一层。HDF5驱动负责数据写入磁盘的机制，通过这个机制可以带来很多有趣的事。

- 操作系统层：
  - Bytes on disk

### Setting Up

#### Python 2 or Python 3

书中使用Python2，在笔记中使用Python3。

#### Code Examples

书中使用Python IDLE进行代码演示。所有的代码假定已经导入`NumPy`和`h5py`两个包。

#### NumPy

书中所有的数组默认使用`NumPy array`类型。`h5py`包会自动将HDF5数据格式映射为`NumPy dtypes`，这种方式便于数据的交互和使用。在HDF5中借鉴了NumPy中的切片思想，并且支持载入部分数据集。

由于NumPy中，切片数据是对原始数据的索引，而非深拷贝，因此对切片数据的操作会同样影响原始数据。因此，尽管切片数据非常快，但是在操作时必须非常小心。但是，HDF5没有继承这点。由于数据保存在磁盘上，因此从文件中读取的永远是原始数据的一份拷贝。

#### HDF5 and h5py

书中使用`h5py`包处理HDF5。这个包提供了对例如文件，组，数据集，属性等HDF5对象的高级封装。除了`h5py`之外，`PyTables`也是基于HDF5的包，而且提供了数据集索引和额外的文件系统。本书着重于讲述HDF5本身的结构和特性，因此主要使用`h5py`包，但是`PyTables`提供的一些特性也值得关注。

#### IPython

尽管书中使用Python IDLE，出于习惯，笔记中代码的编写和调试统一使用IPython环境。

#### Timing and Optimization

书中使用标准库中的`timeit.timeit()`方法进行性能检验。在笔记中，直接使用IPython中的`%timeit`魔法方法。

在提到性能问题时，书中指出，尽管HDF5通常出现在大数据集应用的场景中，但是本书不会过多讨论优化和基准问题。作为用户，只需要合理调用API，将性能问题交给HDF5即可。

建议：

- 除非有显著的性能问题，不要优化任何东西。
- 尽量使用API提供的特性。
- 优先进行算法(algorithmic)层面的优化。
- 确保使用的是正确的数据类型，特别是浮点数的精度问题。
- 在成熟的社区中提问和寻找答案。

### The HDF5 Tools

#### Command Line Tools

除了使用图形化界面（例如略过的两节提到的HDFView和ViTables）查看HDF5文件，使用命令行会是更加简单方便的方式。在这里，使用`h5ls`工具。这个工具可以非常方便的查看HDF5文件包含的数据结构，可以直接在命令行界面下使用如下代码：

```Shell
$ h5ls demo.hdf5
array Dataset {10}
group Group
scalar Dataset{SCALAR}
```

会给出HDF5文件的组成部分名称，和对应的数据结构。加入参数`-vlr`后，会获得更加详细的信息。

### Your First HDF5 File

使用`h5py`操作HDF5文件和Python操作文件非常类似。`h5py`的`File`对象提供了创建数据集和组的功能。类似于Python操作文件，`File`对象同样提供`.filename`和`.mode`属性。

HDF5提供多种模式供文件的读写：

```Python
f = h5py.File("name.hdf5", "w")   # New file overwriting any existing file
f = h5py.File("name.hdf5", "r")   # Open read-only (must exist)
f = h5py.File("name.hdf5", "r+")  # Open read-write (must exist)
f = h5py.File("name.hdf5", "a")   # Open read-write (create if doesn't exist)
```

此外，HDF5提供了额外的模式以避免覆盖已存在的文件。

```Python
f = h5py.File("name.hdf5", "w-")
```

这个模式会创建一个新的文件，但是如果已经有同名文件存在，则创建文件失败。

当Python程序中断或崩溃时，HDF库会自动关闭所有当前打开的文件。

#### Use as a Context Manager

在Python 2.6之后提供了上下文管理器(context managers)的特性。使用这种特性可以自动处理并关闭文件，避免了使用传统`try/except/else/finally`模式的弊端。

#### File Drivers

File drivers用于处理将HDF5文件的地址空间映射到磁盘的机制。通常来说用户不需要考虑这个设置，使用默认值即可。书中给出几种选项作为概览：

- core driver

  Core driver将文件**完全**保存在内存中，同时提供`backing_store`选项，选择`True`将在文件关闭时保存。

  ```Python
  f = h5py.File("name.hdf5", driver="core")
  f = h5py.File("name.hdf5", driver="core", backing_store=True)
  ```

- family driver
  
  当需要将文件拆分为子文件时使用。这个特性主要用来适应文件系统无法处理2GB以上大小文件时。

  ```Python
  # Split the file into 1-GB chunks
  f = h5py.File("family.hdf5", driver="family", memb_size=1024**3)
  ```

- mpio driver

  mpio driver是Parallel HDF5的核心，会在后续章节进行讨论。

#### The User Block

HDF5的一个特性是所有的文件可以由任意用户数据预置。在打开文件时，HDF5库在文件开始处查找HDF5头，然后再文件第512字节处查找，然后第1024字节处查找……这些在文件开始处的空间被成为用户块(user block)，可以在当中存储任何数据。

唯一的限制是块的大小必须为2的幂且必须大于512，同时在写入文件块时不能打开文件：

```Python
In [1]: import numpy as np

In [2]: import h5py

In [3]: f= h5py.File("userblock.hdf5", 'w', userblock_size=512)

In [4]: f.userblock_size
Out[4]: 512

In [5]: f.close()

In [6]: with open("userblock.hdf5", "rb+") as f:
   ...:     f.write("a" * 512)
TypeError: a bytes-like object is required, not 'str'
```

注意这里会出现报错，原因在于Python2和Python3之间的兼容问题。需要将`str`类型转换成`bytes`类型：

```Python
In [7]: with open("userblock.hdf5", "rb+") as f:
   ...:     f.write(str.encode("a") * 512)
```

## Chapter3. Working with Datasets

### Dataset Basics

通过以下简单的代码就可以创建一个HDF5文件，同时将一个`NumPy array`保存到`my dataset`数据集中。

```Python
In [1]: import numpy as np

In [2]: import h5py

In [3]: f = h5py.File("testfile.hdf5")

In [4]: arr = np.ones((5, 2))

In [5]: f["my dataset"] = arr

In [6]: dset = f["my dataset"]

In [7]: dset
Out[7]: <HDF5 dataset "my dataset": shape (5, 2), type "<f8">
```

#### Type and Shape

`Dataset`对象在创建时确定类型，且不能被修改。`Dataset`通常使用标准`NumPy dtype`对象。

```Python
In [8]: dset.dtype
Out[8]: dtype('<f8')

In [9]: dset.shape
Out[9]: (5, 2)
```

`Dataset`对象同样在创建时确定形状，但是可以被修改。

#### Reading and Writing

读取`dataset`和切片操作会返回一个`NumPy array`。

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

在这个过程中，`h5py`将选取数据集中被切片的部分并读取HDF5数据，因此，切片操作会直接读写硬盘。

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

创建数据集并不需要事先已有`NumPy array`的存在。`File`对象的`create_dataset`方法允许根据类型和形状创建空数据集（甚至只需要形状，不需要类型。此时默认类型为`np.float32`单精度浮点数）。

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
-rw-rw-r-- 1 1024 users 4.1G 1月 20 18:05 testfile.hdf5
```

但是，实际发现此时硬盘空间已经真实消耗4G，并未实现书中的示例。查阅资料后发现，应使用如下代码：

```Python
In [23]: del f["big dataset"]

In [24]: f.flush()

In [25]: dset = f.create_dataset("big dataset", (1024**3,), dtype=np.float32, chunks=True)

In [26]: f.flush()

In [27]: !ls -lh testfile.hdf5
-rw-rw-r-- 1 1024 users 4.1K 1月 20 18:06 testfile.hdf5
```

此时验证无误。

参考如下：
> Size on disk of a partly filled HDF5 dataset [StackOverFlow](https://stackoverflow.com/questions/45145389/size-on-disk-of-a-partly-filled-hdf5-dataset?r=SearchResults)

#### Saving Space with Explicit Storage Types

由于HDF5可以接受基本上所有的`NumPy`类型，在没有显式指定保存格式时，`create_dataset`方法会自行推断保存格式。因此，当能够明确数据保存格式时，显式地指定格式可以节省磁盘空间和I/O时间。

通常，为了保证计算精度会使用8位双精度浮点数(`NumPy dtype float64`)进行内存中的计算。但是在数据保存时，常用的方法是使用4位单精度浮点数(`NumPy dtype float32`)进行保存。

```Python
In [28]: bigdata = np.ones((100, 1000))

In [29]: bigdata.dtype
Out[29]: dtype('float64')

In [30]: bigdata.shape
Out[30]: (100, 1000)

In [31]: f.close()
```

显然直接保存时使用的是双精度浮点数，但同样可以指定使用单精度浮点数进行保存。改变保存方法后空间占用节省了一半。

```Python
In [1]: import numpy as np

In [2]: import h5py

In [3]: with h5py.File("big1.hdf5",'w') as f1:
    ...:     f1["big"] = bigdata

In [4]: !ls -lh big1.hdf5
-rwxrwxrwx 1 1024 users 784K 1月 20 18:14 big1.hdf5

In [5]: with h5py.File("big2.hdf5",'w') as f2:
    ...:     f2.create_dataset("big", data=bigdata, dtype=np.float32)

In [6]: !ls -lh big2.hdf5
-rwxrwxrwx 1 1024 users 393K 1月 20 18:15 big2.hdf5
```

但是需要注意的是，一旦指定保存格式后，读取的数据也会变成指定保存的格式。

```Python
In [7]: f1 = h5py.File("big1.hdf5")

In [8]: f2 = h5py.File("big2.hdf5")

In [9]: f1["big"].dtype
Out[9]: dtype('<f8')

In [10]: f2["big"].dtype
Out[10]: dtype('<f4')
```

#### Automatic Type Conversion and Direct Reads

在内存中的双精度向硬盘中的单精度存储时，用户不需要考虑格式转换的问题，HDF5库会自行完成格式转换。但是，当需要从硬盘中储存的单精度读入内存并使用双精度进行运算时，则会带来一定的格式问题。如果数据量极大，显然不能同时在内存中读入单精度数据后再在内存中转换为双精度。

面对这个问题的最佳解决方案为直接向预先分配好正确格式的`NumPy array`中读入硬盘数据。

```Python
In [11]: dset = f2["big"]

In [12]: dset.dtype
Out[12]: dtype('<f4')

In [13]: dset.shape
Out[13]: (100, 1000)
```

读取上节中保存的数据，为单精度浮点数。

```Python
In [14]: big_out = np.empty((100, 1000), dtype=np.float64)  

In [15]: dset.read_direct(big_out)  

In [16]: big_out.dtype
Out[16]: dtype('float64')

In [17]: big_out[0, 0]
Out[17]: 1.0
```

创建双精度浮点数的空数组（`np.empty`不像`np.ones`或`np.zeros`，不需要事先初始化数组），将数据直接读入，可以看到HDF5填充了空数组，并使用了给定的格式。

#### Reading with astype

做格式转换时不一定每次都创建空数组然后读入。使用`Dataset.astype`上下文管理器同样可以起到类似的功能。

```Python
In [18]: with dset.astype("float64"):
    ...:     out = dset[0, :]

In [19]: out.dtype
Out[19]: dtype('float64')

In [20]: f1.close()

In [21]: f2.close()
```

当使用HDF5自动类型转换时，需要记住以下几点：

- 转换仅限于数值型之间，如整型和浮点型、不同精度浮点型之间的转换，HDF5不支持字符型和数值型之间的转换。
- 当从高精度向低精度转换时，HDF5会对数据进行截断。

  ```Python
  In [1]: import numpy as np

  In [2]: import h5py

  In [3]: f = h5py.File("testfile.hdf5")

  In [4]: f.create_dataset("x", data=1e256, dtype=np.float64)
  Out[4]: <HDF5 dataset "x": shape (), type "<f8">

  In [5]: print(f["x"][...])
  1e+256

  In [6]: f.create_dataset("y", data=1e256, dtype=np.float32)
  Out[6]: <HDF5 dataset "y": shape (), type "<f4">

  In [7]: print(f["y"][...])
  inf
  ```

  在这个过程中，HDF5不会做任何提示，因此建议随时注意使用的数据类型。

#### Reshaping an Existing Array

只要总元素数量一致，HDF5支持写入和原始`NumPy array`形状不同的数据，同时不会有任何性能损耗。

```Python
In [8]: imagedata = np.random.rand(100, 480, 640)

In [9]: imagedata.shape
Out[9]: (100, 480, 640)

In [10]: f.create_dataset("newshape", data=imagedata, shape=(100, 2, 240, 640))
Out[10]: <HDF5 dataset "newshape": shape (100, 2, 240, 640), type "<f8">
```

#### Fill Values

当创建新数据集时，默认会使用0填充数据集：

```Python
In [11]: dset = f.create_dataset("empty", (2, 2), dtype=np.int32)

In [12]: dset[...]
Out[12]:
array([[0, 0],
       [0, 0]], dtype=int32)
```

但是同样，也可以选择不同的默认值对数据集进行填充，如-1或NaN等，使用`fillvalue`参数即可。填充的数值只有当数据被读取的时候才会被处理，因此并不会占用额外的存储空间。但是一旦在创建数据集时被确定，则不能被更改，即该数据集所有的空值都会以创建数据集时定义的值填充，除非空值被写入其他值，`fillvalue`同样会作为数据集的属性被记录。

```Python
In [13]: dset = f.create_dataset("filled", (2, 2), dtype=np.int32, fillvalue=42)

In [14]: dset[...]
Out[14]:
array([[42, 42],
       [42, 42]], dtype=int32)

In [15]: dset.fillvalue
Out[15]: 42

In [16]: f.close()
```

### Reading and Writing Data

#### Using Slicing Effectively

```Python
In [1]: import numpy as np

In [2]: import h5py

In [3]: f1 = h5py.File("big1.hdf5")

In [4]: f2 = h5py.File("big2.hdf5")

In [5]: dset = f2["big"]

In [6]: dset
Out[6]: <HDF5 dataset "big": shape (100, 1000), type "<f4">

In [7]: out = dset[0:10, 20:70]

In [8]: out.shape
Out[8]: (10, 50)

In [9]: f1.close()

In [10]: f2.close()
```

在进行切片操作时，`h5py`进行了如下操作：

1. 确定目标数据的形状，在这里是(10, 50)
2. 创建一个符合目标形状的empty `NumPy array`
3. HDF5选出数据集中需要的部分
4. HDF5将数据复制到空`NumPy array`中
5. 返回新填充的数组

由此可见，在每一次进行切片操作时，HDF5都会先确定切片形状，创建空数组，选择数据集范围，然后才会开始读取数据。因此，提升数据读取性能的关键一步就是**选择合理的切片形状**。

```Python
# Check for negative values and clip to 0

# Case 1
for ix in xrange(100):
    for iy in xrange(1000):
        val = deset[ix, iy]            # Read one element
        if val < 0: dset[ix, iy] = 0  # Clip to 0 if needed

# Case 2
for ix in xrange(100):
    val = dset[ix, :]  # Read one row
    val[val < 0] = 0  # Clip negative values to 0
    dset[ix, :] = val  # Write row back out
```

在上例中，从(100, 1000)的数据集进行切片，方法2会有更好的效率。因为方法1会进行100000次切片而方法2只进行了100次切片。

尽管方法1中在内存中进行了`NumPy arrays`的切片，但是一旦在HDF5的机制下会降低性能。

HDF5写入数据和读入数据类似，会先确定数据的形状，确认数据集是否可以进行处理。然后在数据集中选定合适的形状进行写入。因此，一次一个元素、或一次很少的元素写入会极大地降低处理性能。

#### Start-Stop-Step Indexing

h5py使用和`NumPy`几乎相同的切片方式，包括含有步长的切片。

```Python
In [1]: import numpy as np

In [2]: import h5py

In [3]: f = h5py.File("testfile.hdf5")

In [4]: dset = f.create_dataset("range", data=np.arange(10))

In [5]: dset[...]
Out[5]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

In [6]: dset[4]
Out[6]: 4

In [7]: dset[4:8]
Out[7]: array([4, 5, 6, 7])

In [8]: dset[4:8:2]
Out[8]: array([4, 6])

In [9]: dset[:]
Out[9]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

In [10]: dset[4:-1]
Out[10]: array([4, 5, 6, 7, 8])
```

但是，`NumPy`中的一些技巧并不被HDF5支持，如使用步长-1进行数组倒序的操作，在`NumPy`中是可行的而HDF5数据集中会报错，因为步长必须大于等于1。

```Python
In [11]: a
Out[11]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

In [12]: a[::-1]
Out[12]: array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

In [13]: dset[::-1]
ValueError: Step must be >= 1 (got -1)
```

#### Multidimensional and Scalar Slicing

HDF5使用`...`进行切片，在Python中被称为`Ellipsis`，对无需指定的轴进行全选。

```Python
In [14]: dset = f.create_dataset("4d", shape=(100, 80, 50, 20))

In [15]: dset[0,...,0].shape
Out[15]: (80, 50)

In [16]: dset[...].shape
Out[16]: (100, 80, 50, 20)
```

一种较为特殊的情况是所谓的标量(scalar)数据。在`NumPy`中有两种方式储存一个元素的数据。

第一种方式是一个形状为(1,)的一维数组，这种结构可以通过切片或者索引获取数据。

```Python
In [17]: dset = f.create_dataset("1d", shape=(1,), data=42)

In [18]: dset.shape
Out[18]: (1,)

In [19]: dset[0]
Out[19]: 42

In [20]: dset[...]
Out[20]: array([42])
```

这种方式下，使用`Ellipsis`会返回一个元素的数组，而使用索引会直接返回这个元素本身。

第二种方式形状为()，是一个空元组。这种方式不能通过索引获取数据。

```Python
In [21]: dset = f.create_dataset("0d", data=42)

In [22]: dset.shape
Out[22]: ()

In [23]: dset[0]
ValueError: Illegal slicing argument for scalar dataspace

In [24]: dset[...]
Out[24]: array(42)
```

在这种方式下，使用`Ellipsis`同样会返回一个数组，在这里是一个标量数组(scalar array)。

如果在这种方式下同样想获得元素本身，而不是一个`NumPy array`，可以使用一种看似比较奇怪的方式获取：

```Python
In [25]: dset[()]
Out[25]: 42
```

因此：

1. `Ellipsis`始终会以`NumPy array`的形式给出数据集所有的数据
2. 使用空元组(empty tuple"()")也会给出数据集中所有的元素，当一维或更高维时，同样给出数组结构，当0D时，给出标量元素。
3. 在一些历史代码中会见到类似`.value`的形式，这种方式完全等价于`dataset[()]`，在后续`h5py`的版本中将不会再支持。

#### Boolean Indexing

HDF5同样支持使用布尔值进行索引。

```Python
In [26]: data = np.random.random(10) * 2 - 1

In [27]: data
Out[27]:
array([-0.39438298, -0.5841106 , -0.85382983,  0.48593953,  0.73904431,
        0.91193146, -0.30166953,  0.54883998,  0.04091559,  0.21349258])

In [28]: dset = f.create_dataset("random", data=data)

In [29]: dset[data < 0] = 0

In [30]: dset[...]
Out[30]:
array([0.        , 0.        , 0.        , 0.48593953, 0.73904431,
       0.91193146, 0.        , 0.54883998, 0.04091559, 0.21349258])

In [31]: dset[data < 0] = -1 * data[data < 0]

In [32]: dset[...]
Out[32]:
array([0.39438298, 0.5841106 , 0.85382983, 0.48593953, 0.73904431,
       0.91193146, 0.30166953, 0.54883998, 0.04091559, 0.21349258])
```

在这个过程中，先对`data`进行布尔值判断，随后HDF5将布尔值转化为数据集中的坐标进行赋值读取等操作。这种方式带来两个结果：

1. 对于有很多`True`值的极大的索引表达式，在Python端修改数据后再写入数据集会更快。
2. 表达式右侧的值要么是一个标量，要么是一个完全等同于选出数据形状的数组。尽管看似比较复杂，但是实际上当符合条件数据很少时，这是一种非常有效的更新数据的方式。

需要注意的是，在上例中始终是选择`data`进行布尔运算，选择`data`进行赋值，因此`dset`本身没有被覆盖。也可以使用类似于`Pandas DataFrame`的赋值方式，则会直接覆盖`dset`本身。

```Python
In [33]: dset[dset < 0] = 0
TypeError: unorderable types: Dataset() < int()

In [34]: dset[dset[...] > 0.5] = 0

In [35]: dset[...]
Out[35]:
array([0.39438298, 0.        , 0.        , 0.48593953, 0.        ,
       0.        , 0.30166953, 0.        , 0.04091559, 0.21349258])
```

#### Coordinate Lists

`h5py`还从`NumPy`中使用了一些其他的特性，如使用列表进行切片的功能。

```Python
In [36]: dset = f["range"]

In [37]: dset[...]
Out[37]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

In [38]: dset[[1,2,7]]
Out[38]: array([1, 2, 7])

In [39]: f.close()
```

但是`h5py`仍然和`NumPy`有一些不同，主要在于：

1. 一次只能对一根轴上进行列表切片
2. 不能使用重复的列表元素
3. 列表中的索引必须严格递增

#### Automatic Broadcasting

在之前的代码中，使用过`dset[data < 0] = 0`这样的代码，这种表达式使用了类似`NumPy`中的广播(broadcasting)操作。这种操作能够极大地提升性能。

```Python
In [1]: import numpy as np

In [2]: import h5py

In [3]: f2 = h5py.File("big2.hdf5")

In [4]: dset = f2["big"]

In [5]: dset.shape
Out[5]: (100, 1000)

'''alternative method:

data = dset[0,:]
for idx in xrange(100):
    dset[idx,:] = data
'''

In [6]: dset[:, :] = dset[0, :]
```

在例子中，如果需要复制第0行数据并填充剩下的所有行，尽管可以使用循环赋值，但是这样会进行之前所说的多次切片的行为，而且需要保证边际条件准确无误。使用广播则完全没有这方面的问题，同时在性能上也能有很好的提升。

表达式右侧是(1000,)的数组，左侧是(100, 1000)的数组，由于最后一个维度相同，因此`h5py`会自动将所有100行的索引全部重复赋值。这种操作只进行了一次切片，剩余的操作会在将数据写入硬盘时完成。

#### Reading Directly into an Existing Array

回到将HDF5数据直接填入数组中并进行自动格式转换的操作。之前已展示过将`np.float32`数据读入`np.float64`数组中：

```Python
In [7]: dset.dtype
Out[7]: dtype('<f4')

In [8]: out = np.empty((100, 1000), dtype=np.float64)

In [9]: dset.read_direct(out)
```

但是这种方法需要一次性读入所有数据。实际上，还有更加实用的方法。如果需要读第1行所有数据`dset[0,:]`然后将其存入数组第51行`out[50,:]`，可以使用`source_sel`和`dest_sel`关键字，对应*source selection*和*destination selection*。

```Python
In [10]: dset.read_direct(out, source_sel=np.s_[0,:], dest_sel=np.s_[50,:])
```

其中比较奇怪的部分是参数中的`np.s_`，这对out进行了切片操作，返回了一个`NumPy slice`对象。

此外，输出的数组不需要和数据集形状相同，例如求均值，常规做法为：

```Python
In [11]: out = dset[:,0:50]

In [12]: out.shape
Out[12]: (100, 50)

In [13]: means = out.mean(axis=1)

In [14]: means.shape
Out[14]: (100,)
```

使用`read_direct`的做法为：

```Python
In [15]: out = np.empty((100,50), dtype=np.float32)

In [16]: dset.read_direct(out, np.s_[:,0:50])  # dset_sel can be omitted

In [17]: means = out.mean(axis=1)

In [18]: f2.close()
```

单纯上看这两种方法没有什么区别，但是实际上有一些显著的区别。第一种方法中，`out`数组直接通过`h5py`生成，用以存放数据切片；第二种方法中，`out`数组由用户分配，在后续的运算中仍然可以继续使用。

性能方面，(100, 50)的数组很难看出差异，但是当数据量提升后，会发现性能上的差异逐渐明显。

```Python
In [1]: import numpy as np

In [2]: import h5py

In [3]: f = h5py.File("testfile.hdf5")

In [4]: dset = f.create_dataset("perftest", (10000, 10000), dtype=np.float32)

In [5]: dset[:] = np.random.random(10000)  # note the use of broadcasting!

In [6]: def time_simple():
     ...:     dset[:,0:500].mean(axis=1)

In [7]: out = np.empty((10000, 500), dtype=np.float32)

In [8]: def time_direct():
     ...:     dset.read_direct(out, np.s_[:,0:500])
     ...:     out.mean(axis=1)
```

使用`IPython`的`%timeit`魔法方法进行100000000循环后发现，第二种方法在性能上提升了约18%。随着数据量的扩大，`read_direct`的性能优势越明显。

```Python
In [9]: %timeit time_simple
16.6 ns ± 0.163 ns per loop (mean ± std. dev. of 7 runs, 100000000 loops each)

In [10]: %timeit time_direct
13.6 ns ± 0.0798 ns per loop (mean ± std. dev. of 7 runs, 100000000 loops each)
```

由于一些历史原因，仍然存在`read_direct`的逆方法`write_direct`。但是在当前版本的`h5py`中，这种方法相对于常规的切片操作不会有任何性能上的优势。

#### A Note on Data Types

这一节中提到了不同计算机系统间，关于不同字节序的问题。由于不同CPU架构下储存数据的方式不同，当存储数据在不同系统间交互的时候，可能会带来数据类型上的问题。现代Intel x86芯片都使用little-endian格式，但是由于HDF5同样支持big-endian格式，因此`h5py`会默认使用数据存储时使用的格式。根据书中的内容，在x86架构下，两种数据格式会在性能上有接近两倍的差距。

```Python
In [11]: a = np.ones((1000,1000), dtype="<f4")  # Little-endian 4-byte float

In [12]: b = np.ones((1000,1000), dtype=">f4")  # Big-endian 4-byte float

In [13]: %timeit a.mean
30.7 ns ± 1.59 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

In [14]: %timeit b.mean
29.8 ns ± 0.724 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
```

可能是由于当前系统更加优化的原因，这种性能上的差距并不能成功复现。当然书中也提及了如何转换数据格式的方法。

```Python
In [15]: c = b.view("float32")

In [16]: c[:] = b

In [17]: b = c

In [18]: %timeit b.mean
30.3 ns ± 0.824 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
```

数据格式的差异通常会带来性能上的差异。单精度与双精度，甚至浮点数与整型都会产生巨大差异，甚至导致数据计算上的错误。因此，在使用HDF5时，时刻记得检查数据格式，必要时使用HDF5提供的格式转换功能。

### Resizing Datasets

前文已经讲到，当创建一个数据集后，数据集的类型就已经固定，并且不能改变。但是，数据集的形状是可以改变的。但是，尽管形状可以改变，仍然有诸多限制。

```Python
In [19]: dset = f.create_dataset("fixed", (2, 2))

In [20]: dset.shape
Out[20]: (2, 2)

In [21]: dset.maxshape
Out[21]: (2, 2)

In [22]: dset.resize((1,1))
TypeError: Only chunked datasets can be resized
```

在这里，如果想将(2,2)的数据变为(1,1)，会直接引发报错。显然，如果需要改变形状，还需要其他的一些条件。

#### Creating Resizable Datasets

当创建一个数据集时，除了确定数据集的形状，还可以确定数据集最大可以resize的维度。在`h5py`中，这个属性为`maxshape`，即上例中的另一个属性。

类似于`shape`，`maxshape`同样是在数据集创建时确定，但是和`shape`不同，`maxshape`一旦被确定则不能修改。如果创建数据集时用户没有显式地指定`maxshape`，HDF5就会创建一个不可改变形状的数据集，同时设置`maxshape = shape`。同时，这个数据集也会使用连续存储(*contiguous storage*)，这个设置也会阻止resize。关于连续存储和分块存储(*chunked storage*)的区别会在后面章节讨论。

当设置了`maxshape`后，会发现resize的操作已经可以实现了。

```Python
In [23]: dset = f.create_dataset("resizable", (2, 2), maxshape=(2, 2))

In [24]: dset.shape
Out[24]: (2, 2)

In [25]: dset.maxshape
Out[25]: (2, 2)

In [26]: dset.resize((1,1))

In [27]: dset.shape
Out[27]: (1, 1)

```

同样，形状也可以改变回去，但是显然，改变的形状不能超过`maxshape`给定的大小。

```Python
In [28]: dset.resize((2,2))

In [29]: dset.shape
Out[29]: (2, 2)

In [30]: dset.resize((2,3))
ValueError: Unable to set extend dataset (dimension cannot exceed the existing maximal size (new: 3 max: 2))
```

这个设定带来的一个问题在于，如果创建数据集时不确定最大使用的形状应该如何处理。显然，HDF5不会要求用户使用一个非常大的数定义`maxshape`，HDF5使用`None`标记无限制的状况。如果数据集的某轴被设置为`None`，则resize不会受形状上限的控制。

```Python
In [31]: dset = f.create_dataset("unlimited", (2, 2), maxshape=(2, None))

In [32]: dset.shape
Out[32]: (2, 2)

In [33]: dset.maxshape
Out[33]: (2, None)

In [34]: dset.resize((2, 3))

In [35]: dset.shape
Out[35]: (2, 3)

In [36]: dset.resize((2, 2**30))

In [37]: dset.shape
Out[37]: (2, 1073741824)
```

无论如何改变数据集的形状，总维度是不能改变的，数据集的`rank`从一开始即被固定且永远不能被改变。

```Python
In [38]: dset.resize((2, 2, 2))
TypeError: New shape length (3) must match dataset rank (2)
```

#### Data Shuffling with resize

在`NumPy`中，改变数组形状会有一些特性，以一个数组为例：

```Python
In [39]: a = np.array([[1, 2], [3, 4]])

In [40]: a.shape
Out[40]: (2, 2)

In [41]: print(a)
[[1 2]
 [3 4]]
```

如果将这个`NumPy array`改变形状，同时保持元素数量不变，则会得到如下结果：

```Python
In [42]: a.resize((1,4))

In [43]: print(a)
[[1 2 3 4]]
```

如果将数组继续扩大，则会追加新的元素，并使用0进行填充：

```Python
In [44]: a.resize((1,10))

In [45]: print(a)
[[1 2 3 4 0 0 0 0 0 0]]

```

> 辨析：`NumPy array`的`resize`和`reshape`方法：
>
> `resize`会直接修改原数组，没有返回值而`reshape`不会修改原数组，返回值为一个新的数组

这种操作在`NumPy`中非常普遍。但是，在HDF5中，`resize`会有完全不同的机制。通过创建一个新的数据集进行验证：

```Python
In [46]: dset = f.create_dataset("sizetest", (2, 2), dtype=np.int32, maxshape=(None, None))

In [47]: dset[...] = [[1, 2], [3, 4]]

In [48]: dset[...]
Out[48]:
array([[1, 2],
       [3, 4]], dtype=int32)
```

如果对这个数据集使用类似与`NumPy`中同样的操作，会发现得出了完全不同的结果：

```Python
In [49]: dset.resize((1, 4))

In [50]: dset[...]
Out[50]: array([[1, 2, 0, 0]], dtype=int32)

In [51]: dset.resize((1, 10))

In [52]: dset[...]
Out[52]: array([[1, 2, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int32)
```

HDF5不会重新整理数据。如果将(2, 2)的数据变形为(1, 4)，则数据集中`[1, 0]`和`[1, 1]`的数据不会被重新整理，而是会直接消失。因此，在HDF5中，使用`resize`必须非常谨慎，套用NumPy中的经验会导致不可预知的后果。

此外，新添加的数据被初始化为0，这个行为可以使用之前提过的`fillvalue`进行调整。

#### When and How to Use resize

当需要对HDF5数据集进行追加时，合理的使用`resize`可以保证性能。

如果一个数据集每次需要储存1000个元素的数据，但是一开始并不知道会储存多少行，一种显而易见的方法是每次有1000个元素加入，数据集就增加一行。但是这样带来的问题在于，每一次数据的插入都会让数据集resize一次。当添加数据次数很大时，这种方法显得不那么合适。

```Python
In [53]: dset1 = f.create_dataset("timetraces1", (1, 1000), maxshape=(None, 1000))

In [54]: def add_trace_1(arr):
     ...:     dset1.resize((dset1.shape[0] + 1, 1000))
     ...:     dset1[-1, :] = arr
```

因此，另一种方式是记录追加的次数，在全部数据追加完成后，一次性进行resize：

```Python
In [55]: dset2 = f.create_dataset("timetraces2", (5000, 1000), maxshape=(None, 1000))

In [56]: ntraces = 0

In [57]: def add_trace_2(arr):
     ...:     global ntraces
     ...:     dset2[ntraces, :] = arr
     ...:     ntraces += 1

In [58]: def done():
     ...:     dset2.resize((ntraces, 1000))

In [60]: f.close()
```

这种方法在实际运用中会有更好的性能表现。

## Chapter4. How Chunking and Compression Can Help You

### Contiguous Storage

首先，创建一个含有4个元素的二维数组。

```Python
In [1]: import numpy as np

In [2]: import h5py

In [3]: a = np.array([['A', 'B'], ['C', 'D']])

In [4]: print(a)
[['A' 'B']
 ['C' 'D']]

In [5]: a[1, 1]
Out[5]: 'D'
```

显然，可以使用索引方式获取其中的元素。但是在内存中，并不存在二维的存储空间。数组中的元素实际上是被存在一维的缓存中，即：`'A' 'B' 'C' 'D'`，这种方法就被称为*contiguous storage*。因为无论保存在硬盘还是内存中的数据，都是一一排列进行存储。

在默认情况下，只有比较小的HDF5数据集会使用contiguous storage。数据集中的数据会被摊平(flattened)并存储至磁盘中，就像`NumPy`和`C`所做的一样。

在这种机制下，显然一些特定的操作会显著快于其他的操作。

如果创建一个(100, 480, 640)的数组用于存放100张640×460像素的图片，一个contiguous的数据集会将数据按照每640个元素进行排列并连续储存。

```Python
In [6]: f = h5py.File("imagetest.hdf5")

In [7]: dset = f.create_dataset("Images", (100, 480, 640), dtype="uint8")
```

如果需要读取第一张图片的数据，则可以使用切片获取：

```Python
In [8]: image = dset[0, :, :]

In [9]: image.shape
Out[9]: (480, 640)
```

在这种存储方式下，每640个元素组成一个block，当读取第一张图片时，从磁盘中读取480个block合并成为一个大的block。因此，处理数据的一个原则是*locality*，即读取存储在一起的数据会更快。

使用contiguous方式存储数据的好处就是磁盘分布会完全匹配数据集的形状，随着索引移动的过程也是数据在磁盘中的顺序。

但是，如果并不是整张图片的提取，而是在图片中提取一部分，例如在第一张图中提取左上角64×64的部分：

```Python
In [10]: tile = dset[0, 0:64, 0:64]

In [11]: tile.shape
Out[11]: (64, 64)
```

在这种情况下，数据就无法连续的读取，而是需要在第一个640的block中提取索引0-63的数据，随后移动至第二个640的block，提取索引640-703的数据，随后移动至第三个640的block，提取索引1280-1343的数据并以此类推。如果需要在100张图片中都做类似的处理，则会使用这种方式读取整个数据集。因此这种默认使用contiguous的存储机制在上述情况下没有很好的表现。

### Chunked Storage

解决上述问题的方法就是使用分块(*chunking*)。这种方式会让用户明确最符合数据读写需求的N维形状。当将数据写入磁盘时，HDF5先将数据分割为指定形状的分块(*chunk*)，将其摊平后再存入磁盘。这些分块会被分别保存至文件系统不同的地方，使用B树进行索引。

仍然以图片数据为例，同样是(100, 480, 640)的数据集，但是使用分块格式进行保存，这需要在`create_dateset`方法中使用一个新的关键字`chunks`：

```Python
In [12]: dset = f.create_dataset("chunked", (100, 480, 640), dtype="i1", chunks=(1, 64, 64))
```

分块形状(*chunk shape*)在数据集创建时便确定，并且不能进行更改，可以使用`chunks`属性确认分块的形状，如果返回`None`，则说明数据集没有使用分块存储。

```Python
In [13]: dset.chunks
Out[13]: (1, 64, 64)

In [14]: dset[0, 0:64, 0:64]
Out[14]:
array([[0, 0, 0, ..., 0, 0, 0],
       [0, 0, 0, ..., 0, 0, 0],
       [0, 0, 0, ..., 0, 0, 0],
       ...,
       [0, 0, 0, ..., 0, 0, 0],
       [0, 0, 0, ..., 0, 0, 0],
       [0, 0, 0, ..., 0, 0, 0]], dtype=int8)
```

在分块存储下，同样提取第一张图左上角64×64的数据，HDF5从`[0, 0, 0]`开始查找，随后查找`[0, 0, 64]`，直到`[99, 448, 512]`和`[99, 448, 576]`为止（因为一次查找一个分块，即64×64）。在这里，只需读取一个分块即可。

更好的是，由于分块数据已经使用整齐的方式存储，因此可以在读写时使用任一种操作。例如HDF5在压缩文件的压缩和解压缩时就使用了分块。

使用分块只需要知道这是一种存储方式，不需要在读写分块数据集时做任何特殊操作，只需要使用标准`NumPy`切片代码，剩下的HDF5会自行处理。

### Setting the Chunk Shape

#### Auto-Chunking

大部分情况下，`h5py`会自动选择分块的形状，即`h5py`中的自动分块(*auto-chunker*)功能。只需要在`chunks`参数中用`True`替代指定的元组就可以让`h5py`进行自动推断：

```Python
In [15]: dset = f.create_dataset("Images2", (100, 480, 640), 'f', chunks=True)

In [16]: dset.chunks
Out[16]: (7, 30, 80)
```

自动分块会尽量选择在N维下在一定大小范围内最“方”的分块，这个操作也会在没有明确指定分块形状时使用。

因为自动分块无法识别对后续数据集操作的方式，因此会选择最方形的分块来做出权衡。因此如果只是想对文件进行压缩而不用考虑过多细节，同时没有对时间效率上的严格需求，那么使用自动分块选择是比较合适的。同时，分块的选择也会受到系统层面的影响（书中的分块形状是(13, 60, 80)）。

经过测试，当数据集形状不是很常见时（在测试中使用了质数参数），自动分块同样有效：

```Python
In [17]: dset = f.create_dataset("ImagesPrime", (101, 479, 641), 'f', chunks=True)

In [18]: dset.chunks
Out[18]: (7, 30, 81)

In [19]: f.close()
```

#### Manually Picking a Shape

当需要手动选择分块形状时，需要在以下三个限制条件中进行权衡：

  1. 在给定的数据集下，更大的分块会减少分块B树的大小，从而使索引更加容易，提升找到和读取分块的速度。
  2. 因为分块的使用是"all or nothing"的模式，即要么不读取这个分块，要么就会读取整个分块，即使只需要分块中的部分数据。因此，更大的分块可能会导致将不必要的数据读入内存。
  3. HDF5 的高速缓存(cache)只能容纳有限的分块，大于1MiB的分块不会被载入到缓存中。

因此，当需要进行手动分块设置时，需要考虑：

- 是否有必要指定分块大小。应当将手动指定分块大小限制在只有确定对数据集的后续使用方法，同时使用连续存储或者自动分块会明显降低效率的情况下。
- 尽量使用在数据处理时最自然的方式选择分块。例如上文中图像处理的例子，使用N×64×64或N×128×128会是比较合理的选择。
- 分块不要太小。由于HDF5是使用B树进行索引，因此如果分块过小，比如1-byte，那么磁盘空间会被大量的元数据(metadata)占据。最好将分块的大小设置在10KiB以上。
- 分块不要太大。由于分块的读取是一次读取一整个分块，因此如果只需要部分数据，那么会有时间浪费在读取分块中不需要的数据上。同时，由于大于1Mib的分块不会被读入高速缓存中，而是每次直接从磁盘里读取，过大的分块也会导致效率的降低。

### Performance Example: Resizable Datasets

在第三章中讨论了resizable数据集的性能问题，但是实际上HDF5要求这样的数据集都是以分块存储方式存储的。显然，因为连续存储方式存储的数据集，一旦对数据集形状进行改变，则必须要重写整个数据集。

在使用分块对resizable数据集进行处理时，会有一些潜在的隐患，特别是当对性能要求极高时使用自动分块。

使用第三章在`testfile.hdf5`文件中创建的数据集`timetraces1`和`timetraces2`。这两个数据集都是在行上可拓展的数据集，唯一的区别在于两个数据集的初始形状不同。

```Python
In [1]: import numpy as np

In [2]: import h5py

In [3]: f = h5py.File("testfile.hdf5")

In [4]: dset1 = f["timetraces1"]  # dset1 = f.create_dataset("timetraces1", (1, 1000), maxshape=(None, 1000))

In [5]: dset2 = f["timetraces2"]  # dset2 = f.create_dataset("timetraces2", (5000, 1000), maxshape=(None, 1000))
```

在第三章中提到，对数据集追加数据有两种方式：直接追加(`add_trace_1`)和全部追加后再重组(`add_trace_2` and `done`)。根据第三章的结论，方法二会快于方法一，因为方法二进行了更少次数的resize。

```Python
In [6]: def add_trace_1(arr):
   ...:     """ Add one trace to the dataset, expanding it as necessary """
   ...:     dset1.resize((dset1.shape[0] + 1, 1000))
   ...:     dset1[-1, :] = arr

In [7]: ntraces = 0

In [8]: def add_trace_2(arr):
   ...:     """ Add one trace to the dataset, keeping count of the # of traces written """
   ...:     global ntraces
   ...:     dset2[ntraces, :] = arr
   ...:     ntraces += 1

In [9]: def done():
   ...:     """ After all calls to add_trace_2, trim the dataset to size """
   ...:     dset2.resize((ntraces, 1000))
```

通过`%timeit`测试运行时间：

```Python
In [10]: def setup():
    ...:     """ Re-initialize both datasets for the tests """
    ...:     global data, N, dset1, dset2, ntraces
    ...:     data = np.random.random(1000)
    ...:     N = 10000  # Number of iterations
    ...:     dset1.resize((1, 1000))
    ...:     dset2.resize((10001, 1000))
    ...:     ntraces = 0

In [11]: def test1():
    ...:     """ Add N traces to the first dataset """
    ...:     for idx in range(N):
    ...:         add_trace_1(data)

In [12]: def test2():
    ...:     """ Add N traces to the second dataset, and then trim it """
    ...:     for idx in range(N):
    ...:         add_trace_2(data)
    ...:     done()

In [13]: setup()

In [14]: %timeit test1
13.4 ns ± 0.0248 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

In [15]: setup()

In [16]: %timeit test2
13.5 ns ± 0.034 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
```

结果发现结果并不符合预期。（注意这里必须手动使用`setup()`对`global`变量进行重置，否则无法复现书中结果。即使使用`timeit.timeit()`函数中的`setup=`参数也同样无法复现。）

此时再观察数据集的分块大小可以看出：

```Python
In [17]: dset1.chunks
Out[17]: (1, 1000)

In [18]: dset2.chunks
Out[18]: (157, 63)
```

显然，由于自动分块时设置分块的形状是基于数据集初始化时的形状，无法适应当前程序下对分块形状的要求。如果在创建数据集时手动指定分块的大小后，结果会有所不同：

```Python
In [19]: dset1 = f.create_dataset("timetraces3", (1, 1000), maxshape=(None, 1000), chunks=(1, 1000))

In [20]: dset2 = f.create_dataset("timetraces4", (5000, 1000), maxshape=(None, 1000), chunks=(1, 1000))

In [21]: setup()

In [22]: %timeit test1
13.5 ns ± 0.0203 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

In [23]: setup()

In [24]: %timeit test2
13.4 ns ± 0.0323 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

In [25]: f.close()
```

此时发现，方法二的性能得到了提升（使用`timeit.timeit()`函数观察效果会更加明显）。

### Filters and Compression

如果对使用连续存储的数据集进行压缩，显而易见会出现的问题是，每次写入一个元素时，都必须重复解压缩，写入，再压缩的过程。总之，如果需要进行压缩，必须要能够根据使用的数据产出不同大小的结果。

使用分块可以对数据集更好的进行压缩。因为一旦数据集是使用分块保存，则每个分块的初始大小就会固定，而且因为每个分块由B树进行索引，因此可以分布在磁盘的任意位置，而非一个接着一个排列。换句话说，每个分块都可以自由放大或缩小而不涉及其他的分块。

#### The Filter Pipeline

HDF5使用了称作过滤器管道(filter pipeline)的概念，即写入每个分块时进行的一系列操作。每一个过滤器(filter)可以对分块中的数据进行任何处理。当文件读取时，每个filter会进行“反向操作”模式，重新构建原始数据。

当使用`GZIP`和`SHUFFLE`过滤器处理一个数据集时：

  1. `Numpy array` $\Longleftrightarrow$ `Dataset slice` $\Longleftrightarrow$ `HDF5 chunk tree`：即`Numpy array`、数据集切片和HDF5对分块构成的B树索引间互相转化。
  2. `HDF5 chunk tree` $\Longleftrightarrow$ `chunk`：即通过B树找到对应的分块。
  3. 在使用`GZIP`和`SHUFFLE`过滤器时：
      - Writing: `chunk` $\longrightarrow$ `Shuffle` $\longrightarrow$ `GZIP compress` $\longrightarrow$ `DISK`
      - Reading: `DISK` $\longrightarrow$ `GZIP decompress` $\longrightarrow$ `Unshuffle` $\longrightarrow$ `chunk`

注意，在整个流程中，原子级的操作对象是**分块**，在读写任意一个数据，即使只有一个元素时，也是对整个分块的读写和压缩解压缩。这点在选择分块形状，或者决定是否使用压缩时必须要考虑。

#### Compression Filters

HDF5支持多种压缩过滤器，最常见的是GZIP过滤器，也被称作DEFLATE过滤器。

在对一个浮点数数据集进行GZIP压缩时：

```Python
In [1]: import numpy as np

In [2]: import h5py

In [3]: f = h5py.File("testfile.hdf5")

In [4]: dset = f.create_dataset("BigDataset", (1000, 1000), dtype="f", compression="gzip")

In [5]: dset.compression
Out[5]: 'gzip'
```

GZIP并不局限于浮点数，可以对所有固定长度的HDF5格式有效。同时数据也可以正常读写：

```Python
In [6]: dset[...] = 42.0

In [7]: dset[0, 0]
Out[7]: 42.0
```

同时可以看到数据集的一些属性：

```Python
In [8]: dset.compression_opts
Out[8]: 4

In [9]: dset.chunks
Out[9]: (63, 125)
```

`compression_opts`属性显示了compression filter的设置，对应`create_dataset`时设置的关键字参数。在这里，默认的GZIP等级是4。同时自动分块选择了(63, 125)作为分块形状，在压缩时，数据被拆分为63 \* 125 \* (4 bytes) = 30 KiB大小的区块进行处理。

#### GZIP/DEFLATE Compression

使用GZIP过滤器进行处理时最简单且移植性最好的方式，因为所有的HDF5都含有这种过滤器，此外GZIP还有如下优点：

- 支持所有的HDF5数据类型
- HDF5内置，任何地方都能使用
- 适中的压缩速度
- 可以使用SHUFFLE过滤器提升性能

对于GZIP压缩，`compression_opts`可以选择从0到9，默认值为4：

```Python
In [10]: dset = f.create_dataset("Dataset1", (1000,), compression="gzip")

In [11]: dset = f.create_dataset("Dataset2", (1000,), compression=9)

In [12]: dset.compression
Out[12]: 'gzip'

In [13]: dset.compression_opts
Out[13]: 4
```

#### SZIP Compression

SZIP是美国国家航空航天局(NASA)持有的专利压缩技术。通常只有当需要处理卫星数据时才会用到。由于专利限制，很多HDF5安装包禁止了这种压缩方式（但是没有限制解压缩）。

```Python
In [14]: dset = f.create_dataset("Dataset3", (1000,), compression="szip")

In [15]: dset.compression
Out[15]: 'szip'
```

SZIP的特性是：

- 只支持整型(1, 2, 4, 8 byte; signed/unsigned)和浮点型(4/8 byte)数据类型
- 高速压缩和解压缩
- 通常都支持解压缩

#### LZF Compression

对于只在Python中处理的文件，使用LZF是一个非常好的选择。这种方式内置在`h5py`模块中，基于BSD开源许可协议，C源码可以在第三方程序中使用。相对于GZIP，LZF对在低压缩比下的超高速压缩进行了优化。LZF的最佳使用场景是数据集非常大且有非常多冗余数据点时。对于LZF没有`compression_opts`选项：

```Python
In [16]: dset = f.create_dataset("Dataset4", (1000,), compression="gzip")

In [17]: dset.compression
Out[17]: 'lzf'
```

#### Performance

同样，应该进行性能测试以确定提升性能的关键点，书中针对不同的情况提供了一些案例。在这个实验中，一个单精度浮点值组成的4MB的数据集被用来测试LZF，GZIP和SZIP的性能差异，数据集使用了190KiB大小的分块。这些测试并不是绝对的，只是提供了一定的参考，因此在实际运用中还需要进行一定的性能测试。

- 情况1：简单数据序列：

  ```Python
  data[...] = np.arange(1024000)
  ```

  | 压缩算法(Compressor) | 压缩时间(Compression time) (ms) | 解压缩时间(Decompression time) (ms) | 压缩量(Compressed by) |
  |----------------------|:-------------------------------:|:-----------------------------------:|:---------------------:|
  | None | 10.7 | 6.5 | 0.00% |
  | LZF | 18.6 | 17.8 | 96.66% |
  | GZIP | 58.1 | 40.5 | 98.53% |
  | SZIP | 63.1 | 61.3 | 72.68% |

- 情况2：加入噪音的正弦波：

  ```Python
  data[...] = np.sin(np.arange(1024000)/32.) + (np.random(1024000)*0.5 - 0.25)
  ```

  | 压缩算法(Compressor) | 压缩时间(Compression time) (ms) | 解压缩时间(Decompression time) (ms) | 压缩量(Compressed by) |
  |----------------------|:-------------------------------:|:-----------------------------------:|:---------------------:|
  | None | 10.8 | 6.5 | 0.00% |
  | LZF | 65.5 | 24.4 | 15.54% |
  | GZIP | 298.6 | 64.8 | 20.05% |
  | SZIP | 115.2 | 102.5 | 16.29% |

- 情况3：随机数：

  ```Python
  data[...] = np.random(1024000)
  ```

  | 压缩算法(Compressor) | 压缩时间(Compression time) (ms) | 解压缩时间(Decompression time) (ms) | 压缩量(Compressed by) |
  |----------------------|:-------------------------------:|:-----------------------------------:|:---------------------:|
  | None | 9.0 | 7.8 | 0.00% |
  | LZF | 67.8 | 24.9 | 8.95% |
  | GZIP | 305.4 | 67.2 | 17.05% |
  | SZIP | 120.6 | 107.7 | 15.56% |

### Other Filters

HDF5加入了一些其他的过滤器如连续性检查过滤器(consistency check filters)和重组(rearrangement(SHUFFLE) filters)来提升压缩性能。这些过滤器和任意指定的压缩过滤器都在HDF5中被集成进过滤器管道并一个个执行。

#### SHUFFLE Filter

SHUFFLE过滤器通常和GZIP或LZF等压缩过滤器同时使用。这个过滤器的机制基于很多数据集会在某几个只占用非常少空间的元素上有大量的冗余数据，例如一个4 byte unsigned integer构成的数据集当中可能有数千个0，大部分数据只占用了小于2 bytes的空间。

SHUFFLE过滤器会将这些数据重组，将第一个字节上放在一起，然后第二个字节放在一起，以此类推。这种方式相对于基于字典的压缩方式如GZIP或LZF会在压缩大量相同数据时获得效率上的明显提升。

```Python
In [18]: dset = f.create_dataset("Data1", (1000,), compression="gzip", shuffle=True)

In [19]: dset.shuffle
Out[19]: True
```

SHUFFLE过滤器支持所有的HDF5版本，且效率非常高。但是只能和GZIP或LZF等搭配使用。

#### FLETCHER32 Filter

当存储或传输大量数据时，人们希望取出的数据和放入时的数据是完全一致的。因此HDF5使用了checksum过滤器检查写入和读取时的数据字节数是否相同。在每个分块写入时，checksum过滤器计算分块的字节大小并写入分块的元数据中。当分块被读取时，checksum过滤器会再运行一次。并对之前记录的数值进行对比，如果不匹配，则给出报错并使文件读取失败。

```Python
In [20]: dset = f.create_dataset("Data2", (1000,), fletcher32=True)

In [21]: dset.fletcher32
Out[21]: True

In [22]: f.close()
```

FLETCHER32过滤器支持所有的HDF5版本，效率高且和所有无损过滤器兼容。

### Third-Party Filters

除此以外还有一些第三方过滤器。例如在`PyTables`项目中使用的BLOSC压缩算法在速度上进行了优化，此外也有一些基于其他压缩系统的过滤器。

此外在HDF5 1.8.11后加入了称为动态载入过滤器(dynamically loaded filters)的新特性。在之前的版本中，使用过滤器需要手动寄存，例如`h5py`在启动时寄存了LZF过滤器。新特性面对数据集未知过滤器类型时会自动从磁盘中导入过滤器模块。这个特性仍在改进中，有需要可以在`h5py`或者`PyTables`的项目网站查询最新进展。

最后需要注意的是，如果需要使用过滤器，一定要保证接收数据方能够顺利的获取数据。

## Chapter5. Groups, Links, and Iteration: The "H" in HDF5

到目前为止，创建数据集的方式都是直接在文件中创建，例如`myfile["dataset1"]`等，但是这种方式类似于将所有的文件全部放在电脑桌面上，其缺点是显而易见的。

组(*Groups*)作为HDF5的容器对象，类似于文件管理系统中的文件夹，可以存储数据集和其他组。通过组和子组(subgroups)从而创建一种干净清晰的分层结构。

### The Root Group and Subgroups

`File`对象本身就是一个组，作为根组(*root group*)存在，命名为`/`，是进入文件的入口。

更加通用的组对象是`h5py.Group`，而`h5py.File`是它的子类。可以通过`create_group`方法轻松创建其他的组：

```Python
In [1]: import numpy as np

In [2]: import h5py

In [3]: f = h5py.File("Groups.hdf5")

In [4]: subgroup = f.create_group("SubGroup")

In [5]: subgroup
Out[5]: <HDF5 group "/SubGroup" (0 members)>

In [6]: subgroup.name
Out[6]: '/SubGroup'
```

`create_group`方法对所有的组对象都有用，因此可以在子组中继续创建子组：

```Python
In [7]: subsubgroup = subgroup.create_group("AnotherGroup")

In [8]: subsubgroup.name
Out[8]: '/SubGroup/AnotherGroup'
```

此外，创建组也不需要每一层都手动创建，可以直接输入全路径，HDF5会自动创建其中缺失的组：

```Python
In [9]: out = f.create_group("/some/big/path")

In [10]: out
Out[10]: <HDF5 group "/some/big/path" (0 members)>
```

### Group Basics

*组的工作机制基本类似于字典*。尽管并非完全如此，但是多数时候可以这样理解和使用。组是可迭代对象，而且继承标准Python字典API的子集。

为后续案例创建数据：

```Python
In [11]: f["Dataset1"] = 1.0

In [12]: f["Dataset2"] = 2.0

In [13]: f["Dataset3"] = 3.0

In [14]: subgroup["Dataset4"] = 4.0
```

#### Dictionary-Style Access

对象可以使用类似字典的方式直接获取：

```Python
In [15]: dset1 = f["Dataset1"]
```

不同于Python字典，HDF5中可以直接使用路径进行索引，而不需要打开每层组对象：

```Python
In [16]: dset4 = f["SubGroup/Dataset4"]  # Right

In [17]: dset4 = f["SubGroup"]["Dataset4"]  # Works, but inefficient
```

如果尝试访问空组对象会引发`KeyError`报错：

```Python
In [18]: f["BadName"]
KeyError: "Unable to open object (object 'BadName' doesn't exist)"
```

另一种类似的方式是`get`方法，但是使用`get`方法访问空组对象并不会引发报错：

```Python
In [19]: out = f.get("BadName")

In [20]: print(out)
None
```

使用`len`方法可以获取组的长度，但是仅限于当前组下的文件和子组，也就是说，`len`方法并不会递归获取子组下的所有元素：

```Python
In [21]: len(f)
Out[21]: 5

In [22]: len(f["SubGroup"])
Out[22]: 2

In [23]: f.close()
```

`f`即HDF5文件`Groups.hdf5`，其中有三个数据集`Dataset1`，`Dataset2`和`Dataset3`，还有两个组`SubGroup`和`some`，而`Subgroup`下有数据集`Dataset4`和组`AnotherGroup`。

#### Special Properties

当使用分层数据结构时，HDF5在组和数据集对象上提供了一些有用的组件。

第一个是`.file`属性。这个属性内置于每个对象，可以通过这个属性直接访问当前对象所位于的`File`对象：

```Python
In [1]: import numpy as np

In [2]: import h5py

In [3]: f = h5py.File("propdemo.hdf5", 'w')

In [4]: grp = f.create_group("hello")

In [5]: grp.file == f
Out[5]: True
```

第二个是`.parent`属性。这个会返回包含当前对象的组对象：

```Python
In [6]: grp.parent
Out[6]: <HDF5 group "/" (1 members)>

In [7]: f.close()
```

使用这两个属性可以有效避免路径和格式相关的问题。

### Working with Links

根据之前的经验，一个对象的名字似乎是对象的一部分，就像`dtype`或`shape`之于数据集一样。但是实际上，在组对象和它的成员对象之间有一个中间层，这两者通过所谓的链接(*links*)概念连接在一起。

#### Hard Links

HDF5中的链接类似于现代文件管理系统。数据集对象和组对象本身并没有名字，但是它们有自己的地址(*address*)，HDF5根据地址查找文件。当在组中给一个对象指定名称时，对象地址在组中被记录，然后和指定的名称形成一个链接(*link*)。

换句话说，一个HDF5文件中的对象可以有超过一个名字。实际上，只要存在指向对象的链接，就可以有对应的名称。系统会记录指向一个对象的链接的数量，当不再存在这样的链接时，这块对象使用的内存就会被释放。（个人理解为一种类似于Python垃圾回收机制的内存管理方法。）

这种链接方式在HDF5中为默认方式，被称为硬链接(*hard link*)，用于和以后提到的其他链接方式区分。

在下例中，创建了一个包含一个组的普通文件，然后创建了一个硬链接：

```Python
In [1]: import numpy as np

In [2]: import h5py

In [3]: f = h5py.File("linksdemo.hdf5", 'w')

In [4]: grpx = f.create_group('x')

In [5]: grpx.name
Out[5]: '/x'
```

使用Python字典的赋值方式，可以创建指向这个组的第二个链接。当从第二个名称中获取这个组时，可以发现取到了相同的组：

```Python
In [6]: f['y'] = grpx

In [7]: grpy = f['y']

In [8]: grpx == grpy
Out[8]: True
```

如果尝试使用`.name`去确认一个没有唯一名称的对象的名称，系统的返回值为：

```Python
In [9]: grpx.name
Out[9]: '/x'

In [10]: grpy.name
Out[10]: '/y'
```

在这里HDF5尽量会返回使用的名称，但是并不一定会返回用户所希望的。事实上，HDF5完全允许创建一个没有名称的对象，例如：

```Python
In [11]: grpz = f.create_group(None)

In [12]: print(grpz.name)
None
```

在这种情况下，组`grpz`确实存在于文件中，但是没有任何方式可以通过根组去访问。通过创建链接可以避免`grpz`被删除和释放空间：

```Python
In [13]: f['z'] = grpz

In [14]: grpz.name
Out[14]: '/z'
```

多个名称的问题同样会影响`.parent`属性。为了强调这个，在`h5py`中，`obj.parent`被定义为根据`obj.name`得到的父对象。例如如果`obj.name`是`/foo/bar`，那么`obj.parent.name`会是`/foo`。

如果需要移除链接，可以直接使用Python字典类型的语法`del group[name]`：

```Python
In [15]: del f['y']

In [16]: del f['x']  # Last hard link; the group is deleted in the file

In [17]: f.close()
```

#### Free Space and Repacking

当一个对象被删除时，它在磁盘上占用的空间会被回收，供新的对象使用。但是，在写入文件前，HDF5并不会在文件打开/关闭周期中跟踪这些闲置空间。因此，如果在关闭文件时没有重新使用这些空间，那么文件中可能会保留无法回收的不可用空间。

HDF项目正在重点解决这一问题。与此同时，如果存在明显异常庞大的文件，可以使用随HDF5一同的`h5repack`工具：

```Shell
h5repack bigfile.hdf5 out.hdf5
```

#### Soft Links

类Unix用户会对软链接比较熟悉。相比于硬链接直接将名称和文件中的特定对象链接，软链接将路径(*path*)存放在对象中。

首先创建一个包含一个数据集的组：

```Python
In [1]: import numpy as np

In [2]: import h5py

In [3]: f = h5py.File("test.hdf5", 'w')

In [4]: grp = f.create_group("mygroup")

In [5]: dset = grp.create_dataset("dataset", (100,))
```

如果在根组上创建链接至这个数据集的硬链接，那么将永远指向这个对象，即使这个数据集已经被移出或从当前组中取消链接：

```Python
In [6]: f["hardlink"] = dset

In [7]: f["hardlink"] == grp["dataset"]
Out[7]: True

In [8]: grp.move("dataset", "new_dataset_name")

In [9]: f["hardlink"] == grp["new_dataset_name"]
Out[9]: True
```

现在将这个数据集移回，然后创建一个指向路径`/mygroup/dataset`的软链接。在HDF5中创建软链接的方式是分配类`h5py.SoftLink`的实例到文件中的一个名称上：

```Python
In [10]: grp.move("new_dataset_name", "dataset")

In [11]: f["softlink"] = h5py.SoftLink("/mygroup/dataset")

In [12]: f["softlink"] == grp["dataset"]
Out[12]: True
```

`SoftLink`对象只有一个`.path`属性，保存了创建时提供的路径：

```Python
In [13]: softlink = h5py.SoftLink('/some/path')

In [14]: softlink
Out[14]: <SoftLink to "/some/path">

In [15]: softlink.path
Out[15]: '/some/path'
```

需要记住的是，`h5py.SoftLink`实例只是出于Python端便利性考虑，并非包含在任一HDF5中。在将其分配给文件中的一个名称之前，任何事情都不会发生。

回到上例中，因为软链接只保留了路径，因此如果移动或替换数据集，软链接会指向新的对象：

```Python
In [16]: grp.move("dataset", "new_dataset_name")

In [17]: dset2 = grp.create_dataset("dataset", (50,))

In [18]: f["softlink"] == dset
Out[18]: False

In [19]: f["softlink"] == dset2
Out[19]: True
```

由此可见，软链接非常适合于指向保存在**某个特定路径的对象而不是某个特定的对象**。

软链接的值在创建时**并不会**进行检查。如果提供了无效路径，或者这个对象后续被删除或移出，读取会失败并且报出异常。HDF5给出这种异常的方式和当尝试读取不存在的文件时的报错相同，都是`KeyError`：

```Python
In [20]: f["broken"] = h5py.SoftLink("/some/nonexistent/object")

In [21]: f["broken"]
KeyError: 'Unable to open object (component not found)'

In [22]: f.close()
```

此外，由于软链接只记录路径，并不会像硬链接保留在在计数索引中，因此如果有一个软链接`/softlink`指向一个已经硬链接过的对象`/a`，如果删除这个对象`del f["/a"]`，则这个对象会被销毁，同时软链接也会中断。如果使用`items()`或`values()`尝试获取已经中断的软链接，对象会返回`None`。

#### External Links

从HDF5 1.8开始，处理本地硬链接和软链接外，新增了新的链接方式。外链接(*external links*)允许引用其他文件中的对象。这是HDF5中非常酷的特性，但是由于其透明性，在跟踪方面比较棘手。

一个外链接有两个部分组成，文件名称和文件中对象的绝对名称。类似于软链接，需要对对象创建一个标记，在这里是一个实例`h5py.ExternalLink`：

```Python
In [1]: import numpy as np

In [2]: import h5py

In [3]: with h5py.File("file_with_resource.hdf5", 'w') as f1:
   ...:     f1.create_group("mygroup")

In [4]: f2 = h5py.File("linking_file.hdf5", 'w')

In [5]: f2["linkname"] = h5py.ExternalLink("file_with_resource.hdf5", "mygroup")
```

类似于软链接，外链接也是透明的，也就是说，如果链接没有断开，会得到他们指向的组或数据集，而非中间对象。因此如果访问刚刚创建的链接，会得到组作为返回：

```Python
In [6]: grp = f2["linkname"]

In [7]: grp.name
Out[7]: '/mygroup'
```

但是如果仔细观察可以发现，这两个对象位于不同的文件中：

```Python
In [8]: grp.file
Out[8]: <HDF5 file "file_with_resource.hdf5" (mode r+)>

In [9]: f2
Out[9]: <HDF5 file "linking_file.hdf5" (mode r+)>
```

需要注意的是，当使用`.parent`属性获取对象时，指向的是外部文件的根组，而非链接所在的文件：

```Python
In [10]: f2["/linkname"].parent == f2['/']
Out[10]: False
```

使用外链接会同时检查文件名和对象名，因此如果HDF5无法找到文件，或者文件内的指定对象，HDF5将会抛出异常：

```Python
In [11]: f2["anotherlink"] = h5py.ExternalLink("missing.hdf5", '/')

In [12]: f2.close()
```

但是实际测试未报错，原因暂不明确。

使用外链接可能存在两个主要问题：

1. 链接指向的文件可能在需要访问时并不存在。这个问题没有很好的解决方法，需要用户对文件进行良好组织，并且时刻注意什么链接向什么。
2. 通过遍历文件链接，有可能导致读到其他文件。这个问题相对比较危险，特别是当使用一些"Pythonic"的方法获取组成员时，如迭代方法`items()`等，这些都会包含外链接。如果不希望程序超出文件边界，最好要使用`.file`属性检查文件的真实归属。

目前`h5py`并没有设置搜索路径的方法。当遇到外部链接时，HDF5将首先查找与带有链接文件相同目录下的文件，然后会查询当前工作目录下的文件。

#### A Note on Object Names

当返回文件名时，返回的值是一个Python Unicode对象。在高版本的HDF5和Python 3中，文件中的对象名永远被认为是文本字符串，这表示它们永远表示字符序列。而之前使用的字节字符串("byte" string)是8-bit数字序列，存储的编码较少。

这种方式的好处是所有对象名称支持国际化字符，不需要将名称全部ASCII化以适应HDF5系统。在后端，`h5py`会将名称字符串转化为HDF5可接受的UTF-8编码然后存储。但是尽管HDF5支持UTF-8编码字符，还是不建议使用不合规的对象名称。

#### Using get to Determine Object Types

在Dictionary-Style Access一节说明了将`get`方法用于组对象，并且如何处理缺失的组成员而不引发`KeyError`。相比于Python的`get`方法，HDF5提供的`get`方法有更多的功能。除了默认值以外，还有两个关键字`getclass`和`getlink`。

`getclass`关键字允许检查对象的类型(*type*)而无需打开对象。在HDF5层面，这种操作只需要读取元数据，因此速度非常快：

```Python
In [1]: import numpy as np

In [2]: import h5py

In [3]: f = h5py.File("get_demo.hdf5", 'w')

In [4]: f.create_group("subgroup")
Out[4]: <HDF5 group "/subgroup" (0 members)>

In [5]: f.create_dataset("dataset", (100,))
Out[5]: <HDF5 dataset "dataset": shape (100,), type "<f4">

In [6]: for name in f:
   ...:     print(name, f.get(name, getclass=True))
dataset <class 'h5py._hl.dataset.Dataset'>
subgroup <class 'h5py._hl.group.Group'>
```

`getlink`关键字能让用户确定使用的链接的属性：

```Python
In [7]: f["softlink"] = h5py.SoftLink("/subgroup")

In [8]: with h5py.File("get_demo_ext.hdf5", 'w') as f2:
   ...:     f2.create_group("egroup")

In [9]: f["extlink"] = h5py.ExternalLink("get_demo_ext.hdf5", "/egroup")

In [10]: for name in f:
    ...:     print(name, f.get(name, getlink=True))
dataset <h5py._hl.group.HardLink object at 0x000001C90DC485C0>
extlink <ExternalLink to "/egroup" in file "get_demo_ext.hdf5"
softlink <SoftLink to "/subgroup">
subgroup <h5py._hl.group.HardLink object at 0x000001C90DC485C0>
```

可以注意到这里返回了`SoftLink`和`ExternalLink`的实例以及路径信息。这是创建链接后检索此类信息的官方方式。

对于`subgroup`和`dataset`中的硬链接，也存在一个`h5py.HardLink`的实例。这个只是为了支持`get`方法，没有其他的函数、属性或方法。

如果只是关心链接的类型，而不在意所涉及的路径和文件的具体值，可以同时使用`getclass`和`getlink`关键字返回链接类：

```Python
In [11]: for name in f:
    ...:     print(name, f.get(name, getclass=True, getlink=True))
dataset <class 'h5py._hl.group.HardLink'>
extlink <class 'h5py._hl.group.ExternalLink'>
softlink <class 'h5py._hl.group.SoftLink'>
subgroup <class 'h5py._hl.group.HardLink'>

In [12]: f.close()
```

#### Using require to Simplify Your Application

与Python字典不同的是，不能直接覆盖组成员，也不能直接手动创建硬链接对象：

```Python
In [1]: import numpy as np

In [2]: import h5py

In [3]: f = h5py.File("require_demo.hdf5", 'w')

In [4]: f.create_group('x')
Out[4]: <HDF5 group "/x" (0 members)>

In [5]: f.create_group('y')
Out[5]: <HDF5 group "/y" (0 members)>

In [6]: f.create_group('y')
ValueError: Unable to create group (name already exists)

In [7]: f['y'] = f['x']
RuntimeError: Unable to create link (name already exists)
```

这种设定是有意为之的，以避免意外的数据丢失。因为一旦从组中取消链接，则对象会被立刻删除。因此，如果需要删除链接，必须显式地进行：

```python
In [8]: del f['y']

In [9]: f['y'] = f['x']
```

但是这个功能同样带来了一个问题，例如如下代码作为一整个分析的一部分，创建了一个文件并将结果写入数据集中：

```Python
data = do_large_calculation()
with h5py.File("output.hdf5") as f:
    f.create_dateset("result", data=data)
```

如果`output.hdf5`文件中有很多数据集和组，显然不能在每次代码运行到这里时覆盖整个文件，但是如果不使用`w`模式，那么程序只能在第一次运行，除非每次都手工删除产出的结果文件数据集`result`。

为了解决这个问题，`create_group`和`create_dataset`方法提供了`require_group`和`require_dataset`的配套方法。它们执行完全相同的操作，只是会首先检查是否已有组或数据集存在，如果存在则返回它。这两种方法使用相同的参数和关键字，在`require_dataset`方法中还会针对提供的形状和`dtype`检查现有的数据集。如果不匹配也会返回`False`：

```Python
In [10]: f.create_dataset("dataset", (100,), dtype='i')
Out[10]: <HDF5 dataset "dataset": shape (100,), type "<i4">

In [11]: f.require_dataset("dataset", (100,), dtype='i')
Out[11]: <HDF5 dataset "dataset": shape (100,), type "<i4">

In [12]: f.require_dataset("dataset", (100,), dtype='f')
TypeError: Datatypes cannot be safely cast (existing int32 vs new f)
```

此外还有一个细节在于，冲突只会发生在形状不匹配，或者要求的精度高于目前已存在的精度。也就是说，如果已经存在`int64`的数据集，使用`require_dataset`并要求精度位`int32`，则会匹配成功：

```Python
In [13]: f.create_dataset("int_dataset", (100,), dtype="int64")
Out[13]: <HDF5 dataset "int_dataset": shape (100,), type "<i8">

In [14]: f.require_dataset("int_dataset", (100,), dtype="int32")
Out[14]: <HDF5 dataset "int_dataset": shape (100,), type "<i8">
```

### Iteration and Containership

#### How Groups Are Actually Stored

在HDF5中使用B树的结构对组成员进行索引。在这里仅对其简单概括，详细内容见参考资料：

> 从B树、B+树、B*树谈到R树 [CSDN](https://blog.csdn.net/v_JULY_v/article/details/6530142)
>
> B树和B+树总结 [cnblogs](https://www.cnblogs.com/George1994/p/7008732.html)

B树是一种数据结构，非常适合跟踪大量项目，同时仍可快速检索和添加元素。它们通过获取元素的集合，每个元素根据字符串名称或数字标识符等方案进行排序，以及构建类似树的索引来快速检索元素。所有这一切对用户都是透明的。HDF5文件中的每个组都附带一个按字母顺序跟踪成员的索引：

```Python
In [1]: import numpy as np

In [2]: import h5py

In [3]: f = h5py.File("iterationdemo.hdf5", 'w')

In [4]: f.create_group('1')
Out[4]: <HDF5 group "/1" (0 members)>

In [5]: f.create_group('2')
Out[5]: <HDF5 group "/2" (0 members)>

In [6]: f.create_group("10")
Out[6]: <HDF5 group "/10" (0 members)>

In [7]: f.create_dataset("data", (100,))
Out[7]: <HDF5 dataset "data": shape (100,), type "<f4">

In [8]: f.keys()
Out[8]: <KeysViewHDF5 ['1', '10', '2', 'data']>
```

这意味着`h5py`通常会按照字母表顺序对文件中的对象进行迭代，但是不同通常如此。在后台，HDF5实际是按照所谓的本机顺序检索对象，这通常来说意味着尽量快的速度。同时只要不修改组，顺序会保持不变。

#### Dictionary-Style Iteration

通常来说，组的工作方式类似于字典。对组进行迭代会返回成员名称，同时也支持`values()`和`items()`方法（在Python 2中是`itervalues()`和`iteritems()`。在Python 3中`values()`和`items()`返回的是可迭代对象，同时删除了Python 2的这两种方法）：

```Python
In [9]: [x for x in f]
Out[9]: ['1', '10', '2', 'data']

In [10]: [y for y in f.values()]
Out[10]:
[<HDF5 group "/1" (0 members)>,
 <HDF5 group "/10" (0 members)>,
 <HDF5 group "/2" (0 members)>,
 <HDF5 dataset "data": shape (100,), type "<f4">]

In [11]: [(x, y) for x, y in f.items()]
Out[11]:
[('1', <HDF5 group "/1" (0 members)>),
 ('10', <HDF5 group "/10" (0 members)>),
 ('2', <HDF5 group "/2" (0 members)>),
 ('data', <HDF5 dataset "data": shape (100,), type "<f4">)]
```

#### Containership Testing

有一个经常会带来性能问题的情况，**不**要将代码写作：

```Python
if "name" in group.keys():
```

因为这会在每次使用组成员时创建并抛出一个包含所有成员的列表。应当用HDF5对对象名称的索引替换标准Python的容器，这将会**大幅提高速度**：

```Python
if "name" in group:
```

严格来说，也可以使用拓展路径跨越多个组，但是这会影响效率，因为HDF5会查询所有的中间组：

```Python
if "some/big/path" in group:
```

但是注意，使用POSIX风格的路径如`..`代表父目录，在HDF5中并不能有效，而且也不会得到报错信息：

```Python
In [12]: "../1" in f["/1"]
Out[12]: False
```

当然也可以使用Python标准库将其进行转换：

```Python
In [13]: grp = f["/1"]

In [14]: path = "../1"

In [15]: import posixpath as pp

In [16]: path = pp.normpath(pp.join(grp.name, path))

In [17]: path
Out[17]: '/1'

In [18]: path in grp
Out[18]: True

In [19]: f.close()
```

### Multilevel Iteration with the Visitor Pattern

基本迭代适用于单个组的内容，但是如果要迭代文件中的每一个对象，或者指定组下的所有对象，就需要使用HDF5中提供的`visitor`迭代器。用户提供一个可调用的对象然后HDF5调用它。

#### Visit by Name

```Python
In [1]: import numpy as np

In [2]: import h5py

In [3]: f = h5py.File("visit_test.hdf5", 'w')

In [4]: f.create_dataset("top_dataset", data=1.0)
Out[4]: <HDF5 dataset "top_dataset": shape (), type "<f8">

In [5]: f.create_group("top_group_1")
Out[5]: <HDF5 group "/top_group_1" (0 members)>

In [6]: f.create_group("top_group_1/subgroup_1")
Out[6]: <HDF5 group "/top_group_1/subgroup_1" (0 members)>

In [7]: f.create_dataset("top_group_1/subgroup_1/sub_dataset_1", data=1.0)
Out[7]: <HDF5 dataset "sub_dataset_1": shape (), type "<f8">

In [8]: f.create_group("top_group_2")
Out[8]: <HDF5 group "/top_group_2" (0 members)>

In [9]: f.create_dataset("top_group_2/sub_dataset_2", data=1.0)
Out[9]: <HDF5 dataset "sub_dataset_2": shape (), type "<f8">
```

上述代码创建了一个文件并在其中加入了组和数据集。

现在创建一个可调用对象，它接受对象名称作为参数，然后将其提供给`Group`类下的`visit`方法：

```Python
In [10]: def printname(name):
    ...:     print(name)

In [11]: f.visit(printname)
top_dataset
top_group_1
top_group_1/subgroup_1
top_group_1/subgroup_1/sub_dataset_1
top_group_2
top_group_2/sub_dataset_2
```

`visit`方法同样支持在子组中使用：

```Python
In [12]: grp = f["top_group_1"]

In [13]: grp.visit(printname)
subgroup_1
subgroup_1/sub_dataset_1
```

`visitor`模式和标准Python迭代器有所区别，但是非常强大和有用，例如如果要生成文件中每个对象的列表，可以直接写作：

```Python
In [14]: mylist = []

In [15]: f.visit(mylist.append)

In [16]: mylist
Out[16]:
['top_dataset',
 'top_group_1',
 'top_group_1/subgroup_1',
 'top_group_1/subgroup_1/sub_dataset_1',
 'top_group_2',
 'top_group_2/sub_dataset_2']
```

#### Multiple Links and visit

**硬链接时组之间共享对象的好方法**。

对一个硬链接使用`visit`方法：

```Python
In [17]: grp["hardlink"] = f["top_group_2"]

In [18]: grp.visit(printname)
hardlink
hardlink/sub_dataset_2
subgroup_1
subgroup_1/sub_dataset_1
```

可以看到在`/top_group_2`中的组被挂载到`/top_group_1/hardlink`下，`visit`方法也正确返回了结果。

但是如果现在删除刚刚的硬链接，同时重新硬链接到组自身的数据集：

```Python
In [19]: del grp["hardlink"]

In [20]: grp["hardlink_to_dataset"] = grp["subgroup_1/sub_dataset_1"]

In [21]: grp.visit(printname)
hardlink_to_dataset
subgroup_1
```

这时候发现`sub_dataset_1`没有出现在输出中。这是根据设计得到的。因为设计要求一个文件下的每个对象**只能被`visit`一次**，从而避免死循环的可能，例如`f["/root"] = f['/']`这种设计。

这正如在介绍硬链接时讨论的，对象没有“真实”或“原始”名称，因此如果有多个链接指向数据集，使用`visit`可能无法得到需要的结果。

#### Visiting Items

给定提供给回调函数的名称，只需要在迭代的组上使用`getitem`方法就可以检索对象：

```Python
In [22]: def printobj(name):
    ...:     print(grp[name])
```

但是这带来一个问题：由于`visit`方法提供的`name`参数时提供的是*相对路径*，因此函数必须事先知道需要应用于哪个组，即函数`printobj`中硬编码的`grp[name]`，且这个函数只能适用于`grp`组。

HDF5提供了更加通用的方法处理这个问题。方法`visititems`同时提供了每个对象的实例和相对名称：

```Python
In [23]: def printobj2(name, obj):
    ...:     print(name, obj)

In [24]: grp.visititems(printobj2)
hardlink_to_dataset <HDF5 dataset "hardlink_to_dataset": shape (), type "<f8">
subgroup_1 <HDF5 group "/top_group_1/subgroup_1" (1 members)>
```

由于`visititems`会打开每个对象，因此这会带来一定的开销。最好仅在真正需要访问每个对象（例如需要检查对象属性）时使用这个方法。

也可以使用Python内置的方法令`visit`方法更加通用，例如使用`functools.partial`方法：

```Python
In [26]: import posixpath

In [27]: from functools import partial

In [28]: def print_abspath(somegroup, name):
    ...:     """ Print*name* as an absolute path
    ...:         somegroup: HDF5 base group (*name* is relative to this)
    ...:         name: Object name relative to *somegroup*
    ...:     """
    ...:     print(posixpath.join(somegroup.name, name))

In [29]: grp.visit(partial(print_abspath, grp))
/top_group_1/hardlink_to_dataset
/top_group_1/subgroup_1
```

#### Canceling Iteration: A Simple Search Mechanism

在函数`printname`中，没有显式指定返回值，在Python里会返回`None`。如果有任何其他返回内容，那么`visit`或`visititems`方法会立刻中止并返回这个值：

```Python
In [30]: f["top_group_2/sub_dataset_2"].attrs["special"] = 42

In [31]: def findspecial(name, obj):
    ...:     if obj.attrs.get("special") == 42:
    ...:         return obj

In [32]: out = f.visititems(findspecial)

In [33]: out
Out[33]: <HDF5 dataset "sub_dataset_2": shape (), type "<f8">
```

### Copying Objects

#### Single-File Copying

HDF5内置了复制功能，复制数据集会直接创建一个新的数据集，而非引用或链接：

```Python
In [1]: import numpy as np

In [2]: import h5py

In [3]: f = h5py.File("copytest.hdf5", 'w')

In [4]: f.create_group("mygroup")
Out[4]: <HDF5 group "/mygroup" (0 members)>

In [5]: f.create_group("mygroup/subgroup")
Out[5]: <HDF5 group "/mygroup/subgroup" (0 members)>

In [6]: f.create_dataset("mygroup/apples", (100,))
Out[6]: <HDF5 dataset "apples": shape (100,), type "<f4">

In [7]: f.copy("/mygroup/apples", "/oranges")

In [8]: f["oranges"] == f["mygroup/apples"]
Out[8]: False

In [9]: f.copy("mygroup", "mygroup2")

In [10]: def printname(name):
    ...:     print(name)

In [11]: f.visit(printname)
mygroup
mygroup/apples
mygroup/subgroup
mygroup2
mygroup2/apples
mygroup2/subgroup
oranges
```

书中表示可以将数据集复制到组或文件对象中，但是实际结果会报错，原因不明：

```Python
In [12]: dset = f["/mygroup/apples"]

In [13]: f.copy(dset, f)
ValueError: Field names only allowed for compound types

In [14]: f.close()
```

### Object Comparison and Hashing

在之前的示例中，一直使用的`==`判断两个对象是否“相同”，但是这并不代表两个对象时完全一致的：

```Python
In [1]: import numpy as np

In [2]: import h5py

In [3]: f = h5py.File("objectdemo.hdf5", 'w')

In [4]: grpx = f.create_group('x')

In [5]: grpy = f.create_group('y')

In [6]: grpx == f['x']
Out[6]: True

In [7]: grpx == grpy
Out[7]: False

In [8]: id(grpx)  # Uniquely identifies the Python object "grpx"
Out[8]: 2465987856984

In [9]: id(f['x'])
Out[9]: 2465984976376
```

在`h5py`中，相等性测试使用的是底层HDF5工具来确定那些引用指向磁盘中相同的组或数据集。这个还被用来计算对象的哈希值。这使得可以安全的使用组、文件和数据集对象作为字典的键或集合的成员：

```Python
In [10]: hash(grpx)
Out[10]: 3632262033377125284

In [11]: hash(f['x'])
Out[11]: 3632262033377125284
```

在对对象使用`.file`属性时可能会遇到相等性测试的另一个问题，即当组实例表示根组时，文件实例和组实例会被认为时相同的，这是由于文件实例有着双重作用，既表示磁盘上的文件，也表示HDF5端的根组：

```Python
In [12]: f == f['/']
Out[12]: True
```

使用布尔值可以判断一个HDF5对象现在是否存在：

```Python
In [13]: bool(grpx)
Out[13]: True

In [14]: f.close()

In [15]: grpx
Out[15]: <Closed HDF5 group>

In [16]: bool(grpx)
Out[16]: False
```

## Chapter6. Storing Metadata with Attributes

属性是直接附加在文件对象上的元数据，它们是制作自描述文件的关键机制。

### Attribute Basics

属性可以附加在HDF5树形结构上的任何一个对象，然后使用`.attrs`查看对象附加的属性：

```Python
In [1]: import numpy as np

In [2]: import h5py

In [3]: f = h5py.File("attrsdemo.hdf5", 'w')

In [4]: dset = f.create_dataset("dataset", (100,))

In [5]: dset.attrs
Out[5]: <Attributes of HDF5 object at 2388966744136>
```

`attrs`对象也以类似Python字典的方式使用：

```Python
In [6]: dset.attrs["title"] = "Dataset from third round of experiments"

In [7]: dset.attrs["sample_rate"] = 100e6  # 100 MHz digitizer setting

In [8]: dset.attrs["run_id"] = 144

In [9]: dset.attrs["title"]
Out[9]: 'Dataset from third round of experiments'

In [10]: dset.attrs["sample_rate"]
Out[10]: 100000000.0

In [11]: dset.attrs["run_id"]
Out[11]: 144

In [12]: [x for x in dset.attrs]
Out[12]: ['run_id', 'sample_rate', 'title']
```

属性并不需要像组对象一样在删除时进行严格的判定，属性可以随意被覆盖，但是一旦被删除，属性会抛出`KeyError`异常，而检索被删除的组时并不会抛出异常。此外，上文提及过的`keys`, `items`和`values`方法同样适用，同样适用的也有`get`方法：

```Python
In [13]: dset.attrs["another_id"] = 42

In [14]: dset.attrs["another_id"] = 100

In [15]: dset.attrs["another_id"]
Out[15]: 100

In [16]: del dset.attrs["another_id"]

In [17]: dset.attrs["another_id"]
KeyError: "Can't open attribute (can't locate attribute: 'another_id')"

In [18]: [(name, val) for name, val in dset.attrs.items()]
Out[18]:
[('run_id', 144),
 ('sample_rate', 100000000.0),
 ('title', 'Dataset from third round of experiments')]

In [19]: dset.attrs.get("run_id")
Out[19]: 144

In [20]: print(dset.attrs.get("missing"))
None
```

#### Type Guessing

通常来说，在创建数据集时，会指定使用的`NumPy dtype`，但是当不指定时，一同回默认使用单精度浮点是。使用`.dtype`属性可以查看数据集的数据类型：对于HDF5文件的属性来说，这个dtype是会被隐藏的，但是仍然会通过提供的内容进行自动推断：

```Python
In [21]: dset.dtype
Out[21]: dtype('<f4')

In [22]: f.flush()

In [23]: !h5ls -vlr attrsdemo.hdf5
Opened "attrsdemo.hdf5" with sec2 driver.
/                        Group
    Location:  1:96
    Links:     1
/dataset                 Dataset {100/100}
    Attribute: run_id scalar
        Type:      native int
        Data:  144
    Attribute: sample_rate scalar
        Type:      native double
        Data:  1e+08
    Attribute: title scalar
        Type:      variable-length null-terminated UTF-8 string
        Data:  "Dataset from third round of experiments"
    Location:  1:800
    Links:     1
    Storage:   400 logical bytes, 0 allocated bytes
    Type:      native float
```

在进行类型推断时，系统通过将值传递给`np.array`然后存储结果对象。

此外，类型也不仅限于标量值(scalar values)，存储整个`NumPy array`作为属性也是可行的：

```Python
In [24]: dset.attrs["ones"] = np.ones((100,))

In [25]: dset.attrs["ones"]
Out[25]:
array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
       1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
       1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
       1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
       1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
       1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])
```

但是这有一定的限制。在默认情况下，属性的大小被限制在64k以内，例如如果使用一个(100, 100)的数组，则会收到报错信息：

```Python
In [26]: dset.attrs["ones"] = np.ones((100, 100))
RuntimeError: Unable to create attribute (object header message is too large)
```

在书中，返回的报错时`ValueError`，但是在当前的版本下，返回的报错已经变成`RuntimeError`，同时，书中表述一旦出现这个情况，之前对`ones`属性的赋值也会被抹去，但是现在这个属性会被保留。

如果一定需要使用大型数组作为属性，可以将这个数组保存在数据集中，然后创建一个指向这个数据集的链接，然后就可以正常的检索和使用：

```Python
In [27]: ones_dset = f.create_dataset("ones_data", data=np.ones((100, 100)))

In [28]: dset.attrs["ones"] = ones_dset.ref

In [29]: dset.attrs["ones"]
Out[29]: <HDF5 object reference>

In [30]: ones_dset = f[dset.attrs["ones"]]

In [31]: ones_dset[...]
Out[31]:
array([[1., 1., 1., ..., 1., 1., 1.],
       [1., 1., 1., ..., 1., 1., 1.],
       [1., 1., 1., ..., 1., 1., 1.],
       ...,
       [1., 1., 1., ..., 1., 1., 1.],
       [1., 1., 1., ..., 1., 1., 1.],
       [1., 1., 1., ..., 1., 1., 1.]])
```

#### Strings and File Compatibility

针对字符串和文件的兼容性，HDF5存在一些细微的区别。在前文案例中，`title`属性的数据类型是一个变长ASCII字符串(*variable-length* ASCII string)，但是笔记中，已经被识别为UTF-8格式。通常来说这个不存在问题，但是一些基于FORTRAN的程序会无法识别变长ASCII字符串，因此也可以通过`np.string_`创建使用定长字符串。此外，自然可以使用UTF-8格式字符串进行赋值：

```Python
In [32]: dset.attrs["title_fixed"] = np.string_("Another title")

In [33]: dset.attrs["Yet another title"] = u"String with accent (\u00E9)"

In [34]: f.flush()

In [35]: !h5ls -vlr attrsdemo.hdf5
Opened "attrsdemo.hdf5" with sec2 driver.
/                        Group
    Location:  1:96
    Links:     1
/dataset                 Dataset {100/100}
    Attribute: Yet\ another\ title scalar
        Type:      variable-length null-terminated UTF-8 string
        Data:  "String with accent (\37777777703\37777777651)"
    Attribute: ones scalar
        Type:      object reference
        Data:  DATASET-1:1680
    Attribute: run_id scalar
        Type:      native int
        Data:  144
    Attribute: sample_rate scalar
        Type:      native double
        Data:  1e+08
    Attribute: title scalar
        Type:      variable-length null-terminated UTF-8 string
        Data:  "Dataset from third round of experiments"
    Attribute: title_fixed scalar
        Type:      13-byte null-padded ASCII string
        Data:  "Another title"
    Location:  1:800
    Links:     1
    Storage:   400 logical bytes, 0 allocated bytes
    Type:      native float
/ones_data               Dataset {100/100, 100/100}
    Location:  1:1680
    Links:     1
    Storage:   80000 logical bytes, 80000 allocated bytes, 100.00% utilization
    Type:      native double
```

在之前的笔记中已经有涉及字节字符串(*byte* string)和文本字符串(*text* string)的区别，这主要在Python 3中体现的比较明显，因为Python 3对其进行了严格的区分。而且当从文件中读取属性时，对象格式会自动转换成HDF5支持的格式，因此如果存入一个`NumPy int32`，读取时会获得`int32`格式。这意味着在Python 3中，不标准的HDF5字符串会被读取为字节字符串，这就会带来一定处理上的问题。因此在Python 3中，所有的标量字符串在读取时全部会转换为文本字符串。

#### Python Objects

当然，也不能将任何对象保存为属性。

```Python
In [36]: dset.attrs["object"] = {}
TypeError: Object dtype dtype('O') has no native HDF5 equivalent
```

正如报错信息指出，HDF5并没有本地内置类型来表示Python对象。但是如果一定要使用Python对象，那最好的方法是使用序列化方法转换为字符串：

```Python
In [37]: import pickle

In [38]: pickled_object = pickle.dumps({"key": 42}, protocol=0)

In [39]: pickled_object
Out[39]: b'(dp0\nVkey\np1\nI42\ns.'

In [40]: dset.attrs["object"] = pickled_object

In [41]: obj = pickle.loads(dset.attrs["object"])

In [42]: obj
Out[42]: {'key': 42}

In [43]: f.close()
```

这个时候需要手工确认那些对象进行了序列化，因此尽量避免使用这种情况。

#### Explicit Typing

除了使用默认的自动属性类型识别，有时为了保持外部兼容性，需要显式指定属性类型。HDF5提供了一些机制对其进行处理。`attrs`代理对象有一个`create`方法，可以接受传入名称、数值和类型：

```Python
In [1]: import numpy as np

In [2]: import h5py

In [3]: f = h5py.File("attrs_create.hdf5", 'w')

In [4]: dset = f.create_dataset("dataset", (100,))

In [5]: dset.attrs.create("two_byte_int", 190, dtype="i2")

In [6]: dset.attrs["two_byte_int"]
Out[6]: 190

In [7]: f.flush()

In [8]: !h5ls -vlr attrs_create.hdf5
Opened "attrs_create.hdf5" with sec2 driver.
/                        Group
    Location:  1:96
    Links:     1
/dataset                 Dataset {100/100}
    Attribute: two_byte_int scalar
        Type:      native short
        Data:  190
    Location:  1:800
    Links:     1
    Storage:   400 logical bytes, 0 allocated bytes
    Type:      native float
```

在字符串方面，书本中说明默认使用的字符串是定长字符串，但是当前Python 3环境下无论是使用默认还是指定`vlen=str`，都会以变长字符串存储，而且也不存在使用ASCII字符串，统一使用UTF-8编码的变长字符串：

```Python
In [9]: dset.attrs["strings"] = ["Hello", "Another string"]

In [10]: dset.attrs["strings"]
Out[10]: array(['Hello', 'Another string'], dtype=object)

In [11]: dt = h5py.special_dtype(vlen=str)

In [12]: dset.attrs.create("more_strings", ["Hello", "Another string"], dtype=dt)

In [13]: dset.attrs["more_strings"]
Out[13]: array(['Hello', 'Another string'], dtype=object)

In [14]: f.flush()

In [15]: !h5ls -vlr attrs_create.hdf5
Opened "attrs_create.hdf5" with sec2 driver.
/                        Group
    Location:  1:96
    Links:     1
/dataset                 Dataset {100/100}
    Attribute: two_byte_int scalar
        Type:      native short
        Data:  190
    Location:  1:800
    Links:     1
    Storage:   400 logical bytes, 0 allocated bytes
    Type:      native float
```

最后补充的一个方式是`modify`，这种方法也会保留属性的类型。但是如果属性类型无法容纳提供的数值，则会对数值进行裁剪：

```Python
In [16]: dset.attrs.modify("two_byte_int", 33)

In [17]: dset.attrs["two_byte_int"]
Out[17]: 33

In [18]: dset.attrs.modify("two_byte_int", 40000)

In [19]: dset.attrs["two_byte_int"]
Out[19]: 32767

In [20]: f.close()
```

## Chapter7. More About Types

HDF5的功能之一是它支持的多种数据类型。在某些情况下，HDF5的特性较NumPy更多，为了保持性能并创建可交互的文件，需要了解各种数据类型的使用情况。

### The HDF5 Type System

与NumPy一样，HDF5中的所有数据都具有关联的类型。 HDF5类型系统非常灵活，并且包含了常见的对象，例如各种精度的整数和浮点数，以及字符串和向量类型。同时能够映射到NumPy当中：

| Native HDF5 type | NumPy equivalent |
|---------------------------|---------------------------------------------------------------------|
| `Integer` | `dtype("i")` |
| `Float` | `dtype("f")` |
| `Strings(fixed width)` | `dtype("S10")` |
| `Strings(variable width)` | `h5py.special_dtype(vlen=btyes)` |
| `Compound` | `dtype([("field1": "i"), ("field2": "f")])` |
| `Enum` | `h5py.special_dtype(enum=("i", {"RED": 0, "GREEN": 1, "BLUE": 2}))` |
| `Array` | `dtype("(2,2)f")` |
| `Opaque` | `dtype("V10")` |
| `Reference` | `h5py.special_dtype(ref=h5py.Reference)` |

此外`h5py`和`PyTables`包引入了额外的类型用以适配Python端：

| Python type | NumPy expression | Stored as |
|-------------|-----------------------|-----------------------------------|
| `Boolean` | `np.dtype("bool")` | HDF5 enum with FALSE=0, TRUE=1 |
| `Complex` | `np.dtype("complex")` | HDF5 compound with fields r and i |

### Integers and Floats

HDF5支持所有的NumPy整型，但是如果将一个太大的数值保存到一个较小的数据集中，HDF5和NumPy会采取不同的处理方法，HDF5会直接截断数据：

```Python
In [1]: import numpy as np

In [2]: import h5py

In [3]: f = h5py.File("typesdemo.hdf5")

In [4]: dset = f.create_dataset("smallint", (10,), dtype=np.int8)

In [5]: dset[0] = 300

In [6]: dset[0]
Out[6]: 127

In [7]: a = np.zeros((10,), dtype=np.int8)

In [8]: a[0] = 300

In [9]: a[0]
Out[9]: 44
```

HDF5支持单精度和双精度浮点数。此外还有对一些不常见的浮点数精度的支持，例如半精度浮点数。这是一种2-byte浮点数，在NumPy中以`np.float16`表示，通常运用在图像和视频处理应用中的数据存储。因为这种精度仅占用等价单精度浮点数一半的存储空间，非常适合精度要求不高且动态范围比16位整数所能提供的范围更大的情况，例如数值介于$10^{-8}$和$60000$之间，同时对精度要求不高时，这种方式可以大幅节省磁盘空间。

但是这种格式最好仅作为数据存储方式。如果需要直接在NumPy中进行运算，NumPy就会进行强制类型转换，从而影响性能。可以使用`Dataset.read_direct`，`Dataset.astype`等方法进行处理：

```Python
In [10]: dset = f.create_dataset("half_float", (100, 100, 100), dtype=np.float16)

In [11]: a = dset[...]

In [12]: a = a.astype(np.float32)
```

### Fixed-Length Strings

关于定长字符串的问题主要是来源于历史，例如从FORTRAN时代遗留的字符串格式。在本书完成时这仍然是一个问题，但是目前版本下基本不存在类似问题：

```Python
In [13]: dt = np.dtype("S10")  # 10-character byte string

In [14]: dset = f.create_dataset("fixed_string", (100,), dtype=dt)

In [15]: dset[0] = "Hello"
TypeError: No conversion path for dtype: dtype('<U5')

In [16]: dset[0] = "thisstringhasmorethan10characters"
TypeError: No conversion path for dtype: dtype('<U33')
```

在书中，这两种赋值方式分别会得到`'Hello'`和`'thisstring'`，但是Python 3下已经直接使用变长字符串，且已经很好地支持了Unicode字符编码，因此会抛出`TypeError`。

### Variable-Length Strings

NumPy的一个特性在于数组中所有的元素都有相同的大小，这在使用数值型时非常方便，例如双精度浮点数都是8字节宽，从而提升了性能。但是在面对字符串时无法保证每个字符串的长度都是固定的。当使用8字节ASCII字符串类型时，需要显式地指定字符串的长度，这带来的问题是会让超出长度的字符串被截断：

```Python
In [17]: dt = np.dtype("S3")

In [18]: a = np.array(["a", "ab", "abc", "abcd"], dtype=dt)

In [19]: a
Out[19]: array([b'a', b'ab', b'abc', b'abc'], dtype='|S3')
```

通过返回值可以看出，当前版本下的NumPy已经默认使用了Unicode字符串，同时自动适配字符串长度：

```Python
In [20]: b = np.array(["a", "ab", "abc", "abcd", "abcde", "thisstringislongenoughandover32characters"])

In [21]: b
Out[21]:
array(['a', 'ab', 'abc', 'abcd', 'abcde',
       'thisstringislongenoughandover32characters'], dtype='<U41')
```

#### The vlen String Data Type

在本书完成时，NumPy还完全不支持变长字符串，因此需要使用`h5py`提供的类型：

```Python
In [22]: dt = h5py.special_dtype(vlen=str)

In [23]: dt
Out[23]: dtype('O')

In [24]: dt.kind
Out[24]: 'O'
```

这使得NumPy将数据类型设置为Python的`object`类型，从而存储字符串。在目前来说这个问题已经不复存在。

#### Working with vlen String Datasets

使用基于`object`类型的字符串，就可以存储各类字符串数值：

```Python
In [25]: dset = f.create_dataset("vlen_dataset", (100,), dtype=dt)

In [26]: dset[0] = "Hello"

In [27]: dset[1] = np.string_("Hello2")

In [28]: dset[2] = 'X' * 10000

In [29]: out = dset[0]

In [30]: type(out)
Out[30]: str

In [31]: dset[0:2]
Out[31]: array(['Hello', 'Hello2'], dtype=object)

In [32]: out = dset[0:1]

In [33]: out.dtype
Out[33]: dtype('O')
```

#### Byte Versus Unicode Strings

正如前卫所说，本书的示例都是基于Python 2，Python 2和Python 3对于字符串存在编码风格的差异。这种存储方式的不同可能会带来移植性和兼容性的问题。在Python 2中的字符串本质为字节字符串(*byte string*)，这在Python 2/3中都支持，只是在Python 2中作为默认`str`的类型，而Python 3中不是，这点可以从笔记和书中示例结果的不同看出。由于很多使用HDF5的第三方引用仅支持ASCII编码字符串，因此使用这种编码方式会带来最好的可移植性。

#### Using Unicode String

在Python 3中，`str`恰恰对应的是Unicode字符（和Python 2颠倒了）。也就是说，之前的代码：

```Python
h5py.special_dtype(vlen=str)
```

在Python 2中，等价于

```Python
h5py.special_dtype(vlen=btyes)
```

但是在Python 3中则等价于`h5py.special_dtype(vlen=unicode)`，事实上，在当前版本下，已经没有`unicode`作为`vlen`参数的值了：

```Python
In [34]: dt = h5py.special_dtype(vlen=unicode)
NameError: name 'unicode' is not defined
```

#### Don't Store Binary Data in Strings

由于HDF5允许存放ASCII编码字符串，因此如果在字符串中存在二进制编码的数据，则会被直接处理而不进行任何反馈。例如如果字符串中存在`\x00`，即`NULL`，则会直接被截断。存放原始二进制数据的最好实现是后文提到的不透明类型(opaque type)。

#### Future-Proofing Your Python 2 Application

由于Python 2和Python 3之间存在的关于编码的问题，因此为了保证健壮性，尽量遵循一些一致的规则，例如始终牢记文本字符串和字节字符串之间的差异，当使用字节字符串时，永远使用`h5py.special_dtype(vlen=btyes)`的方式，同时注意观察字符串前的标识符，`'u'`对应Unicode而`'b'`对应bytes。

### Compound Types

对于一些数据，需要使用复合数据类型，类似于C语言中的结构体或像SQL数据库、CSV文件一样的多列数据。NumPy支持结构化数组，关于结构化数组可以参考官方文档和：

> 一文彻底搞懂numpy的结构化数组——structured array[CSDN](https://blog.csdn.net/qq_27825451/article/details/82425512)

结构化数组的`NumPy dtype`包含了一系列的字段，这些字段包含自己的名称和格式，例如当创建一个100个包含气候监测实验结果的数据集，其中有气温、气压和风速三个数据：

```Python
In [35]: dt = np.dtype([("temp", np.float), ("pressure", np.float), ("wind", np.float)])

In [36]: a = np.zeros((100,), dtype=dt)
```

可以直接使用字段名称作为索引获取数据，在单个字段上可以使用类字典的方式获取数据：

```Python
In [37]: out = a["temp"]

In [38]: out.shape
Out[38]: (100,)

In [39]: out.dtype
Out[39]: dtype('float64')

In [40]: out = a[0]

In [41]: out
Out[41]: (0., 0., 0.)

In [42]: out["temp"]
Out[42]: 0.0
```

HDF5提供了更加灵活的操作方式，可以更加简单的使用切片，甚至混合使用字段和切片：

```Python
In [43]: dset = f.create_dataset("compound", (100,), dtype=dt)

In [44]: out = dset["temp", "pressure"]

In [45]: out.shape
Out[45]: (100,)

In [46]: out.dtype
Out[46]: dtype([('temp', '<f8'), ('pressure', '<f8')])

In [47]: out = dset["temp", 90:100]

In [48]: out.shape
Out[48]: (10,)

In [49]: out.dtype
Out[49]: dtype('<f8')
```

这仍然是一种非常高效的方式，因为HDF5只从磁盘中读取所需要的数据。因此，也可以选择只更新需要更新的字段：

```Python
In [50]: out[...] = 98.6

In [51]: dset["temp", 90:100] = out
```

### Complex Numbers

NumPy和Python都支持复数。复数对象实际是由两个浮点数结合而成，一个表示实部，一个表示虚部。在NumPy中可以使用8位单精度，16位双精度和24位扩展精度的复数。

尽管HDF5没有内置复数的数据格式，但是`h5py`配套了相关的标准，即使用`r`表示实部，使用`i`表示虚部：

```Python
In [52]: dset = f.create_dataset("single_complex", (100,), dtype="c8")

In [53]: f.flush()

In [54]: !h5ls -vlr typesdemo.hdf5
Opened "typesdemo.hdf5" with sec2 driver.
/                        Group
    Location:  1:96
    Links:     1

...

/single_complex          Dataset {100/100}
    Location:  1:16544
    Links:     1
    Storage:   800 logical bytes, 0 allocated bytes
    Type:      struct {
                   "r"                +0    native float
                   "i"                +4    native float
               } 8 bytes

...
```

### Enumerated Types

这一节介绍的是C语言用户所熟悉的枚举(*enumerated types* or *enums*)类型。由于NumPy不支持这个数据类型，因此又需要使用`h5py.special_dtype`进行处理。在这里，需要使用`enum`关键字，并同时提供一个基本类型和将名称映射至值的字典，然后就可以像正常的整型数据集一样处理，也可以像变长字符串一样读取数据类型：

```Python
In [55]: mapping = {"RED": 0, "GREEN": 1, "BLUE": 2}

In [56]: dt = h5py.special_dtype(enum=(np.int8, mapping))

In [57]: dset = f.create_dataset("enum", (100,), dtype=dt)

In [58]: dset[0]
Out[58]: 0

In [59]: dset[0].dtype
Out[59]: dtype('int8')
```

需要注意的是，无论是HDF5还是NumPy，**都不会对枚举中的数值进行检查**，也就是说，即使存入一个不符合枚举的值，HDF5同样会接受这个值：

```Python
In [60]: dset[0] = 100

In [61]: dset[0]
Out[61]: 100
```

因此使用枚举需要非常谨慎，同时保证用户都能正确理解这是枚举（而不是其他整型数值）。

### Booleans

当存储布尔值时，常用方法是使用整数。NumPy本身支持布尔数组，即数据类型`np.bool`，但是在底层，布尔类型的数组存储为单字节整数。HDF5没有原生布尔类型，但是`h5py`提供一个通过枚举实现的数据类型（类似于复数），其基本类型为`np.int8`，映射为`{"FALSE": 0, "TRUE": 1}`。

```Python
In [62]: with h5py.File("bool.hdf5", 'w') as ff:
    ...:     ff.create_dataset("bool", (100,), dtype=np.bool)

In [63]: !h5ls -vlr bool.hdf5
Opened "bool.hdf5" with sec2 driver.
/                        Group
    Location:  1:96
    Links:     1
/bool                    Dataset {100/100}
    Location:  1:800
    Links:     1
    Storage:   100 logical bytes, 0 allocated bytes
    Type:      enum native signed char {
                   FALSE            = 0
                   TRUE             = 1
               }
```

### The array Type

如果需要在一个元素中存储多个相同类型的值，那么可以使数组类型，这种方式不同于使用复合类型，数组不存在字段，每个元素自身就是一个多维数组。

```Python
In [64]: dt = np.dtype("(2,2)f")

In [65]: dt
Out[65]: dtype(('<f4', (2, 2)))

In [66]: dset = f.create_dataset("array", (100,), dtype=dt)

In [67]: dset.dtype
Out[67]: dtype(('<f4', (2, 2)))

In [68]: dset.shape
Out[68]: (100,)

In [69]: out = dset[0]

In [70]: out
Out[70]:
array([[0., 0.],
       [0., 0.]], dtype=float32)
```

注意当这里重新读取一个元素时，数值类型已经不是一开始定义的数组类型，NumPy将数组自动提升为基本类型的完整数组，这也是`dset[...].dtype != dset.dtype`的情况之一。

同样，如果使用原生NumPy数组，并令数据类型为数组类型，NumPy也会将多余的轴转化为NumPy多维数组：

```Python
In [71]: a = np.zeros((100,), dtype=dt)

In [72]: a.dtype
Out[72]: dtype('float32')

In [73]: a.shape
Out[73]: (100, 2, 2)
```

如果数组类型都会被自动转换，那么何时是适合的使用场景呢？通常来说，数组类型可以和复合类型结合，例如需要记录一个时间戳以及对应的(2,2)的传感器数据：

```Python
In [74]: dt_timestamp = np.dtype("uint64")

In [75]: dt_sensor = np.dtype("(2,2)f")

In [76]: dt = np.dtype([("time", dt_timestamp), ("sensor", dt_sensor)])
```

通过创建一个使用数组的复合数据类型，可以非常方便的记录这种数据：

```Python
In [77]: import time

In [78]: dset = f.create_dataset("mydata", (100,), dtype=dt)

In [79]: dset["time", 0] = time.time()

In [80]: dset["sensor", 0] = ((1,2), (3,4))
ValueError: When changing to a larger dtype, its size must be a divisor of the total size in bytes of the last axis of the array.
```

**注意**！如果原样输入书中的示例代码，这里会出现`ValueError`报错。由于网上并没有相关资料，经过尝试发现正确的做法为：

```Python
In [81]: dset["sensor", 0] = (1,2,3,4)

In [82]: dset["sensor", 0]
Out[82]:
array([[1., 2.],
       [3., 4.]], dtype=float32)
```

这样才能产出正确的数据。其原因实际上正如上文所说，在这里使用的数据类型并不是一开始定义好的数据类型（数组），NumPy自动将其提升为多维数组，因此如果在赋值时再使用多维数组赋值，就会导致数组大小不匹配，从而报错。正确的赋值方式应该是直接使用一维数组，转化为多维数组的操作应该交给NumPy自行处理。

接下来就可以正常使用：

```Python
In [83]: out = dset[0]

In [84]: out
Out[84]: (1580741547, [[1., 2.], [3., 4.]])

In [85]: out["sensor"]
Out[85]:
array([[1., 2.],
       [3., 4.]], dtype=float32)
```

当用户使用的数据包含类似这种结构时，使用数组类型会优于在数据集中添加额外的维度，这不仅令获取数据更加简单，也使得整体的数据结构更加有直观含义。

### Opaque Types

使用不透明类型(*opaque type*)的情况比较少见，主要适用于无法使用NumPy格式表示的数据结构，例如一些非数值形式的二进制数据。HDF5提供了一种处理这种问题的机制。

NumPy的`void "V"`类型用来存储这类不透明数据。这种类型类似于定宽字符串类型`"S"`。例如要在NumPy中存储200字节长的不透明字段：

```Python
In [86]: dt = np.dtype("V200")

In [87]: a = np.zeros((10,), dtype=dt)  # 10 elements each 200 bytes long

In [88]: dset = f.create_dataset("opaque", (10,), dtype=dt)

In [89]: dset.dtype
Out[89]: dtype('V200')

In [90]: dset.shape
Out[90]: (10,)
```

当需要存储原始二进制数据时，应当考虑使用不透明数据类型。尽管可以将数据存储在字符串中，但是HDF5中的字符串仅能存储ASCII或Unicode编码类型。书中给出一个在HDF5不透明数据和Python字节字符串之间往返的案例，这里将二进制数据作为属性存放：

```Python
In [91]: binary_blob = b"A\x00B\x00"  # Try storing this directly! It won't work.

In [92]: dset.attrs["name"] = np.void(binary_blob)  # "Void" type maps to HDF5 opaque

In [93]: out = dset.attrs["name"]

In [94]: out
Out[94]: void(b'\x41\x00\x42\x00')

In [95]: binary_blob = out.tostring()

In [96]: binary_blob
Out[96]: b'A\x00B\x00'

In [97]: f.close()
```

### Dates and Times

在HDF5中存储日期和时间是非常常见的需求。尽管HDF5中有日期类型，但是基本没有人使用。通常表示时间的方式是使用Unix时间戳或POSIX时间戳，计算自1970年1月1日UTC时间至今经过的秒数。

如果只需要精确至秒，使用整型就足够：

```Python
timestamp = np.dtype("u8")
```

也可以使用标准库中`time.time()`的双精度浮点数

```Python
In [1]: import time

In [2]: time.time()
Out[2]: 1580750916.2593997
```

标准库`datetime`提供的`datetime`对象提供ISO标准格式字符串以获得较好的阅读体验：

```Python
In [3]: import datetime

In [4]: datetime.datetime.now().isoformat()
Out[4]: '2020-02-04T01:30:01.490901'
```

这种格式是所谓的原始时间戳，即不包含时区或闰秒信息。如果程序不在一个时区内工作，或者对闰秒敏感，则需要在文件中存储适当的数据，例如使用复合数据类型。

## Chapter8. Organizing Data with References, Types, and Dimension Scales

通常来说，数据文件并不仅是组、数据集和属性的集合，HDF5提供了一些很好的特性可以表达数据间的关系。

本章包含了HDF5中用以连接不同数据类型的三个最有用的构造。引用，即HDF5的指针类型，可以很好的将链接像数据一样存储。命名类型可以跨数据集实施类型一致性。 标尺尺度(*Dimension Scales*)是一种HDF5标准，让用户可以使用一种第三方程序可以理解的方式将有意义的数据轴附加到数据上。

### Object References

在之前的章节中介绍了在组中链接如何定位对象。这里提供另一种进行链接的机制，同时还能作为数据存储在数据集和属性中。

#### Creating and Resolving References

创建一个包含两个组和一个数据集的文件：

```Python
In [1]: import numpy as np

In [2]: import h5py

In [3]: f = h5py.File("refs_demo.hdf5", 'w')

In [4]: grp1 = f.create_group("group1")

In [5]: grp2 = f.create_group("group2")

In [6]: dset = f.create_dataset("mydata", shape=(100,))
```

这里发现`grp1`有一个新的属性`ref`。使用`ref`返回一个HDF5对象引用(*object reference*)，这是对于文件中对象的指针：

```Python
In [7]: grp1.ref
Out[7]: <HDF5 object reference>
```

再次使用引用对象进行解除引用就能获取原始对象，引用的Python类型和`h5py.Reference`完全相同：

```Python
In [8]: out = f[grp1.ref]

In [9]: out == grp1
Out[9]: True

In [10]: isinstance(grp1.ref, h5py.Reference)
Out[10]: True
```

由于引用是定位对象的“绝对”方法，因此可以不局限于根组，而是可以在任何组中使用（但是这是一种个人感觉很奇怪的使用方式），同时显然也不能在超出所属文件的地方使用：

```Python
In [11]: out = grp2[grp1.ref]

In [12]: out == grp1
Out[12]: True

In [13]: with h5py.File("anotherfile.hdf5", 'w') as f2:
    ...:     out = f2[grp1.ref]
ValueError: Unable dereference object (bad object header version number)
```

#### References as "Unbreakable" Links

但就上例中给出的特性看，引用相比链接并没有任何提升。这里指出一个重要的区别在于，引用可以作为数据存储，且完全独立于后续可能的重命名。例如如果需要在一个组中加入一个指向数据集`mydata`的属性，可以直接将名称作为属性记录：

```Python
In [14]: grp1.attrs["dataset"] = dset.name

In [15]: grp1.attrs["dataset"]
Out[15]: '/mydata'

In [16]: out = f[grp1.attrs["dataset"]]

In [17]: out == dset
Out[17]: True
```

这时候是完全一致的，但是一旦对数据集重命名，这种方式会立刻失效：

```Python
In [18]: f.move("mydata", "mydata2")

In [19]: out = f[grp1.attrs["dataset"]]
KeyError: "Unable to open object (object 'mydata' doesn't exist)"
```

但是如果使用引用，即使对数据集进行重命名也不会出现这样的问题：

```Python
In [20]: grp1.attrs["dataset"] = dset.ref

In [21]: grp1.attrs["dataset"]
Out[21]: <HDF5 object reference>

In [22]: out = f[grp1.attrs["dataset"]]

In [23]: out == dset
Out[23]: True

In [24]: f.move("mydata2", "mydata3")

In [25]: out = f[grp1.attrs["dataset"]]

In [26]: out == dset
Out[26]: True
```

#### References as Data

引用是HDF5的一种完整类型，可以在属性和数据集中自由使用。但是显然NumPy并不支持引用这一格式，因此需要使用`special_dtype`结合`ref`关键字：

```Python
In [27]: dt = h5py.special_dtype(ref=h5py.Reference)

In [28]: dt
Out[28]: dtype('O')
```

`dt`在这里直接作为一种常规对象类型显示。有了这个格式就可以创建引用类型数据集。但是由于这里的引用并没有初始化，因此如果试图检索其中的元素，会返回空值引用。同时，类似于C语言中的空指针，由于引用没有指向任何对象，因此试图对一个空值引用解除引用会抛出`ValueError`异常：

```Python
In [29]: ref_dset = f.create_dataset("references", (10,), dtype=dt)

In [30]: out = ref_dset[0]

In [31]: out
Out[31]: <HDF5 object reference (null)>

In [32]: f[out]
ValueError: Invalid HDF5 object reference
```

而不适用异常捕获检查是否为空值引用的简单方式是进行布尔运算：

```Python
In [33]: bool(out)
Out[33]: False

In [34]: bool(grp1.ref)
Out[34]: True
```

但是布尔运算返回`True`并不代表引用可以解析出某个对象，只是说明这个引用不是空值引用。例如对一个对象创建引用后再删除这个对象，使用布尔运算仍然可以得到`True`值，但是如果想要对其进行解除引用，则依然会抛出`ValueError`异常。

### Region References

区域引用可以存储对数据集一部分创建的引用。

#### Creating Region References and Reading

对之前创建的数据集`dset`使用`regionref`属性：

```Python
In [35]: dset.name
Out[35]: '/mydata3'

In [36]: dset.shape
Out[36]: (100,)

In [37]: dset.regionref
Out[37]: <h5py._hl.base._RegionProxy at 0x17ad7f44448>
```

使用这个对象就可以存储选择的区域。通过使用切片可以创建所需的区域引用：

```Python
In [38]: ref_out = dset.regionref[10:90]

In [39]: ref_out
Out[39]: <HDF5 region reference>
```

类似于对象引用，区域引用也是不透明的，通常只查看其形状和选择区域的形状：

```Python
In [40]: dset.regionref.shape(ref_out)
Out[40]: (100,)

In [41]: dset.regionref.selection(ref_out)
Out[41]: (80,)
```

一旦使用了区域引用，就可以直接从数据集中检索数据：

```Python
In [42]: data = dset[ref_out]

In [43]: data
Out[43]:
array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32)

In [44]: data.shape
Out[44]: (80,)
```

#### Fancy Indexing

一旦使用某种“花式”索引，例如布尔数组，则**形状将始终为一维**。这模仿了NumPy对于此类选择的行为。例如给定一个二维数组，选择其中大于0.5的值，可以对这个数组创建一个区域引用：

```Python
In [45]: dset_random = f.create_dataset("small_example", (3, 3))

In [46]: dset_random[...] = np.random.random((3, 3))

In [47]: dset_random[...]
Out[47]:
array([[0.37649217, 0.11262173, 0.6997954 ],
       [0.5739028 , 0.28569105, 0.9787948 ],
       [0.2525628 , 0.09163964, 0.2544896 ]], dtype=float32)

In [48]: index_arr = dset_random[...] > 0.5

In [49]: index_arr
Out[49]:
array([[False, False,  True],
       [ True, False,  True],
       [False, False, False]])

In [50]: random_ref = dset_random.regionref[index_arr]

In [51]: dset_random.regionref.selection(random_ref)
Out[51]: (3,)
```

这里有三个符合的元素，这些元素被展开为一个含有三个元素的一维数组。如果查看这些元素，可以看见这些数按照从行到列的顺序读取，即`[0, 2], [1, 0], [1, 2]`的顺序：

```Python
In [52]: data = dset_random[random_ref]

In [53]: data
Out[53]: array([0.6997954, 0.5739028, 0.9787948], dtype=float32)
```

#### Finding Datasets with Region References

使用区域引用的一个技巧是：区域引用可以当作对象引用来检索数据集。

以之前的`(80,)`的区域`ref_out`为例，直接对文件使用可以获取这个数据集，然后就可以直接获取引用的区域对象：

```Python
In [54]: f[ref_out]
Out[54]: <HDF5 dataset "mydata3": shape (100,), type "<f4">

In [55]: f[ref_out]
Out[55]: <HDF5 dataset "mydata3": shape (100,), type "<f4">

In [56]: f[ref_out][ref_out]
Out[56]:
array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32)
```

这个技巧在将区域引用作为属性存储时非常有用。这意味着只要使用区域引用，就可以不需要额外保存对象引用来确定使用这个引用的位置。

### Named Types

HDF5中还有一个链接概念，它比对象或区域引用都微妙得多。

当创建数据集或属性时，是使用固定的数据类型创建的。如果一个文件中有多个数据，而用户需要使这些数据的类型完全相同。在这种情况下，HDF5原生提供了一种方式对这种类型进行保存，同时**完全独立于**任何数据集或属性。

#### The Datatype Object

创建一个命名类型，只需要将一个`NumPy dtype`赋值给文件中的一个名称即可：

```Python
In [57]: f["mytype"] = np.dtype("float32")
```

当打开这个名称时，不会得到数据类型的返回：

```Python
In [58]: out = f["mytype"]

In [59]: out
Out[59]: <HDF5 named type "mytype" (dtype <f4)>
```

类似于数据集对象，这里的`h5py.Datatype`也是一个允许用户访问HDF5数据类型的代理，最常见的属性是`Datatype.dtype`，会返回等价的`NumPy dtype`对象：

```Python
In [60]: out.dtype
Out[60]: dtype('<f4')
```

由于这是一个完整的对象，因此还有一些其他的属性.也可以像数据集和组一样使用`.file`（`h5py.File`的示例），`.ref`（对象引用），属性等：

```Python
In [61]: out.name
Out[61]: '/mytype'

In [62]: out.parent
Out[62]: <HDF5 group "/" (6 members)>

In [63]: out.attrs["info"] = "This is an attribute on a named type object"
```

#### Linking to Named Types

创建数据集或属性时使用命名类型只需要提供`Datatype`的示例作为`dtype`即可：

```Python
In [64]: dset = f.create_dataset("typedemo", (100,), dtype=f["mytype"])
```

在这里，HDF5不会将这个数据类型复制到数据集中，它实际上创建了一个指向这个数据类型的引用。因此使用这种方式可以在保持数据组织良好的情况下节省磁盘空间。

对于属性，则需要通过`create`方法显式提供类型：

```Python
In [65]: f.attrs.create("attribute_demo", 1.0 ,dtype=f["mytype"])
```

#### Managing Named Types

一旦命名类型创建完毕，则不能进行任何修改，但是可以将其从文件中取消链接：

```Python
In [66]: del f["mytype"]
```

但是取消链接后试图使用一个新的不同的类型再次赋值是不可行的。这个链接仍然在内部存在，直到所有使用这个命名类型的数据集和属性都被删除为止：

```Python
In [67]: f["mytype"] = np.dtype("int16")

In [68]: dset = f["typedemo"]

In [69]: dset.dtype
Out[69]: dtype('<f4')
```

### Dimension Scales

真实世界数据通常会附加数据单位。假设如下场景，一个记录大气层温度数据的三维数据集：

```Python
In [70]: dset = f.create_dataset("temperatures", (100, 100, 100), dtype='f')
```

显然温度需要指定单位，在这里可以使用一个属性记录这个标尺：

```Python
In [71]: dset.attrs["temp_units"] = "C"
```

问题在于接下来。如果在$x, y, z$三个轴上的数据分辨率不同，例如$x$或$y$轴这个水平面上每10千米获取一个数据点，但是在$z$轴这个垂直层面上每100米就需要获取一个数据点，则需要加入新的属性说明步长存在不同：

```Python
In [72]: dset.attrs["steps"] = [10000, 10000, 100]
```

但是这个属性无法让人确定其是否是按照$x, y, z$这样的顺序排列的，因此还需要再加入一个属性说明数据轴的顺序：

```Python
In [73]: dset.attrs["axes"] = ["x", "y", "z"]
```

这样一系列的操作导致数据集显得很破碎，而且需要花费大量时间在用户间确认格式。

基于这种情况，HDF5提供了标尺尺度(*Dimension Scales*)规范。就像之前的属性系统一样，它是基于HDF5构建的功能，以标准化的方式使用数据集，属性和引用的机制来构建更具表现力的对象。这些类似的特性由HDF组进行了一系列的标准化，使得第三方应用程序知道如何处理组、数据集、属性和引用的特定组合。

#### Creating Dimension Scales

可以看到数据集有一个之前没有使用过的属性`.dims`：

```Python
In [74]: for name in dset.attrs:
    ...:     del dset.attrs[name]

In [75]: dset.dims
Out[75]: <Dimensions of HDF5 object at 1627110343688>
```

这个是使用标尺尺度的入口。在HDF5中，标尺尺度是一个带有某些元数据的单独的“轴”数据集，这个数据集使用引用链接到主数据集。在之前的案例上，需要创建三个标尺尺度，对于$x$轴和$y$轴，步长设置为10 km，对于$z$轴，步长设置为100 m。

```Python
In [76]: f.create_dataset("scale_x", data=np.arange(100)*10e3)
Out[76]: <HDF5 dataset "scale_x": shape (100,), type "<f8">

In [77]: f.create_dataset("scale_y", data=np.arange(100)*10e3)
Out[77]: <HDF5 dataset "scale_y": shape (100,), type "<f8">

In [78]: f.create_dataset("scale_z", data=np.arange(100)*100.0)
Out[78]: <HDF5 dataset "scale_z": shape (100,), type "<f8">
```

然后就可以对`dset.dims`对象使用`create_scale`来将其创建为HDF5标尺尺度数据集。

```Python
In [79]: dset.dims.create_scale(f["scale_x"], "Simulation X (North) axis")

In [80]: dset.dims.create_scale(f["scale_y"], "Simulation Y (East) axis")

In [81]: dset.dims.create_scale(f["scale_y"], "Simulation Z (Vertical) axis")
```

如果查看数据集的属性可以看出，`create_scale`方式本质是在数据集中加入了标准化的属性名称和值：

```Python
In [82]: for key, val in f["scale_x"].attrs.items():
    ...:     print(key, ':', val)
CLASS : b'DIMENSION_SCALE'
NAME : b'Simulation X (North) axis'
```

#### Attaching Scales to a Dataset

在有了三个标尺之后，就可以将其关联至数据集。这这里，需要**将数据集每个轴和对应标尺关联**。这通过对`Dataset.dims`对象使用索引实现：

```Python
In [83]: dset.dims[0].attach_scale(f["scale_x"])

In [84]: dset.dims[1].attach_scale(f["scale_y"])

In [85]: dset.dims[2].attach_scale(f["scale_z"])
```

在这里`dims[N]`对象也是一个代理，可以确认使用的标尺尺度所关联的数据集的轴。同样，一个轴**可以**关联多个标尺尺度。

`dims[N]`的工作方式类似于有序词典，并支持按名称和索引进行访问。在这种情况下，索引指的是标尺的添加顺序。 例如，要获取包含$x$标尺的数据集，我们可以选择数据集的维度0相关联的第一个比例尺：

```Python
In [86]: dset.dims[0][0]
Out[86]: <HDF5 dataset "scale_x": shape (100,), type "<f8">
```

如果要获得轴上的真实数据，对数据集使用切片即可：

```Python
In [87]: dset.dims[0][0][...]
Out[87]:
array([     0.,  10000.,  20000.,  30000.,  40000.,  50000.,  60000.,
        70000.,  80000.,  90000., 100000., 110000., 120000., 130000.,
       140000., 150000., 160000., 170000., 180000., 190000., 200000.,
       210000., 220000., 230000., 240000., 250000., 260000., 270000.,
       280000., 290000., 300000., 310000., 320000., 330000., 340000.,
       350000., 360000., 370000., 380000., 390000., 400000., 410000.,
       420000., 430000., 440000., 450000., 460000., 470000., 480000.,
       490000., 500000., 510000., 520000., 530000., 540000., 550000.,
       560000., 570000., 580000., 590000., 600000., 610000., 620000.,
       630000., 640000., 650000., 660000., 670000., 680000., 690000.,
       700000., 710000., 720000., 730000., 740000., 750000., 760000.,
       770000., 780000., 790000., 800000., 810000., 820000., 830000.,
       840000., 850000., 860000., 870000., 880000., 890000., 900000.,
       910000., 920000., 930000., 940000., 950000., 960000., 970000.,
       980000., 990000.])
```

也可以使用在创建标尺时的名称通过字典方式获取。字典中的`items`，`keys`，`values`等方法都可以使用：

```Python
In [88]: dset.dims[0]["Simulation X (North) axis"]
Out[88]: <HDF5 dataset "scale_x": shape (100,), type "<f8">
```

最后，还可以对数据集的每个轴添加标签，可以合理存放轴的名称：

```Python
In [89]: dset.dims[0].label = 'x'

In [90]: dset.dims[1].label = 'y'

In [91]: dset.dims[2].label = 'z'
```

## Chapter9. Concurrency: Parallel HDF5, Threading, and Multiprocessing

### Python Parallel Basics

广义上讲，有三种方法可以在Python中进行并发编程：线程，多进程模块`multiprocessing`，和对消息传递接口(Message Passing Interface, MPI)使用绑定。

基于线程的代码非常适合GUI和调用不占用Python解释器的外部库的应用程序。由于GIL的存在，运行纯Python程序时只能使用一个内核。由于HDF5库将所有调用序列化，因此使用线程在HDF5方面也没有性能优势。

多进程模块`multiprocessing`支持基于`fork()`的并行处理。主要限制在于HDF5库，即使以只读方式打开文件，并行进程也不能共享单个HDF5文件。基于多进程模块的代码非常适合长期运行、CPU受限且数据I/O占是主进程相对较小的程序。使用多进程模块是Python编写基于多个内核的并行代码的最简单方法，强烈建议用于通用计算。

基于MPI的并行HDF5(MPI-based Parallel HDF5)是最好的选择。MPI是HDF5库官方支持的并行方式。可以有无限数量的进程，这些进程可以共享同一打开的HDF5文件，并支持读写，修改文件结构等操作。使用这种方式编写代码需要更加注意，但是是在并行运算中使用HDF5最优雅，性能最好的方式。

除此之外还有第四中并行计算机制目前正逐步流行起来。IPython作为解释器接口，围绕ZeroMQ网络系统设计了自己的集群功能。它甚至可以在后端使用MPI来提高并行代码的性能。目前在IPython并行模型中使用`h5py`还不多见于实际场景，但是应该对其保持关注。

### Threading

HDF5没有对线程级并行的原生支持，尽管可以在线程中使用HDF5和`h5py`，但是这不会带来性能上的提升。

Python本身包含一个用于控制对解释器功能访问的主锁，称为全局解释器锁(Global Interpreter Lock, GIL)。GIL将对从多个线程到基本资源（如对象引用计数）的访问进行序列化。因此尽管在Python程序中可以具有任意多个线程，但是一次只能使用一个解释器。这在编写需要花费大量时间等待用户输入的GUI或基于Web的程序时不存在问题。因为可以在等待的时间释放GIL，同时让其他线程可以使用解释器。

`h5py`使用类似的概念。使用锁定对HDF5的访问进行序列化，因此一次只有一个线程可以使用这个库。与Python中的其他I/O机制不同，对HDF5库的所有使用都是阻塞的，一旦对HDF5进行了调用，则GIL在完成之前不会释放。

`h5py`是线程安全的，因此安全地在线程之间共享对象而不用担心对象损坏，并且没有一个全局状态可以使一个线程在另一个线程之上。但是对于某些高级操作并不能保证是原子操作。因此建议使用递归锁来管理对HDF5对象的访问。

```Python
In [1]: import threading

In [2]: import time

In [3]: import random

In [4]: import numpy as np

In [5]: import h5py

In [6]: f = h5py.File("thread_demo.hdf5", 'w')

In [7]: dset = f.create_dataset("data", (2, 1024), dtype='f')

In [8]: lock = threading.RLock()

In [9]: class ComputeThread(threading.Thread):
    ...:     def __init__(self, axis):
    ...:         self.axis = axis  # One thread does dset[0,:], the other dset[1, :].
    ...:         threading.Thread.__init__(self)
    ...:
    ...:     def run(self):
    ...:         for idx in range(1024):
    ...:             random_number = random.random()*0.01
    ...:             time.sleep(random_number)  # Perform computation
    ...:             with lock:
    ...:                 dset[self.axis, idx] = random_number     # Save to dataset

In [10]: thread1 = ComputeThread(0)

In [11]: thread2 = ComputeThread(1)

In [12]: thread1.start()

In [13]: thread2.start()

In [14]: # Wait until both threads have finished

In [15]: thread1.join()

In [16]: thread2.join()

In [17]: f.close()
```

### Multiprocessing

由于GIL的存在，任何一个基于线程的Python程序都不可能快过使用一个处理器的时间。在Python 2.6之后，Python提供了多进程模块用以进行并行处理。

只要采取一些预防措施，就可以将多进程与HDF5一起使用。需要记住的最重要的一点是**子进程会从父进程中继承HDF5库的状态**，这会很容易导致多个进程在一个打开的文件中以互相“打架”结束。在本书完成时（2013年10月），即使对只读文件也会出现这个状况。这与如何在Linux/Unix操作系统上使用`fork()`系统调用实现多进程的细节有关。有必要在使用时查看当前版本相关的更新情况。

为了避免这个问题，本书提供了三个建议：

1. 在主过程中执行所有文件I/O，但在调用多进程模块时功能时保证没有文件打开。
2. 多个子进程可以安全地从同一文件读取，但是**只在新进程后创建后再打开文件**。
3. 让每个子进程写入不同的文件，在进程完成后进行合并。

使用Pythonic的并行运算方式是使用进程池对进程进行管理，`multiprocessing.Pool`中的`map`方法基本类似于内置`map`方法：

```Python
In [1]: from multiprocessing import Pool

In [2]: p = Pool(2)  # Create a 2-process pool

In [3]: words_in = ["hello", "some", "words"]

In [4]: words_out = p.map(str.upper, words_in)

In [5]: print(words_out)
['HELLO', 'SOME', 'WORDS']
```

假设有一个包含坐标对的一维数据集：

```Python
In [6]: import numpy as np

In [7]: import h5py

In [8]: with h5py.File("coords.hdf5", 'w') as f:
   ...:     dset = f.create_dataset("coords", (1000, 2), dtype="f4")
   ...:     dset[...] = np.random.random((1000, 2))
```

需要计算每个坐标点到原点的距离。这是一个非常简单的并行问题，因为每个计算间都是独立的。现在使用包含4个进程的进程池进行运算，需要注意的是在使用`map`时，没有任何文件是打开的：

```Python
import numpy as np
from multiprocessing
import Pool import h5py

def distance(arr):
    """ Compute distance from origin to the point (arr is a shape-(2,) array)
    """
    return np.sqrt(np.sum(arr**2))

# Load data and close the input file
with h5py.File('coords.hdf5', 'r') as f:
    data = f['coords'][...]

# Create a 4-process pool
p = Pool(4)

# Carry out parallel computation
result = np.array(p.map(distance, data))

# Write the result into a new dataset in the file
with h5py.File('coords.hdf5') as f:
    f['distances'] = result
```

实际上这段程序运行之后会持续抛出`RuntimeError`报错，且无法使用`<Ctrl>+C`终止程序，原因暂不确定。

在更复杂的需求下，例如不能读取相同的文件时，那么需要要么显式在主进程中进行I/O，要么每个进程生成一个文件碎片然后将其合并：

```Python
import os
import numpy as np
from multiprocessing
import Pool import h5py

def distance_block(idx):
    """ Read a 100-element coordinates block, compute distances, and write back out again to a process-specific file.
    """
    with h5py.File('coords.hdf5','r') as f:
        data = f['coords'][idx:idx+100]

    result = np.sqrt(np.sum(data**2, axis=1))

    with h5py.File("result_index_%d.hdf5"%idx, 'w') as f:
        f["result"] = result

# Create out pool and carry out the computation
p = Pool(4)
p.map(distance_block, range(0, 1000, 100))

with h5py.File('coords.hdf5') as f:
    dset = f.create_dataset("distances", (1000,), dtype="f4")

    # Loop over our 100-element "chunks" and merge the data into coords.hdf5
    for idx in range(0, 1000, 100):
        filename = "result_index_%d.hdf5"%idx
        with h5py.File(filename, 'r') as f2:
            data = f2["result"][...]

        dset[idx:idx+100] = data
        os.unlink(filename)  # no longer needed
```

### MPI and Parallel HDF5

基于MPI的应用程序通过启动Python解释器的多个并行实例来工作。这些实例通过MPI库相互通信。与多进程相比主要区别在于这些进程是对等的，而不是`Pool`使用的子进程。这意味着所有文件访问也必须通过MPI库进行协调。否则，多个进程将争夺磁盘上的同一文件。好在HDF5本身几乎处理了所有与此有关的细节。用户需要做的就是使用特殊的驱动程序打开共享文件，并遵循一些约束以确保数据一致性。

由于MPI的使用需要一些前置知识，笔记中暂不详述。
