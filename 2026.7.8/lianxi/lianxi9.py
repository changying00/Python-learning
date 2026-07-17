"""【运算符】假如用一个数字 代表 某一个用户 
指定月份的签到情况 (二进制的 每一位代表 
每一天的是否签到 1代表已签到、 0 代表未签到) 、
请输入2个数字 一个代表 每一天的签到情况、
另一个代表 几号 、例如 34546 和 3 ，
 编写程序 计算 3号是否签到 ~~~
 
 data = int(input("输入一个数字(代表某月每一天的签到情况):"))
data1 = int(input("输入一个数字(代表某月几号):"))
#把每一天的签到情况数字，转为2进制
data_er = int(bin(data))

#输入一个数字(代表几号)，转为2进制
data_er1 = 2 ** (data_er1 -1)

if data_er & data_er1 > 0:
     print(data1,"号已签到",sep= "")
else:
     print(data1,"号没有签到",sep = "")"
 
 """
#输入一个数字(代表某月每一天的签到情况）
data = int(input("输入一个数字(代表某月每一天的签到情况):"))、
#输入一个数字(代表某月几号)
day = int(input("输入一个数字(代表某月几号):"))

#打印一下data
print(bin(data))

#把日期由2进制转换成十进制数
mask = 2 ** (day - 1)

#打印一下mask
print(bin(mask))

#把日期和以前的每月签到情况进行与运算，
if (data & mask) > 0:
    print(day, "号已签到", sep="")
else:
    print(day, "号没有签到", sep="")
    