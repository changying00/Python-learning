"""
【数组&约瑟夫环】15个人围成一个圈进行报数、从1开始、如果报的数字是 7 或者 7的倍数则该人从队伍中移除，请问最后一个人是谁？
"""
# 定义一个列表、用来存储 15个人 
person_list = list(range(1, 16))

n = 0 
# 定义一个索引 、用来控制 人员 
index = 0 

# 使用 while 循环 模拟 报数 
while len(person_list) > 1:
    # 报数 
    n = n + 1 
    # 输出 谁 在报数、且数字是多少 
    print("编号为", person_list[index], "的人正在报数、数字为", n)
    # 判断 报的数字 是否 是 7 或者 7 的倍数 
    if n % 7 == 0:
        # 将 当前索引 对应的人 淘汰 、从 列表中 移除 
        code = person_list.pop(index) 
        print("编号为", code , "的人 被移除队伍")
    else:
        index += 1

    if index == len(person_list):
        # 如果 上述条件成立、说明 此时 是 最后一个人员报数 
        index = 0
 
print("剩下的人编号是:", person_list[0])


