#【字典】合并两个字典中相同 key 的 value（假设 value 是数字），
# 不同的 key 保留。示例：{'a':1,'b':2} + {'a':3,'c':4} → {'a':4,'b':2,'c':4}
#定义一个变量储存字典dic1
dic1 ={'a':1,'b':2}
#定义一个变量存储字典dic2
dic2 ={'a':3,'c':4}
#定义一个空的字典
for key,value in dic1.items():
    if key in list(dic2):
       dic2[key] = dic1[key] + dic2[key]
    else:
       dic2[key] = dic1[key]
print(dic2)