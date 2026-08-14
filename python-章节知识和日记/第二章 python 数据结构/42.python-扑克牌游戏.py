"""
斗地主的扑克牌游戏，相信许多人都会玩，本例要求编写一个斗地主的洗牌发牌程序，
要求按照斗地主的规则完成洗牌发牌的过程。一副扑克总共有54张牌，
牌面由花色和数字组成（包括J、Q、K、A字母）组成，花色有♠、♥、♦、♣ 四种，
分别表示黑桃、红桃、方块、梅花，小☺、大☻分别表示小王和大王。斗地主游戏共有三位玩家参与，
首先将这54张牌的顺序打乱每人轮流摸一次牌，剩余3张留作底牌，然后在控制台打印三位玩家的牌和三张底牌。
刘麟
"""
import random 


# 定义一个变量 、用来存储 4 种 花色
colors = ("♠", "♥", "♣", "♦")
# 定义一个变量 、用来存储 3 ~ A 
letters = ("3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "2")

kings = ("☺",  "☻")

# 交叉组合 colors 和 letters 、构建 54张 扑克牌 
all_letters = sorted([c + le for c in colors for le in letters], key=lambda d: (letters.index(d[1:]), colors.index(d[0]))) + list(kings) 

# 定义一个 排序规则 (主要处理 大小王)
rules = all_letters.copy()

# 模拟 洗牌 
all_letters.sort(key=lambda d: random.random()) 

# 定义 三个玩家 
play_a, play_b, play_c = [], [], []

# 模拟发牌
while len(all_letters) > 3:
    play_a.append(all_letters.pop(0))
    play_b.append(all_letters.pop(0))
    play_c.append(all_letters.pop(0))

# 模拟 对 手牌 进行排序 

print(sorted(play_a, key=lambda d: rules.index(d) ))
print(sorted(play_b, key=lambda d: rules.index(d) ))
print(sorted(play_c, key=lambda d: rules.index(d) ))

print(all_letters)