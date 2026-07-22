"""
闭包 ：是一种 特殊的 函数嵌套、外部函数 返回 内部函数的应用 对象


闭包的作用:
    1，闭包 可以 延长 非局部变量的 作用的范围


"""
#定义一个变量、用来存储唯一的标识
def generator_key():
    #定义一个 非局部变量
    identify = 0
    def  generator_unique_number():
        """生成唯一不重复的连续数字"""
        nonlocal identify
        identify += 1
        return identify
    return generator_unique_number
gen = generator_key()
print(gen())

print(gen())

#只要 gen 这个闭包对象还存在，identify 就会在上一次的基础上继续累加。
#它不是“永久”存在于整个 Python 世界中，而是存在于 gen 这个闭包对象的生命周期内。

"""

一句话总结：

闭包 = 函数 + 它记住的外部变量。

你的 gen 不只是一个函数，它还携带着一个“记忆”——identify 的当前值。每次调用 gen()，这个记忆都会被更新。
"""