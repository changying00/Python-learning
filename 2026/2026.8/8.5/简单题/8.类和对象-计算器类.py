"""
【类与对象】计算器类：创建一个简单的计算器类，它具有加、减、乘、除等方法。
"""
class Calculator:
    """计算器类"""
    def __init__(self):
        """初始化计算器"""
        self.result = 0  # 存储计算结果
    def add(self, num1, num2):
        """加法"""
        self.result = num1 + num2
        print(f"{num1} + {num2} = {self.result}")
        return self.result
    def subtract(self, num1, num2):
        """减法"""
        self.result = num1 - num2
        print(f"{num1} - {num2} = {self.result}")
        return self.result
    def multiply(self, num1, num2):
        """乘法"""
        self.result = num1 * num2
        print(f"{num1} × {num2} = {self.result}")
        return self.result
    def divide(self, num1, num2):
        """除法"""
        if num2 == 0:
            print("错误：除数不能为0！")
            return None
        self.result = num1 / num2
        print(f"{num1} ÷ {num2} = {self.result}")
        return self.result


# 测试
if __name__ == "__main__":
    # 创建计算器对象
    calc = Calculator()
    print("计算器测试")
    print("-" * 30)
    # 测试运算
    calc.add(10, 5)
    calc.subtract(10, 5)
    calc.multiply(10, 5)
    calc.divide(10, 5)
    print("-" * 30)
    # 测试除零错误
    calc.divide(10, 0)