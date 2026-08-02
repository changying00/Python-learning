"""
【正则表达式】编写一个函数 email_secure(email) ，
实现对邮箱账号脱敏。 例如 huokundian@qikux.com
脱敏后 h********@qikux.com (星号数量固定即可)
要求： 完成邮箱校验后再脱敏（允许调用已写好的函数）

"""
import re


# 定义一个函数
def email_secure(email):
    """对邮箱进行脱敏"""
    # 编写正则匹配
    regex = r"([a-zA-Z0-9])[a-zA-Z0-9]+(@[a-zA-Z0-9]+\.com)"
    return re.sub(regex, r"\1*******\2", email)


if __name__ == '__main__':
    print(email_secure("huokundian@qikux.com"))
    print(email_secure("dgx2541104422@gamil.com"))
#导入re模块
