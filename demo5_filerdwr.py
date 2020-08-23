# 文件的读写
# f = open('path', mode)
# mode: x,独占写模式，在写该文件的时候不允许其余进程调用该文件
#       w,r: write和read模式
#       a,append模式
#       b,二进制模式，配合其余主模式使用
#       t,文本模式默认
#       +，读写模式，配合r,w,a使用
#       缺省值为‘rt'

#  1. 文件的读写
#  readline函数自动从文件中读取一行的文件，如果有参数则读取其中前k个字符
#  readlines()函数将文件中所有行文本都读出来返回成为一个字符串序列
#  读到一行处后自动加换行符执行换行，文件中的句柄还是逐行逐字符的读下去
import os

# 利用os。sep系统自动填写路径间隔符号\
writepath = 'TestDoc' + os.sep + 'Bob.txt'

f = open('SomeoneLikeYou.txt', 'r')
lineNum = 3
for k in range(0, lineNum):
    print(f.readline())
f.close()

# 读写操作时可以利用with as 语句自动实现文件的关闭
with open('SomeoneLikeyou.txt', 'r') as f:
    for k in range(0, 3):
        print(f.readline(k + 10))

#  在一个文件中，如果没有位置指定，写模式自动从文件开头写入覆盖原有内容
with open(writepath, 'w') as f:
    f.write('Bob is a student aged 19\n')
    f.write('Bob is going to travel to W\n')

# 如果希望从文件的末尾写入需要使用文件的append 模式
txt_append = 0
if txt_append == 1:
    with open('SomeoneLikeYou.txt', 'a') as f:
        f.write('PS: It is the end of the song\n')
# 2. Random Access--简单的文件函数实现随机存取

#  随机存取主要利用seek函数来指定文件指针位置
#  seek函数中第一个参数是相对当前文件指针的位移offset
#  另外一个指定偏移方向和位置whence
#  在io中, io.SEEK_SET,指向文件开头处,代号为0
#         io.SEEK_END,指向文件末尾处,代号为2
#         io.SEEK_CUR,指向当前指针,代号为1
import io

writepathRA = 'TestDoc' + os.sep + 'randomaccess.txt'

# 注意指定插入只能在写模式下使用，如果使用append模式自动设置所加的所有语句都在文件末尾处
with open(writepathRA, 'w+') as f:
    sText = '_'.join(str(x) for x in range(1, 20))  # join函数用前面的字符连接若干字符串序列
    f.write(sText)
    f.seek(10, io.SEEK_SET)  # 寻找第10个字节处的字符插入
    f.write('Insert_10')
    print('Current position after seek and write:', f.tell())
    f.seek(0, io.SEEK_END)
    f.write('\n')
    f.write('The end of random access file.\n')

with open(writepathRA, 'r+') as f:
    print(f.read())

# 3. 标准输入输出-管道重定向到指定文件中
#    sys.stdin--标准输入流
#    sys.stdout--标准输出流
#    sys.stderr--标准错误信息流
#    本部分输出结果见相应文件
#   操作系统的重定向功能实现
#   Linux/Unix Terminal: cat title.txt|python wordsStat.py
#   Windows Dos        : type title.txt|python wordsStat.py
import sys

writepathStdIn = 'TestDoc' + os.sep + 'StdIn.txt'
writepathStdOut = 'TestDoc' + os.sep + 'StdOut.txt'
writepathStdErr = 'TestDoc' + os.sep + 'StdErr.txt'
with open(writepathStdIn, 'w') as f:
    f.write('Peter\n')
    f.write('22\n')
    f.write('MALe\n')
fIn = open(writepathStdIn, 'r')
sys.stdin = fIn
fOut = open(writepathStdOut, 'w')
sys.stdout = fOut
fErr = open(writepathStdErr, 'w')
sys.stderr = fErr

# 实现从StdIn文件中取出用户信息，并将相应输出和错误信息传入到StdOut和StdErr文件中
sName = input('What\'s your name?\n')
iAge = int(input('How old are you?\n'))
iGender = input('Boy or girl?\n')

print(sName.title(), 'is a', 'boy' if iGender.lower() == 'male' else 'girl', 'aged {}.'.format(iAge))

fIn.close()
fOut.close()
raise Exception('Error Info')
fErr.close()
