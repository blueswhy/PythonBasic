# 除却常用的dict,tuple,list等数据类型,collections模块提供几个额外的数据类型

import collections as clt
# nametuple('Name','Property list'),以一个坐标点定义说明
# 定义一个名叫PoinT的Point元组类型, 有两个元素x,y
Point = clt.namedtuple('PoinT', ['x', 'y'])
p1 = Point(1, 2)
print('Type of p1:', type(p1))
print('p1.x = {}, p2.y = {}'.format(p1.x, p1.y))


# deque: 高效实现插入和删除操作的双向列表, 当线性结构list的数据量过大时,实现插入和删除的功能变慢
#        提供appendleft()和popleft()函数，实现列表头部的元素插入和pop操作
dq1 = clt.deque(['1', 'a', 'c'])
dq1.popleft()
dq1.appendleft('0')
print(dq1)

# OrderedDict: 保持key有序的字典
# defaultdict: 直接使用dict时,如果字典中没有该key,在进行查询,删除等操作时会返回错误,而defaultdict对于字典中未定义的key查询时返回定义的默认值
d1 = clt.defaultdict(lambda: 'None')
d1['Name'] = 'Bob'
print('Name: {}, Age: {}'.format(d1['Name'], d1['Age']))

# 设定一个默认值为列表的字典
d2 = clt.defaultdict(list)
values = [1, 3, 12, 97, 15, 68, 35, 79]
for value in values:
    if value > 60:
        d2['AboveList'].append(value)
    else:
        d2['BelowList'].append(value)
print(d2)

# Counter: 跟踪值出现的次数, 是一个无序的容器类型, 以字典的键值对形式存储, 其中key-value对为元素-出现次数
exp1 = 'abuwadadasdwdawasdw'
print(clt.Counter(exp1))