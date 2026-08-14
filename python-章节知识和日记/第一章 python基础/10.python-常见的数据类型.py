"""
常见的数据类型:
   
   a) 数字类型 
   
      1) 整数类型、使用 int 表示 
      2) 浮点数类型、使用 float 表示
      3) 复数、使用 complex 表示 (了解)
      
   b) 字符串类型、使用 str 表示 
     
   c) 布尔类型、 代表 真假、 使用 bool 表示
   
   d) NoneType、 代表 空、有且只有 1个值 None 

"""
# 定义一个变量，用来存储整数 
a = 10
# 使用 type函数 可以获取指定数据的类型
print(a, type(a))

# 定义一个变量、用来存储浮点数
b = 20.3
print(b, type(b))

# 定义一个变量、用来存储复数 
#   +4 实数 、 +3j 虚数
c = 4 + 3j
print(c, type(c))

# 定义一个变量、用来存储文本内容
# 在 python 中，字符串 支持使用 双引号、单引号、三引号 引起来
d = "hello"
print(d, type(d))

d1 = 'hello'
print(d1, type(d1))

d2 = """hello"""
print(d2, type(d2))

# 定义一个变量、用来存储 真 (True) / 假 (False)
e = True 
print(e, type(e))

e1 = False 
print(e1, type(e1))

# 定义一个变量，用来存储 空 
f = None 
print(f, type(f))







