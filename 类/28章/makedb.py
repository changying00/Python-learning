"""（把 Person 对象存进 shelve 数据库）"""
# from person_14 import Person,Manager
# bob = Person("Bob Smith")
# sue = Person("Sue Jones",job = "dev",pay  =100000)
# pat = Manager("Pat Jones",50000)
#
import shelve
# # 对象存储到的文件名
# db = shelve.open('persondb')
# # 用对象的 name 属性作键
# for obj in  (bob,sue,pat):
#     # 按键把对象存入 shelf
#     db[obj.name]=obj
#     # 做出修改后要关闭
# db.close()


import glob

# print(glob.glob("persondb*"))
# print(open('persondb.bak', 'rb').read())
# print(open('persondb.dat', 'rb').read())
# print(open('persondb.dir', 'rb').read())

db = shelve.open("persondb")  # 重新打开 shelf
print(len(db)) # 存了三个对象

print(list(db.keys()))  # keys 就是索引

pat = db['Pat Jones']# 按键取对象
print(pat.lastName()) # 运行来自 Person 的 lastName

print(pat)    # 运行来自 AttrDisplay 的 __repr__

for key in sorted(db):  # 迭代、排序、取、打印
    print(key, '=>', db[key])

