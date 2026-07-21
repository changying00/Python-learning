"""
【函数】编写一个函数 is_lower_letter , 判断一个字符串是否是纯小写字母

"""
def is_lower_letter(s):
     for i in s:
         if not ("a" <= i <="z"):
            return False
     return True
print(is_lower_letter("abAlDADADAa"))
print(is_lower_letter("abc"))

# def is_lower_letter(s):
#     for i in s:
#         # 判断字符是否不在小写字母范围
#         if not ('a' <= i <= 'z'):
#             return False
#     return True
# print(is_lower_letter("abcxyz"))
# print(is_lower_letter("abAxyz"))