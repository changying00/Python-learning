"""
【函数】编写一个函数、用来校验是否是手机号，手机号规则：
1.  第一位必须是 1
2.  第二位可能是 3， 4， 5， 6， 7， 8， 9 中的任意一个
3.  长度必须是 11位
4.  必须是 纯数字组成
"""
def is_phone_number(num):
    #判断长度
    if len(num) != 11:
        return False
    #判断第一位是否为1
    if num[0] != "1":
        return False
    #判断第二位是否在指定范围内
    if num[1] not in "3456789":
        return False
    #判断是否全部为数字
    if not num.isdigit():
        return False
    #全部满足返回true
    return True
print(is_phone_number("23303701853"))
# #第二种
# def is_phone_number(phone):
#     return (
#         len(phone) == 11 and
#         phone.isdigit() and
#         phone[0] == "1" and
#         phone[1] in "3456789"
#     )
# print(is_phone_number("23303701853"))
