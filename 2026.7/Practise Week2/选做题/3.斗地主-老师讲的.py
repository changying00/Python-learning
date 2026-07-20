import  random

#定义一个变量、用来存储4种花色
colors = ("黑桃","红桃","梅花","方块")

#定义一个变量用来存储3~A
letters = ("3","4","5","6","7","8","9","10","J","Q","K","A","2")

kings = ("大王","小王")
#交叉组合 colors 和 Letters、构建 54张扑克牌
all_letters = [c + le for c in colors  for le in letters]  + list(kings)
#定义一个排序规则(处理大小王)
rules = letters + kings

#模拟洗牌
all_letters.sort(key= lambda d : random.random())
#定义 三个玩家
play_a ,play_b,play_c = [] ,[],[]

#模拟发牌
while len(all_letters)>3:
    play_a.append(all_letters.pop())
    play_b.append(all_letters.pop())
    play_c.append(all_letters.pop())
#模拟 对手牌 进行排序
print(sorted(play_a,key=lambda d: (rules.index(d), )if d in kings else (letters.index(d[2:]),colors.index(d[:2])) ))
print(sorted(play_b,key=lambda d: (rules.index(d), )if d in kings else (letters.index(d[2:]),colors.index(d[:2])) ))
print(sorted(play_c,key=lambda d: (rules.index(d), )if d in kings else (letters.index(d[2:]),colors.index(d[:2])) ))

print(all_letters)