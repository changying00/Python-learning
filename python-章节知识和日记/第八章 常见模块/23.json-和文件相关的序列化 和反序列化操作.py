"""
json.dumps(obj):将python 对象 序列化成json 字符串
json.loads(string): 将json字符串 反序列化python 对象

json.dump(obj,fp): 将序列化的数据 写入到指定的文件fp中
json.load(fp):从json文件中读取数据 并反序列化为 python对象
"""
import json

# 用法 和 dumps 相同， 区别是 将 序列化后的 结果 存储到 指定的 文件中

# dct = {
#     "name": "张三",
#     "age": 20
# }

# with open("./dct.txt", "wt", encoding="utf-8") as f:
#     json.dump(dct, f, ensure_ascii=False, indent=4)

with open("./dct.txt", "rt", encoding="utf-8") as f:
    # 从 json 文件中 读取数据
    d = json.load(f)

print(d, d["name"])