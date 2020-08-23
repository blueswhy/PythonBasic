# 自定义函数集合，一般一个函数是一个文件，便于查看和管理
# * A传递多个参数不需要反应其位置，**A则表示A是一个字典变量，表示传参省略掉一系列关键字


def func_factorial(x: int):
    """阶乘函数，输入必须是正整数"""
    assert x > 0
    if x > 1:
        return x * func_factorial(x - 1)  # 以递归的方式做阶乘处理
    else:
        return x


def func_splitN(N: int):
    """分解正整数N,打印相应的连续正整数序列"""
    N_seq = range(1, N + 1)
    print(*[list(range(N_seq[x - 1], N_seq[x - 1] + y)) for x in N_seq for y in N_seq \
            if sum(range(N_seq[x - 1], N_seq[x - 1] + y)) == N and N_seq[x - 1] + y <= N + 1])


def func_MultiParaPrint(title, *content):
    """利用*实现多参数传递"""
    print(title + ':')
    for x in content:
        print('\t', x)


def func_DictPrint(title, **content):
    """利用**实现字典传递"""
    print(title + ':')
    for x, v in content.items():
        print('{:>20}:{:>10}'.format(x, v))  # 使用format函数来规定输出格式
