"""

"""
from logging import lastResort

# #定义一个c_cord变量，列表储存i所对应的Ci
# c_cord = [9,1,3,5,0,1,0,0,21,0,0,0,1,0,0,30,4]
# #定义一个变量接收和
# sum_cord = 0
# #定义一个w_cord变量，列表储存i所对应的Wi
# w_cord = [1,3,9,27,19,26,16,17,20,29,25,13,8,24,10,30,28]
# #定义一个变量cord_last 接收算出来的最后校验码
# cord_last = 0
# for i in range(17):
#     sum_cord += c_cord[i] * w_cord[i]
#     #计算余数
# cot = sum_cord % 31
#     #最终的校验码cord_last
# cord_last = 31 -cot
# if cord_last != c_cord[16]:
#     print("同一社会信用代码格式不正确")
# else:
#      print("同一社会信用代码格式正确")
# print(sum_cord)

#
# # 社会信用代码
# c_cord = "91350100M000100Y4Z"
# # 字母对应数字
# zi = {
#     "A":10, "B":11, "C":12, "D":13,
#     "E":14, "F":15, "G":16, "H":17,
#     "J":18, "K":19, "L":20, "M":21,
#     "N":22, "P":23, "Q":24, "R":25,
#     "T":26, "U":27, "W":28,
#     "X":29, "Y":30
# }
# # 权重 Wi
# w_cord = [
#     1,3,9,27,19,26,16,17,
#     20,29,25,13,8,24,10,30,28
# ]
# # 保存总和
# sum_cord = 0
# # 计算前17位
# for i in range(17):
#     # 当前字符
#     c = c_cord[i]
#     # 如果是数字
#     if c.isdigit():
#         ci = int(c)
#     # 如果是字母
#     else:
#         ci = zi[c]
#     # Ci * Wi
#     sum_cord += ci * w_cord[i]
# # 计算校验码
# cot = sum_cord % 31
# cord_last = 31 - cot
# # 如果结果为31，校验码为0
# if cord_last == 31:
#     cord_last = 0
# # 反向字典
# zi_reverse = {
#     value:key for key,value in zi.items()
# }
#
# # 得到校验字符
# check = zi_reverse.get(cord_last, str(cord_last))
#
# # 比较
# if check == c_cord[17]:
#     print("统一社会信用代码格式正确")
# else:
#     print("统一社会信用代码格式不正确")

#老师方法
#定义一个变量，存储社会信用代码
code = "914101003494370024"
#定义加权因子
w =[1,3,9,27,19,26,16,17,20,29,25,13,8,24,10,30,28]
# 定义一个列表、用来存储 字符 和索引的映射关系
diest_list = [str(x) for x in range(10)]
#定义一个列表、存储21个字母
letter_list = [chr(x) for x in range(65,91) if chr(x) not in ["I","O","Z","S","V"]]
#合并 上述俩个列表[0,1,2....9,A,.....Y]
symbol_list = diest_list+ letter_list

# 定义一个变量、用来存储前17项对应的和
S = 0
for i in range(17):
    #根据 字符 获取 该字符 在 列表中的索引值
    ci = symbol_list.index(code[i])
    S += w[i] * ci
# 计算 公式中的 c18、 它的取值范围是1~31
    c18 = 31 - S % 31
# 将c18 的取值范围更改为 0~30
    if c18 == 31:
        c18 = 0.
# c18 对应的数字 找到 它所对应的字符 即社会信用代码的最后一位
last_code = symbol_list[c18]
if code[-1] ==last_code:
    print(code,"是真的")
else:
    print(code,"是假的，它的最后一位应该是",last_code)
