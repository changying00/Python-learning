"""

【循环题】假如将俄罗斯方块的每一个图形 看作一个数字。要求在控制台上将指定的图形打印出来， 图形用 * 符号输出即可

"""

num = int(input("请输入图形编号(1~7)："))

if num == 1:
    # I 型
    for i in range(4):
        print("*", end="")
    print()

elif num == 2:
    # 竖着的 I 型
    for i in range(4):
        print("*")

elif num == 3:
    # O 型
    for i in range(2):
        for j in range(2):
            print("*", end="")
        print()

elif num == 4:
    # L 型
    for i in range(3):
        print("*")
    print("**")

elif num == 5:
    # T 型
    print("***")
    print(" * ")

elif num == 6:
    # Z 型
    print("** ")
    print(" **")

elif num == 7:
    # S 型
    print(" **")
    print("** ")

else:
    print("输入错误！")