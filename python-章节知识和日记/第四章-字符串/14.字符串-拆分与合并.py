"""
拆分 和 合并 相关的方法
    split(sep,   maxsplit=-1)  :  将 字符串 按照 指定的 分割符 sep (默认是 空白符)  进行拆分,支持设置 拆分的次数、  返回一个 字符串列表、
    默认 分隔符是 空白字符 、空白字符包含空格、制表符换行符等
    rsplit(sep ,  maxsplit=-1)  :  将 字符串 按照 指定的 分割符 sep (默认是 空白符)  从 右向左 进行拆分
    splitlines(keepends=False) :  按照换行符 进行字符串拆分 、keepends 用来设置是否保留换行符 。且支持 是否换行符
    join(iterable[str])  :  将一个可迭代对象中的数据(数据的类型必须是 字符串) 按照 指定的 字符 进行 合并 返回一个字符串
"""
string = "DGX SHI S S"
print(string.split())
print("\n")

string = "123.212.3.1.2"
print(string.split("."))
a = (string.split("."))
print("".join(a))
print("\n")

ls = [1,2,23,4,56,4,33]
print("".join([str(x) for x in ls]))
print(":".join([str(x) for x in ls]))
print("\n")

string = "hello\nworld\nqiku"
print(string.split("\n"))
print(string.splitlines(keepends=False))
