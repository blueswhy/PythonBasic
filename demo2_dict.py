# 字典用{}或者dict创建，dict中存储的是键值对（key-value)
# 字典中键的顺序和添加顺序无关，是由Hash值确定的
# 字典中的数据只能按照key来读取，每个key创建时系统自动返回Hash值作为该key的id
# 字典中的键必须是可哈希类型，可以理解为只读类型，但一般都是用字符串来表示键以表明其意义
# 字典中的key是字符串时，需要加入“或者‘声明字符串属性
# dict[key]实际上是在执行dict.__getitem__函数
# 1. 创建字典
key_list = 'name', 'sno', 'gender', 'age'  # 序列类型可以加括号也可以不加括号
value_list = 'David', '10002', 'male', 21
david = {}
for david_key, david_value in zip(key_list, value_list):  # 序列拆分
    david[david_key] = david_value
print('The dict using sequence packing', david)

david_map = dict(zip(key_list, value_list))
print('The dict using dict mapping', david_map)
david_direct = dict(name='David', sno='10002', gender='male', age=21)
print('The dict using dict directly', david_direct)
print(id(david), id(david_map))  # 验证两个字典的id不同
print(id(david['sno']), id(david_map['sno']), id(value_list[1]))  # 验证两个内部两个数据的id是相同的，因为来源同一个数组

# 2. 字典嵌套
bookID = '100', '103', '201'
bookName = 'Go with the wind', 'A Game of Thrones', 'And Then There Were None'
bookdict = dict(zip(bookID, bookName))  # 用特定的类做成list更合适
david['booklist'] = bookdict
print('The dict after nested', david)

# 3. 字典函数
david.pop('booklist')
# 找字典中是否有key，没有则返回默认值
print('The dict after pop and get:', david.get('height', 'unknown'))
david_keys = david.keys()  # 返回david中的所有属性，相应的有items，返回所有值
print('The keys\' list of the dict:', david_keys)
# update 函数: 传入一些key-value对用来更新，如果有key则更新value，没有则加入键值对
david.update(height=178, weight=70)
print('The dict after update', david)
david_map.update({'height': 178, 'weight': 70, 'age': 19})
print('The map dict after update:', david_map)
david_direct.update([('height', 178), ('age', 19), ('weight', 70)])
print('The direct dict after update:', david_direct)
david_map.clear()

peter = dict.fromkeys(list(key_list), 'None')  # fromkeys的key参数需要时列表类型
for peter_key, peter_value in peter.items():
    print(peter_key, '-', peter_value)  # 序列解包
peter.update(name='Peter', sno='10012', gender='male', age=21)
# 4. copy函数和deepcopy函数,复制非只读元素的方式不同
peter['booklist'] = list(bookName)
peter_copy = peter.copy()
print(peter)
print(peter_copy)
print(id(peter), id(peter_copy))
print(id(peter['booklist']), id(peter_copy['booklist']))

from copy import deepcopy

peter_deepcopy = deepcopy(peter)
print(id(peter['booklist']), id(peter_deepcopy['booklist']))

# 结果中两种copy方式下中的嵌套列表的id有所不同，因此当改变原有嵌套列表内部信息时两种复制字典有不同改变

peter['booklist'].pop()  # 弹出原有嵌套列表的一个元素
print(peter_copy['booklist'], peter_deepcopy['booklist'])
