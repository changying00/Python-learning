"""
中等题【循环】从键盘输入任意一个整数、将它 和 它的 倒序数字 进行 相加、如果是 回文数、则输出该回文数、否则 继续 重复的操作、直到产生回文数 为止。
回文数:  一个数字 正读 和 倒读 一样、 例如  171 、 2552 等 数字 。
例如 从键盘输入 一个 271

271 + 172 = 443
443 + 344 = 777

777 是一个回文数、输出该数字结束即可！！！
如果 输入的数字 是 196， 会发生什么？？？
"""

# 从键盘输入任意一个正整数 
number = _number = int(input("请输入任意一个正整数"))

while True: 
    # 判断 number 是否是一个回文数 
    # 定义一个变量、用来存储反转后的数字 
    reverse_number = 0
    # 使用 while 循环 计算 这个数字 倒序
    while _number > 0:
        # 获取 _number 的个位数 
        x = _number % 10 
        # 将 得到的数字 和 reverse_number 进行合并 
        reverse_number = reverse_number * 10 + x 
        # 将 _number 缩小 10 倍
        _number //= 10

    # 将 反转后的 数字 和 原数字进行比较 、如果相同，则说明该数字是回文数 
    if number == reverse_number:
        print(number)
        break 
        
    # 如果 上述条件不成立、则将 原数字和 倒序数字 做加法运算、并将结果 赋值给 number 和 _number
    number = _number = number + reverse_number 
