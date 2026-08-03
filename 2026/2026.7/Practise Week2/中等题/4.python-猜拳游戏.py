"""
中等题 【循环】使用 随机模块 ，编写一个 人机猜拳小游戏 ，效果如下格式！
欢迎进入猜拳小游戏
请输入您的名字、例如 小明
游戏开始、三局两胜
第1回合： 请输入一个数字 1 石头、 2 剪刀  3 布
本局您出的布、机器出的石头、您赢了、当前比分 1：0
第2回合：请输入一个数字 1 石头、 2 剪刀  3 布
本局您出的石头、机器出的剪刀、您赢了、当前比分 2：0
恭喜小明胜出
"""
import random
#定义一个变量存储玩家的分数
score_name =  0
#定义一个变量存储机器人的分数
score_robot = 0
# 定义一个字典dir1，记录对应的规则
dir1 = {1: "石头", 2: "剪刀", 3: "布"}
#  定义一个变量存储当前局数，首先为1
play_game = 1
print("欢迎进入猜拳游戏")
# 定义一个变量name存储玩家的姓名
name = input("请输入你的姓名:\n")
print("游戏的规则为三局俩胜利")
#也可以用True
while score_name < 2 and score_robot < 2:
    #定义一个变量，记录玩家输出的第一个数字
    num1 = int(input("第"+ str(play_game)  +"回合:请输入一个数字 1 石头、 2 剪刀  3 布:"))
    #产生一个随机数1，2，3赋值给num2
    num2 = random.randint(1, 3)
    if num1 == num2:
        print( "本局您出的",dir1[num1],"机器人出的",dir1[num2],"平局" )

    # (num1,num2) in [(1,2),(2,3),(3,1)]还能这样写！！！
    elif ((num1 == 1 and num2 ==2)or
          (num1 ==2 and num2 ==3) or
          (num1 == 3 and num2 ==1)):
        score_name +=1
        print("本局您出的",dir1[num1],"机器人出的",dir1[num2],"您赢了、当前比分",score_name,":",score_robot)
    else:
        score_robot += 1
        print("本局您出的", dir1[num1], "机器人出的", dir1[num2], "您输了、当前比分", score_name, ":", score_robot)
    play_game += 1
    if score_robot >=2:
        print("机器人胜出")
    # break while 后面用True可以加break
    elif score_name >= 2:
        print(name,"胜出")
    #break

