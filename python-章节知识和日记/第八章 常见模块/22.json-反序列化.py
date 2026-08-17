"""
JSON 反序列化:  将 JSON 格式的 字符串 转成 python 中的 字典/列表 等对象

    反序列化 默认规则:  {} 转成字典 、 [] 转成 列表


json.loads(string, * , object_hook) :

    {} 默认转成字典 、可以通过 object_hook 将 {} 转成 指定的 对象 、例如 Person


    object_hook: 它的值是一个 功能型函数 、消费 一个 字典对象、返回一个 指定的对象


"""
import json
from datetime import datetime


class Person:

    def __init__(self, *, name=None, age=None, gender=None, createAt=None, isSington=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.createAt = createAt
        self.isSington = isSington


    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"


strings = """
{
   "name": "张三", 
   "age": 20,
   "gender": "男",
   "createAt": "2026-10-10 20:10:12",
   "isSington": true
}
"""

# 使用 json 反序列化技术 实现 转成字典
data = json.loads(strings)

print(data, type(data))

string2 = """
[
    {
        "name": "张三", 
        "age": 20,
        "gender": "男",
        "createAt": "2026-10-10 20:10:12",
        "isSington": true
    },

    {
        "name": "李四", 
        "age": 20,
        "gender": "男",
        "createAt": "2026-10-10 20:10:12",
        "isSington": true
    }
]

"""

def convetor_person(dct):
    # 获取 dct 中的  createAt
    createAt = dct.pop("createAt")
    # 进行日期的反格式化
    createTime = datetime.strptime(createAt, "%Y-%m-%d %H:%M:%S")

    dct["createAt"] = createTime
    return Person(**dct)


# 将 上述 数据转成一个列表、且 列表中的数据 为 person 对象
data = json.loads(string2, object_hook=convetor_person)

print(data)

