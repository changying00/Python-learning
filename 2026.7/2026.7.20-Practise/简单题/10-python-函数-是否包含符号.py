"""
【函数】编写一个函数 has_symbol、 判断指定的字符串中是否包含 逗号、冒号、下划线、中划线、英文句号、加号、减号、乘号
"""
#定义一个函数，看字符串是否包含符号
def has_symbol(str_symbol):
    symbol_count = [",",":","_","-",".","+","-","*"]
    for i in str_symbol:
        if i in symbol_count:
            return "包含符号"
    return "不含符号"

print(has_symbol("ab+c")) #包含符号
print(has_symbol("abc")) #不含符号