# python中常用数据结构，list列表[]，和元组tuple()的性质类似，
# 不过列表是动态创建，元组是静态创建，需要提前预分配内存

# 1. 用循环函数快速创建列表,在python中列表名可以理解为指针，指示的内存单元由其id决定
from numpy import *

nlist1 = [x**2 + y for x in range(1, 9, 2) if x != 5 for y in range(1, 6)]  # 按照函数约束创建一个3*5的矩阵
print(nlist1)  # 先生成相应的一维数组
nlist2 = reshape(nlist1, (3, 5))  # 利用reshape函数将数组转化成矩阵形式
print(nlist2)  # 另外有一种shape函数直接对原有列表处理

nlist3 = [[0]*4]*5  # 生成一个4*5的零矩阵列表
print('The zeros list:', nlist3)
nlist4 = [[x + y for x in range(1, 5)] for y in range(1, 4)]  # 直接利用列表构建一个4*3的矩阵
print(nlist4)

# 2. 介绍列表函数，python中的内存管理属于垃圾回收机制
namelist = ['Amy', 'Bob', 'Caser', 49, 'Ella']
print('The origin list:', namelist, ',The id:', id(namelist))
namelist.append(['Hector', 'Jack'])  # append函数在列表末尾增加变量的整体
print('The list after append:', namelist)
namelistcy = namelist.copy()
print('The copy list:', namelistcy, 'The id:', id(namelistcy))  # 同样是复制数组内容，copy函数是重新分配内存复制列表
namelist2 = namelist  # 赋值语句则是将列表的id赋值给另外一个变量，可以理解为指针赋值，没有申请空间
print('The list after "=":', namelist2, 'The id:', id(namelist2))
namelistcy.extend(['Hector', 'Jack'])  # extend 将变量中的元素依次加入列表中
print('The copy list after extend:', namelistcy)
print('The "Hector" in the copy list:', namelistcy.count('Hector'))  # 计数函数
namelist.remove('Caser')  # remove函数参数是列表中的变量
namelist.pop()  # pop函数参数相当于堆栈中的第几个位置，默认为1即列表中的最后一个元素
namelist.pop(2)
print('The list after pop and remove:', namelist)
namelistcy.clear()  # 等效于 del list[:]
print('The copy list after clear:', namelistcy)
namelist.insert(0, 'Peter')  # insert函数在列表中相应索引处添加元素
print('The list after insert:', namelist)
namelist.reverse()
print('The list after inverse:', namelist)

numlist = [-3, -7.5, 10, 4, 5]
numlist.sort(key=abs, reverse=True)  # sort函数按照key指代的函数排序，reverse代表非递增，缺省值为非递减
print('The numlist after sort:', numlist)  # sort处理后相应的列表会发生变化，而sorted函数不会对原有列表发生变化

# 3. range(x,y,z)类似于x:y:z:表示[x,y)的整数范围内，以z步长取数,都必须是int变量
numlist3 = [x for x in range(0, 13, 2)]
print('The list using range:', numlist3)
print('numlist[1::3]', numlist3[1::3])  # 下标从1到end，python内的索引1表示第二个元素
print('numlist[-1:-7:-2]', numlist3[-1:-7:-2])
