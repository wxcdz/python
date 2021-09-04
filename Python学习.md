# Python学习

## 00 python规范

### 0.1 Python注释

**Python 单行注释**

Python使用 `#` 作为单行注释符号

```
# 注释内容
```

**Python  多行注释**

python 连续的三个单引号或连续三个双引号作为多行注释

```
'''
使用 3 个单引号分别作为注释的开头和结尾
可以一次性注释多行内容
这里面的内容全部是注释内容
'''
```

python 多行注释不支持嵌套

### 0.2 Python标识符命名规范

**Python中标识符命名规则**

1. 标识符是由字符（A~Z 和 a~z）、下划线和数字组成，但第一个字符不能是数字。
2. 标识符不能和 Python 中的保留字相同。
3. Python中的标识符中，不能包含空格、@、% 以及 $ 等特殊字符。
4. 在 Python 中，标识符中的字母是严格区分大小写的，也就是说，两个同样的单词，如果大小格式不一样，多代表的意义也是完全不同的。
5. Python 语言中，以下划线开头的标识符有特殊含义
   - 以单下划线开头的标识符（如 `_width`），表示不能直接访问的类属性，其无法通过 `from...import*` 的方式导入；
   - 以双下划线开头的标识符（如`__add`）表示类的私有成员；
   - 以双下划线作为开头和结尾的标识符（如 `__init__`），是专用标识符。

**不同场景中的标识符，其名称也有一定的规范可循**

1. 当标识符用作模块名时，应尽量短小，并且全部使用小写字母，可以使用下划线分割多个字母，例如 game_mian、game_register 等。
2. 当标识符用作包的名称时，应尽量短小，也全部使用小写字母，不推荐使用下划线，例如 com.mr、com.mr.book 等。
3. 当标识符用作类名时，应采用单词首字母大写的形式。例如，定义一个图书类，可以命名为 Book。
4. 模块内部的类名，可以采用 "下划线+首字母大写" 的形式，如` _Book`;
5. 函数名、类中的属性名和方法名，应全部使用小写字母，多个单词之间可以用下划线分割；
6. 常量命名应全部使用大写字母，单词之间可以用下划线分割；

### 0.3 Python关键字（保留字）

Python 包含的保留字可以执行如下命令进行查看

```python
import keyword

print(keyword.kwlist)
# Output: ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

```



![image-20210715013755143](assets\image-20210715013755143.png)

### 0.4 Python内置函数



![image-20210715014252160](assets\image-20210715014252160.png)

## 01 变量类型和运算符

### 1.1 Python变量的定义和使用

**Python 变量的赋值**

将数据放入变量的过程叫做赋值

```
name = value
```

name表示变量名，value表示值。

变量名要遵守Python标识符规范。

**Python 变量的使用**

```python
"""
变量的定义和使用
\t 制表符
\n 换行符


标识符
    变量名、类名、包名、方法名
标识符命名规则：
    组成部分：
        字母(包含汉字)、数字、下划线
        数字不能开头，大小写敏感
        不能使用系统关键字

    驼峰命名
        1.大驼峰
            MaxNum = 10
        2.小驼峰
            minMum = 20
        3.下划线连接
            average_num = 15
"""
count = 123
print("count = %g " % count)
# Output: count = 123
count2 = 456


print("count = %g \t count2 = %g" % (count, count2))
# Output: count = 123 	 count2 = 456

s = 123
print(s)
# Output: 123

s = 'abc'
print(s)
# Output: abc

```

**python为弱类型语言**

- 变量无须声明就可以直接赋值，对一个不存在的变量赋值就相当于定义一个新变量
- 变量的数据类型可以随时改变，比如，同一个变量可以



### 1.2 Python整数类型（int）

python的整数不分类型，或者说它只有一种类型的整数。Python 整数的取值范围是无限的，不管多大或者多小的数字，Python 都能轻松处理。

#### 整数的不同进制

**十进制形式**

整数就是十进制形式，它由 0~9 共十个数字排列组合而成。

**二进制形式**

由 0 和 1 两个数字组成，书写时以`0b`或`0B`开头

**八进制**

八进制整数由 0~7 共八个数字组成，以`0o`或`0O`开头。注意，第一个符号是数字 0，第二个符号是大写或小写的字母 O。

**十六进制**

由 0~9 十个数字以及 A~F（或 a~f）六个字母组成，书写时以`0x`或`0X`开头

```bash

a = 78
print(a)
print(type(a))
# <class 'int'>

# 十六进制
hex1 = 0x45
hex2 = 0x4AF

print("hex1Value:", hex1)
# hex1Value: 69
print("h3x2Value:", hex2)
# h3x2Value: 1199


# 二进制
bin1 = 0b10
print("bin1Value:", bin1)
# Output: bin1Value: 2
bin2 = 0b110
print("bin2Value:", bin2)
# Output: bin2Value: 6

#八进制
oct1 = 0o26
print("oct1Value:", oct1)
# Output: oct1Value: 22
oct2 = 0O41
print("oct2Value:", oct2)
# Output: oct2Value: 33

# 数字分隔符
click = 1_301_547
distance = 384_000_000
print("Python教程阅读量：", click)
# Python教程阅读量： 1301547
print("地球和月球的距离：", distance)
# 地球和月球的距离： 384000000
```

### 1.3 Python小数/浮点数（float）

**十进制形式**

小数形式，例如 34.6、346.0、0.346

**指数形式**

Python小数的指数形式的写法为：

aEn或aen

a为尾数部分，是一个十进制数，n为指数部分，是一个十进制整数； E或e是固定的字符，用于分割尾数部分和指数部分

指数形式的小数举例：

- 2.1E5 = 2.1×105，其中 2.1 是尾数，5 是指数。
- 3.7E-2 = 3.7×10-2，其中 3.7 是尾数，-2 是指数。
- 0.5E7 = 0.5×107，其中 0.5 是尾数，7 是指数。

```python
f1 = 12.5
print("f1Value: ", f1)
print("f1Type: ", type(f1))
# Output: f1Type:  <class 'float'>

f3 = 0.0000000000000000000000000847
print("f3Value: ", f3)
print("f3Type: ", type(f3))
# f3Value:  8.47e-26
# f3Type:  <class 'float'>
f4 = 345679745132456787324523453.45006
print("f4Value: ", f4)
print("f4Type: ", type(f4))

f6 = 12.3 * 0.1
print("f6Value: ", f6)
print("f6Type: ", type(f6))
# f4Value:  3.456797451324568e+26
# f4Type:  <class 'float'>
```

