"""
【分支】编写程序，声明2个float型变量并赋值。判断第一个数大于10.0，且第2个数小于20.0，打印两数之和。否则，打印两数的乘积。

"""
#定义一个num1变量,接收第一个float 值

num1 = float(input("请你输入第一个值:"))

#定义一个num2变量，接收第二个float 值

num2 = float(input('请你输入第二个值:'))
# 判断第一个数大于10.0并且第二个数下雨20.0
if  num1 > 10.0 and num2 < 20.0:
#定义一个corrt变量，把俩数之和赋值给他
    corrt = num1 +  num2 
    print("俩数之和为:" ,corrt)
else:
    cheng = num1 * num2 
    print("俩数之积为:",cheng)