"""
简单题 【类的定义】超市里有很多商品、根据面向对象的设计思想、找到商品的特征和行为、并使用类 进行描述 。 测试要求：
a) 测试代码 写到  main 中
b) 支持 根据 商品名、价格 快速 构建商品对象
c) 支持 不传入任何参数 构建商品对象
d) 修改 商品的价格、可以实现在原价基础上 提升 百分之多少
e) 在类中定义一个 show 方法、负责展示商品信息、调用该方法完成测试
f) 打印对象的时候，希望能够展示对象中的属性信息
g) 能够使用 str 函数 将对象转成字符串，且信息为 对象中的属性信息
"""
"""【类的定义】超市商品类：根据面向对象思想设计商品类"""


class Product:
    """商品类 - 描述超市商品"""
    def __init__(self, name=None, price=None):
        """
        初始化商品
        :param name: 商品名称（可选）
        :param price: 商品价格（可选）
        """
        if name is None and price is None:
            # 不传入任何参数：创建默认商品
            self.name = "未知商品"
            self.price = 0.0
        else:
            # 根据商品名、价格快速构建
            self.name = name if name is not None else "未知商品"
            self.price = price if price is not None else 0.0
    def increase_price(self, percent):
        """
        在原价基础上提升价格
        :param percent: 提升百分比（如10表示提升10%）
        """
        if percent <= 0:
            print(f"提升百分比必须大于0")
            return
        old_price = self.price
        self.price = self.price * (1 + percent / 100)
        print(f"价格从 ¥{old_price:.2f} 提升 {percent}% 到 ¥{self.price:.2f}")

    def show(self):
        """展示商品信息"""
        print("=" * 40)
        print(f"商品信息")
        print("=" * 40)
        print(f"商品名称：{self.name}")
        print(f"商品价格：¥{self.price:.2f}")
        print("=" * 40)
    def __str__(self):
        """使用str函数时返回商品信息"""
        return f"Product(name='{self.name}', price=¥{self.price:.2f})"
    def __repr__(self):
        """在交互环境中直接显示对象时调用"""
        return self.__str__()
# 测试代码
if __name__ == "__main__":
    print("超市商品系统测试")
    print("=" * 50)

    # 测试b: 根据商品名、价格快速构建商品对象
    print("\n【测试1：根据商品名和价格创建】")
    product1 = Product("苹果", 5.50)
    product1.show()

    # 测试c: 不传入任何参数构建商品对象
    print("\n【测试2：不传入任何参数创建】")
    product2 = Product()
    product2.show()

    # 测试d: 修改商品价格，在原价基础上提升百分比
    print("\n【测试3：价格提升】")
    print("原价：¥5.50")
    product1.increase_price(10)  # 提升10%
    product1.increase_price(20)  # 再提升20%

    # 测试e: show方法展示商品信息
    print("\n【测试4：使用show方法展示】")
    product1.show()
    product2.show()

    # 测试f: 打印对象展示属性信息
    print("\n【测试5：直接打印对象】")
    print(product1)
    print(product2)

    # 测试g: 使用str函数转成字符串
    print("\n【测试6：使用str函数】")
    str_info = str(product1)
    print(f"str转换结果：{str_info}")

    # 额外测试：创建多个商品
    print("\n【额外测试：创建多个商品】")
    product3 = Product("牛奶", 8.00)
    product4 = Product("面包", 12.00)

    products = [product3, product4]
    for product in products:
        print(product)

    # 测试价格提升的边界情况
    print("\n【边界测试：价格提升0%】")
    product3.increase_price(0)