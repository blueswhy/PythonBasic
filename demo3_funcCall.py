# 对于python自带的模块和函数, 查看其详细功能可借助python的离线doc
# Pycharm查看方法: 鼠标光标移动到待查看对象 -> 点看view找到external Documentation
# 1. 函数的调用
from demo3_myfunc import func_splitN

N = 21
print('The function\'s document:', func_splitN.__doc__)
func_splitN(N)

from demo3_myfunc import func_factorial

m = 6
print('The function\'s document:', func_factorial.__doc__)
print('{0}! = {1}'.format(m, str(func_factorial(m))))  # 注意format函数的用法，是对一个字符串进行函数调用
# 2. 传递带有*和**的形参

musicList = ('Kiss the Rain', 'Canon', 'Castle in the Sky')
title = 'The unforgettable piano music list'
from demo3_myfunc import func_MultiParaPrint

func_MultiParaPrint(title, *musicList)  # 这里的*A表示将序列拆解成相应的若干个变量
func_MultiParaPrint(title, musicList)

from demo3_myfunc import func_DictPrint

key_list = 'name', 'sno', 'gender', 'age'
value_list = 'David', '10002', 'male', 21
david = dict(zip(key_list, value_list))
func_DictPrint('David\'s baisc information', **david)  # **A传递参数表示把字典拆分为若干个键值对

# 3. 用递归实现正整数N的分解
from func_decomposedN import func_decomposeN, func_decomposeNListPrint

n1 = 5
decomposedNlist = func_decomposeN(n1, 0)
func_decomposeNListPrint(decomposedNlist)
