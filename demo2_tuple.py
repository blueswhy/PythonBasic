# 介绍元组概念
# 元组属于只读序列，用()或者tuple表示。元组中的数据创建之后只能观看而无法改变
# 非只读类型的数据类型有：列表、字典。
# 变量用等号赋值时理解为两步：系统随机分配内存给定右值，返回该值的id，将该id给左边的变量
# 删除变量的时候相当于将变量的id清除，但是相应内存单元的值是随着垃圾回收机制自行清除的


exp1 = 'python tuple'
str_tuple = tuple(exp1)
print(str_tuple, str_tuple.count('t'))
# 元组相加，等于两个元组的合并
str2_tuple = (tuple('Amy'), tuple('Peter'))
strplus_tuple = str_tuple + str2_tuple
print(strplus_tuple, type(strplus_tuple))
print(id(strplus_tuple[1]), id(str_tuple[1]))  # 比较相加之后相应的数据的id是否相同：True
print(id(strplus_tuple[strplus_tuple.index('e') + 1]), id(str2_tuple[0]))
# 元组的遍历
for str_member in str_tuple:
    print(str_member, end=',')
print()
