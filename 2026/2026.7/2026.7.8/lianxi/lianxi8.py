"""
【运算符】在一个大的笼子中，有鸡和兔若干只，
从上看有 35个头， 从下看有94只脚。 
问鸡和兔各有多少只
a = 12 b = 23 
4a = 48 2b =46
"""
"""
#输入鸡兔多少个头
heart = int(input("鸡和兔共几个头:"))

#输入鸡兔多少只腿
leg = int(input("鸡和兔共多少只腿:"))
#设鸡有x只,
chicken = heart - y
chicken_leg = (heart - y)*2
#设兔有y只,腿为4y条
Rabbit = heart - x
Rabbit_leg = 4*(heart - x)


2x + 4y = leg"""
#输入鸡兔多少只腿
leg = 94
#输入鸡兔多少个头
heart = 35

a = (leg - 2*heart)/2
b = heart - a
print("鸡有",b,"只")
print("兔有",a,"只")