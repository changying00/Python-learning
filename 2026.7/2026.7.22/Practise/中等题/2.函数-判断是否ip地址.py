#【函数】编写一个函数 convert_ip_to_num(ipaddr) :
# 将一个 IP地址转换成一个数字（可以将一个 IPv4 地址看作是 256进制的数字）。
# 要求: 使用正则表达式验证 是否是 IP 地址，如果不是，直接返回 False
# import re
# #定义一个函数将ipv4,地址转成一个数字
# def convert_ip_t0_num(ipaddr):
#     """
#        将 IPv4 地址转换为一个整数
#        如果 IP 地址不合法，返回 False
#        """
#     # 正则表达式验证 IPv4 地址
#     pattern = r"^((25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)$"
#
#     # 如果不是合法 IP，直接返回 False
#     if not re.match(pattern,ipaddr):
#         return False
#     # 按 . 分割成四段
#     ip_list = ipaddr.split(".")
#     # 转换为整数
#     number = 0
#     for part in ip_list:
#         number = number * 256 + int(part)
#     return number
#
# # 测试
# print(convert_ip_t0_num("11.244.173.97"))   # 200584545
# print(convert_ip_t0_num("0.1.74.65"))       # 84545
# print(convert_ip_t0_num("300.1.1.1"))       # False
# print(convert_ip_t0_num("abc.def.1.1"))     # False

def convert_ipv4_to_number(ipaddr):
    array  = ipaddr.split(".")

    number = 0
    #遍历 列表
    for index,n in enumerate(array):
        number += int(n) * 255 ** (len(array)-index-1)
    return number

print(convert_ipv4_to_number("182.52.55.1"))