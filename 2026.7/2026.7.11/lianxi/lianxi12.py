"""

【分支】输入3个数，按从小到大排序

"""
#定义a 接收第一个数
a = int(input("输入第一个数:"))

#定义b 接收第二个数
b = int(input("输入第二个数:"))

#定义a 接收第三个数
c = int(input("输入第三个数:"))

if a>b and b >c :
    print(c,b,a)
elif a> c and c > b :
    print(b,c,a)
elif b > a and a > c:
    print(c,a,b)
elif b > c and c > a:
    print(a,c,b)
elif c > a  and a > b:
    print(b,a,c)
elif c > b and b > a:
    print(a,b,c)

"""
#定义a 接收第一个数
a = int(input("输入第一个数:"))

#定义b 接收第二个数
b = int(input("输入第二个数:"))

#定义a 接收第三个数
c = int(input("输入第三个数:"))

max  = min =a
if max< b:
    max = b
if max < c :
    max = c
if min > b:
    min = b
if min > c:
    min = c
"""
