"""
写入 纯文本 内容  可以使用  wt ,  at 两个模式
    wt :  覆盖式写入 文本文件
    at :  追加式写入 文本文件
写入的时候， 文件 可以不存在 、会自动创建 、但是 它所在的目录必须存在
"""
# 定义一个文件路径 
file = "./test.txt"
# 创建一个 写入文件的 通道
f = open(file, "wt", encoding="utf-8")
# 向文件中写入 纯文本 
# f.write("hello world2!")
# f.write("\n")
# f.write("你好、中国2！")
str_lines = [
    "hello 中国",
    "hello 奇酷"
]
# 一次性将 字符串组成的可迭代对象中的文本内容 写入
f.writelines(str_lines)
# 关闭通道 
f.close()
