"""
range :  生成一个 指定的数字 序列对象 

range 函数 有 3个使用方式 

 a)  range(n) :   生成一个 [0, n)  包含 0 但 不包含 n 的数字序列对象 

 b)  range(m, n) :  生成一个 [m, n) 包含 m 但 不包含 n 的数字 序列对象

 c)  range(m, n, step=1) :  生成一个 [m, n) 包含 m 但 不包含 n 且 步长为 step 的数字序列对象 

        如果 m > n,  则 step 必须 < 0 ,  否则 step > 0
"""

x = range(10)

print(x,  list(x))

y = range(100, 200)

print(y, list(y))

z = range(100, 200, 2)

print(z, list(z))

a = range(10, 1, -1)

print(a, list(a))