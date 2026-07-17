"""
【分支结构】 编写一个程序，接受用户输入的一个字符，判断该字符是大写字母、小写字母、数字还是其他字符。
Python 中字符可以直接比较，因为字符实际上对应着 ASCII 码。

ch = input("请输入一个字符：")

code = ord(ch)

if 65 <= code <= 90:
    print("大写字母")
elif 97 <= code <= 122:
    print("小写字母")
elif 48 <= code <= 57:
    print("数字")
else:
    print("其他字符")
"""

# 接收用户输入一个字符 
ch = input("请输入一个字符：")

if 'A' <= ch <= 'Z':
    print("大写字母")
elif 'a' <= ch <= 'z':
    print("小写字母")
elif '0' <= ch <= '9':
    print("数字")
else:
    print("其他字符")