#【生成器】编写一个生成器函数，生成一个无限序列，该序列包含所有素数。
"""
设计一个判断给定的大于1的正整数不是质量数的函数。质量数只能被1和自身整除的正整数（大于1），如果一个大于1的正整数
N是质数，也就是说在2到N−1之间都没有它的因子。
"""
#定义一个生成器使其生成无限序列、包含所有的素数

def su_num():
    num = 2
    while True:
      for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
      else:
           yield num
      num += 1
if __name__ == '__main__':
    g = su_num()
    for  _ in range(20):
        print(next(g))
    # g = su_num()
    # ls1 = []
    # while True:
    #     ls1.append(next(g))
    #     print(ls1)
