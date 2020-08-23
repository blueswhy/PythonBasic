def func_decomposeN(N: int, m: int):
    """分解正整数N,返回所有累加得到N的不重复序列ComposedList,m用来限制N分解的程度"""
    assert N > 0
    composedList = []
    if N == 1:
        return [[1]]
    else:
        k = 1
        while k <= N / 2:
            if k <= m:
                k += 1
                continue  # 防止分解重复，用m来限制分解
            subList = func_decomposeN(N - k, k - 1)
            for subunit in subList:
                composedList.append([k] + subunit)
            k += 1
        composedList.append([N])
        return composedList


def func_decomposeNListPrint(decomposedList):
    """打印N正整数分解得到的结果"""
    try:
        N = sum(decomposedList[0])
        print('All the decomposed lists of {}:'.format(N))
        for subunit in decomposedList:
            print(*subunit, sep='+', end='=%i' % N)
            print()
    except(ValueError, TypeError) as errmsg:
        print('Valid decomposed list', errmsg)
