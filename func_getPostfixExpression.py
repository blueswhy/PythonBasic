from func_getInfixExpression import func_getInfixExpression
import re
from warnings import warn


def func_getOpPri(op: str):
    """Get the operotor's execute priority. """
    if op == '(':
        return 1
    elif op in '+-':
        return 2
    elif op in '*/':
        return 3
    elif op == '**' or 'q':
        return 4
    elif op == ')':
        return 10                # 设置高一些, 以便更多操作符的加入
    else:
        warn('Get a invalid operator.')
        raise Exception


def func_getPostfixExpression(exp: str):
    """Transfer the Infix expression list to the Postfix expression list."""
    listInfixExp = func_getInfixExpression(exp)

    ret = []
    stack = []
    regValidNum = re.compile(r'-?\d+\.\d*|-?\d+')
    for sElement in listInfixExp:
        if regValidNum.match(sElement):
            ret.append(sElement)  # 遇到合法数字, 直接输出到结果
        else:
            if len(stack) == 0 or sElement == '(':
                stack.append(sElement)
            elif sElement == ')':
                t = stack.pop()  # 处理中缀表达式中的括号
                while t != '(':
                    ret.append(t)
                    t = stack.pop()
            else:
                opPri1 = func_getOpPri(sElement)  # 存放当前操作符的优先级
                while stack:
                    t = stack[-1]
                    opPri2 = func_getOpPri(t)
                    if opPri2 >= opPri1:
                        ret.append(stack.pop())
                    else:
                        break
                stack.append(sElement)

    while stack:
        ret.append(stack.pop())

    return ret
