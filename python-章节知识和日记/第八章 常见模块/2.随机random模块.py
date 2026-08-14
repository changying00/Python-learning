"""


"""
import random 


print(random.random()) 

# 随机 10 ~ 20 且不包含 N 的整数 
# int(random.random() * (20 - 10) + 10)

print(random.randrange(10, 20))

print(random.randint(10, 20))

ls = [1, 2, 3, 4]

print(random.choice(ls))

print(random.choices(ls, k=5))

print(random.sample(ls, k=4))

print(random.uniform(0.1, 0.2))

ls = {1, 2, 3, 4, 5}
random.shuffle(ls)

print(ls)