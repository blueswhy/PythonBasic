# 实现WindowsDos系统下的文件管道重定向
# 分词对象SomeoneLikeYou.txt
import sys

sConetents = sys.stdin.read()  # 从标准输入获取内容
words = sConetents.split()  # 字符串分词
wordsStat = {}
for x in words:
    wordsStat[x] = wordsStat.get(x, 0) + 1

sOutput = ''
for k, v in wordsStat.items():
    sOutput = sOutput + k + ':' + str(v) + '\t'
print(sOutput)
