"""

【循环题】从键盘输入一个数字、例如 2 ，则计算 2 + 22 + 222 + 2222 + 22222 前 5项的和

"""
#定义一个用户输入变量
num = int(input("请输入一个数字:"))
# 定义一个循环变量
x = 1
# 定义一个存储结果的变量
count =  num 
while x <= 4 :
    num  =  num * 10  +  2   
    count = count + num     
    x  +=  1
print(count)    