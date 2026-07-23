#【生成器】编写一个生成器函数，生成一个无限序列，该序列包含所有自然数的平方
#定义一个函数用于生成自然数的平方
def natural_squares():
    #唯一标识
    num = 0
    #通过while循环，无限生成产生自然数的平方
    while True:
        #yield 返回当前的平方数、并暂停函数
        yield num ** 2
        #下次恢复执行时、num加1
        num += 1

#测试生成器
if __name__ == '__main__':
    gen = natural_squares()
    # 只取前 10 个自然数的平方
    for _ in range(10):
        print(next(gen))

    #定义一个空列表ls1
    # ls1 =[]
    # #定义一个循环用于无限把自然数的平方增加到列表中
    # while True:
    #     #调用一次增加到列表中
    #     ls1.append(next(gen))
    #     #打印观察列表中的数据
    #     print(ls1)