"""【类与对象】员工类：创建一个员工类，具有属性（例如姓名、工号、职位等）和方法（例如计算工资、升职等）。"""

class Stall:
#定义员工类的属性
    def __init__(self,name,employee_ID,Position):
         self.name=name
         self.employee_ID=employee_ID
         self.Position=Position

    #定义方法计算工资
    def count_salary(self,salary):
        print(f"你的姓名为:{self.name}\n你的工号为:{self.employee_ID}\n你的职位为:{self.Position}\n你的工资为:{salary}")
if __name__=="__main__":
    #实例化一个对象
    stall = Stall("DGX","001",'高级职工')
    #调用对象的计算工资的方法
    stall.count_salary(100)