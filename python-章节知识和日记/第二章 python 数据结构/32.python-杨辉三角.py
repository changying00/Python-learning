"""
编写一段程序 、从键盘输入 n , 输出 n 行 杨辉三角
 
1
1   1
1   2	1
1   3	3    1
1   4	6    4	  1
1   5	10   10	  5   1


规则：

    1)  每一行 开始 和 结束 均为 1 

    2)  第 n 行 有 n 个数字

    3)  第 n 行 第 x 位置的数字 =  第 n - 1 行 第 x 位置的数字 +   第 n - 1 行 第 x - 1 位置的数字


杨辉三角 计算的是 11 的幂次方 、 第 n 行 代表 11**n 

"""
# 定义一个变量 n , 代表 输出的行数 
 
n = int(input("请输入一个正整数\n"))

# 构建 一个 代表 n 行 的 二维列表 、 且 每行的 列数 等于 行数 
data = [[1 for _ in range(x+1) ] for x in range(n)] 

# 从 第三行 遍历 data 准备 填充数据 
for y in range(2, len(data)):
    # 获取 当前 y 行 对应的列表 
    arr = data[y]
    # 遍历 arr 列表 、从 1 ~ length -1 进行填充 
    for x in range(1, len(arr) - 1):
        # 获取 要填充的数据 
        arr[x] = data[y-1][x] + data[y-1][x-1]


# 循环结束后、完成所有数据的填充 
for arr in data:
    for v in arr:
        print(v, end="\t")
    print()




