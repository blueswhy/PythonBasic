# Word Frequency文件中的词频统计
import re

f = open('SomeoneLikeYou.txt', 'r')
sContents = f.read()
regWord = re.compile(r'-|\.|,|\?|\n|\s|\t')  # 利用分割符拆分其中的所有单词
words = [x for x in regWord.split(sContents) if x != '']  # 去除其中的空字符

WordsStat = {}
for k in words:
    WordsStat[k] = WordsStat.get(k, 0) + 1

sOutput = ''
count = 0
for k, v in WordsStat.items():
    count += 1
    sOutput = sOutput + k + ':' + str(v) + '\t'
    if count % 5 == 0:
        sOutput = sOutput + '\n'
print(sOutput)
f.close()
