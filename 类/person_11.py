from person import Person
pat = Person("Pat Jones")
print(pat)
print(pat.__class__)   # 指向类对象的链接
#<class 'person.Person'>

print(pat.__class__.__name__)
#Person 显示类名

print(pat.__dict__)
#{'name': 'Pat Jones', 'job': None, 'pay': 0}

print(pat.__dict__.keys())
# 属性就是字典的键 dict_keys(['name', 'job', 'pay'])
for key in pat.__dict__:# 遍历属性字典
        print(key, '=>', pat.__dict__[key])   # 手动索引：不做继承查找


for key in pat.__dict__:    # obj.attr 的等价写法，但 attr 是字符串
        print(key, '=>', getattr(pat, key))   # 会执行属性继承
print(Person.__name__)
print(dir(pat))
print(list(pat.__dict__))