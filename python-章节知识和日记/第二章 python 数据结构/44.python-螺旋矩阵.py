"""
【数组&方法】螺旋矩阵：给定一个整数n，生成一个n×n的螺旋矩阵，螺旋顺序从外到内逐层递增。 
例如，当n=3时，生成的螺旋矩阵为：
1 2 3
8 9 4
7 6 5

"""
# 定义一个变量，存储一个整数 n 
n = int(input("请输入一个正整数"))

# 定义 两个变量、分别存储 x, y 坐标 
x = y = 0 

# 定义 一个 变量、 用来 控制 填充数据的方向 

direction = 1

# 定义一个 n * n 的 二维列表 
data = [[0 for _ in range(n)] for _ in range(n)]

# 从 1 ~ n ** 2 遍历 数字、准备 填充数据 
for k in range(1, n ** 2 + 1):
    # 向 x, y 坐标的位置上 填充数据 
    data[y][x] = k 
    # 判断 即将 要填充的数据 位置 是否合适 
    if direction == 1 and x + 1 < n and data[y][x+1] == 0:
        x = x + 1
    elif direction == 1:
        # 将 填充方向设置为向下 
        direction = 2
        # 将 y 自增 1
        y = y + 1
    elif direction == 2 and y + 1 < n and data[y+1][x] == 0:
        y = y + 1
    elif direction == 2:
        direction = 3
        # 将 x 自减 1
        x = x - 1
    elif direction == 3 and x - 1 >= 0 and data[y][x-1] == 0:
        x = x - 1
    elif direction == 3:
        direction = 4
        y = y - 1
    elif data[y-1][x] == 0:
        y = y - 1
    else:
        direction = 1
        x = x + 1

# 输出 螺旋矩阵 
for arr in data:
    for v in arr:
        print(v, end="\t")
    print("")
