import random
# 创建牌
colors = ["黑桃", "红桃", "方块", "梅花"]
numbers = [
    "A","2","3","4","5",
    "6","7","8","9","10",
    "J","Q","K"
]
cards = []
# 普通牌52张
for num in numbers:
    for color in colors:
        cards.append(color + num)
# 加入大小王
cards.append("小王")
cards.append("大王")
print(cards)
# 洗牌
random.shuffle(cards)
# 发牌
player1 = cards[0::3][:17]
player2 = cards[1::3][:17]
player3 = cards[2::3][:17]
# 底牌 cards[0::3] 取玩家1所有牌： [:17] 只拿前17张：
bottom_cards = cards[51:]
print("玩家1:")
print(player1)
print("\n玩家2:")
print(player2)
print("\n玩家3:")
print(player3)
print("\n底牌:")
print(bottom_cards)


list()
dict()
set()
tuple()