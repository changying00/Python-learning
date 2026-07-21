"""
 编写一段程序、获取密码的强度
(1)密码长度
①小于等于4个字符， 得分 5分
②5 ~ 7个字符、得分 10分
③大于 等于 8个字符、得分 25分
(2)字母
①没有字母 0 分
②全部为大写或小写字母 10分
③大小写混合 20分
(3)数字
①没有数字 0分
②3个数字以下 10分
③3个或3个以上数字得 20分
(4)符号
①没有符号 0分
②1个符号 10分
③大于 1个符号 25分
(5)奖励
①大小写字母、数字和符号  10分
②数字、字母、符号 5分
③字母 和 数字 2分
强度规则：
--> >= 90: 非常安全,      强度返回 A
--> >= 80: 安全（Secure） 强度为 B
--> >= 70: 非常强        强度为 C
--> >= 60: 强（Strong）   强度为 D
--> >= 50: 一般（Average）强度为E
--> >= 25: 弱（Weak）    强度为 F
--> >= 0: 非常弱          强度为 G
"""
#写一个判断密码安全的程度
def  password_strong(password):
    """
    :param password: 传入你要输入的密码
    :return: 返回强度值
    """
    #定义一个变量储存密码的分数
    score = 0
    #1.写第一个判断密码的长度，得分
    if len(password) <= 4:
        score += 5
    elif 5 <=len(password) <= 7:
        score += 10
    else:
        score += 25

        # 统计
        lower = 0
        upper = 0
        digit = 0
        symbol = 0

        for i in password:

            if i.islower():
                lower += 1

            elif i.isupper():
                upper += 1

            elif i.isdigit():
                digit += 1

            else:
                symbol += 1

        # 2.字母评分
        if lower == 0 and upper == 0:
            score += 0

        elif lower > 0 and upper > 0:
            score += 20

        else:
            score += 10

        # 3.数字评分
        if digit == 0:
            score += 0

        elif digit < 3:
            score += 10

        else:
            score += 20

        # 4.符号评分
        if symbol == 0:
            score += 0

        elif symbol == 1:
            score += 10

        else:
            score += 25

        # 5.奖励
        if lower > 0 and upper > 0 and digit > 0 and symbol > 0:
            score += 10

        elif (lower > 0 or upper > 0) and digit > 0 and symbol > 0:
            score += 5

        elif (lower > 0 or upper > 0) and digit > 0:
            score += 2

    if score >= 90:
        return "非常安全, A"
    elif score >=80:
        return "安全（Secure）B"
    elif score >= 70:
        return "非常强  C"
    elif score >= 60:
        return  "强（Strong）D"
    elif score >= 50:
        return  " 一般（Average）E"
    elif score >= 25:
        return  "弱（Weak）F"
    else :
        return "非常弱  G"

print(password_strong("88888"))