"""
【运算符】现有一个权限系统， 4 代表 可读， 2 代表 可写 ， 1 代表可执行 ， 
当输入一个 0 ~ 7 之间的任意一个数字时候，判断对应的权限有哪些。
"""
#定义用户输入0~7之间的数
num = int(input("请输入一个(0~7)的数:"))
Read = 4
Write = 2
Execute = 1

if num & Read:
    print("可读")

if num & Write:
    print("可写")

if num & Execute:
    print("可执行")
"""
#进行if先判断数字是否满足条件，满足进行下一步，不满足提示重新输入
if  0 <= num <= 7 :
    if num  & Read == Read :
        if num & Write == Write:
            if num & Execute == Execute:
                print("你有读和写和执行的权限")
            else:
                print("你有读和写的权限")
        else:
            if num & Execute == Execute:
                print("你有读和执行的权限")
            else:
                print("你有读的权限")
    else:
        if num & Write == Write:
            if num & Execute == Execute:
                 print("你有写和执行的权限")
            else:
                 print("你有写权限")
        else:
            if num & Execute == Execute:
                  print("你有执行的权限")
            else:
                  print("你没有任何的权限")
else:
    print("你输入的数不正确请重新输入")
"""