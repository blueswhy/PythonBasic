# 随机数模块
import random as rd
print('random decimal between 0 and 1: ', rd.random())
print('random integer between 1 and 6: ', rd.randint(1, 6))
print('random decimal between 1 and 3: ', rd.uniform(1, 3))
print('random number in the set 5<=x<=13 stepped by 3: ', rd.randrange(5, 13, 3))
seq_set = (1, '90', [23, 12], '81')
print('one random number in the seqs: ', rd.choice(seq_set))
print('two random sets in the seqs: ', rd.sample(seq_set, 2))
num_set = [x for x in range(0, 20, 3)]
rd.shuffle(num_set)
print('The number set after shuffle: ', num_set)

# 一些常用的分布
# random.uniform(a, b): a到b中的均匀分布
# random.triangular(low, high, mode): 三角分布
# random.betavariate(alpha, beta): Beta分布
# random.expovariate(lambd): 指数分布
# random.gammavariate(alpha, beta): Gamma分布
# random.gauss(mu, sigma): Guass分布, 和下面的标准正态分布函数而言实现更快
# random.lognormvariate(mu, sigma)
# random.normalvariate(mu, sigma): 标准正态分布