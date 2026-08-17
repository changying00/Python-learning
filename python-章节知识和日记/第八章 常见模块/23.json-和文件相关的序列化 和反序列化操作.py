"""
json.dumps(obj):将python 对象 序列化成json 字符串
json.loads(string): 将json字符串 反序列化python 对象

json.dump(obj,fp): 将序列化的数据 写入到指定的文件fp中
json.load(fp):从json文件中读取数据 并反序列化为 python对象
"""
import json
dct = {
    "name":"张三",
    "age":22,
    "birth":"2004/06/19"
}
with open("./dct.json","w",encoding="utf-8") as f:
    json.dump(dct,f,ensure_ascii=False,indent=4)

with open("./dct.json","rt",encoding="utf-8") as f:
    instance = json.load(f)

print(instance,instance["name"])