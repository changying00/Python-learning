count  =  int(input("请你输入你的成绩:"))
#  A 代表优秀   B 代表良好  C代表中等 D 代表及格 E 代表不及格

count_fen = "你的分数不对范围为(0-100)" if count >= 100 else "优秀" if count >= 90 else "良好" if count >= 80  else "中等" if count >=70  else "及格" if count >=60  else "不及格" if 0 < count < 60 else "超出分数范围了" 

print(count_fen)





"""

count = int(input("请输入你的成绩："))

count_fen = (
    "超出分数范围了" if count < 0 or count > 100 else
    "优秀" if count >= 90 else
    "良好" if count >= 80 else
    "中等" if count >= 70 else
    "及格" if count >= 60 else
    "不及格"
)

print(count_fen)



"""