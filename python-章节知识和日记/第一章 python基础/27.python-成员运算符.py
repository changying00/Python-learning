"""

    1. 算术运算符 :  +, -, *, / , // , %, **
    
    2. 位运算符 :  &,  | ,  ~ ,  ^
    
    3. 位移运算符 :  <<,   >>
    
    4. 赋值运算符 :  =, +=, -=, ...
    
    5. 海象运算符 :  :=
    
    6. 关系运算符 :  >,  >=,  <,  <=,  ==,  !=
    
    7. 逻辑运算符 :  and,  or,  not 
    
    8. 三元运算符 :  exp1 if condition else exp2
    
    9. 身份运算符 :  is (是),  is not (不是)
    
    10.成员运算符 :  in (在 ... 里面)  、 not in (不在 ... 里面)
         
    
成员运算符 主要应用在 可迭代对象中、常见的可迭代对象包含 字符串、列表、元组、集合 和 字典 

成员运算符 返回一个 bool 类型的结果 

"""

# 定义一个字符串 
string = "hello world!"

# 判断 el 字符串 是否在 string 中
print("el" in string)
# 判断 eo 字符串 是否在 string 中 
print("eo" in string)

# 定义一个列表 
ls = [34, 76, 23, 8, 9]

# 判断 7 在不在 列表中 
print(7 in ls)
# 判断 23 是不是列表中的成员
print(23 in ls)

# 定义一个元组 
tp = ("hello", "world", "qiku")

# 判断 el 是否是元组的成员 
print("el" in tp)
print("qiku" in tp)


# 定义一个集合 
sets = {"hello", "world", "qiku"}
# 判断 el 是不是 集合的成员
print("el" in sets)
print("qiku" in sets)

# 定义一个字典、 每一个值有 2部分组成 、这两部分分别称为  键 和 值 
dct = {"name": "张三" , "age": 20,  "gender": "男"}

# 判断 张三 在不在 字典中 (在 字典中 使用 in 成员运算符、只能 判断 键是否存在 )
print("张三" in dct)

# 判断 gender 是否是字典中成员 
print("gender" in dct)





