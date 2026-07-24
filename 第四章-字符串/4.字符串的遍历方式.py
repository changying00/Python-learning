"""
字符串 遍历方式 :

    基于 索引的遍历 方式   len

    基于 值的遍历方式 

    基于 索引和值 的遍历方式 enumerate


字符串 切片 只 支持 提取数据 、切片语法 [start:end:step]

"""

string = "hello"

# 
for i in range(len(string)):
    print(i,  string[i])

print("=" * 50)

# 值遍历 
for v in string:
    print(v)

print("=" * 50)

# 值和索引 的遍历方式 
for i, v in enumerate(string):
    print(i, v)


string = "hello"
# 将 字符串 进行反转 
print(string[::-1])
