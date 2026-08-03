# 输入数字1，添加学生信息（id，名字，年纪，性别）
# 第一个学生id为101 后续学生自动加1
# 输入数字2，查看所有学生信息
# 输入数字3，统计学生平均年纪
# 输入数字4，统计学生性别比例
# 输入数字5，退出系统


#定义一个循环，使得程序循环进行弹出输入框
students = []
id1 = 101
while True :
    num = int(input("*" * 100 +"\n"
                    "输入数字1，添加学生信息（id，名字，年纪，性别）\n"
                    "输入数字2，查看所有学生信息\n"
                    "输入数字3，统计学生平均年纪\n"
                    "输入数字4，统计学生性别比例\n"
                    "输入数字5，退出系统\n"
                    + "*" * 100 +"\n请输入数字:" ))
    if num == 1 :
        print("请你输入要添加学生信息(id,名字，年纪，性别)")
        name = input("名字:")
        #int类型强转
        age = int(input("年纪:"))
        gender = input("性别:")
        student ={
            "id":id1,
            "姓名":name,
            "年龄":age,
            "性别":gender
        }
        students.append(student)
        id1 += 1
        print("添加成功")
    elif num == 2:
        if len(students) == 0:
            print("暂无学生")

        else:
            for student in students:
                print(
                    f"编号:{student['id']} "
                    f"姓名:{student['姓名']} "
                    f"年龄:{student['年龄']} "
                    f"性别:{student['性别']}"
                    + "\n"
                )
    elif num ==3:
        if len(students) == 0:
            print("暂无学生")
        else:
            total_age = 0
            for student in students:
                total_age += int(student["年龄"])
            avg = total_age / len(students)
            print("平均年龄:", avg,"\n")
    elif num ==4:
        if len(students) == 0:
            print("暂无学生")

        else:

            male = sum(
                1 for student in students
                if student["性别"] == "男"
            )

            female = sum(
                1 for student in students
                if student["性别"] == "女"
            )

            print("男生:", male)
            print("女生:", female)

            print("男生比例:", male / len(students) * 100,"%","\n")
            print("女生比例:", female / len(students)* 100,"%","\n")
    elif num == 5:
        break