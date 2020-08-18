# 测试程序各模块
from func_getInfixExpression import func_getInfixExpression
from func_getPostfixExpression import func_getPostfixExpression
from func_computeExpression import func_computeExpression
# import time


#  验证序列, 可以计算带有{}[]() ** 的简单算式
# sTest = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
# sTest = '-2-3**6 -[12/5 - 90]'
# sTest = '-2 + 5/{9-9}-2**2'
# sTest = '1+(2-3)**3/(9-4)+4/2'
# sTest = '[1**9+100]/(2**20)'
sTest = '-10.2-4.5*8.4--6.9'                 # 计算时认为--6.9是+6.9
# sTest = '-sqrt(5*5- 4**2)'
# sTest = '-sqrt-3'                            # 测试根号算子中加负数的效果
# sTest = '-3sqrt-27'
# sTest = '(-27)**(1/3)'
# sTest ='1+sin6'
# sTest = 'sqrt3**2'
ret = func_getInfixExpression(sTest)
print('The infix expressin:', ret)
ret = func_getPostfixExpression(sTest)
print('The postfix expression:', ret)
# t1 = time.time()
ret = func_computeExpression(sTest)
# t2 = time.time()
print('The eval\'s result :', eval(sTest))
# print(f'Execute time: func_computeExpression->{t2 - t1:.6f} s, eval->{time.time()-t2:.6f} s')
