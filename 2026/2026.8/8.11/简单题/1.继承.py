"""
【继承】假设你有一个基类 Person，表示人的基本信息，比如姓名和年龄。
现在，你想创建两个子类 Student 和 Teacher。
Student 类应该包含额外的属性：学校和学生ID，并且可以有一个方法 study 用于表示学习的行为。
Teacher 类应该包含额外的属性：学科和工资，并且可以有一个方法 teach 用于表示教学的行为。
你需要创建这些类并测试它们。
"""
#创建基类Person
class Person:
    #通过__init__初始化属性
    def __init__(self, name,age):
        self.name = name
        self.age = age

#创建子类 Student继承Student
class Student(Person):
    #在初始化补充新的属性
    def __init__(self,name,age,school,student_id):
        super().__init__(name,age)
        self.school = school
        self.student_id = student_id
    #定义一个方法study 用于表示学校习的行为
    def study(self):
        return f"名字为:{self.name},年龄为:{self.age},学号为:{self.student_id}的学生，在{self.school}学习"

#创建子类 Teacher继承Person
class Teacher(Person):
    #初始化当前子类的属性
    def __init__(self,name,age,subject,salary):
        super().__init__(name,age)
        self.subject = subject
        self.salary = salary

    #定义方法 teach
    def teach(self):
        return (
            f"名字为:{self.name}，"
            f"工资为:{self.salary}，"
            f"正在教授{self.subject}"
        )
    def __str__(self):
        return f'Teacher[{self.name},{self.age},{self.subject},{self.salary}]'
#测试
if __name__ == '__main__':
    student1= Student("DGX",22,"郑州商学院",230054470238)
    print(student1.study())
    teacher1 = Teacher("hx","20","English",5500)
    print(teacher1)
    print(teacher1.teach())
