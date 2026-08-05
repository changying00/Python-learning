"""
【类的定义】超市结算时、会产生订单信息、商品信息、将订单、商品 设计为类、请分析订单中包含哪些属性、商品中包含哪些属性、并编写 订单类 、商品类 、并进行相关测试
"""
"""【类的定义】超市订单系统：订单类和商品类"""


class Product:
    """商品类"""
    def __init__(self, name, price):
        self.name = name  # 商品名称
        self.price = price  # 商品价格
class Order:
    """订单类"""
    def __init__(self, order_id):
        self.order_id = order_id  # 订单编号
        self.items = []  # 商品列表 [(商品对象, 数量), ...]
        self.total = 0.0  # 总金额
    def add_item(self, product, quantity=1):
        """添加商品"""
        self.items.append((product, quantity))
        self.total += product.price * quantity
        print(f"添加 {product.name} x {quantity}")
    def remove_item(self, product_name):
        """移除商品"""
        for item in self.items:
            if item[0].name == product_name:
                self.items.remove(item)
                # 重新计算总价
                self.total = 0
                for p, q in self.items:
                    self.total += p.price * q
                print(f"移除 {product_name}")
                return
        print(f"没有找到 {product_name}")
    def show_order(self):
        """显示订单"""
        print(f"\n订单号：{self.order_id}")
        print("商品明细：")
        for product, quantity in self.items:
            print(f"  {product.name} x {quantity} = ¥{product.price * quantity:.2f}")
        print(f"总计：¥{self.total:.2f}")
# 测试
if __name__ == "__main__":
    # 创建商品
    apple = Product("苹果", 5.50)
    milk = Product("牛奶", 8.00)
    bread = Product("面包", 12.00)
    # 创建订单
    order = Order("ORD001")
    # 添加商品
    order.add_item(apple, 3)
    order.add_item(milk, 2)
    order.add_item(bread, 1)
    # 显示订单
    order.show_order()
    # 移除商品
    order.remove_item("面包")
    # 再显示订单
    order.show_order()