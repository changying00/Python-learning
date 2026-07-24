"""
【格式化】编写一个函数 lpad(string, width, char=" ") 实现将传入的字符串使用 char 字符 左补齐 width 长度 (要求使用字符串格式化实现)
"""
#定义一个函数ipad
def lpad(string, width, char=" "):
    return f"{string:{char}>{width}}"
# 测试
print(lpad("abc", 8))
print(lpad("abc", 8, "0"))
print(lpad("Python", 12, "*"))