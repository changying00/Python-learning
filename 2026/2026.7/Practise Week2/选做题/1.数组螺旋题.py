# 【数组&方法】螺旋矩阵：给定一个整数n，生成一个n×n的螺旋矩阵，螺旋顺序从外到内逐层递增。 例如，当n=3时，生成的螺旋矩阵为：
# 1 2 3   1  2  3  4
# 8 9 4   12 13 14 5
# 7 6 5   11 16 15 6
#         10 9  8  7
# 输入矩阵大小
# n = int(input("请输入n，生成n*n螺旋矩阵:"))
# # 创建 n*n 的二维列表
# matrix = [
#     [0] * n
#     for _ in range(n)
# ]
# # 定义四个边界
# top = 0          # 上边界
# bottom = n - 1   # 下边界
# left = 0         # 左边界
# right = n - 1    # 右边界
# # 当前填入的数字
# num = 1
# # 当还有区域没有填充时继续
# while top <= bottom and left <= right:
#     # =====================
#     # 第一步：从左往右填充
#     # =====================
#     for i in range(left, right + 1):
#         matrix[top][i] = num
#         num += 1
#     # 第一行已经填完
#     top += 1
#     # =====================
#     # 第二步：从上往下填充
#     # =====================
#     for i in range(top, bottom + 1):
#
#         matrix[i][right] = num
#         num += 1
#     # 最右边已经填完
#     right -= 1
#     # =====================
#     # 第三步：从右往左填充
#     # =====================
#     for i in range(right, left - 1, -1):
#
#         matrix[bottom][i] = num
#         num += 1
#     # 最下面已经填完
#     bottom -= 1
#     # =====================
#     # 第四步：从下往上填充
#     # =====================
#     for i in range(bottom, top - 1, -1):
#         matrix[i][left] = num
#         num += 1
#     # 最左边已经填完
#     left += 1
# # 输出矩阵
# for row in matrix:
#     print(row)
n = int(input("请你输入一个n的数字:"))
direction = 1
#定义一个 n * n的二维列表
data = [ [ 0 for _ in  range(n)]for _ in range(n)]
x , y = 0, 0
#从1 ~ n * n的二维列表
for k in range(1,n * n + 1):
    # 向 x，y坐标的位置上 填充数据
    data[y][x] = k
    #判断 即将 要填充的数据位置 是否合适
    if direction == 1 and x + 1 < n and data[y][x+1] == 0:
        x = x + 1
    elif direction == 1:
        #将 填充方向设置为向下
        direction = 2
        #将 y 自增1
        y = y + 1
    elif direction == 2 and y + 1 < n and data[y+1][x] == 0:
        y = y + 1
    elif direction == 2:
        direction = 3
        #将 x 自减1
        x = x -1
    elif direction == 3 and x -1 >= 0 and data[y][x-1] == 0:
        x = x - 1
    elif direction == 3:
        direction = 4
        y = y -1
    elif  data[y-1][x] == 0:
        y = y -1
    else:
        direction = 1
        x = x + 1
for arr in data:
    for v in arr:
        print(v, end="\t")
    print()

