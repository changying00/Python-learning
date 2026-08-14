"""
随机数 

random.random() :  返回一个 随机的 [0, 1) 的随机小数 。

如何 实现 随机  [m, n) 区间的整数 

公式:  int(random.random() * (n - m) + m)


使用随机模块、将0 - 9 随机存入到长度为10的列表中、元素不允许重复

"""
import random 

# # 定义一个 变量、存储最终的 列表数据
# data = []

# # 使用  while 循环 
# while len(data) < 10:
#     # 生成一个 [0, 10) 区间的整数
#     n = int(random.random() * 10)
#     # 判断 n 是否是列表中的元素 
#     if n not in data:
#         # 如果 n 不再 data 中
#         data.append(n)
    
# # 循环结束、输出最终的结果
# print(data)

print("欢迎您进入猜拳小游戏")
name = input("请输入您的角色名\n")

handlers = {1: "石头", 2: "剪刀", 3: "布"}
# 定义 一个 赢的规则 
win_rules = [(1, 2), (2, 3), (3, 1)] 
# 定义 一个 变量、用来 控制 回合数 
play_count = 0

# 定义一个变量、存储本次游戏的 得分 
score_list = [0, 0] 

# 模拟 不断的猜拳
while True:
    # 随机产生 石头、剪刀、布 对应的 三个数字 
    random_number = int(random.random() * 3 + 1)
    # 引导 玩家 输入 手势
    play_number = int(input("请输入一个数字。 1 石头、 2 剪刀  3 布\n"))
    # 游戏 次数 + 1
    play_count += 1

    if random_number == play_number:
        print(f'本局您出的{handlers.get(play_number)}、机器出的{handlers.get(random_number)}、打平')

    elif (play_number, random_number) in win_rules:
        # 玩家赢了 、玩家比分 + 1
        score_list[0] += 1
        print(f'本局您出的{handlers.get(play_number)}、机器出的{handlers.get(random_number)}、您赢了、本次比分: {score_list}')
    else:
        # 机器赢了 、玩家比分 + 1
        score_list[1] += 1
        print(f'本局您出的{handlers.get(play_number)}、机器出的{handlers.get(random_number)}、机器赢了、本次比分: {score_list}')

    if 2 in score_list or play_count == 3:
        # 如果 猜拳 3次 或者 有人率先 达到 2分 、游戏 结束
        break

# 比较得分情况 
play_score, computer_score = score_list

if play_score > computer_score:
    print(f"{name}胜出")
elif play_score == computer_score:
    print("平局")
else:
    print("机器胜出")

