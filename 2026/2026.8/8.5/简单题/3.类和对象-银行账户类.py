"""【类与对象】银行账户类：创建一个简单的银行账户类，具有存款、取款、查询余额等方法。"""
#定义一个银行类
class Bank:
    #定义类的属性，银行的名，
    def __init__(self,bank_name,account_holder,initial_balance = 0):
        """  初始化银行账户
        :param bank_name: 银行名称
        :param account_holder: 账户持有人
        :param initial_balance: 初始余额（默认为0)
        """
        self.bank_name = bank_name
        self.account_holder = account_holder
        self.balance = initial_balance  # 关键：使用实例属性存储余额
    #定义一个存款方法
    def deposit(self,amount):
        """
           存款方法
        :param amount: 存款金额
        :return: 是否存款成功
        """
        if amount > 0:
            self.balance += amount  # 使用self.balance访问实例属性
            print(f"存款成功！存入 {amount} 元，当前余额为 {self.balance} 元")
            return True
        else:
            print("存款金额必须大于0")
            return False
    #定义一个取款方法
    def withdraw(self,amount):
        """
               取款方法
               :param amount: 取款金额
               :return: 是否取款成功
               """
        if amount <= 0:
            print("取款金额必须大于0")
            return False
        if amount > self.balance:
            print(f"余额不足！当前余额为 {self.balance} 元，需要 {amount} 元")
            return False
        self.balance -= amount
        print(f"取款成功！取出 {amount} 元，当前余额为 {self.balance} 元")
        return True
    #定义一个查询余额的方法
    def check_balance(self):
        """查询余额"""
        print(f"{self.bank_name} - 账户持有人：{self.account_holder}")
        print(f"当前余额为：{self.balance} 元")
        return self.balance
if __name__=="__main__":
    # 创建账户实例
    account = Bank("工商银行", "张三", 1000)  # 初始余额1000元

    # 查询余额
    print("\n1. 初始余额查询：")
    account.check_balance()

    # 存款
    print("\n2. 存款操作：")
    account.deposit(2000)

    # 再次查询余额
    print("\n3. 存款后查询：")
    account.check_balance()

    # 取款
    print("\n4. 取款操作：")
    account.withdraw(500)