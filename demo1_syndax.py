# 1. 算数运算符和逻辑运算符
# 运算符的优先级类比于C，为了增强可读性，在一些有歧义的地方加上()更好
# +，-，*，/:  和C相同表示为加减乘除，除法得到浮点数
# **:          ^表示为幂运算，也可以使用pow()函数
# //:          整除运算，是向下取整
# % :          模运算，可以理解为取余
import math
print('算数运算')
print('11 / 3 = %.4f' % (11 / 3))
print('11 // 3 = ', 11 // 3)
print('11 + 3 * 3^2 =', 11 + 3 * 3 ** 2)

# and,or,not : 依次表示与或非逻辑运算
# python中逻辑运算均返回bool变量，在print中也显示True或者False

print('逻辑运算')
n1 = 11
print('11 > 3 : ', n1 > 3)
print('11 > 3 and 11 <= 11 : ', 3 < n1 <= 11)
print('11 > 100 or 11 <= 11 : ', n1 > 100 or n1 <= 11)
print('not 11 > 100 : ', not n1 > 100)

# 2. 函数
# 简单的计算函数引入math模块
# pow(),round(),abs() :  幂函数，四舍五入，取绝对值
# floor(),ceil()      :  分别表示向下取整和向上取整
# sqrt()              :  平方根
# exp(),log()         :  指数函数，对数运算-其中对数的底可以改变，默认为e,不过这两个函数需要引用外部模块math

a1 = math.exp(3)
a2 = math.log(a1)
a3 = math.log(a1, 10)

print('a1 = ', a1)
print('In(e^3) = ', a2)
print('lg(e^3) = ', a3)
print('10^(lg(e^3)) = ', pow(10, a3))

# 时间函数
# time.time()   : 取系统时间秒数，指的是1970年到目前的总秒数，可以用这个函数计算程序段执行的时间
# datetime.datetime.now():  取系统时间，返回值是一个存储时间的Struct变量
import time
import datetime

t1 = time.time()
t2 = datetime.datetime.now()

print('All the Secs from 1970-00-00 00:00:00 to now : ', t1, 's')
print('CurSecond : %d s' % (t1 % 60))
print('CurDay: %d-%02d-%02d' % (t2.year, t2.month, t2.day), \
      'CurTime: %d:%02d:%02d' % (t2.hour, t2.minute, t2.second))  # 当一行代码太长影响观看时，可以使用\分行书写


# 自定义函数def
def myPytho(a1, a2 = 5):  # a2 = 5表示a2的默认值为5
    return a1 ** 2 + a2 * a2


print('7^2 + 24^2 = ', myPytho(7, 24))

# 调用外部模块函数时，使用更简单的方法
from turtle import Pen

tPen = Pen()
iCircleCount = 10
for i in range(iCircleCount):
    tPen.circle(100)  # 指示画圆的半径
    tPen.right(360 / iCircleCount)  # 每完成一个圆后所偏移的角度

# 输入函数input(),[]不同于数组，类似于cell概念，拥有stack的性质
list_Month = ['January', 'February', 'March', 'April', 'May', 'June', \
              'July', 'August', 'September', 'October', 'November', 'December']
imonth = input('Which month do you want to know?')
iMonth = int(imonth)
if 0 < iMonth < 13:
    print('The %sth month you want to know:' % imonth, list_Month[iMonth - 1])
else:
    print('error: The number is not in the limit')

# 3. 条件语句和循环语句
# 条件语句中用if else较多，可以带pass语句来占位，其中elif=else if,python 中没有switch-case语句，可以借助字典实现
# 循环语句 for x in range() 或者 while  loop(循环体中要有和while条件对应变量的控制，防止出现死循环)
# 循环语句中中断循环语句有break，continue以及pass(跳出循环，结束当前循环，占位语句)
for x in 'python':
    if x == 't' or x == 'h':
        continue
    else:
        print(x, end=',')
print()
x = 1
while x <= 10:
    print(x, end=',')
    x += 2
print()
# 循环解包,结合zip函数,zip函数不单独在内存中产生数据，而是一种对应关系
namelist1 = ['Amy', 'Bob', 'Caser', 'Ella']
salarylist1 = [1000, 2000, 2300, 1200]
for name1, salary1 in zip(namelist1, salarylist1):
    print(name1, "'s salary is ", salary1, 'per week')
# 4. python中变量保存的是对象的引用, 称作引用语义(对象语义、指针语义), 不需要提前向系统申请空间,
#    和C语言固定存储方式相比, 使用更灵活, 但也更复杂和抽象.
#    python中每个变量存储该变量的地址(id), 而不是值本身. 特定的数据结构也是这样.
#    因此对于一个变量的重复初始化实际上是先在内存中开辟空间存入内容, 再将该内容的地址赋值给变量.
#    内存管理使用垃圾回收机制.
#    以列表变量为例, 当对列表元素进行增删改操作时, 不同影响到list1自身的列表地址的, 只会改变其
#    内部变量的地址引用. 当对于list1进行重新初始化时, 相当于给list1重新指定了一个地址, 至于其
#    内部元素的地址改不改变, 需要看系统的判断.
#    了解以上原理后, 就可以弄懂深拷贝deepcopy()和浅拷贝copy()的概念了.
#    对于一个嵌套列表而言, copy()只会复制所有元素的第一层地址, 即内嵌列表中指向的内嵌元素的地址不
#    会被复制, 因此该情况下, 当内嵌列表发生改变时, 原列表和被复制列表都会发生改变.
#    deepcopy()则会在内存中重新开辟空间, 只要遇到可能发生改变的数据类型, 就重新开辟内存空间将这些
#    对象的地址复制下来, 直到不再有复杂的数据类型(即内存空间), 从而保持原引用.此时,当原列表中的任何
#    元素发生变化时, 复制列表都会保持原样, 作为一个拷贝存在.