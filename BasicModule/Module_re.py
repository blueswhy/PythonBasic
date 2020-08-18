# 简单介绍re模块和相应的正则表达式
# re模块: python独有的匹配字符串的模块，使用正则表达式实现模糊匹配功能
# 正则表达式: 字符组匹配时使用[]来表示,一些特殊的表示方法如下:
#           [0-9] 表示0-9的数字
#           [a-z] 表示所有小写字母
#           [A-Z] 表示所有大写字母
#           [0-9a-fA-G] 是三个正则表达式的组合
# 字符匹配: .     匹配除换行符以外的任意字
#          \w    字母或数字或下划线
#          \s    任意的空白符
#          \d    数字
#          \n    一个换行符
#          \t    一个制表符
#          \b    一个单词的结尾
#          ^     字符串的开始
#          $     字符串的结尾
#          \W    非(字母或者数字或者下划线)
#          \D    非数字
#          \S    非空白符
#          a|b   字符a或者b
#          ()    括号内的表达式，也可以表示为一个组
#          [...] 字符组内的字符, []中的字符不需要加\来标识,如+-*/等
#          [^...]除了字符组内的所有字符
#   \n,\s,\t在python中有具体含义,使用时需要加转移符\
#  量词:    *     重复零次或者更多次
#          +     重复一次或者更多次
#          ？    重复零次或者一次
#          {n}   重复n次
#          {n,}  重复n次或者更多次
#          {n,m} 重复n到m次
#          量词中的重复次数在字符串匹配中对应为字符个数
#  举例说明正则表达式的使用
#  对于同一个匹配字符 abefacagad 而言, 正则表达式和匹配结果对应关系如下：
#  a.       abefacagad
#  ^a.      ab              仅仅取匹配词的前两个字符
#  a.$      ad              仅仅取匹配词的后两个字符
#  a.?      ab ac ag ad     * + ?都是贪婪匹配，如果再加？变成惰性匹配
#  a.*      abefacagad      匹配a后面0个或者多个字符
#  a.+      abefacagad      匹配a后面一个或者多个字符
#  a.{1,2}  abe ac ag ad    匹配a后面1个或者2个字符，符合2个字符的就优先2个字符，贪婪匹配
#  a.*?     a a a a         惰性匹配,匹配尽量短的字符串
#  a[bef]*  abef            匹配abef字符
#  a[^f]*   abe ag ac ad    匹配a开头但是不含f的所有字符串
#  re模块中的常用函数
#  匹配函数，可用参数包含两个pattern 正则表达式 和 string 待匹配字符串(flags=0,未知参数不作修正)
#    compile():  将正则表达式编译为正则表达式对象，再用相应的函数进行匹配
#    search() :  扫描字符串查找和正则项相匹配的第一个位置，并返回相应的match对象,有则返回第一个对象，没有则返回None
#    match()  :  和search不同，从字符串开始位置和正则项匹配,如果从开头就不符合匹配要求就返回None
#    fullmatch():要求整个字符串和该正则项匹配，否则返回None
#    split()    :  通过模式来拆分字符串,模式是拆分字符串的根据,多一个参数maxsplit表示最大分割次数,达到maxsplit后会直接将后续所有字符作为一个分割字符串返回
#    findall()  :  以string列表形式返回字符串中的所有符合正则项的非重叠匹配结果
#    finditer() :  返回一个迭代器，该迭代器在string类型的RE模式的所有非重叠匹配对象，从左到右扫描字符串，并以找到的顺序返回匹配项
#    escape()   :  escape special characters in a string.自动转义所有字符图案，
import re

regExp1 = re.compile('[a-z]{2}')  # 将连续两个小写字母作为正则匹配对象
sContents = 'MicroSoft Office_Ali+SSpre123okay'
print(regExp1.search(sContents).group())
print(regExp1.match(sContents))
print(regExp1.fullmatch(sContents))
print(regExp1.findall(sContents))

regExp1Iter = regExp1.finditer(sContents)
print(next(regExp1Iter))

# split()函数的优先级查询
# 正则表达式在匹配部分加上()之后保留被匹配的部分分割原有项
regExp2 = re.compile(r'\W+|_|\d+')
# print('maxsplit = 4:', regExp2.split(sContents,maxsplit=4))
print(regExp2.split(sContents))
regExp3 = re.compile(r'(\W+|_|\d+)')
print(regExp3.split(sContents))

# sub(pattern , repl , string ,count = 0, flags = 0)
# 用repl替换string中的匹配完成的字符串,如果没有匹配项,则返回原有字符串。count控制替换次数，从左边第一个被匹配词作为第一个，count=0表示所有匹配词。
#  repl可以是字符串或者函数,若是字符串。处理其中的任何反斜杠\作为转义,即将其转换为单个换行符转换为回车。
#  subn()函数功能相同，返回一个元组,第一个是替换后的字符串,第二次是替换次数
phone_num = '133_1239-2082'
regJoinNum = re.compile('-| |_')
repl = ''
phone_numSubn = regJoinNum.subn(repl, phone_num)
print('phone number after subn:', phone_numSubn)

# 4. 手机号的合法性检验
#    开头 13 14 15 18,共11位,都是由数字构成

phone_num = '133_1239-2082'  # 原始输入信息可能有一些空格、_和-的分割符
regJoinNum = re.compile('-| |_')
phone_number = ''.join(regJoinNum.split(phone_num))

regPhoneNum = re.compile('^(13|14|15|18)[0-9]{9}$')
if regPhoneNum.match(phone_number):
    print('valid phone number:', phone_num)
else:
    print('invalid phone number:', phone_num)

# 5. 匹配一个表达式中的整数(有负号认为是负数)和小数
mathExp = '1-2*60+40.35/4.5*3-2'
regDecimal = re.compile(r'-?\d+\.\d*')
# 利用findall()函数的优先级搜索将搜索得到的小数不再显示到匹配结果中
# 执行流程,findall先根据第一个正则项选出字符串中的所有小数,再根据第二个正则项选出剩余字符串中的所有整数,由于括号的优先级输出直接输出第二部分
regInteger = re.compile(r'-?\d+\.\d*|(-?\d+)')  # 注意第二个表达式中的括号和两个匹配的顺序

print('The Decimals in the math exp:', regDecimal.findall(mathExp))
print('The Intergers in the math exp:', regInteger.findall(mathExp))

regTwoDigits = re.compile(r'-?\d+\.\d*|(-?\d{2,})')
ret = regTwoDigits.findall(mathExp)

# 使用remove函数删除列表中的值时,一般不要使用for循环,在remove时会出现下标越级现象
# while '' in ret:
#     ret.remove('')                                         # remove单次仅仅删除一个值
ret = [x for x in ret if x != '']
print('The two-digits Integers in the math exp:', ret)

# 5. 匹配一个汉字
regChChar = re.compile(r'[\u4e00-\u9fa5]{1, }')
txtExp = 'NeverMind,I will find someone like you.勿念，芳草天涯皆有之'
print(regChChar.findall(txtExp))

# 6. 编写一个简单的eval()计算程序--详细函数见demo中的ComputeExpression模块
sText = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'