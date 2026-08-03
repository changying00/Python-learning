#count = 0 
#while count < 10 : 
# print("hello world",count)
# count += 1
#第一题
#count = 1
#while count <=  100:
#  print(count)
#   count +=1
   
   
# 第二题
#count = 1
#while count < 100:
#   if count % 2:
#        print(count)
#优化 count += 1 写一次
#   count += 1


# 第二题改版
x = 1
while x < 100:
    print(x)
    x =  x + 2
"""
# 第三题
count = 1
score = 0
while count <= 100:
      score += count
      print(score)      #优化先打印后自加
      count += 1      
   
"""


"""   
# 第四题
count = 1
score = 0
while count <= 100:
    score += 1/count
    print(score)
    count += 1      
"""

"""
#第 五题
count = 1
num = 0
while count <=100:
    if not(count % 2):
        num  -= 1/count
#优化少写一次 count += 1
    else:
        num  += 1/count
#优化少写一次 count += 1 ,还得优化先打印后输出
    print(count,num)
    count += 1
"""
#第五题改版

x = 1
s = 0
symbol = 1
while x <= 100:
   s +=  1 /x * symbol
   x +=  1
   symbol *=   -1
print(s)