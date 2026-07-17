"""a  = 6 
b  = 13
print(a ^ b) 


x  = "我"

key =2026

y = chr(ord(x)^ key)

z = chr(ord(y)^key)


ls = []

n = 0

for x in ls:
     n  = n ^ x
print(n)

a = 18523
b = a & 255
a << 8

a = 16 
b = a & 1

"""


#定义一个数字
number = 3456754635
print(bin(number))
#可以将 IP 地址看作一个 256进制的数字
ip4 = number & 0xff
#将 number 右移8位
number = number >> 8  # ==>  number >>= 8
#获取ip3
ip3 = number & 0xff
#将 number 右移8位
number = number >> 8
#获取ip2
ip2 = number & 0xff
#将 number 右移8位
number = number >> 8
#获取ip1
ip1 = number & 0xff

# 获取 IP地址
ip_addr = str(ip1)+"."+str(ip2)+"."+str(ip3)+"."+str(ip4)

print(ip_addr)