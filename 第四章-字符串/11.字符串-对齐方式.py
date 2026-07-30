"""
字符串的 对齐方式
     ljust(width,fillchar = ""): 左对齐、右填充
     rjust(width,fillchar = ""): 右对齐、左填充
     center(width,fillchar = ""):居中对齐
     zfill 要在字符串的左侧补零，也可以使用方法

"""
string = "hello"

print(string.center(10,"-"))
print(string.ljust(10,"-"))
print(string.rjust(10,"-"))
print(string.zfill(10))

print(f"{string:/<10},everyone")#左对齐、右填充
print(f"{string:！>10},everyone")#右对齐、左填充
print(f"{string:？^10},everyone")#居中对齐、俩边填充