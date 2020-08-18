import re
from warnings import warn


def func_isValidExpression(exp: str):
    """Judge whether the expression is a valid symbolic expression."""
    regCheck1 = re.compile(
        # r'^(-?\d+|\(|\[|\{)(\-?\d+|\-?\d+\.\d*|\*{1,2}|\+|\-|\/|\s|\(|\)|\{|\}|\[|\]){1,}(-?\d+|\)|\]|\}|\=)$')  # 直接匹配原有符号表达式
        r'^(\-|\d+|\(|q)(\-?\d+|\-?\d+\.\d*|\*{1,2}|\+|\-|\/|q|\(|\)){1,}(-?\d+|\)|\=)$')    # 匹配预处理后的符号表达式
    regCheck2 = re.compile(r'\*{3,}')
    if regCheck1.match(exp) and not regCheck2.search(exp):
        return True
    else:
        return False


def func_getInfixExpression(exp: str):
    """Transfer the expression inputted to an infix expression list."""
    sExpSub = re.sub(r'[\[{]', '(', exp)
    sExpSub = re.sub(r'[\]}]', ')', sExpSub)
    sExpSub = sExpSub.replace('sqrt', 'q')  # 为了简单将根号->字母q, 其实 ** 求方也可以用替换字段的方式更好处理^
    sExpSub = re.sub(r'\s', '', sExpSub)  # 去除多余空格
    if func_isValidExpression(sExpSub):
        regSplit = re.compile(r'(-?\d+\.\d*|-?\d+|\(|\)|q|\=)')
        listExpSplit1 = regSplit.split(sExpSub)  # 根据小数|整数|括号为标志初步分离表达式(含有空字符)
        listExpSplit2 = [sElement for sElement in listExpSplit1 if sElement != '']  # 去除其中的空白符
        if listExpSplit2[-1] != '=':
            listExpSplit2.append('=')  # 设置结束标志

        idx = 0
        regValidNum = re.compile(r'-?\d+\.\d*|-?\d+')
        regValidNeg = re.compile(r'-\d+\.\d*|-\d+')
        while True:
            sElement1 = listExpSplit2[idx]
            sElement2 = listExpSplit2[idx + 1]
            if sElement2 == '=':
                break
            if regValidNum.match(sElement1) and regValidNum.match(sElement2):
                listExpSplit2.insert(idx + 1, '+')
                idx += 1
            if idx == 0 and sElement1 == '-':
                listExpSplit2.insert(idx, '0')
            else:
                if sElement2 == '**' and regValidNeg.match(sElement1):
                    sElement3 = sElement1.lstrip('-')
                    if listExpSplit2[idx - 1] == '+':
                        listExpSplit2[idx - 1] = '-'
                        listExpSplit2[idx] = sElement3
                        idx += 1
                    else:
                        listExpSplit2.insert(idx, '0')
                        listExpSplit2.insert(idx + 1, '-')
                        listExpSplit2[idx + 2] = sElement3
                        idx += 3
                if idx == 0 and sElement1 == 'q':
                    listExpSplit2.insert(idx, '2')  # 如果只有一个q作为根号, 添加一个数字2作为根号2
                    idx += 1
                elif sElement2 == 'q' and regValidNeg.match(sElement1):
                    sElement3 = sElement1.lstrip('-')  # 出现-3q4这种情况: 拆分成 -, 3, q, 4
                    if listExpSplit2[idx - 1] == '+':
                        listExpSplit2[idx - 1] = '-'
                        listExpSplit2[idx] = sElement3
                        idx += 1
                    else:
                        listExpSplit2.insert(idx, '0')
                        listExpSplit2.insert(idx + 1, '-')
                        listExpSplit2[idx + 2] = sElement3
                        idx += 3
                elif sElement2 == 'q' and not regValidNum.match(sElement1):
                    sElement3 = listExpSplit2[idx + 2]  # 检验单独的根号内部不能存在负数
                    if regValidNeg.match(sElement3):
                        warn('The op "sqrt" can not be followed by a negative.')
                        raise Exception
                    listExpSplit2.insert(idx + 1, '2')  # 单独的q5, 这种情况加上操作数2, 指代根号2
                    idx += 1
            idx += 1
        listExpSplit2.pop()  # 删去结束标志
        return listExpSplit2
    else:
        warn('Please input valid expression, only {+,-,*,/,(),[],{},**,sqrt} for ops and fractions included.')
        raise Exception
# Test tips: 写正则表达式时, 切勿随意加空格
