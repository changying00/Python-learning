#【列表】使用随机模块、将0 - 9 随机存入到长度为10的列表中、元素不允许重复
#导入模块
import random
#定义一个空列表用于储存元素
ls = []
#判断列表的长度不能超过10
while len(ls)<10:
    # 随机数赋值给num1变量
    num1 = random.randint(0, 9)
    #跟随机数对比如果不同增加到列表中
    if num1 not in ls:
        #增加到列表
        ls.append(num1)
print(ls)

