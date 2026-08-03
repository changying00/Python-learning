"""
f-string 字符串格式化 技巧 

{ exp: [填充的字符][对齐方式][填充宽度] [数字分隔符][.精度][类型] }

exp : 支持 任意 python 表达式  (不支持 海象运算符)

"""

a = 3
b = 4

def sum(a, b):
    return a + b

print(f"{a:0>4} + {b:0>4} = { sum(a, b):.2f}")



