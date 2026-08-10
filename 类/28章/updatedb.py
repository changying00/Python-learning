import shelve

# 用同一文件名重新打开 shelf
db = shelve.open('persondb')
#打印当前数据库里面的 数据
for key in sorted(db):                  # 迭代以显示数据库中的对象
    print(key, '\t=>', db[key])         # 用自定义格式打印
sue = db['Sue Jones']                   # 1. 读：反序列化出一个 Person 实例
sue.giveRaise(.10)                      # 2. 改：内存中调用方法（pay *= 1.1）
db['Sue Jones'] = sue                   # 3. 写：重新序列化覆盖该键
db.close()                              # 关闭，改动落盘
# 做出修改后关闭
#上面运行完了重新写入数据库，由于sue.giveRaise 改变了， 并重新写入数据库 下面的代码打印新的数据
db = shelve.open("persondb")
rec = db['Sue Jones']
print(rec)
print(rec.lastName(),rec.pay)
