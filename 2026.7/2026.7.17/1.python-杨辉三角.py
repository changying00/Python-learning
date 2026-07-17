"""
规则:
  1) 每一行 开始和结束 均为1
  2) 第n 行 有 n 个数字
  3) 第 n行 第 x 位置的数字 = 第n -1 行 第x 位置的数字 + 第 n -1行 第 x -1位置的数字
"""
# 定义一个变量n,代表 输出的行数

n = int(input("请输入一个正整数\n"))

# 构建一个代表 n 行的二维列表、 且每行的 列数等于行数
data  = [[1 for _ in range(x + 1)] for x in range(n)]

#从 第三行 开始遍历 data 准备填充数据
for y in range(2,len(data)):
    #获取当前 y行 对应的列表
    arr = data[y]
    #遍历 arr 列表、从 1~ Length -1 进行填充
    for x in range(1,len(arr) -1):
        #获取要填充的数据
        arr[x] = data[y-1][x] + data[y-1][x-1]
#循环结束后、完成所有数据的填充

for arr in data:
    for v in arr:
        print(v,end="\t")
    print()