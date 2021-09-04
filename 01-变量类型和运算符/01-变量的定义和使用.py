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
