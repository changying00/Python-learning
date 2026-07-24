"""
【生成器】编写一个函数 fac() 、该函数不需要任何参数、实现 每次调用 next 获取 斐波那契数列 中的 一个数字。

1 1 2 3  5  8  13  21 .....
"""
#定义一个函数fac(),没有参数实现，每次调用取值
def fac():
    #a是第一个数字
    a = 1
    #b是第二个数字
    b = 1
    while True:
        yield a
        a , b =  b , a + b
if __name__ == "__main__":
      re = fac()
      print(next(re))
      print(next(re))
      print(next(re))
      print(next(re))
      print(next(re))
      print(next(re))
      print(next(re))

