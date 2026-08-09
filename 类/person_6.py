"""处理内嵌的内置对象）"""
class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print(bob.name.split()[-1])     # 取出对象的姓
    sue.pay *= 1.10                 # 给这个对象涨薪
    print(f'{sue.pay:,.2f}')