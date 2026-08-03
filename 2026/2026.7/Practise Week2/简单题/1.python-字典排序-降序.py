#字典】给定 students=[{'name':'Tom','score':80},{'name':'Jerry','score':90}]，
# 按分数从高到低排序后返回列表。
#定义字典
students=[{'name':'Tom','score':80},{'name':'Jerry','score':90}]
#reverse =True 把取到的score 反转排序，
students.sort(key=lambda x: x.get("score"), reverse=True)
print(students)