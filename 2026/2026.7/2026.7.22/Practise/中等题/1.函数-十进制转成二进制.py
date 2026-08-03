#【函数】编写一个函数 convert_num_to_ip(number) 实现将一个数字转换成 IPv4。
#定义一个函数、将一个数字转成IPv4
def convert_num_t0_ip(number):
    """
    将一个整数转换为 IPv4 地址字符串
    例如：200584545 -> "11.244.173.97"
    """
    # 取出最低 8 位，作为 IPv4 的第 4 段
    ip4 = number & 0xff
    # 右移 8 位，去掉已经取出的部分
    number >>= 8
    # 取出新的最低 8 位，作为 IPv4 的第 3 段
    ip3 = number & 0xff
    number>>= 8
    # 取出 IPv4 的第 2 段
    ip2 = number & 0xff
    number >>= 8
    # 取出 IPv4 的第 1 段
    ip1 = number & 0xff
    #将获取的四段ip字符串拼接，赋值给ip_addr
    ip_addr = str(ip1) + "." + str(ip2) + "." + str(ip3) + "." + str(ip4)
    #返回ip_addr的值
    return ip_addr
#测试
print(convert_num_t0_ip(200584545)) #11.244.173.97
print(convert_num_t0_ip(84545))#0.1.74.65
print(convert_num_t0_ip(121200584545))#56.30.39.97