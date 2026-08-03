#【闭包】使用闭包技术编写一个函数、能够让其每次调用 返回的结果 在上一次的结果上 + 1

# 使用闭包实现一个计数器：每次调用返回值都在上一次基础上 +1
def create_counter():
    """创建并返回一个计数器函数"""
    # 外层函数中的变量，用来保存计数状态
    count = 0
    #定义一个内层函数实现闭包
    def counter ():
        """每调用一次，计数值加 1 并返回"""
        # nonlocal 表示：这里使用并修改的是外层函数中的 count
        nonlocal count
        # 在上一次结果的基础上加 1
        count += 1
        # 返回最新的计数值
        return count
    # 返回内层函数，而不是调用它
    # 这样counter就携带着外层的 count 变量形成闭包
    return counter

# 创建一个计数器对象
counter_new = create_counter()

# 多次调用同一个闭包函数
print(counter_new())  # 第一次调用，输出 1
print(counter_new())  # 第二次调用，输出 2
print(counter_new())  # 第三次调用，输出 3
