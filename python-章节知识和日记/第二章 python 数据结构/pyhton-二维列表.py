# 定义 一个二维列表 3*4的列表
ls = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

#编写一段 代码 将 3 * 4 二维列表 转成 4 * 3的二维列表
#定义一个 4* 3 的二维列表

array = [[0 for _ in range(3)]for _ in range(4)]

#遍历 原 二维列表
for y in range(len(ls)):
    # 获取 y 位置的元素
    arr = ls[y]
    # 遍历 arr 列表
    for x in range(len(arr)):
        #交换坐标
        array[x][y] = ls[y][x]

# 将二维 列表中的数据 安装 3* 4 的方式 输出到控制台上
# 外层 循环 控制 负责输出的行数

for arr in  array:
    # 内层循环 控制输出的列数
    for v in arr:
        # 输出 具体的内容
        print(v,end="\t")
    # 外层循环 负责换行
    print()