"""
在一个大的笼子中，有鸡和兔若干只，从上看 有 35个头， 从下看 有94只脚。 问 鸡和兔各有多少只
"""

head = 35

# x 代表 鸡的数量 
for x in range(head+1):

    if x * 2 + (head - x) * 4 == 94:
        print("鸡的数量为", x,  "兔子的数量为", head -x)
        break