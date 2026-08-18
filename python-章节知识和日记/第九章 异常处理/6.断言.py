"""
断言 assert : 

语法 :
    assert exp, message 
        断言 exp 表达式 是 True, 如果 断言失败、则 抛出一个 AssertError , 且 失败原因是 message

"""
a = 10.2

# 判断 a 是否是整数 、如果 不是 、则抛出错误 
# if type(a) != int:
#     raise Exception(f"{a} 不是整数")

assert type(a) == int , f"{a} 不是整数"