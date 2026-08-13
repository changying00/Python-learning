"""
【随机模块】编写一个函数 generator_uuid() 生成一个随机的 uuid 格式的字符串
1.UUID格式为  xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx 的字符串、格式为 8-4-4-4-12
2. 整个字符由   0123456789abcdef  这16个字符组成
"""
# import uuid
# #定义一个函数
# def generator_uuid():
#     #把字符赋值给string
#     string = "0123456789abcdef"
#     #使用uuid1生成一个
#     x = uuid.uuid1()
#     #使用uuid3在进行重新加密
#     x1 = uuid.uuid3(x,string)
#     return x1
#
# if __name__ == '__main__':
#     print(generator_uuid())
# import uuid
# def generator_uuid():
#     # uuid4()：随机生成 UUID
#     x = uuid.uuid4()
#     # 转换成字符串
#     return str(x)
# if __name__ == '__main__':
#     print(generator_uuid())

import random
def generator_uuid():
    string = "0123456789abcdef"
    # UUID各部分长度：8-4-4-4-12
    lengths = [8, 4, 4, 4, 12]
    result = []
    for length in lengths:
        part = ""
        for _ in range(length):
            part += random.choice(string)
        result.append(part)
    return "-".join(result)

if __name__ == '__main__':
    print(generator_uuid())