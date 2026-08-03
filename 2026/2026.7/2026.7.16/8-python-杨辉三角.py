# 【二维列表】编写一段程序 、从键盘输入 n , 输出 n 行 杨辉三角
#
# 1
# 1   1
# 1   2	1
# 1   3	3    1
# 1   4	6    4	  1
# 1   5	10   10	  5   1
# .....
# 提示： 定义一个 长度 为 n 的 列表、 列表中 每一个元素仍旧是一个 列表。 观察 规律后，实现如上图内容的输出
# 输入杨辉三角行数
n = int(input("请输入多少行杨辉三角:"))
# 创建长度为n的二维列表
yanghui = [[] for _ in range(n)]
# 生成杨辉三角
for i in range(n):
    # 每一行第一个元素都是1
    yanghui[i].append(1)
    # 生成中间数字
    for j in range(1, i):
        # 当前数字 = 上一行左边数字 + 上一行右边数字
        yanghui[i].append(yanghui[i-1][j-1] + yanghui[i-1][j])
    # 每一行最后一个元素都是1
    if i > 0:
        yanghui[i].append(1)
# 输出杨辉三角
for row in yanghui:
    for num in row:
        print(num, end="\t")
    print()