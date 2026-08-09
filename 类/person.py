class Person: #开始一个类
    def __init__(self, name, job =None ,pay = 0):#构建函数 接受三个参数
        self.name = name         #创建时填好字段   # 把局部变量 name 存入新实例的 __dict__（键 'name'）
        self.job = job           #self 是新建的实例对象   # 同上，键 'job'
        self.pay = pay           # 同上，键 'pay'
# 仅当作为脚本运行测试时执行，如果外部import 这个文件看不到我们的测试数据
if __name__ == '__main__':
# 仅当作为脚本运行（__name__ 为 '__main__'）时执行
    # 自动运行__init__
    bob = Person("Bob smith")
    sue = Person("Sue Jones",job = "dev",pay = 10000)
    #取出已挂上的属性 sue 和bob的属性不同
    print(bob.name, bob.pay) # 取出属性：访问实例的 __dict_
    print(sue.name, sue.pay)
    print(bob.name.split()[-1]) #取出对象的姓名 ,对属性应用字符串操作
    sue.pay *=1.10 #给这个对象涨薪资,：对属性应用数字操作
    print(f"{sue.pay:,.2f}")#f-string 格式化：逗号千分位 + 两位小数
