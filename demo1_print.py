# -*-coding:utf-8 -*-
# import io
# import sys
# #改变标准输出的默认编码
# sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
# print func: 标准输出函数，输出默认补换行符\n

# print("Hello world!")
# 输出格式说明
# % 转义符
# %s, %r, %c : 以str(),repr()格式输出字符串,字符变量
# %b,%o,%d%i,%x: 依次代表以2,8,10,16进制输出整数%d和%i表示的都是十进制整数
# %e,%E: 科学计数法则，大小写表示基底分别用不同的大小写e来表示
# %f,%F: 浮点数输出，默认小数6位
# %g,%G: 系统根据变量大小自动输出两种格式，科学计数或者浮点数输出
# %%: 输出%号的方法，类似于输出\转义符的方法
# %04.d: 0表示在规定字符长度为4的情况下，向左边用0作为空余位，默认为空格，一般用于日期调整和进制补零
import math

mypi = math.pi
print('圆周率=%.6f' % mypi)

# print: 用end函数来调整print函数的默认换行处理
for n in range(0, 9):
    print("%02d" % n, end=',')
print()

# 浮点数在python中的存储说明
fnum = 0.14
if fnum * 100 == 14:
    print('0.14 * 100 =14')
else:
    print('0.14 * 100 <> 14')
print('In python: 0.14 * 100 = ', fnum * 100)

# type()函数显示变量的数据类型

print('the datatype of fnum in python:', type(fnum))

# python 中非零即真，因此用判断条件最好用bool变量
# 和C不同python中书写省略了函数代表域的{}，用格式中的空格代替，
# 因此，在书写python时要把握好格式中的空格避免缩进错误。
