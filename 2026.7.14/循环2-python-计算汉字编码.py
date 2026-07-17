#【循环】在 unicode 编码中，已知汉字的 起始码点值为 0x4e00,
# 结束码点值为 0x9fa5, 输出所有的汉字、并统计收录的汉字个数
#ord() 把字符 ==》编码  print(ord("中")) 输出 20013

#chr() 把编码 ==》字符  print(chr(0x4e2d)) 输出 中

#定义一个变量当计数器，
count = 0
#控制循环的次数
for i in range(0x4e00, 0x9fa6):
    # 把循环得到的i,转换成字符，打印出来
    print(chr(i), end=" ")
    # 计数器加1记录多少个
    count += 1

print()

print("汉字数量:", count)