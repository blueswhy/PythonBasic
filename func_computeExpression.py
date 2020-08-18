# v1.0
# 目前版本仅能执行简单的+-*/, 平方, 开方
# Modification for more operators such as sin, cos:
# Step1: 定义好用户需要输入的符号, 比如三角正弦函数, 即作sin;
# Step2: 为了简单, 在字符串预处理过程中将sin映射为单字符s, 同时由于特殊符号的加入, 符号表达式
# 的匹配/分割正则表达式有相应改变, 得到加入s操作符的中缀字符串数组;
# Step3: 定义特殊符号s的优先级, 一般设置sin, cos, tan这种三角函数优先级相同, 但是高于根号,
# 将中缀表达式转换为后缀表达式;
# Step4: 定义对于符号s的计算功能, 由于是sin函数只有一个操作数, 更改时要注意。因为后缀表达式规
# 则上需要两个操作数执行一次操作符, 可以在得到中缀表达式过程中将sina 转化为1sina, 1相当于sin
# 的占位符, 更简单一点将sin预处理时替换为1s字段, 既能实现sin功能, 又能符合后缀表达式的实现.

# v2.0: 可以往UI方向设计, 实现交互式输入输出
# v3.0: 封装, 实现用户管理, 在产品上可以设置用户等级和高级计算功能

from func_getPostfixExpression import func_getPostfixExpression
from warnings import warn
import re


def isInteger(a: float):
    """Judge whether the float variable: a is an integer."""
    b = int(a)
    if b == a:
        return True
    else:
        return False


def op_ab(op: str, a: float, b: float):
    """Get the result of 'a op b'.Notice the order of a and b."""
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    elif op == '**':
        if a < 0 and not isInteger(b) and (1/b) % 2 != 0:
            return - (-a) ** b
        else:
            return a ** b
    elif op == 'q':
        if b < 0 and not isInteger(1/a) and a % 2 != 0:
            return - (-b)**(1/a)
        else:
            return b ** (1/a)
    else:
        warn('Get an invalid operator.')
        raise Exception


def func_computeExpression(exp: str):
    """Compute the result of the valid symbolic expression inputted."""
    try:
        listPostfixExp = func_getPostfixExpression(exp)  # 得到后缀表达式
        regValidNum = re.compile('-?\d+\.\d*|-?\d+')
        stack = []
        for sElement in listPostfixExp:
            if regValidNum.match(sElement):
                fElement = float(sElement)  # 字符串转化为可运算的数字
                stack.append(fElement)  # 遇到数字存入栈
            else:
                fElement2 = stack.pop()
                fElement1 = stack.pop()
                fRet = op_ab(sElement, fElement1, fElement2)
                stack.append(fRet)  # 遇到操作符op,从栈中取出两个数字计算得到fRet, 并存入栈
        ret = stack.pop()
    except ZeroDivisionError as e:
        print('Can not divide by zero:', e)
    except(ValueError, TypeError) as e:
        print('Invalid expression:', e)
    except Exception as e:
        print('Some expression my function cannot process:', e)
    else:
        if isinstance(ret, complex):
            warn('The result belongs to complex domain, which can not be processed.')
        elif -0.0001 < ret < 0.0001 :
            warn('The result of the expression is close to 0.')
        print(exp, ' = ', ret)
        return ret
