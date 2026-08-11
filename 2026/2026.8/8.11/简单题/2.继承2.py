"""
【继承】Employee：这是所有员工的父类，包含属性：员工的姓名, 员工的生日月份。
方法：get_salary(int month) 根据参数月份来确定工资，如果该月员工过生日，
则公司会额外奖励100元。

SalariedEmployee：Employee的子类，拿固定工资的员工。属性：月薪

HourlyEmployee：Employee的子类，按小时拿工资的员工，每月工作超出160小时的部分按照1.5倍工资发放。
属性：每小时的工资、每月工作的小时数

SalesEmployee：Employee的子类，销售人员，工资由月销售额和提成率决定。
属性：月销售额、提成率

BasePlusSalesEmployee：SalesEmployee的子类，有固定底薪的销售人员，工资由底薪加上销售提成部分。
属性：底薪。

写一个测试代码，并把若干不同类型的员工放在一个列表里，
1. 打印出某月每个员工的工资数额。
2. 打印出某月 最高薪资的员工信息
3. 按照月薪资 进行升序排序
"""
#定义员工的父类
class Employee:
    #初始化员工的属性
    def __init__(self,name,birth_month):
        self.name = name
        self.birth_month = birth_month

    #定义方法属性 get_salary()
    def get_salary(self,month):
        if month == self.birth_month:
            return 100
        return 0
    def __str__(self):
        return f"员工:{self.name},生日:{self.birth_month}月"
#定义SalariedEmployee：继承Employee
class SalariedEmployee(Employee):
    def __init__(self,name,birth_month,month_salary):
        super().__init__(name,birth_month)
        self.month_salary = month_salary

    def get_salary(self,month):
        # 先看是否使生日月 能否加100块工资
        birth_month_money = super().get_salary(month)
        return self.month_salary + birth_month_money

#定义HourlyEmployee：Employee的子类
class HourlyEmployee(Employee):
    def __init__(self,name,birth_month,hour_salary,month_hour):
        super().__init__(name,birth_month)
        self.hour_salary = hour_salary
        self.month_hour = month_hour
    def get_salary(self,month):
        #先看是否使生日月 能否加100块工资
        result = super().get_salary(month)
        #然后根据小时算月工资
        if self.month_hour <= 160:
            salary = self.month_hour * self.hour_salary
        else:
            salary = (160 * self.hour_salary +(self.month_hour - 160) * self.hour_salary * 1.5 )
        return salary + result
#SalesEmployee：Employee
class SalesEmployee(Employee):
    #初始化属性
    def __init__(self,name,birth_month,count_month_salary,commission_rate):
        super().__init__(name,birth_month)
        self.count_month_salary = count_month_salary
        self.commission_rate = commission_rate
    #定义工资方法
    def get_salary(self,month):
        # 先看是否使生日月 能否加100块工资
        birth_month_money = super().get_salary(month)
        result = self.count_month_salary * self.commission_rate + birth_month_money
        return result
#BasePlusSalesEmployee：SalesEmployee的子类
class  BasePlusSalesEmployee(SalesEmployee):
        def __init__(self,name,birth_month,count_month_salary,commission_rate,base_salary):
            super().__init__(name,birth_month,count_month_salary,commission_rate)
            self.base_salary = base_salary
        def get_salary(self,month):
           return super().get_salary(month) + self.base_salary

if __name__ == '__main__':
    #SalariedEmployee员工实例
    people1= SalariedEmployee("SalariedEmployee员工",6,5000)

    #HourlyEmployee员工实例
    people2= HourlyEmployee("HourlyEmployee员工",9,20,240)


    #SalesEmployee员工实例
    people3 = SalesEmployee("SalesEmployee员工",5,18000,0.25)

    #BasePlusSalesEmployee员工实例

    people4 = BasePlusSalesEmployee("BasePlusSalesEmployee员工",3,1000,0.25,3000)
    #按照4月工资来看
    #员工1
    print(people1.get_salary(4))
    #员工2
    print(people2.get_salary(4))
    #员工3
    print(people3.get_salary(4))
    #员工4
    print(people4.get_salary(4))

    employees = [
        people1,
        people2,
        people3,
        people4
    ]

    max_employee = max(employees,key=lambda x: x.get_salary(4))

    print("最高工资:", max_employee.name, max_employee.get_salary(4))

    employees.sort(key=lambda x: x.get_salary(4))

    for emp in employees:
        print(emp.name,emp.get_salary(4))

    print(max_employee)