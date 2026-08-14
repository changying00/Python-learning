"""
UUID :  由 16进制 组成的 长度为 32位、外加 四个 - 组成 的 唯一不重复的 字符串 ~~~

格式为  8-4-4-4-12 

"""
import uuid

print(str(uuid.uuid1()),  uuid.uuid1().hex)

print(uuid.uuid3(uuid.uuid1(), "qiku"))

print(uuid.uuid4(),  uuid.uuid4().hex)

print(uuid.uuid5(uuid.uuid4(), "qiku"))