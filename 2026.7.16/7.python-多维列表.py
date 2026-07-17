#【多维列表】现有1个元组、 格式为 ("name", "age" , "sex") ，
# 有 一个二维列表 [ ("张三", 20, "男" ), ("李四", 20, "女" ) ]
# 将 上述 二个格式的数据转换为 [ [("name", "张三" ) , ("age", 20), ("sex", "男") ] , [("name", "李四" ) , ("age", 20), ("sex", "女") ] ]
tup = ("name","age","sex")
ls_student = [("张三",20,"男"),("李四",20,"女")]
#定义一个空列表
array = []
#循环遍历ls_student，
for student in ls_student:
    #定义一个空列表temp
    temp = []
    #定义一个循环for 遍历
    for i in range(len(tup)):
        #把ls_student对应的元素和tup，组成一个元组在加到temp中
        temp.append((tup[i],student[i]))
    #最后再把列表temp加到array列表中
    array.append(temp)
print(array)