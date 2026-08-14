"""
三元运算符: 是一个表达式 、会返回结果 

语法: 

exp1 if condition else exp2 

当 condition 表达式 的结果为 真的时候， 整个运算符 返回 exp1 表达式执行结果、 否则 返回 exp2 表达式执行结果

从键盘输入一个学生的成绩、  >=90 (优秀)  >=80 (良好),  >=70 (中等),  >= 60 (及格) 其它情况 不及格

"""

# 定义一个正数 
a = 24

# 输出该正数 是 奇数还是偶数
b = "奇数" if a & 1 else "偶数"

print(b)


# 定义一个变量、用来存储某个人的性别  m 代表 男、 f 代表 女 、s 代表 保密
gender = "x"

# 输出 该人的性别 
gender_text = "男" if gender == 'm' else "女" if gender == 'f' else "保密" if gender == 's' else "未知"

print(gender_text)



