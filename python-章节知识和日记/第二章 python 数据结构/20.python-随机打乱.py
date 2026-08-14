"""
随机打乱 :   类似于 洗牌 


"""
import random 

# 随机模块中 有一个方法 random()  可以 随机 返回 [0, 1) 之间的 小数

print(random.random())

# 定义一个列表 
ls = [23, 56, 78, 23, 76, 3, 8, 12, 76, 12, 87, 132, 8, 28,1 ,87, 45, 9,12, 80,32]

# 随机打乱 
ls.sort(key=lambda d: random.random())

print(ls)