复数（Complex）是 [Python](http://c.biancheng.net/python/) 的内置类型，直接书写即可。换句话说，Python 语言本身就支持复数，而不依赖于标准库或者第三方库。

复数由实部（real）和虚部（imag）构成，在 Python 中，复数的虚部以`j`或者`J`作为后缀，具体格式为：

a + bj      a 表示实部，b 表示虚部。

### 1.4 Python复数类型（complex）

```python
c1 = 12 + 0.2j
print("c1Value: ", c1)
print("c1Type", type(c1))
c2 = 6 - 1.2j
print("c2Value: ", c2)
#对复数进行简单计算
print("c1+c2: ", c1+c2)
print("c1*c2: ", c1*c2)
```

### 1.5 为什么Python浮点类型存在误差？



### 1.6 Python字符串

### 1.7 Python字符串使用哪种编码格式？

### 1.8 Python bytes

### 1.9 Python bool布尔类型

### 1.10 Python初始化变量，并不一定开辟新的内存！

### 1.11 Python input()函数：获取用户输入的字符串

### 1.12 Python print()函数高级用法

### 1.13 Python格式化字符串

### 1.14 Python转义字符

### 1.15 Python数据类型转换

### 1.16 Python算术运算符

### 1.17 Python赋值运算符

### 1.18 Python位运算符

### 1.19 Python比较运算符

### 1.20 Python逻辑运算符

### 1.21 Python三目运算符

### 1.22 Python运算符优先级和结合性

## 02 列表、元组、字典和集合

### 2.1 什么是序列，Python序列详解

所谓序列，值的就是一块可存放多个值得连续内存空间，这些值一定顺序排列，可通过每个值所在位置的编号(索引)访问。

#### 序列索引

序列中，每个元素都有属于自己的索引，从0开始递增。python还支持索引值是负数，此类索引是从右向左计数(使用负值作为列序中各元素的索引值时，是从-1开始，而不是从0开始)

#### 序列切片

切片操作是访问序列中元素的另一种方法，它可以访问一定范围内的

```go
sname[start:end:step]
```

各个参数的含义是：

- sname: 表示序列的名称
- start：表示切片的开始索引位置（包括该位置），此参数也可以不指定，会默认为 0，也就是从序列的开头进行切片；
- end：表示切片的结束索引位置（不包括该位置），如果不指定，则默认为序列的长度；
- step：表示在切片过程中，隔几个存储位置（包含当前位置）取一次元素，也就是说，如果 step 的值大于 1，则在进行切片去序列元素时，会“跳跃式”的取元素。如果省略设置 step 的值，则最后一个冒号就可以省略。

```python
def func_01():
    str_num = '0123456789'

    result = str_num[0:2]
    print(result)

    result1 = str_num[:2:1]
    print(result1)

    result2 = str_num[:2:2]
    print(result2)

    # step为负值表示从右往左取
    result5 = str_num[::-1]
    print(result5)
```



#### 序列相加

```python

```

#### 序列相乘

```python

```

#### 和序列相关的内置函数

| 函数                     | 功能                                                         |
| ------------------------ | ------------------------------------------------------------ |
| len()                    | 计算序列的长度，即返回序列中包含多少个元素。                 |
| max()                    | 找出序列中的最大元素。注意，对序列使用 sum() 函数时，做加和操作的必须都是数字，不能是字符或字符串，否则该函数将抛出异常，因为解释器无法判定是要做连接操作（+ 运算符可以连接两个序列），还是做加和操作。 |
| min()                    | 找出序列中的最小元素。                                       |
| list()                   | 将序列转换为列表。                                           |
| str()                    | 将序列转换为字符串。                                         |
| sum()                    | 计算元素和。                                                 |
| sorted()                 | 对元素进行排序。                                             |
| reversed()               | 反向序列中的元素。                                           |
| enumerate()              | 将序列组合为一个索引序列，多用在 for 循环中。                |
| find()/rfind()           | 如果有返回索引值，没有返回-1                                 |
| index()/rindex()         | 如果有返回索引值，没有找到的话 raise ValueError              |
| count()                  | 对字符串进行计数                                             |
| split()                  | 进行字符串拆分                                               |
| capitalize()             | 将首字母大写                                                 |
| startswith()/endswith()  | 以字符串开头/以字符串结束                                    |
| upper()/lower()          |                                                              |
| ljust()/fjust()/center() |                                                              |
| lstrip()/rstrip()        |                                                              |
| partition()/rpartition   |                                                              |
| isalpha()/isdigit()      |                                                              |
| isalnum()/isspace()      |                                                              |
|                          |                                                              |
### 2.2 Python列表（list）

#### Python创建列表

python创建列表的方法分为两种。

**1 使用[] 直接创建列表**

使用`[ ]`创建列表后，一般使用`=`将它赋值给某个变量，具体格式如下：

```python
listname = [element1 , element2 , element3 , ... , elementn]
```

```
def func_01():
    num = [1, 2, 3, 4, 5, 6, 7]
    print(num)
    # Output: [1, 2, 3, 4, 5, 6, 7]
```



#### 使用list() 函数创建列表

除了使用`[ ]`创建列表外，Python 还提供了一个内置的函数 list()，使用它可以将其它数据类型转换为列表类型。

```python
def func_02():
    # 将字符串转换成列表
    list1 = list("hello")
    print(list1)
    # Output: ['h', 'e', 'l', 'l', 'o']
    # 将元组转换成列表
    tuple1 = ('Python', 'Java', 'C++', 'JavaScript')
    list2 = list(tuple1)
    print(list2)
    # Output: ['Python', 'Java', 'C++', 'JavaScript']
    # 将字典转换成列表
    dict1 = {'a': 100, 'b': 42, 'c': 9}
    list3 = list(dict1)
    print(list3)
    # Output: ['a', 'b', 'c']
    # 将区间转换成列表
    range1 = range(1, 6)
    list4 = list(range1)
    print(list4)
    # Output: [1, 2, 3, 4, 5]
    # 创建空列表
    print(list())
    # Output: []
```

### 2.3 Python list列表添加元素

列表是序列的一种，所以也可以使用`+`进行连接，这样就相当于在第一个列表的末尾添加了另一个列表。

```python
def func_01():
    language = ["Python", "C++", "Java"]
    birthday = [1991, 1998, 1995]
    info = language + birthday
    print("language =", language)
    # Output:language = ['Python', 'C++', 'Java']
    print("birthday =", birthday)
    # Output:birthday = [1991, 1998, 1995]
    print("info =", info)
    # Output:info = ['Python', 'C++', 'Java', 1991, 1998, 1995]
```

#### append()方法添加元素

append() 方法用于在列表的末尾追加元素，该方法的语法格式如下：

```
listname.append(obj)
```

其中，listname 表示要添加元素的列表；obj 表示到添加到列表末尾的数据，它可以是单个元素，也可以是列表、元组等。

```python
def func_02():
    l = ['Python', 'C++', 'Java']
    # 追加元素
    l.append('PHP')
    print(l)
    # Output: ['Python', 'C++', 'Java', 'PHP']
    # 追加元组，整个元组被当成一个元素
    t = ('JavaScript', 'C#', 'Go')
    l.append(t)
    print(l)
    # Output: ['Python', 'C++', 'Java', 'PHP', ('JavaScript', 'C#', 'Go')]
    # 追加列表，整个列表也被当成一个元素
    l.append(['Ruby', 'SQL'])
    print(l)
    # Output: ['Python', 'C++', 'Java', 'PHP', ('JavaScript', 'C#', 'Go'), ['Ruby', 'SQL']]
```



#### extend()方法添加元素

extend() 和 append() 的不同之处在于：extend() 不会把列表或者元祖视为一个整体，而是把它们包含的元素逐个添加到列表中。

extend() 方法的语法格式如下：

```
listname.extend(obj)
```

其中，listname 指的是要添加元素的列表；obj 表示到添加到列表末尾的数据，它可以是单个元素，也可以是列表、元组等，但不能是单个的数字。

```python
def func_03():
    l = ['Python', 'C++', 'Java']
    # 追加元素
    l.extend('C')
    print(l)
    # Output: ['Python', 'C++', 'Java', 'C']
    # 追加元组，元祖被拆分成多个元素
    t = ('JavaScript', 'C#', 'Go')
    l.extend(t)
    print(l)
    # Output: ['Python', 'C++', 'Java', 'C', 'JavaScript', 'C#', 'Go']
    # 追加列表，列表也被拆分成多个元素
    l.extend(['Ruby', 'SQL'])
    print(l)
    # Output: ['Python', 'C++', 'Java', 'C', 'JavaScript', 'C#', 'Go', 'Ruby', 'SQL']
```



#### insert()方法插入元素

append() 和 extend() 方法只能在列表末尾插入元素，如果希望在列表中间某个位置插入元素，那么可以使用 insert() 方法。

insert() 的语法格式如下：

```
listname.insert(index , obj)
```

其中，index 表示指定位置的索引值。insert() 会将 obj 插入到 listname 列表第 index 个元素的位置。

当插入列表或者元祖时，insert() 也会将它们视为一个整体，作为一个元素插入到列表中，这一点和 append() 是一样的。

```python
def func_04():
    l = ['Python', 'C++', 'Java']
    # 插入元素
    l.insert(1, 'C')
    print(l)
    # Output: ['Python', 'C', 'C++', 'Java']
    # 插入元组，整个元祖被当成一个元素
    t = ('C#', 'Go')
    l.insert(2, t)
    print(l)
    # Output: ['Python', 'C', ('C#', 'Go'), 'C++', 'Java']
    # 插入列表，整个列表被当成一个元素
    l.insert(3, ['Ruby', 'SQL'])
    print(l)
    # Output: ['Python', 'C', ('C#', 'Go'), ['Ruby', 'SQL'], 'C++', 'Java']
    # 插入字符串，整个字符串被当成一个元素
    l.insert(0, "http://c.biancheng.net")
    print(l)
    # Output: ['http://c.biancheng.net', 'Python', 'C', ('C#', 'Go'), ['Ruby', 'SQL'], 'C++', 'Java']

```



### 2.4 Python list列表删除元素

在 Python 列表中删除元素主要分为以下 3 种场景：

- 根据目标元素所在位置的索引进行删除，可以使用 del 关键字或者 pop() 方法；
- 根据元素本身的值进行删除，可使用列表（list类型）提供的 remove() 方法；
- 将列表中所有元素全部删除，可使用列表（list类型）提供的 clear() 方法。

#### del: 根据索引值删除元素

del 是 Python 中的关键字，专门用来执行删除操作，它不仅可以删除整个列表，还可以删除列表中的某些元素

```
del listname[index]
```

listname 表示列表名称，index 表示元素的索引值。

```python
def func_01():
    lang = ["Python", "C++", "Java", "PHP", "Ruby", "MATLAB"]
    # 使用正数索引
    del lang[2]
    print(lang)
    # Output: ['Python', 'C++', 'PHP', 'Ruby', 'MATLAB']
    # 使用负数索引
    del lang[-2]
    print(lang)
    # Output: ['Python', 'C++', 'PHP', 'MATLAB']

    lang = ["Python", "C++", "Java", "PHP", "Ruby", "MATLAB"]
    del lang[1: 4]
    print(lang)
    # Output: ['Python', 'Ruby', 'MATLAB']
    lang.extend(["SQL", "C#", "Go"])
    del lang[-5: -2]
    print(lang)
    # ['Python', 'C#', 'Go']
```

####  pop()：根据索引值删除元素

Python pop() 方法用来删除列表中指定索引处的元素，具体格式如下：

```
listname.pop(index)
```

其中，listname 表示列表名称，index 表示索引值。如果不写 index 参数，默认会删除列表中的最后一个元素

```python
def func_02():
    nums = [40, 36, 89, 2, 36, 100, 7]
    nums.pop(3)
    print(nums)
    # Output:[40, 36, 89, 36, 100, 7]
    nums.pop()
    print(nums)
    # Output: [40, 36, 89, 36, 100]
```



#### remove()：根据元素值进行删除

remove() 方法只会删除第一个和指定值相同的元素，而且必须保证该元素是存在的，否则会引发 ValueError 错误。

```python
def func_03():
    nums = [40, 36, 89, 2, 36, 100, 7]
    # 第一次删除36
    nums.remove(36)
    print(nums)
    # Output: [40, 89, 2, 36, 100, 7]
    # 第二次删除36
    nums.remove(36)
    print(nums)
    # Output: [40, 89, 2, 100, 7]
    # 删除78
    nums.remove(78)
    print(nums)
    # 最后一次删除，因为 78 不存在导致报错，所以我们在使用 remove() 删除元素时最好提前判断一下。
```

#### clear()：删除列表所有元素

```python
def func_04():
    url = list("http://c.biancheng.net/python/")
    url.clear()
    print(url)
```



### 2.5 Python list列表修改元素

#### 修改单个元素

```python
def func_01():
    nums = [40, 36, 89, 2, 36, 100, 7]
    nums[2] = -26  # 使用正数索引
    nums[-3] = -66.2  # 使用负数索引
    print(nums)
    # Output: [40, 36, -26, 2, -66.2, 100, 7]
```



#### 修改一组元素

```python
def func_02():
    nums = [40, 36, 89, 2, 36, 100, 7]
    # 修改第 1~4 个元素的值（不包括第4个元素）
    nums[1: 4] = [45.25, -77, -52.5]
    print(nums)
    # Output: [40, 45.25, -77, -52.5, 36, 100, 7]
def func_03():
    # 如果对空切片（slice）赋值，就相当于插入一组新的元素：
    nums = [40, 36, 89, 2, 36, 100, 7]
    # 在4个位置插入元素
    nums[4: 4] = [-77, -52.5, 999]
    print(nums)
    # Output: [40, 36, 89, 2, -77, -52.5, 999, 36, 100, 7]
    # 但是如果使用字符串赋值，Python 会自动把字符串转换成序列，其中的每个字符都是一个元素，请看下面的代码：
    s = list("Hello")
    s[2:4] = "XYZ"
    print(s)
    # Output: ['H', 'e', 'X', 'Y', 'Z', 'o']
```

### 2.6 Python list列表查找元素

#### index() 方法

index() 方法用来查找某个元素在列表中出现的位置（也就是索引），如果该元素不存在，则会导致 ValueError 错误，所以在查找之前最好使用 count() 方法判断一下。

```python
listname.index(obj, start, end)
```

start 和 end 参数用来指定检索范围：

- start 和 end 可以都不写，此时会检索整个列表；
- 如果只写 start 不写 end，那么表示检索从 start 到末尾的元素；
- 如果 start 和 end 都写，那么表示检索 start 和 end 之间的元素。

```python
def func_01():
    nums = [40, 36, 89, 2, 36, 100, 7, -20.5, -999]
    # 检索列表中的所有元素
    print(nums.index(2))
    # 检索3~7之间的元素
    print(nums.index(100, 3, 7))
    # 检索4之后的元素
    print(nums.index(7, 4))
    # 检索一个不存在的元素
    print(nums.index(55)) #  ValueError: 55 is not in list
```



#### Python list列表排序

```python
def func_02():
    nums = [40, 36, 89, 2, 36, 100, 7, -20.5, 36]
    # 统计元素出现的次数
    print("36出现了%d次" % nums.count(36))
    # 判断一个元素是否存在
    if nums.count(100):
        print("列表中存在100这个元素")
    else:
        print("列表中不存在100这个元素")
```



### 2.7 Python tuple元组详解

元组和列表的不同:

- 列表的元素时可以更改的，包括修改元素值，删除和插入元素，所以列表可变序列。
- 元组一旦创建，它的元素就不可以更改了，所以元组是不可变序列

#### 创建元组

使用 `()`直接创建

```
tuplename = (element1, element2, ..., elementn)
```

uplename 表示变量名，element1 ~ elementn 表示元组的元素。

```python
def func_01():
    num = (7, 14, 21, 22, 44)
    abc = ("Python", 19, [1, 2], ('c', 2.0))
```

元组通常都是使用一对小括号将所有元素包围起来的，但小括号不是必须的，只要将各元素用逗号隔开，Python 就会将其视为元组，请看下面的例子：

```python
def func_02():
    course = "Python教程", "c语言教程"
```

当创建的元组中只有一个字符串类型的元素时，该元素后面必须要加一个逗号。

```python

def func_03():
    a = ("java",)
    print(type(a))
    print(a)

    b = ('java')
    print(type(b))
    print(b)
```

使用`tuple()`函数创建元组

`tuple`的语法格式如下:

```python
```



```python
def func_04():
    # 将字符串转换成元组
    tup1 = tuple("hello")
    print(tup1)
    # 将列表转换成元组
    list1 = ['Python', 'Java', 'C++', 'JavaScript']
    tup2 = tuple(list1)
    print(tup2)
    # 将字典转换成元组
    dict1 = {'a': 100, 'b': 42, 'c': 9}
    tup3 = tuple(dict1)
    print(tup3)
    # 将区间转换成元组
    range1 = range(1, 6)
    tup4 = tuple(range1)
    print(tup4)
    # 创建空元组
    print(tuple())

```



####  访问元组元素

和列表一样，我们可以使用索引（Index）访问元组中的某个元素（得到的是一个元素的值），也可以使用切片访问元组中的一组元素（得到的是一个新的子元组）。

使用索引访问元组元素的格式为：

```python
tuplename[i]
```

tuplename 表示元组名字，i 表示索引值。元组的索引可以是正数，也可以是负数。

使用切片访问元组元素的格式为：

```python
tuplename[start : end : step]
```

其中，start 表示起始索引，end 表示结束索引，step 表示步长。

```python
# 访问元组
def func_05():
    url = tuple("http://www.baidu.com.cn/")
    # 使用索引访问元组中的某个元素
    print(url[3])  # 使用正数索引
    print(url[-4])  # 使用负数索引
    # 使用切片访问元组中的一组元素
    print(url[9: 18])  # 使用正数切片
    print(url[9: 18: 3])  # 指定步长
    print(url[-6: -1])  # 使用负数切片
```



#### 修改元组

```python
# 修改元组
def func_06():
    tup1 = (100, 0.5, -36, 73)
    tup2 = (3 + 12j, -54.6, 99)
    print(tup1 + tup2)
    print(tup1)
    print(tup2)
```

#### 删除元组

```python
# 删除元组
def func_07():
    tup = ('Java教程',)
    print(tup)
    del tup
    # print(tup)
```



### 2.8 Python dict字典



### 2.9 Python dict字典基本操作

### 2.10 Python dict字典方法完全攻略

### 2.11 Python使用字典格式化字符串

#### keys()、values()、和items() 方法



#### update()方法

#### pop() 和 popitem() 方法



#### setdefault() 方法

#### copy() 方法

### 2.12 Python set集合

#### 创建set集合

#### 访问set集合

#### 删除set集合

### 2.13 Python set集合基本操作

#### 向set 集合中添加元素



#### 从set集合中删除元素



#### Python set集合做交集、并集、差集运算



### 2.14 Python set集合方法

### 2.25 Python frozenset集合



## 03 Python字符串常用方法

### 3.1 Python字符串拼接（包含字符串拼接数字）

python**可以直接将两个字符串紧挨着写在一起**

```python
def func_01():
    str1 = "Python教程" "www.python.org"
    print(str1)
    str2 = "Java" "Python" "C++" "PHP"
    print(str2)
```

使用`+`拼接字符串常量

```python
```

字符串和数字的拼接

python不允许直接拼接数字和字符串，所以我们必须先将数字转换字符串。可以使用`str()`函数和`repr()`将数字转换为字符串

```python
str(obj)
repr(obj)
```

str() 和 repr() 的区别:

- str() 用于将数据转换成适合人类阅读的字符串形式。
- repr() 用于将数据转换成适合解释器阅读的字符串形式（Python 表达式的形式），适合在开发和调试阶段使用；如果没有等价的语法，则会发生 SyntaxError 异常。

```

```



### 3.2 Python截取字符串

#### 获取单个字符

```
strname[index]
```

Python 允许从字符串的两端使用索引：

- 当以字符串的左端（字符串的开头）为起点时，索引是从 0 开始计数的；字符串的第一个字符的索引为 0，第二个字符的索引为 1，第三个字符串的索引为 2 ……
- 当以字符串的右端（字符串的末尾）为起点时，索引是从 -1 开始计数的；字符串的倒数第一个字符的索引为 -1，倒数第二个字符的索引为 -2，倒数第三个字符的索引为 -3 ……

```python
def func_01():
    str = 'www.python.org python官网'
    print(str.split('.'))
    print(str.split())
```



#### 获取多个字符

使用`[ ]`除了可以获取单个字符外，还可以指定一个范围来获取多个字符，也就是一个子串或者片段，具体格式为：

```
strname[start : end : step]
```

对各个部分的说明：

- strname：要截取的字符串；
- start：表示要截取的第一个字符所在的索引（截取时包含该字符）。如果不指定，默认为 0，也就是从字符串的开头截取；
- end：表示要截取的最后一个字符所在的索引（截取时不包含该字符）。如果不指定，默认为字符串的长度；
- step：指的是从 start 索引处的字符开始，每 step 个距离获取一个字符，直至 end 索引出的字符。step 默认值为 1，当省略该值时，最后一个冒号也可以省略。

```python
def func_02():
    url = 'www.laowang.com.cn'
    # 获取索引从3处22（不包含22）的子串
    print(url[7: 22])  # 输出 zy
    # 获取索引从7处到-6的子串
    print(url[7: -6])  # 输出 zyit.org is very
    # 获取索引从-7到6的子串
    print(url[-21: -6])
    # 从索引3开始，每隔4个字符取出一个字符，直到索引22为止
    print(url[3: 22: 4])

def func_03():
    url = 'www.laowang.com.cn'
    # 获取从索引5开始，直到末尾的子串
    print(url[7:])
    # 获取从索引-21开始，直到末尾的子串
    print(url[-21:])
    # 从开头截取字符串，直到索引22为止
    print(url[: 22])
    # 每隔3个字符取出一个字符
    print(url[:: 3])
```

### 3.3 Python len()函数：获取字符串长度或字节数

查看一个字符串有多少个字符，或者一个字符串占用多少个字节，可以使用`len()`函数

```
len(str)
```

python中，不同的字符所占字节数不同，数字、英文字母、小数点、下划线及空格，各占一个字节，而一个汉字可能占2~4个字节，具体占用多少，取决于采用的编码方式。例如，汉字GBK/GB2312编码中占用2个字节，而在UTF-8编码中一般占用3个字节

```python
def func_02():
    str1 = "人生苦短，我用Python"
    print(len(str1.encode('utf-8')))
    # Output: 27
    print(len(str1.encode('gbk')))
    # Output: 20
```

### 3.4 Python split()分割字符串方法

split() 方法可以实现将一个字符串按照指定的分隔符切分成多个子串，这些子串会被保存到列表中（不包含分隔符），作为方法的返回值反馈回来。该方法的基本语法格式如下：

```python
str.split(sep, maxsplit)
```

1. str：表示要进行分割的字符串；
2. sep：用于指定分隔符，可以包含多个字符。此参数默认为 None，表示所有空字符，包括空格、换行符“\n”、制表符“\t”等。
3. maxsplit：可选参数，用于指定分割的次数，最后列表中子串的个数最多为 maxsplit+1。如果不指定或者指定为 -1，则表示分割次数没有限制。

在 split 方法中，如果不指定 sep 参数，那么也不能指定 maxsplit 参数。

```
同内建函数（如 len）的使用方式不同，字符串变量所拥有的方法，只能采用“字符串.方法名()”的方式调用。这里不用纠结为什么，学完类和对象之后，自然会明白。
```

在未指定 sep 参数时，split() 方法默认采用空字符进行分割，但当字符串中有连续的空格或其他空字符时，都会被视为一个分隔符对字符串进行分割

```python

```



### 3.5 Python join()合并字符串方法

使用 join() 方法合并字符串时，它会将列表（或元组）中多个字符串采用固定的分隔符连接在一起。

此方法中各参数的含义如下：

1. newstr：表示合并后生成的新字符串；
2. str：用于指定合并时的分隔符；
3. iterable：做合并操作的源字符串数据，允许以列表、元组等形式提供。

```python
def func_01():

    list = ['www', 'python', 'org']
    newstr = '.'.join(list)
    print(newstr)
    nums = []
    for i in range(10):
        nums.append(i)
    print('-'.join(str(nums)))
```



### 3.6 Python count()统计字符串出现的次数

count 方法用于检索指定字符串在另一字符串中出现的次数，如果检索的字符串不存在，则返回 0，否则返回出现的次数。

```
str.count(sub[,start[,end]])
```

此方法中，各参数的具体含义如下：

1. str：表示原字符串；
2. sub：表示要检索的字符串；
3. start：指定检索的起始位置，也就是从什么位置开始检测。如果不指定，默认从头开始检索；
4. end：指定检索的终止位置，如果不指定，则表示一直检索到结尾。

```python
```



### 3.7 Python find()检测字符串中是否包含某子串

find() 方法用于检索字符串中是否包含目标字符串，如果包含，则返回第一次出现该字符串的索引；反之，则返回 -1。

```
str.find(sub[,start[,end]])
```

此格式中各参数的含义如下：

1. str：表示原字符串；
2. sub：表示要检索的目标字符串；
3. start：表示开始检索的起始位置。如果不指定，则默认从头开始检索；
4. end：表示结束检索的结束位置。如果不指定，则默认一直检索到结尾。

rfind() 方法，与 find() 方法最大的不同在于，rfind() 是从字符串右边开始检索。

```
def func_01():
    str = 'www.python.org'
    print(str.find('.')) # Output: 3
    print(str.find('.', 4)) # Output: 10
    print(str.rfind('.')) # Output: 10

### 3.8 Python index()检测字符串中是否包含某子串

同 find() 方法类似，index() 方法也可以用于检索是否包含指定的字符串，不同之处在于，当指定的字符串不存在时，index() 方法会抛出异常。

```
str.index(sub[,start[,end]])
```

此格式中各参数的含义分别是：

1. str：表示原字符串；
2. sub：表示要检索的子字符串；
3. start：表示检索开始的起始位置，如果不指定，默认从头开始检索；
4. end：表示检索的结束位置，如果不指定，默认一直检索到结尾。

字符串变量还具有 rindex() 方法，其作用和 index() 方法类似，不同之处在于它是从右边开始检索

​```python
def func_01():
    str = 'www.python.org'
    print(str.index('.')) # Output: 3
    print(str.index('.', 4)) # Output: 10
    print(str.rindex('.')) # Output: 10
    # print(str.index('.11’)) # Output: 10
```

### 3.9 Python ljust()、rjust()和center()方法

#### python ljust() 方法

ljust() 方法的功能是向指定字符串的右侧填充指定字符，从而达到左对齐文本的目的。

```
S.ljust(width[, fillchar])
```

- S：表示要进行填充的字符串；
- width：表示包括 S 本身长度在内，字符串要占的总长度；
- fillchar：作为可选参数，用来指定填充字符串时所用的字符，默认情况使用空格。

```
def func_01():
    S = 'http://www.python.org'
    addr = 'http://c.biancheng.net'
    print(S.ljust(35))
    print(addr.ljust(35))
```



#### python rjust() 方法



```python
def func_02():
    S = 'http://www.python.org'
    addr = 'http://c.biancheng.net'
    print(S.rjust(35))
    print(addr.rjust(35))

```



#### python center() 方法

```python
def func_03():
    S = 'http://www.python.org'
    addr = 'http://c.biancheng.net'
    print(S.center(35))
    print(addr.center(35))

```

### 3.10 Python startswith()和endswith()

#### startswith()方法

startswith() 方法用于检索字符串是否以指定字符串开头，如果是返回 True；反之返回 False。


```
tr.startswith(sub[,start[,end]])
```

此格式中各参数的含义如下：

1. str：表示原字符串；
2. sub：表示要检索的字符串；
3. start：指定检索开始时的起始位置索引（字符串第一个字符对应的索引值为 0），如果不指定，默认从头开始检索。
4. end：指定检索的结束位置索引，如果不指定，默认一直检索到结束。

```
def func_01():
    str = 'http://www.python.org'
    print(str.startswith('ht'))
    print(str.startswith('pythons'))
    print(str.startswith('w', 8))
```



#### endswith()方法

endswith() 方法用于检索字符串是否以指定字符串结尾，如果是则返回 True；反之则返回 False。

```
tr.endsswith(sub[,start[,end]])
```

```
def func_02():
    str = 'http://www.python.org'
    print(str.endswith('org'))
```



### 3.11 Python字符串大小写转换



#### title()方法

title() 方法用于将字符串中每个单词的首字母转为大写，其他字母全部转为小写，转换完成后，此方法会返回转换得到的字符串。如果字符串中没有需要被转换的字符，此方法会将字符串原封不动地返回。

#### lower() 方法

lower() 方法用于将字符串中的所有大写字母转换为小写字母，转换完成后，该方法会返回新得到的字符串。如果字符串中原本就都是小写字母，则该方法会返回原字符串。

####  upper() 方法

upper() 的功能和 lower() 方法恰好相反，它用于将字符串中的所有小写字母转换为大写字母，和以上两种方法的返回方式相同，即如果转换成功，则返回新字符串；反之，则返回原字符串。

```python
def func_01():
    str = 'http://www.python.org'
    print(str.title()) # Output: Http://Www.Python.Org
    print(str.upper()) # Output: HTTP://WWW.PYTHON.ORG
    print(str.lower()) # Output: http://www.python.org
```

### 3.12 Python去除字符串中空格

字符串变量提供了 3 种方法来删除字符串中多余的空格和特殊字符，它们分别是：

1. strip()：删除字符串前后（左右两侧）的空格或特殊字符。
2. lstrip()：删除字符串前面（左边）的空格或特殊字符。
3. rstrip()：删除字符串后面（右边）的空格或特殊字符。

```
str.strip([chars])
str.lstrip([chars])
str.rstrip([chars])
```

```
def func_01():
    str = '  www.python.org \t\n\r'
    print(str.strip())
    print(str.lstrip())
    print(str.rstrip())
```

### 3.13 Python format()格式化输出方法

字符串类型（str）提供了 format() 方法对字符串进行格式化

```
str.format(args)
```

此方法中，str 用于指定字符串的显示样式；args 用于指定要进行格式转换的项，如果有多项，之间有逗号进行分割。

 format() 方法的难点，在于搞清楚 str 显示样式的书写格式。在创建显示样式模板时，需要使用`{}`和`：`来指定占位符，其完整的语法格式为：

```
{ [index][ : [ [fill] align] [sign] [#] [width] [.precision] [type] ] }
```

注意，格式中用 [] 括起来的参数都是可选参数，即可以使用，也可以不使用。各个参数的含义如下：

- index：指定：后边设置的格式要作用到 args 中第几个数据，数据的索引值从 0 开始。如果省略此选项，则会根据 args 中数据的先后顺序自动分配。

- fill：指定空白处填充的字符。注意，当填充字符为逗号(,)且作用于整数或浮点数时，该整数（或浮点数）会以逗号分隔的形式输出，例如（1000000会输出 1,000,000）。

- align：指定数据的对齐方式，具体的对齐方式如表 1 所示。

  | align | 含义                                                         |
  | ----- | ------------------------------------------------------------ |
  | <     | 数据左对齐。                                                 |
  | >     | 数据右对齐。                                                 |
  | =     | 数据右对齐，同时将符号放置在填充内容的最左侧，该选项只对数字类型有效。 |
  | ^     | 数据居中，此选项需和 width 参数一起使用。                    |
  
- sign：指定有无符号数，此参数的值以及对应的含义如表 2 所示。

  ign参数含义+正数前加正号，负数前加负号。-正数前不加正号，负数前加负号。空格正数前加空格，负数前加负号。#对于二进制数、八进制数和十六进制数，使用此参数，各进制数前会分别显示 0b、0o、0x前缀；反之则不显示前缀。

- width：指定输出数据时所占的宽度。

- .precision：指定保留的小数位数。

- type：指定输出数据的具体类型，如表 3 所示。

  | type类型值 | 含义                                                  |
  | ---------- | ----------------------------------------------------- |
  | s          | 对字符串类型格式化。                                  |
  | d          | 十进制整数。                                          |
  | c          | 将十进制整数自动转换成对应的 Unicode 字符。           |
  | e 或者 E   | 转换成科学计数法后，再格式化输出。                    |
  | g 或 G     | 自动在 e 和 f（或 E 和 F）中切换。                    |
  | b          | 将十进制数自动转换成二进制表示，再格式化输出。        |
  | o          | 将十进制数自动转换成八进制表示，再格式化输出。        |
  | x 或者 X   | 将十进制数自动转换成十六进制表示，再格式化输出。      |
  | f 或者 F   | 转换为浮点数（默认小数点后保留 6 位），再格式化输出。 |
  | %          | 显示百分比（默认显示小数点后 6 位）。                 |

### 3.14 Python encode()和decode()方法

#### encode()方法

encode() 方法为字符串类型（str）提供的方法，用于将 str 类型转换成 bytes 类型，这个过程也称为“编码”。

```
str.encode([encoding="utf-8"][,errors="strict"])
```

| 参数               | 含义                                                         |
| ------------------ | ------------------------------------------------------------ |
| str                | 表示要进行转换的字符串。                                     |
| encoding = "utf-8" | 指定进行编码时采用的字符编码，该选项默认采用 utf-8 编码。例如，如果想使用简体中文，可以设置 gb2312。  当方法中只使用这一个参数时，可以省略前边的“encoding=”，直接写编码格式，例如 str.encode("UTF-8")。 |
| errors = "strict"  | 指定错误处理方式，其可选择值可以是：strict：遇到非法字符就抛出异常。ignore：忽略非法字符。replace：用“？”替换非法字符。xmlcharrefreplace：使用 xml 的字符引用。该参数的默认值为 strict。 |

使用 encode() 方法对原字符串进行编码，不会直接修改原字符串，如果想修改原字符串，需要重新赋值。

```python
def func_01():
    str = 'python天下第一'
    print(str.encode('gbk'))
    print(str.encode('utf-8'))
```



#### decode() 方法

和encode() 方法相反， decode() 方法用于将 bytes 类型的二进制数据转为 str 类型，这个过程称为 解码

```
bytes.decode([encoding="utf-8"][,errors="strict"])
```



| 参数              | 含义                                                         |
| ----------------- | ------------------------------------------------------------ |
| bytes             | 表示要进行转换的二进制数据。                                 |
| encoding="utf-8"  | 指定解码时采用的字符编码，默认采用 utf-8 格式。当方法中只使用这一个参数时，可以省略“encoding=”，直接写编码方式即可。  注意，对 bytes 类型数据解码，要选择和当初编码时一样的格式。 |
| errors = "strict" | 指定错误处理方式，其可选择值可以是：strict：遇到非法字符就抛出异常。ignore：忽略非法字符。replace：用“？”替换非法字符。xmlcharrefreplace：使用 xml 的字符引用。该参数的默认值为 strict。 |

```python
def func_02():
    str = 'python天下第一'
    bytes = str.encode("GBK")
    print(bytes.decode('GBK'))
    # print(bytes.decode()) 默认utf-8会抛出异常
```



### 3.15 Python dir()和help()

dir() 函数用来列出某个类或者某个模块中的全部内容，包括变量、方法、函数和类等，它的用法为：

```
dir(obj)
```

```python

def func_01():
    print(dir(str))
```





help() 函数用来查看某个函数或者模块的帮助文档，它的用法为：

```
help(obj)
```

```python
def func_02():
    help(str)
```



## 04 Python流程控制

### 4.1 Python if else条件语句

```
if 表达式 1：
    if 表示式 2：
        代码块 1
    else：
        代码块 2
```

```
if 表示式 1：
    if 表达式 2：
        代码块 1
    else：
        代码块 2
else：
    if 表达式 3：
        代码块 3
    else：
        代码块 4
```

```python
def func_01():
    proof = int(input("输入驾驶员每 100ml 血液酒精的含量："))
    if proof < 20:
        print("驾驶员不构成酒驾")
    else:
        if proof < 80:
            print("驾驶员已构成酒驾")
        else:
            print("驾驶员已构成醉驾")
```



### 4.2 Python pass assert断言

####  pass语句

Python 提供了一种更加专业的做法，就是空语句 pass。**pass** 是 Python 中的关键字，用来让解释器跳过此处，什么都不做。

```python
def func_01():
    age = int( input("请输入你的年龄：") )
    if age < 12 :
        print("婴幼儿")
    elif age >= 12 and age < 18:
        print("青少年")
    elif age >= 18 and age < 30:
        print("成年人")
    elif age >= 30 and age < 50:
        pass
    else:
        print("老年人")
```



#### assert断言函数

assert 语句，又称断言语句，可以看做是功能缩小版的 if 语句，它用于判断某个表达式的值，如果值为真，则程序可以继续往下执行；反之，Python 解释器会报 AssertionError 错误。

```
assert 表达式
```

```
if 表达式==True:
    程序继续执行
else:
    程序报 AssertionError 错误
```



```
def func_02():
    mathmark = int(input())
    # 断言数学考试分数是否位于正常范围内
    assert 0 <= mathmark <= 100
    # 只有当 mathmark 位于 [0,100]范围内，程序才会继续执行
    print("数学考试分数为：", mathmark)
```

当 assert 语句后的表达式值为真时，程序继续执行；反之，程序停止执行，并报 AssertionError 错误。

### 4.3 Python while循环语句



### 4.4 Python for循环

### 4.5 Python循环结构中else用法

### 4.6 Python循环嵌套

### 4.11 Python嵌套循环实现冒泡排序

### 4.12 Python break：跳出当前循环体

### 4.13 Python continue：直接执行下次循环

### 4.14 教你一招，彻底告别死（无限）循环！

### 4.15 Python推导式，快速初始化各种序列！

### 4.16 Python zip函数

### 4.17 Python reversed函数

### 4.18 Python sorted函数

## 05 函数和lambda表达式

### 5.1 Python函数

### 5.2 Python函数值传递和引用传递（包括形式参数和实际参数）

### 5.3 深度剖析Python函数参数传递的内部机制

### 5.4 Python位置参数

### 5.5 Python关键字参数

### 5.6 Python默认参数

### 5.7 Python函数如何传入任意个参数？

### 5.8 Python如何用序列中元素给函数传递参数？

### 5.9 Python None（空值）

### 5.10 Python return函数返回值

### 5.11 Python函数怎样返回多个值？

### 5.12 Python partial偏函数

### 5.13 从实例出发，攻克Python函数递归

### 5.14 Python变量作用域（全局变量和局部变量）

### 5.15 Python如何在函数中使用同名的全局变量？

### 5.16 Python局部函数

### 5.17 更高级的Python函数用法，玩转Python函数！

### 5.18 Python闭包函数

### 5.19 Python lambda表达式（匿名函数）

### 5.20 Python eval()和exec()函数

### 5.21 使用exec()和eval()，不要犯这样的低级错误！

### 5.22 Python函数式编程（map()、filter()和reduce()）详解

### 5.23 函数注解，号称Python3新增的最独特的功能！

### 5.24 如何才能提高代码颜值，让代码变得有逼格？

## 06 Python类和对象

### 6.1 Python面向对象

#### 6.1.1面向对象相关术语

- 类:  可以理解是一个模板，通过它可以创建出无数个具体实例。
- 对象：类并不能直接使用，通过类创建出的实例（又称对象）才能使用。
- 属性:  类中所有变量称为属性。
- 方法:  类中所有函数称为方法。 类方法至少要包含self 参数。类方法无法单独使用只能和类的对象一起使用

### 6.2 Python class：定义类

类的使用使用循序

1. 创建类
2. 创建类的实例对象

类 与 对象

- 类是抽象的
- 对象是具体的
-  对象是类中的具体的某一个

对象是类中具体的一个，类中具备的特点，对象都有
```
面向对象:
    核心: 类
创建类的语法:

class 类名():
    #属性

    # 行为,能力,动态特征,方法
    def 方法名(self,其他参数)
        pas
```

```python
class Driver:
    def drive_car(self):
        print("%d号司机为您服务" % self.id)
        print("开车")
driver = Driver()
# 手动添加属性
driver.id = 1001
driver.drive_car()
```

### 6.3 Python` __init__()`类构造方法

构造方法用于创建对象时使用，每当创建一个类的实例对象时, python解释器都会自动调用它

`__init__()` 方法可以包含多个参数，但必须包含一个名为 self 的参数，且必须作为第一个参数。也就是说，类的构造方法最少也要有一个 self 参数

```python
class Driver:
    def __init__(self, id):
        print("我是init方法")
        # 给自己加属性
        self.id = id

    def driver_car(self):
        print("工号:%d为您服务" % self.id)


driver1 = Driver(1001)
driver1.driver_car()
```

### 6.4 Python类对象的创建和使用

```
类的封装:
        属性(成员变量)
        行为(成员方法)
    语法
        class 类名():
            def __init__(self,属性...):
                self.属性 = 属性

创建对象:
    a = 类名(参数个数取决于init方法中参数的个数)
访问属性:
    a.属性名
访问方法:
    a。方法名(参数)
```

```python
```



### 6.5 Python self

在定义类的过程中，无论是显式创建类的构造方法，还是向类中添加实例方法，都要求将 self 参数作为方法的第一个参数。

```python
class Person:
    def __init__(self, name):
        print("正在执行构造方法")
        self.name = name
    # 定义一个study()实例方法
    def study(self):
        print(self,"正在学Python")
zhangsan = Person('zs')
zhangsan.study()
lisi = Person('ls')
lisi.study()

```

同一个类可以产生多个对象，当某个对象调用类方法时，该对象会把自身的引用作为第一个参数自动传给该方法，换句话说，Python 会自动绑定类方法的第一个参数指向调用该方法的对象。如此，Python解释器就能知道到底要操作哪个对象的方法了。

> 无论是类中的构造函数还是普通的类方法，实际调用它们的谁，则第一个参数 self 就代表谁。

### 6.6 Python类属性和实例属性

在类体中，根据变量定义的位置不同，以及定义的方式不同，类属性又可细分为以下 3 种类型：

1. 类体中、所有函数之外：此范围定义的变量，称为类属性或类变量；
2. 类体中，所有函数内部：以“self.变量名”的方式定义的变量，称为实例属性或实例变量；
3. 类体中，所有函数内部：以“变量名=变量值”的方式定义的变量，称为局部变量。

不仅如此，类方法也可细分为实例方法、静态方法和类方法，后续章节会做详细介绍。

#### 类变量(类属性)

类变量指的是在类中，但在各个类方法外定义的变量。

```python
class CLanguage :
    # 下面定义了2个类变量
    name = "C语言"
    add = "www.c++.com"
    # 下面定义了一个say实例方法
    def say(self, content):
        print(content)
```

变量的特点是，所有类的实例化对象都同时共享类变量，也就是说，类变量在所有实例化对象中是作为公用资源存在的。类方法的调用方式有 2 种，既可以使用类名直接调用，也可以使用类的实例化对象调用。

```python
def func_01():
    # 使用类名直接调用
    print(CLanguage.name)
    print(CLanguage.add)
    # 修改类变量的值
    CLanguage.name = "Python教程"
    CLanguage.add = "http://c.biancheng.net/python"
    print(CLanguage.name)
    print(CLanguage.add)

因为类变量为所有实例化对象共有，通过类名修改类变量的值，会影响所有的实例化对象。

```python
def func_02():
    print("修改前，各类对象中类变量的值：")
    clang1 = CLanguage()
    print(clang1.name)
    print(clang1.add)
    clang2 = CLanguage()
    print(clang2.name)
    print(clang2.add)
    print("修改后，各类对象中类变量的值：")
    CLanguage.name = "Python教程"
    CLanguage.add = "http://c.biancheng.net/python"
    print(clang1.name)
    print(clang1.add)
    print(clang2.name)
    print(clang2.add)
```

通过类对象是无法修改类变量的。通过类对象对类变量赋值，其本质将不再是修改类变量的值，而是在给该对象定义新的实例变量。

除了可以通过类名访问类变量之外，还可以动态地为类和对象添加类变量。

```
```

#### 实例变量 

在类中，name、add 以及 catalog 都是实例变量。其中，由于 __init__() 函数在创建类对象时会自动调用，而 say() 方法需要类对象手动调用。因此，CLanguage 类的类对象都会包含 name 和 add 实例变量，而只有调用了 say() 方法的类对象，才包含 catalog 实例变量。

```python
class GoLanguage:
    def __init__(self):
        self.name = "go語言中文网"
        self.add = "www.go.com"
        # 下面定义了一个say实例方法

    def say(self):
        self.catalog = 13
```

通过类对象可以访问类变量，但无法修改类变量的值。这是因为，通过类对象修改类变量的值，不是在给“类变量赋值”，而是定义新的实例变量。

```python
def func_04():
    clang = GoLanguage()
    print(clang.name)
    print(clang.add)
    # 由于 clang 对象未调用 say() 方法，因此其没有 catalog 变量，下面这行代码会报错
    # print(clang.catalog)
    clang2 = GoLanguage()
    print(clang2.name)
    print(clang2.add)
    # 只有调用 say()，才会拥有 catalog 实例变量
    clang2.say()
    print(clang2.catalog)
```

和类变量不同，通过某个对象修改实例变量的值，不会影响类的其它实例化对象，更不会影响同名的类变量。

```python
def func_05():
    clang = GoLanguage()
    # clang访问类变量
    print(clang.name)
    print(clang.add)
    clang.name = "Python教程"
    clang.add = "http://c.biancheng.net/python"
    # clang实例变量的值
    print(clang.name)
    print(clang.add)
    # 类变量的值
    print(GoLanguage().name)
    print(GoLanguage().add)
```



### 6.7 Python实例方法、静态方法和类方法

和类属性一样，类方法也可以进行更细致的划分，具体可分为类方法、实例方法和静态方法。

用 @classmethod 修饰的方法为类方法；采用 @staticmethod 修饰的方法为静态方法；不用任何修改的方法为实例方法。

> 其中 @classmethod 和 @staticmethod 都是函数装饰器，后续章节会对其做详细介绍。

#### 实例方法

实例方法最大的特点就是，它最少也要包含一个 self 参数，用于绑定调用此方法的实例对象，实例方法通常会用类对象直接调用。

Python 也支持使用类名调用实例方法，但此方式需要手动给 self 参数传值

```python
class CLanguage:
    #类构造方法，也属于实例方法
    def __init__(self):
        self.name = "C语言中文网"
        self.add = "http://c.biancheng.net"
    # 下面定义了一个say实例方法
    def say(self):
        print("正在调用 say() 实例方法")

def func_01():
    clang = CLanguage()
    clang.say()

    # 类名调用实例方法，需手动给 self 参数传值
    clang2 = CLanguage()
    CLanguage.say(clang2)
```



#### 类方法

python 类方法和实例方法相似，它最少也要包含一个参数，只不过类方法中通常将其命名为 cls，Python 会自动将类本身绑定给 cls 参数（注意，绑定的不是类对象）。也就是说，我们在调用类方法时，无需显式为 cls 参数传参。

```python
```

> 注意，如果没有 ＠classmethod，则 Python 解释器会将 fly() 方法认定为实例方法，而不是类方法。



#### 静态方法

静态方法，其实就是我们学过的函数，和函数唯一的区别是，静态方法定义在类这个空间（类命名空间）中，而函数则定义在程序所在的空间（全局命名空间）中。

静态方法没有类似 self、cls 这样的特殊参数，因此 Python 解释器不会对它包含的参数做任何类或对象的绑定。也正因为如此，类的静态方法中无法调用任何类属性和类方法。

静态方法需要使用`＠staticmethod`修饰

静态方法的调用，既可以使用类名，也可以使用类对象

```
class CLanguage:
    @staticmethod
    def info(name,add):
        print(name,add)
        
#使用类名直接调用静态方法
CLanguage.info("C语言中文网","http://c.biancheng.net")
#使用类对象调用静态方法
clang = CLanguage()
clang.info("Python教程","http://c.biancheng.net/python")
```



### 6.8 Python类调用实例方法

描述符类基于以下 3 个特殊方法，换句话说，这 3 个方法组成了描述符协议：

- __set__(self, obj, type=None)：在设置属性时将调用这一方法（本节后续用 setter 表示）；
- __get__(self, obj, value)：在读取属性时将调用这一方法（本节后续用 getter 表示）；
- __delete__(self, obj)：对属性调用 del 时将调用这一方法。

其中，实现了 setter 和 getter 方法的描述符类被称为数据描述符；反之，如果只实现了 getter 方法，则称为非数据描述符。

描述符协议中的方法都由类对象的特殊方法 __getattribute__() 调用（注意不要和 __getattr__() 弄混）。也就是说，每次使用类对象.属性（或者 getattr(类对象，属性值)）的调用方式时，都会隐式地调用 __getattribute__()，它会按照下列顺序查找该属性：

1. 验证该属性是否为类实例对象的数据描述符；
2. 如果不是，就查看该属性是否能在类实例对象的 __dict__ 中找到；
3. 最后，查看该属性是否为类实例对象的非数据描述符。

> 除了使用描述符类自定义类属性被调用时做的操作外，还可以使用 property() 函数或者 @property 装饰器

```python

```

### 6.11 Python property()

在不破坏类封装原则的基础上，为了能够有效操作类中的属性，类中应包含读（或写）类属性的多个 getter（或 setter）方法，这样就可以通过“类对象.方法(参数)”的方式操作属性。

```python
class CLanguage:
    #构造函数
    def __init__(self,name):
        self.name = name 
    #设置 name 属性值的函数 
    def setname(self,name):
        self.name = name
    #访问nema属性值的函数
    def getname(self):
        return self.name
    #删除name属性值的函数
    def delname(self):
        self.name="xxx"
clang = CLanguage("C语言中文网")
#获取name属性值
print(clang.getname())
#设置name属性值
clang.setname("Python教程")
print(clang.getname())
#删除name属性值
clang.delname()
print(clang.getname())
```

Python 中提供了 property() 函数，可以实现在不破坏类封装原则的前提下，让开发者依旧使用“类对象.属性”的方式操作类中的属性。

property() 函数的基本使用格式如下：

```python
属性名=property(fget=None, fset=None, fdel=None, doc=None)
```

fget 参数用于指定获取该属性值的类方法，fset 参数用于指定设置该属性值的方法，fdel 参数用于指定删除该属性值的方法，最后的 doc 是一个文档字符串，用于说明此函数的作用。

> 注意，在使用 property() 函数时，以上 4 个参数可以仅指定第 1 个、或者前 2 个、或者前 3 个，当前也可以全部指定。也就是说，property() 函数中参数的指定并不是完全随意的。

```python
class CLanguage:
    #构造函数
    def __init__(self,n):
        self.__name = n
    #设置 name 属性值的函数
    def setname(self,n):
        self.__name = n
    #访问nema属性值的函数
    def getname(self):
        return self.__name
    #删除name属性值的函数
    def delname(self):
        self.__name="xxx"
    #为name 属性配置 property() 函数
    name = property(getname, setname, delname, '指明出处')
#调取说明文档的 2 种方式
#print(CLanguage.name.__doc__)
help(CLanguage.name)
clang = CLanguage("C语言中文网")
#调用 getname() 方法
print(clang.name)
#调用 setname() 方法
clang.name="Python教程"
print(clang.name)
#调用 delname() 方法
del clang.name
print(clang.name)
```

注意，在此程序中，由于 getname() 方法中需要返回 name 属性，如果使用 self.name 的话，其本身又被调用 getname()，这将会先入无限死循环。为了避免这种情况的出现，程序中的 name 属性必须设置为私有属性，即使用 __name（前面有 2 个下划线）。

> 有关类属性和类方法的属性设置（分为共有属性、保护属性、私有属性）

property() 函数也可以少传入几个参数。以上面的程序为例，我们可以修改 property() 函数如下所示

```python
name = property(getname, setname)
```

这意味着，name 是一个可读写的属性，但不能删除，因为 property() 函数中并没有为 name 配置用于函数该属性的方法。也就是说，即便 CLanguage 类中设计有 delname() 函数，这种情况下也不能用来删除 name 属性。 

```
name = property(getname)    # name 属性可读，不可写，也不能删除
name = property(getname, setname,delname)    #name属性可读、可写、也可删除，就是没有说明文档
```

### 6.12 Python @property装饰器

### 6.13 Python封装

### 6.14 探究Python封装的底层实现原理

### 6.15 Python继承机制

### 6.16 在子类中，Python到底是如何找到父类的属性和方法的？（深度揭秘）

### 6.17 Python父类方法重写

### 6.18 如何使用Python继承机制提高开发效率？

### 6.19 Python super()

### 6.20 切记，super()只能在新式类中使用！

### 6.21 使用super()，这些“坑”千万别踩！

### 6.22 Python __slots__

### 6.23 Python type()动态创建类

### 6.24 Python MetaClass元类

### 6.25 Python底层是如何实现MetaClass元类的？

### 6.26 什么是多态，Python多态及用法详解

### 6.27 Python枚举类

### 6.28 [Python项目实战]利用面向对象思想实现搜索引擎

## 07 类特殊成员（属性和方法）

### 7.1 Python __new__

### 7.2 Python __repr__

### 7.3 Python __del__()

### 7.4 Python __dir__()

### 7.5 Python __dict__

### 7.6 Python setattr、getattr、hasattr

### 7.7 Python issubclass和isinstance

### 7.8 Python __call__()

### 7.9 什么是运算符重载，Python可重载运算符有哪些？

### 7.10 Python重载运算符实现自定义序列

### 7.11 Python迭代器

### 7.12 【Python项目实战】迭代器实现字符串的逆序输出

### 7.13 Python生成器

### 7.14 Python更高级的生成器用法！

### 7.15 Python @函数装饰器

### 7.16 结合实例，深入了解装饰器！

## 08 Python异常处理机制

### 8.1 什么是异常处理

### 8.2 为什么一定要学Python异常处理机制？

### 8.3 Python try except

### 8.4 深度剖析Python异常处理机制的底层实现

### 8.5 Python try except else

### 8.6 Python try except finally

### 8.7 一篇文章，带你重温整个Python异常处理机制

### 8.8 Python raise

### 8.9 Python sys.exc_info()获取异常信息

### 8.10 Python traceback模块：获取异常信息

### 8.11 Python如何自定义一个异常类？

### 8.12 正确使用Python异常处理机制

### 8.13 Python使用logging模块调试程序

### 8.14 Python IDLE调试程序

### 8.15 Python assert调试程序

## 09 Python模块和包

Python 提供了强大的模块支持，主要体现在，不仅 Python 标准库中包含了大量的模块（称为标准模块），还有大量的第三方模块，开发者自己也可以开发自定义模块。

### 9.1 python导入模块

#### import 模块名 as 别名

```python
# 导入sys整个模块
import sys
# 使用sys模块名作为前缀来访问模块中的成员
print(sys.argv())
```



#### from 模块名 import 成员名 as 别名

```python
# 导入sys模块的argv成员
from sys import argv
# 使用导入成员的语法，直接使用成员名访问
print(argv[0])
```



### 9.2 Python自定义模块





### 9.3 Python导入模块的3种方式

通常情況下，当使用 import 导入模块后，python 会按照一下顺序查找指定的模块文件

- 在当前目录，即当前执行的程序文件所在目录下查找；
- 到 PYTHONPATH（环境变量）下的每个目录中查找；
- 到 Python 默认的安装目录下查找。

解决“Python找不到指定模块”的方法有 3 种，分别是：

1. 向 sys.path 中临时添加模块文件存储位置的完整路径；
2. 将模块放在 sys.path 变量中已包含的模块加载路径中；
3. 设置 path 系统环境变量。

#### 导入模块方式一: 临时添加模块完整路径

模块文件的存储位置，可以临时添加到 sys.path 变量中

```python
import sys
sys.path.append(目录路径)
```

####  导入模块方式二: 将模块保存到指定位置

如果要安装某些通用性模块，比如复数功能支持的模块、矩阵计算支持的模块、图形界面支持的模块等，这些都属于对 Python 本身进行扩展的模块，这种模块应该直接安装在 Python 内部，以便被所有程序共享，此时就可借助于 Python 默认的模块加载路径。

Python 程序默认的模块加载路径保存在 sys.path 变量中，因此，我们可以在 say.py 程序文件中先看看 sys.path 中保存的默认加载路径，向 say.py 文件中输出 sys.path 的值



#### 导入模块方式三: 设置环境变量

### 9.7 Python导入模块的本质

### 9.8 Python __all__变量

### 9.9 Python包：存放多个模块的文件夹

### 9.10 Python创建包，导入包

### 9.11 Python __init__.py的作用

### 9.12 Python查看模块方法

### 9.13 Python `__doc__`

在使用 `dir()`函数和 `__all__`变量的基础上，能知晓指定模块或包 中所有可用的成员 (变量、函数和类)

```python
import string
print(string.__all__)
```

```
['ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'capwords', 'digits', 'hexdigits', 'octdigits', 'printable', 'punctuation', 'whitespace', 'Formatter', 'Template']
```



### 9.14 Python `__file__`

当指定模块（或包）没有说明文档时，仅通过 help() 函数或者 __doc__ 属性，无法有效帮助我们理解该模块（包）的具体功能。在这种情况下，我们可以通过 __file__ 属性查找该模块（或包）文件所在的具体存储位置

```python
import my_package
print(my_package.__file__)
```

```python
import string
print(string.__file__)
```

通过调用 __file__ 属性输出的绝对路径，可以很轻易地找到该模块（或包）的源文件

## 10 Python文件操作（I/O）

### 10.1 Python文件基本操作

绝对路径和相对路径

- 绝对路径
- 相对路径

文件的操作有很多种，常见的操作包括创建、删除、修改权限、读取、写入等，这些操作可大致分为以下 2 类：

1. 删除、修改权限：作用于文件本身，属于系统级操作。
2. 写入、读取：是文件最常用的操作，作用于文件的内容，属于应用级操作。

### 10.2 Python open

Python中，对文件的操作有很多种，常见的操作包括创建、删除、修改权限、读取、写入等

1. 删除、修改权限：作用于文件本身，属于系统级操作。
2. 写入、读取：是文件最常用的操作，作用于文件的内容，属于应用级操作。

文件的应用级操作可以分为以下 3 步，每一步都需要借助对应的函数实现：

1. 打开文件：使用 open() 函数，该函数会返回一个文件对象；
2. 对已打开文件做读/写操作：读取文件内容可使用 read()、readline() 以及 readlines() 函数；向文件中写入内容，可以使用 write() 函数。
3. 关闭文件：完成对文件的读/写操作之后，最后需要关闭文件，可以使用 close() 函数。

#### open() 函数

open() 函数用于创建或打开指定文件，该函数的常用语法格式如下：

```
file = open(file_name [, mode='r' [ , buffering=-1 [ , encoding = None ]]])
```

此格式中，用 [] 括起来的部分为可选参数，即可以使用也可以省略。其中，各个参数所代表的含义如下：

- file：表示要创建的文件对象。
- file_name：要创建或打开文件的文件名称，该名称要用引号（单引号或双引号都可以）括起来。需要注意的是，如果要打开的文件和当前执行的代码文件位于同一目录，则直接写文件名即可；否则，此参数需要指定打开文件所在的完整路径。
- mode：可选参数，用于指定文件的打开模式。可选的打开模式如表 1 所示。如果不写，则默认以只读（r）模式打开文件。
- buffering：可选参数，用于指定对文件做读写操作时，是否使用缓冲区（本节后续会详细介绍）。
- encoding：手动设定打开文件时所使用的编码格式，不同平台的 ecoding 参数值也不同，以 Windows 为例，其默认为 cp936（实际上就是 GBK 编码）。

| 模式 | 意义                                                         | 注意事项                                                     |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| r    | 只读模式打开文件，读文件内容的指针会放在文件的开头。         | 操作的文件必须存在。                                         |
| rb   | 以二进制格式、采用只读模式打开文件，读文件内容的指针位于文件的开头，一般用于非文本文件，如图片文件、音频文件等。 |                                                              |
| r+   | 打开文件后，既可以从头读取文件内容，也可以从开头向文件中写入新的内容，写入的新内容会覆盖文件中等长度的原有内容。 |                                                              |
| rb+  | 以二进制格式、采用读写模式打开文件，读写文件的指针会放在文件的开头，通常针对非文本文件（如音频文件）。 |                                                              |
| w    | 以只写模式打开文件，若该文件存在，打开时会清空文件中原有的内容。 | 若文件存在，会清空其原有内容（覆盖文件）；反之，则创建新文件。 |
| wb   | 以二进制格式、只写模式打开文件，一般用于非文本文件（如音频文件） |                                                              |
| w+   | 打开文件后，会对原有内容进行清空，并对该文件有读写权限。     |                                                              |
| wb+  | 以二进制格式、读写模式打开文件，一般用于非文本文件           |                                                              |
| a    | 以追加模式打开一个文件，对文件只有写入权限，如果文件已经存在，文件指针将放在文件的末尾（即新写入内容会位于已有内容之后）；反之，则会创建新文件。 |                                                              |
| ab   | 以二进制格式打开文件，并采用追加模式，对文件只有写权限。如果该文件已存在，文件指针位于文件末尾（新写入文件会位于已有内容之后）；反之，则创建新文件。 |                                                              |
| a+   | 以读写模式打开文件；如果文件存在，文件指针放在文件的末尾（新写入文件会位于已有内容之后）；反之，则创建新文件。 |                                                              |
| ab+  | 以二进制模式打开文件，并采用追加模式，对文件具有读写权限，如果文件存在，则文件指针位于文件的末尾（新写入文件会位于已有内容之后）；反之，则创建新文件。 |                                                              |

```python
```

#### open()是否需要缓冲区

通常情况下、建议大家在使用 open() 函数时打开缓冲区，即不需要修改 buffing 参数的值。

> 如果 buffing 参数的值为 0（或者 False），则表示在打开指定文件时不使用缓冲区；如果 buffing 参数值为大于 1 的整数，该整数用于指定缓冲区的大小（单位是字节）；如果 buffing 参数的值为负数，则代表使用默认的缓冲区大小。

如果使用缓冲区，则程序在执行输出操作时，会先将所有数据都输出到缓冲区中，然后继续执行其它操作，缓冲区中的数据会有外设自行读取处理；同样，当程序执行输入操作时，会先等外设将数据读入缓冲区中，无需同外设做同步读写操作。

####  open()文件对象常用的属性

- file.name：返回文件的名称；
- file.mode：返回打开文件时，采用的文件打开模式；
- file.encoding：返回打开文件时使用的编码格式；
- file.closed：判断文件是否己经关闭。

```python
def func_02():
    # 以默认方式打开文件
    f = open('a.txt')
    # 输出文件是否已经关闭
    print(f.closed)
    # 输出访问模式
    print(f.mode)
    # 输出编码格式
    print(f.encoding)
    # 输出文件名
    print(f.name)
```

### 10.3 Python read、readline()和readlines()

python提供了如下 3 种函数，它们都可以帮我们实现读取文件中数据的操作：

1. read() 函数：逐个字节或者字符读取文件中的内容；
2. readline() 函数：逐行读取文件中的内容；
3. readlines() 函数：一次性读取文件中多行内容。

```
file.read([size])
file.readline([size])
file.readlines()
```

- 对于借助 open() 函数，并以可读模式（包括 r、r+、rb、rb+）打开的文件，可以调用 read() 函数逐个字节（或者逐个字符）读取文件中的内容。
- 由于 readline() 函数在读取文件中一行的内容时，会读取最后的换行符“\n”，再加上 print() 函数输出内容时默认会换行，所以输出结果中会看到多出了一个空行。
- readlines() 函数用于读取文件中的所有行，和 readline() 函数一样，readlines() 函数在读取每一行时，会连同行尾的换行符一块读取。

file 表示已打开的文件对象；size 作为一个可选参数，用于指定一次最多可读取的字符（字节）个数，如果省略，则默认一次性读取所有内容。

```python
def func_01():
    # 以 utf-8 的编码格式打开指定文件
    f = open("a.txt", encoding="utf-8")
    # 输出读取到的数据
    print(f.read())
    # 关闭文件
    f.close()

def func_02():
    f = open("my_file.txt")
    # 读取一行数据
    byt = f.readline()
    print(byt)

    # 以二进制形式打开指定文件
    f = open("my_file.txt", 'rb')
    byt = f.readline(6)
    print(byt)

def func_03():
    f = open("my_file.txt", 'rb')
    byt = f.readlines()
    print(byt)
```





### 10.4 Python write和writelines

python中的文件对象提供了 write() 函数，可以向文件中写入指定内容。

```
file.write(string)
```

file 表示已经打开的文件对象；string 表示要写入文件的字符串（或字节串，仅适用写入二进制文件中）。

在使用 write() 向文件中写入数据，需保证使用 open() 函数是以 r+、w、w+、a 或 a+ 的模式打开文件，否则执行 write() 函数会抛出 io.UnsupportedOperation 错误。

Python 的文件对象中，不仅提供了 write() 函数，还提供了 writelines() 函数，可以实现将字符串列表写入文件中。

通过设置 open() 函数的 buffering 参数可以关闭缓冲区，这样数据不就可以直接写入文件中了？对于以二进制格式打开的文件，可以不使用缓冲区，写入的数据会直接进入磁盘文件；但对于以文本格式打开的文件，必须使用缓冲区，否则 Python 解释器会 ValueError 错误。

### 10.5 Python close()和flush()
close() 函数是专门用来关闭已打开文件的

可能需要在将数据成功写入到文件中，但并不想关闭文件。这也是可以实现的，调用 flush() 函数即可

### 10.6 Python seek()和tell()

当向文件中写入数据时，如果不是文件的尾部，写入位置的原有数据不会自行向后移动，新写入的数据会将文件中处于该位置的数据直接覆盖掉。

实现对文件指针的移动，文件对象提供了 tell() 函数和 seek() 函数。tell() 函数用于判断文件指针当前所处的位置，而 seek() 函数用于移动文件指针到文件的指定位置。

#### tell()

```
file.tell()
```

其中，file 表示文件对象。

```python
def func_01():
    f = open("a.txt", 'r')
    print(f.tell())
    print(f.read(3))
    print(f.tell())
```

使用 open() 函数打开文件时，文件指针的起始位置为 0，表示位于文件的开头处，当使用 read() 函数从文件中读取 3 个字符之后，文件指针同时向后移动了 3 个字符的位置。这就表明，当程序使用文件对象读写数据时，文件指针会自动向后移动：读写了多少个数据，文件指针就自动向后移动多少个位置。

seek()

seek() 函数用于将文件指针移动至指定位置

```
file.seek(offset[, whence])
```

- file：表示文件对象；
- whence：作为可选参数，用于指定文件指针要放置的位置，该参数的参数值有 3 个选择：0 代表文件头（默认值）、1 代表当前位置、2 代表文件尾。
- offset：表示相对于 whence 位置文件指针的偏移量，正数表示向后偏移，负数表示向前偏移。例如，当`whence == 0 &&offset == 3`（即 seek(3,0) ），表示文件指针移动至距离文件开头处 3 个字符的位置；当`whence == 1 &&offset == 5`（即 seek(5,1) ），表示文件指针向后移动，移动至距离当前位置 5 个字符处。

```python
def func_02():
    f = open('a.txt', 'rb')
    # 判断文件指针的位置
    print(f.tell())
    # 读取一个字节，文件指针自动后移1个数据
    print(f.read(1))
    print(f.tell())
    # 将文件指针从文件开头，向后移动到 5 个字符的位置
    f.seek(5)
    print(f.tell())
    print(f.read(1))
    # 将文件指针从当前位置，向后移动到 5 个字符的位置
    f.seek(5, 1)
    print(f.tell())
    print(f.read(1))
    # 将文件指针从文件结尾，向前移动到距离 2 个字符的位置
    f.seek(-1, 2)
    print(f.tell())
    print(f.read(1))
```



### 10.7 Python with as

使用 with as 操作已经打开的文件对象（本身就是上下文管理器），无论期间是否抛出异常，都能保证 with as 语句执行完毕后自动关闭已经打开的文件。

```
with 表达式 [as target]：
    代码块
```

此格式中，用 [] 括起来的部分可以使用，也可以省略。其中，target 参数用于指定一个变量，该语句会将 expression 指定的结果保存到该变量中。with as 语句中的代码块如果不想执行任何语句，可以直接使用 pass 语句代替。

### 10.13 Python pickle模块

pickle 模块提供了以下 4 个函数供我们使用：

1. dumps()：将 Python 中的对象序列化成二进制对象，并返回；
2. loads()：读取给定的二进制对象数据，并将其转换为 Python 对象；
3. dump()：将 Python 中的对象序列化成二进制对象，并写入文件；
4. load()：读取指定的序列化数据文件，并返回对象。

以上这 4 个函数可以分成两类，其中 dumps 和 loads 实现基于内存的 Python 对象与二进制互转；dump 和 load 实现基于文件的 Python 对象与二进制互转。

#### pickle.dumps()函数

此函数用于将 Python 对象转为二进制对象

```
dumps(obj, protocol=None, *, fix_imports=True)
```

此格式中各个参数的含义为：

- obj：要转换的 Python 对象；
- protocol：pickle 的转码协议，取值为 0、1、2、3、4，其中 0、1、2 对应 Python 早期的版本，3 和 4 则对应 Python 3.x 版本及之后的版本。未指定情况下，默认为 3。
- 其它参数：为了兼容 Python 2.x 版本而保留的参数，Python 3.x 中可以忽略。



#### pickle.loads()函数



#### pickle.load()函数





#### pickle.load()函数



### 10.14 Python fileinput模块：逐行读取多个文件

fileinput 模块，通过该模块中的 input() 函数，我们能同时打开指定的多个文件，还可以逐个读取这些文件中的内容。

```
fileinput.input（files="filename1, filename2, ...", inplace=False, backup='', bufsize=0, mode='r', openhook=None）
```

此函数会返回一个 FileInput 对象，它可以理解为是将多个指定文件合并之后的文件对象。其中，各个参数的含义如下：

- files：多个文件的路径列表；
- inplace：用于指定是否将标准输出的结果写回到文件，此参数默认值为 False；
- backup：用于指定备份文件的扩展名；
- bufsize：指定缓冲区的大小，默认为 0；
- mode：打开文件的格式，默认为 r（只读格式）；
- openhook：控制文件的打开方式，例如编码格式等。

> 注意，和 open() 函数不同，input() 函数不能指定打开文件的编码格式，这意味着使用该函数读取的所有文件，除非以二进制方式进行读取，否则该文件编码格式都必须和当前操作系统默认的编码格式相同，不然 Python 解释器可能会提示 UnicodeDecodeError 错误。

和 open() 函数返回单个的文件对象不同，fileinput 对象无需调用类似 read()、readline()、readlines() 这样的函数，直接通过 for 循环即可按次序读取多个文件中的数据。

| 函数名                  | 功能描述                                        |
| ----------------------- | ----------------------------------------------- |
| fileinput.filename()    | 返回当前正在读取的文件名称。                    |
| fileinput.fileno()      | 返回当前正在读取文件的文件描述符。              |
| fileinput.lineno()      | 返回当前读取了多少行。                          |
| fileinput.filelineno()  | 返回当前正在读取的内容位于当前文件中的行号。    |
| fileinput.isfirstline() | 判断当前读取的内容在当前文件中是否位于第 1 行。 |
| fileinput.nextfile()    | 关闭当前正在读取的文件，并开始读取下一个文件。  |
| fileinput.close()       | 关闭 FileInput 对象。                           |

> 文件描述符是一个文件的代号，其值为一个整数。后续章节将会介绍关于文件描述符的操作。

### 10.15 Python linecache模块用法：随机读取文件指定行

linecache 模块常用来读取 Python 源文件中的代码，它使用的是 UTF-8 编码格式来读取文件内容。这意味着，使用该模块读取的文件，其编码格式也必须为 UTF-8，否则要么读取出来的数据是乱码，要么直接读取失败（Python 解释器会报 SyntaxError 异常）。

| 函数基本格式                                             | 功能                                                         |
| -------------------------------------------------------- | ------------------------------------------------------------ |
| linecache.getline(filename, lineno, module_globals=None) | 读取指定模块中指定文件的指定行（仅读取指定文件时，无需指定模块）。其中，filename 参数用来指定文件名，lineno 用来指定行号，module_globals 参数用来指定要读取的具体模块名。注意，当指定文件以相对路径的方式传给 filename 参数时，该函数以按照 sys.path 规定的路径查找该文件。 |
| linecache.clearcache()                                   | 如果程序某处，不再需要之前使用 getline() 函数读取的数据，则可以使用该函数清空缓存。 |
| linecache.checkcache(filename=None)                      | 检查缓存的有效性，即如果使用 getline() 函数读取的数据，其实在本地已经被修改，而我们需要的是新的数据，此时就可以使用该函数检查缓存的是否为新的数据。注意，如果省略文件名，该函数将检车所有缓存数据的有效性。 |

### 10.16 Python pathlib模块

### 10.17 Python os.path模块

| 方法                                | 说明                                                         |
| ----------------------------------- | ------------------------------------------------------------ |
| os.path.abspath(path)               | 返回 path 的绝对路径。                                       |
| os.path.basename(path)              | 获取 path 路径的基本名称，即 path 末尾到最后一个斜杠的位置之间的字符串。 |
| os.path.commonprefix(list)          | 返回 list（多个路径）中，所有 path 共有的最长的路径。        |
| os.path.dirname(path)               | 返回 path 路径中的目录部分。                                 |
| os.path.exists(path)                | 判断 path 对应的文件是否存在，如果存在，返回 True；反之，返回 False。和 lexists() 的区别在于，exists()会自动判断失效的文件链接（类似 Windows 系统中文件的快捷方式），而 lexists() 却不会。 |
| os.path.lexists(path)               | 判断路径是否存在，如果存在，则返回 True；反之，返回 False。  |
| os.path.expanduser(path)            | 把 path 中包含的 "~" 和 "~user" 转换成用户目录。             |
| os.path.expandvars(path)            | 根据环境变量的值替换 path 中包含的 "$name" 和 "${name}"。    |
| os.path.getatime(path)              | 返回 path 所指文件的最近访问时间（浮点型秒数）。             |
| os.path.getmtime(path)              | 返回文件的最近修改时间（单位为秒）。                         |
| os.path.getctime(path)              | 返回文件的创建时间（单位为秒，自 1970 年 1 月 1 日起（又称 Unix 时间））。 |
| os.path.getsize(path)               | 返回文件大小，如果文件不存在就返回错误。                     |
| pip install jupyter-echarts-pypkg   | 判断是否为绝对路径。                                         |
| os.path.isfile(path)                | 判断路径是否为文件。                                         |
| os.path.isdir(path)                 | 判断路径是否为目录。                                         |
| os.path.islink(path)                | 判断路径是否为链接文件（类似 Windows 系统中的快捷方式）。    |
| os.path.ismount(path)               | 判断路径是否为挂载点。                                       |
| os.path.join(path1[, path2[, ...]]) | 把目录和文件名合成一个路径。                                 |
| os.path.normcase(path)              | 转换 path 的大小写和斜杠。                                   |
| os.path.normpath(path)              | 规范 path 字符串形式。                                       |
| os.path.realpath(path)              | 返回 path 的真实路径。                                       |
| os.path.relpath(path[, start])      | 从 start 开始计算相对路径。                                  |
| os.path.samefile(path1, path2)      | 判断目录或文件是否相同。                                     |
| os.path.sameopenfile(fp1, fp2)      | 判断 fp1 和 fp2 是否指向同一文件。                           |
| os.path.samestat(stat1, stat2)      | 判断 stat1 和 stat2 是否指向同一个文件。                     |
| os.path.split(path)                 | 把路径分割成 dirname 和 basename，返回一个元组。             |
| os.path.splitdrive(path)            | 一般用在 windows 下，返回驱动器名和路径组成的元组。          |
| os.path.splitext(path)              | 分割路径，返回路径名和文件扩展名的元组。                     |
| os.path.splitunc(path)              | 把路径分割为加载点与文件。                                   |
| os.path.walk(path, visit, arg)      | 遍历path，进入每个目录都调用 visit 函数，visit 函数必须有 3 个参数(arg, dirname, names)，dirname 表示当前目录的目录名，names 代表当前目录下的所有文件名，args 则为 walk 的第三个参数。 |
| os.path.supports_unicode_filenames  | 设置是否可以将任意 Unicode 字符串用作文件名。                |

```python
def func_01():
    # 获取绝对路径
    print(path.abspath("my_file.txt"))
    # 获取共同前缀
    print(path.commonprefix(['C://my_file.txt', 'C://a.txt']))
    # 获取共同路径
    print(path.commonpath(['http://www.python.org/python/', 'http://www.python.org/shell/']))
    # 获取目录
    print(path.dirname('C://my_file.txt'))
    # 判断指定目录是否存在
    print(path.exists('my_file.txt'))
```



### 10.18 Python fnmatch模块

fnmatch 模块主要用于文件名称的匹配，其能力比简单的字符串匹配更强大，但比使用正则表达式相比稍弱。。如果在数据处理操作中，只需要使用简单的通配符就能完成文件名的匹配，则使用 fnmatch 模块是不错的选择。

| 函数名                                 | 功能                                                         |
| -------------------------------------- | ------------------------------------------------------------ |
| fnmatch.filter(names, pattern)         | 对 names 列表进行过滤，返回 names 列表中匹配 pattern 的文件名组成的子集合。 |
| fnmatch.fnmatch(filename, pattern)     | 判断 filename 文件名，是否和指定 pattern 字符串匹配          |
| fnmatch.fnmatchcase(filename, pattern) | 和 fnmatch() 函数功能大致相同，只是该函数区分大小写。        |
| fnmatch.translate(pattern)             | 将一个 UNIX shell 风格的 pattern 字符串，转换为正则表达式    |

### 10.20 Python tempfile模块：生成临时文件和临时目录

tempfile 模块专门用于创建临时文件和临时目录

| tempfile 模块函数                                            | 功能描述                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| tempfile.TemporaryFile(mode='w+b', buffering=None, encoding=None, newline=None, suffix=None, prefix=None, dir=None) | 创建临时文件。该函数返回一个类文件对象，也就是支持文件 I/O。 |
| tempfile.NamedTemporaryFile(mode='w+b', buffering=None, encoding=None, newline=None, suffix=None, prefix=None, dir=None, delete=True) | 创建临时文件。该函数的功能与上一个函数的功能大致相同，只是它生成的临时文件在文件系统中有文件名。 |
| tempfile.SpooledTemporaryFile(max_size=0, mode='w+b', buffering=None, encoding=None, newline=None, suffix=None, prefix=None, dir=None) | 创建临时文件。与 TemporaryFile 函数相比，当程序向该临时文件输出数据时，会先输出到内存中，直到超过 max_size 才会真正输出到物理磁盘中。 |
| tempfile.TemporaryDirectory(suffix=None, prefix=None, dir=None) | 生成临时目录。                                               |
| tempfile.gettempdir()                                        | 获取系统的临时目录。                                         |
| tempfile.gettempdirb()                                       | 与 gettempdir() 相同，只是该函数返回字节串。                 |
| tempfile.gettempprefix()                                     | 返回用于生成临时文件的前缀名。                               |
| tempfile.gettempprefixb()                                    | 与 gettempprefix() 相同，只是该函数返回字节串。              |

tempfile 模块还提供了 tempfile.mkstemp() 和 tempfile.mkdtemp() 两个低级别的函数。上面介绍的 4 个用于创建临时文件和临时目录的函数都是高级别的函数，高级别的函数支持自动清理，而且可以与 with 语句一起使用，而这两个低级别的函数则不支持，因此一般推荐使用高级别的函数来创建临时文件和临时目录。

此外，tempfile 模块还提供了 tempfile.tempdir 属性，通过对该属性赋值可以改变系统的临时目录

​```python
```



上面程序以两种方式来创建临时文件：

1. 第一种方式是手动创建临时文件，读写临时文件后需要主动关闭它，当程序关闭该临时文件时，该文件会被自动删除。
2. 第二种方式则是使用 with 语句创建临时文件，这样 with 语句会自动关闭临时文件。

