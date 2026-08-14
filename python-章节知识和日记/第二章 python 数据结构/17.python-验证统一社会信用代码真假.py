"""


"""

# 定义一个 字符串、用来表示 某组织 对应的 社会信用代码 
code = "91410100349437002X"
# 定义加权因子 
W = [1, 3, 9, 27, 19, 26, 16, 17, 20, 29, 25, 13, 8, 24, 10, 30, 28]

# 定义一个列表 、用来存储 字符和 索引的映射关系 
diest_list = [str(x) for x in range(10)]
# 定义一个列表 、存储 21 个 字母 
letter_list = [chr(x) for x in range(65, 91) if chr(x) not in ['I', 'O', 'Z', 'S', 'V']] 
# 合并 上述 两个列表  [0, 1, ... 9, A,  ... Y]
symbol_list = diest_list + letter_list  

# 定义一个变量、用来存储前 17项 对应的 和 
S = 0 
for i in range(17):
    # 根据 字符 获取 该字符 在 列表中的索引值 
    ci = symbol_list.index(code[i])
    S += W[i] * ci 

# 计算 公式中的 C18 、它的取值范围是 1 ~ 31
c18 = 31 - S % 31 

# 将 c18 的取值范围更改位 0 ~ 30
if c18 == 31:
    c18 = 0

# c18 对应的数字 找到 它所对应的 字符 即 社会信用代码的最后一位 
last_code = symbol_list[c18]

if code[-1] == last_code:
    print(code, "是真的")
else:
    print(code, "是假的、它的最后一位应该是", last_code)


