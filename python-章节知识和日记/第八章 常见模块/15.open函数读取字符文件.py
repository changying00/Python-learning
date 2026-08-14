
# 定义一个变量、用来存储即将要读取的文件 
path = r"C:\Users\Administrator\Desktop\python基础\第八章 常见模块\1.数学math模块.py"

# 使用 open函数 读取 文本文件 
f = open(path, "rt", encoding="utf-8") 

# 1. 一次性 将所有数据读取到内存中 、适合 小文件的读取
content = f.read()
# 输出内容 
print(content)

# 2. 每次 读取 一定长度的内容 、适合 大文件的读取 
#   read(n)  一次 读取 n 个 字符 、返回 读取的内容 、 当 read(n) 返回 空字符串的时候、 代表 已读取完成 

# content = ""
# while (text := f.read(100)) != '':
#     # 一次性读取 100 个字符
#     content += text 

# print(content)

# 3. 文本文件 支持 一次读取 一行内容 
#  readline() 一次读取 一行内容、 当读取完成 的时候，返回 一个 空字符串 
# while (text := f.readline()) != "":
#     print(text, end="")


# 4. 一次读取所有内容，并将 结果存储到 列表中， 列表中的每一个数据 代表 文件的中一行内容
# content = f.readlines()
# for v in content:
#     print(v, end="")

# 文件读取完成后、 必须关闭通道 
f.close()