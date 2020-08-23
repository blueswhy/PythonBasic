# 二进制文件的读取存储操作
# struct模块作Bytes和bitsteam->可读字符串之间的转化
import struct
import os
import matplotlib.pyplot as plt
import numpy as np

# # 生成一个简单的sin函数数据

# import math
#

# data = [math.sin(x) for x in np.arange(-3, 3, 0.02) ]
# filename = 'TestDoc' + os.sep + 'puresin.dat'
# with open(filename, 'wb') as f:
#     for x in data:
#         a = struct.pack('f', x)
#         f.write(a)
#
#  从二进制文件中提取原始数据
filename = 'TestDoc' + os.sep + 'puresin.dat'
with open(filename, 'rb') as f:
    rawData = f.read()

iSampleCount = len(rawData) // 4           # 向下取整, 防止溢出
convertData = []
for i in range(iSampleCount):
    fValue, = struct.unpack('<f', rawData[i*4:i*4+4])      # 每四个字节取出解包得到相应的浮点数
    convertData.append(fValue)
plt.plot(np.arange(-3, 3, 0.02), convertData, 'r-')
plt.show()
