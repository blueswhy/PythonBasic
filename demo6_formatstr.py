# 字符串的格式化输出, 简单操作使用该部分, 涉及更复杂的查找替换等操作时用re模块
import os



# 1. format() 函数, 在字符串中定义key: fmt, fmt中不需要再加%占位符
averScore = 79.132213
studentSno = 'GZ102321'
sText = 'Sno:{sno}, average score:{score:.2f}'.format(sno=studentSno, score=averScore)
print(sText)
sText = f'Sno:{studentSno}, average score:{averScore:.3f}'
print(sText)

# 尝试输出表情包到文件中, 直接输出在run窗口中不支持字符转换产生乱码
faceList = list(range(0x1f601, 0x1f64f + 1)) + list(range(0x2702, 0x27b0 + 1))\
           + list(range(0x1f680, 0x1f6c0 + 1)) + list(range(0x1f681, 0x1f6c5 + 1))\
           + list(range(0x1f30d, 0x1f567 +1))
facePath = 'TestDoc' + os.sep + 'face.txt'
with open(facePath, 'w', encoding='utf-8') as f1:
    for idx, x in enumerate(faceList):
        if (idx > 0 and idx % 50 == 0):
            f1.write('\n')
        f1.write(f'{x:c}')

# 不指定key时, format函数按照输入顺序进行格式化输出, 但是fmt格式符前面要有:作为占位标识
print('2^64 = {:,}'.format(2 ** 64))      # ,表示对一个大整数进行分节
print('{1:=+10.3} is bigger than {0:07.4}'.format(12.1232131, 17.213177))  # 序号指代填入位置

# 2.Pudding and positioning
print('python'.center(40, '-'))
print('python'.rjust(40, '*'), 'Pycharm'.zfill(10))
print('python'.ljust(40, '-'))

# 3. find()
sText = 'Never mind, I will find someone like you.'
print(sText.find('like', 0, len(sText)))      # 从字符串的左边找目标, 找到第一个目标后返回其位置
print(sText.rfind('like'))                    # 从字符串的右边找目标, 找到第一个目标后返回其位置
print(f'The index of "will" in the text:{sText.index("will")}, the count of "n" in the text:{sText.count("n")}')

# 4. join(), split(), replace()

pText = r'C:\Users\user\AppData\Local\Programs\Python\Python38\python.exe'
rpText = pText.replace('Local', 'local')      # 原有字符串不变, 调换相应字字符串后生成一个新字符串赋给新对象
plist = rpText.split('\\')                     # 注意转义符的使用
print('The result after split:', plist)
print('The plist after join:', '\\'.join(plist))

# 还有一些特殊的函数 startswith(), endswith(), isupper(), islower(), isdigit(), isdecimal()等, 不作详细介绍

# 5. 字符串常用函数
#    eval(), exec(), complie()
#    eval()将字符串类型的代码执行并返回结果
#    exec()仅仅执行字符串类型的代码, 不返回结果
#    compile(src, filename, mode, ...) 处理字符串类型的代码, 进行编译
#    src: 字符串或者Abastract Syntax Trees对象->需要动态执行的代码段
#    filename: 代码文件名称. 一般传入scr参数时, 该参数设置为空.
#    model: 指定编译种类. 'exec'->包含流程语句, eval->简单的求值表达式, 'single'->包含交互式命令语句