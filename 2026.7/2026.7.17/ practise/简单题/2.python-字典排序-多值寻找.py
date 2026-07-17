#【字典】给定学生列表 students=[{'name':'Tom','score':80},{'name':'Jerry','score':90}]，
# 找出分数最高的学生姓名。

students=[{'name':'Tom','score':80},{'name':'Jerry','score':90}]

students.sort(key=lambda x:x.get('score'),reverse =True)

print(students[0]["name"])