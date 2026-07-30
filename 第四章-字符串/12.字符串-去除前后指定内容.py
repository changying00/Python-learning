"""
去除 字符串 前后 指定字符默认空格

    strip(chars=""): 去除 字符串前后的指定 字符、默认为空格

    lstrip(chars=""):去除 字符串前 满足条件 字符、默认为空格

    rstrip(chars=""):去除 字符串后 满足条件 字符、默认为空格

    removeprefix(prefix):移除 字符串 指定的 前缀
    removesuffix(suffix):移除 字符串 指定的 后缀
"""
string  = "1111hello00000"
print(string.strip("10"))
print(string.lstrip("1"))
print(string.rstrip("0"))
string=  "xyzxhellozykzxyz"
print(string.strip('xyz'))
print(string.removeprefix('xyz'))
print(string.removesuffix('xyz'))