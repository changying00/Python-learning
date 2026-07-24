"""
【格式化】编写一个函数、支持格式化整数， 例如 1234567890，使用逗号分隔千位，结果为 1,234,567,890

"""
# 定义函数
def format_number(num):
    return f"{num:,}"

# 测试
print(format_number(1234567890))
print(format_number(100))
print(format_number(123456789012345))