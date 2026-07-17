"""
【循环】编写一段程序、计算 5! + 4! + 3! + 2! + 1!
"""

sum1 = 0
for i in range(5, 0, -1):
    count = 1
    for j in range(i, 0, -1):
        count *= j
    sum1 += count
print(sum1)