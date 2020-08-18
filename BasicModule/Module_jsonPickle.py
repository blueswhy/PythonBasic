# 序列化模块
# 举例而言就是讲序列化数据如字典转化成字符串存入文件中, 反序列化是指将数据从文件中提取出来转换成字典进行使用的方法.
# 一般反序列化可以使用eval()函数, 将字符串当成有效的表达式求值并返回计算结果. 不过执行命令中含有破坏性语句时， 使用eval()会承担一定的风险。
# 下面介绍两个python提供的序列化模块: Json和Pickle.
# Json: 用于字符串和python数据之间进行类型转换.json实现了对于python以外语言数据文件的接口.
# 提供四个方法, dump()->序列化存储存入文件中, dumps()->序列化将数据转化为字符串, loads->反序列化读取, load.
# 参数说明:
# Skipkeys：默认值是False，如果dict的keys内的数据不是python的基本类型(str,unicode,int,long,float,bool,None)，
# 设置为False时，就会报TypeError的错误。此时设置成True，则会跳过这类key
# ensure_ascii:，当它为True的时候，所有非ASCII码字符显示为\uXXXX序列，只需在dump时将ensure_ascii设置为False即可，
# 此时存入json的中文即可正常显示.)
# indent：如果是0就是顶格分行显示，如果为空就是一行最紧凑显示，否则会换行且按照indent的数值显示前面的空白分行显示，这样
# 打印出来的json数据也叫pretty-printed json
# separators：分隔符，(item_separator, dict_separator)的一个元组，默认的就是(‘,’,’:’), 这表示dictionary内keys
# 之间用“,”隔开，而key和value之间用“:”隔开.
# sort_keys：将数据根据keys的值进行排序.


# Pickle: 用于python特有的类型 和python的数据类型进行转换.pickle序列化之后的文件只有用python语言才能读出反序列为原有数据.
# 提供的四个方法中dump, dumps, load, loads, 其序列化是将数据类型转化为二进制字节流, 反序列化是将这些字节流转化为原来的数据类型.
# 参照docs可以找到二者的对比: JSON is human-readable, while pickle is not...

import io
import os
import json
import pickle

datapath = '../demo' + os.sep + 'TestDoc' + os.sep + 'dictBob.txt'
f1 = open(datapath, 'r+')
# dictBob = {'Name':'Bob', 'Age':21, 'Gender':'Male'}               # 将字典数据以字符串序列化后单引号变成双引号存在文件中
# json.dump(dictBob, f1)
# f1.close()
dictBob = json.load(f1)
print(type(dictBob), dictBob)
dictBob['国籍'] = '英国'
ret = json.dumps(dictBob, ensure_ascii=True)
f1.seek(0, io.SEEK_SET)
f1.write(ret + '\n')
f1.close()

BobPicklePath = '../demo' + os.sep + 'TestDoc' + os.sep + 'pickleBob.txt'
with open(BobPicklePath, 'wb') as f2:
    pickle.dump(dictBob, f2)
with open(BobPicklePath, 'rb') as f3:
    Bobpickle = pickle.load(f3)
    print('The binary stream convert to sequence data:', Bobpickle)
