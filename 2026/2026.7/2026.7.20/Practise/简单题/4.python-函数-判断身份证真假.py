"""
【函数】 编写一个函数、用来校验身份证的真假、并返回对应的性别
"""
def check_id_card(id_card):
    # 权重
    wi = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    # 校验码
    check = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    # 判断长度
    if len(id_card) != 18:
        return "身份证长度错误"

    # 加权求和
    s = 0
    for i in range(17):
        Ai = int(id_card[i])  # 取身份证第i位
        s += Ai * wi[i]  # 累加

    # 求余数
    y = s % 11
    # 根据余数获取正确校验码
    code = check[y]
    if code != id_card[17]:
        return "身份证不合法"
    if int(id_card[16]) & 1 != 0 :
        gender = "男生"
    else:
        gender = "女生"
    return "身份证合法,性别为",gender
print(check_id_card("411426200406191230"))