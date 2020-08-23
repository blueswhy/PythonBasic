# python中的异常处理
# 系统自带的错误类型见doc文件
# 1. try-except-else-finally
# 2. warning
from warnings import warn


def myDivide(a, b):
    return a / b


while True:
    sFirst = input('First Number:')
    sSecond = input('Second Number:')
    if sFirst == 'q' or sSecond == 'q':
        break
    try:
        iFirst = int(sFirst)
        iSecond = int(sSecond)
        fResult = myDivide(iFirst, iSecond)
    except ZeroDivisionError as e:
        print('Can not divide by zero:', e)
    except(ValueError, TypeError) as e:
        print('Illegal value, please input two numbers or q to execute the termination:', e)
    except Exception as e:
        print('An Exception found, the program can not process:', e)
        raise  # 当有其余错误函数自身不处理, 传递给上一级, 若一直没有处理, 系统会将错误信息传递给sys.excepthook
    else:
        if -0.0001 < fResult < 0.0001:
            warn('The result is too little to display.')
        print(sFirst, '/', sSecond, f'={fResult:.3f}')  # try 中的语句没有发生异常, 即执行else语句
    finally:
        print('Finally will be executed whatever happpens.')

# 3. 错误日志, 将错误记录在日志文件中以备查看
#    由于一般程序出现错误一般涉及到调用子程序和主程序中相应的关系, 调用traceback模块来找到这些错误
import traceback  # 打印或者检索堆栈回溯 模块
import sys
import os
from datetime import datetime

filename = 'TestDoc' + os.sep + 'except_error.log'
fError = open(filename, 'a')


def UserExceptHook(eType, eVal, eTraceback):
    tracelist = traceback.format_tb(eTraceback)
    html = repr(eType) + '\n'
    html += (repr(eVal) + '\n')
    for line in tracelist:
        html += (line + '\n')
    print(html, file=sys.stderr)
    print(datetime.now(), file=fError)
    print(html, file=fError)
    fError.close()


def main():
    s_first = input('First Number:')
    s_second = input('Second Number:')
    try:
        i_first = int(s_first)
        i_second = int(s_second)
        f_result = myDivide(i_first, i_second)
    except ZeroDivisionError as err:
        print('Can not divide by zero:', err)
    except Exception as err:
        print('An Exception found, the program can not process:', err)
        raise  # 当有其余错误函数自身不处理, 传递给上一级, 若一直没有处理, 系统会将错误信息传递给sys.excepthook
    else:
        if -0.0001 < f_result < 0.0001:
            warn('The result is too little to display.')
        print(s_first, '/', s_second, f'={f_result:.3f}')  # try 中的语句没有发生异常, 即执行else语句


sys.excepthook = UserExceptHook  # 钩子
main()
fError.close()

#4 Unit Test, 测试驱动的开发, 单元测试
# import unittest      # 测试函数开发模块
#
# class IsPrimeTestCase(unittest.TestCase):
#     def testIsPrime(self):
#         self.assertEqual(isPrime(3), True, '3 is Prime, but judge wrong')
#         self.assertEqual(isPrime(1), False, '1 is not Prime, but judge wrong')
#         self.assertEqual(isPrime(11), True, '11 is Prime, but judge wrong')
#
# if __name == '__main__':           # 当且仅当测试模块所在文件被当成主文件来测试的时候, 该语句为True开始执行
#    unittest.main()                 # 执行待测试模块的所有测试语句

