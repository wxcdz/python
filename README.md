# python

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