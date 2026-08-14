"""
循环 :  通过特定的指令、可以将某一段任务 重复执行、直到 条件不满足为止 ~~~

python 中 实现 循环的 手段 有 2种 

    1)  while 循环 ： 善于处理 循环次数 不确认的 任务
    
    2)  for 循环 ：主要处理 循环次数 确定的任务 


while循环的语法:


while condition:
    pass
    
condition : 循环执行的条件、当满足条件的时候，才会执行重复的任务 

pass : 循环体、编写 重复执行的任务代码


练习题：

    1.  编写循环在控制台上 输出 1, 2, 3, ... 100
    
    2.  编写循环在控制台上 输出 1， 3， 5， 7，... 99
    
    3.  编写循环 计算 1 + 2 + 3 + ... + 100 的和 
    
    4.  编写循环 计算 1/1 + 1/2 + 1/3 + ... + 1/100 的和 
    
    5.  编写循环 计算 1 - 1/2 + 1/3 - 1/4 + .... -1/100 的和 


"""

# 定义一个计数器从1开始 
x = 1
# 定义一个变量、用来存储最终的结果 
s = 0

# 定义一个变量、用来控制累加求和的每一项的符号
symbol = 1

while x <= 100:
   # 当 产生一个 x 、就 和 s 进行 累加求和 
   s = s + 1 / x * symbol 
   # 将 计数器增加 1
   x = x + 1
   # 将 符号进行切换
   symbol = symbol * -1
   
# 循环结束后、输出计算的结果
print(s)


# 定义一个计数器从1开始 
x = 1

while x < 100:
    # 输出 x 
    print(x)
    # 将 x 每次自增 1 
    x = x + 2



# 定义一个计数器、从1开始 
x = 1
# 定义循环条件
while x <= 100:
    # 输出 x 
    print(x)
    # 将 x 进行自增 
    x = x + 1




# 请在控制台上输出 10万个 hello world!
# 定义一个计数器
count = 0

while count < 100000:
    # 输出任务
    print("hello world!!!", count + 1)
    # 将计算器的值 增加 1
    count += 1


num = 2
while num <= 10000:
    total = 0
    i = 1
    while i < num:
        if num % i == 0:
            total = total + i
        i = i + 1
    if total == num:
        print(num)
    num = num + 1


