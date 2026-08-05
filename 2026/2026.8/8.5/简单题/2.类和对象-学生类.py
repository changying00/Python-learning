"""【类与对象】学生类：创建一个学生类，具有属性（例如姓名、年龄、学号等）和方法（例如打印学生信息）。"""

#定义学生类
class Student:
    #类对象的属性
    def __init__(self,name,age,student_id):
        self.name=name
        self.age=age
        self.student_id=student_id

    #定义一个打印信息的方法
    def print_Student(self):
        print(f"你的姓名{self.name}\n你的年龄为{self.age}\n你的学号为{self.student_id}")

if __name__=="__main__":
    #实例化对象
    student1=Student("dgx","22","230054470238")
    #调用方法
    student1.print_Student()