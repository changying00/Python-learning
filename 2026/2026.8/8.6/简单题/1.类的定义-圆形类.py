"""
【类的定义】编写一个 圆形 类 、 定义一个 半径属性（私有化） 、完成计算 圆 周长、面积 行为，
并编写代码 完成对应的测试。 要求 构建圆对象的时候， 半径可提供、可不提供，如果不提供、默认为 0

"""
import math


# 定义一个圆形类
class Circle:
    """圆形类：半径私有化，可计算周长和面积"""

    def __init__(self, radius=0):
        """构造方法：半径可提供，不提供时默认为 0"""
        self.__radius = radius  # 私有属性：半径

    # 半径的 getter
    @property
    def radius(self):
        return self.__radius

    # 半径的 setter
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("半径不能为负数")
        self.__radius = value

    def get_perimeter(self):
        """计算圆的周长：C = 2 * π * r"""
        return 2 * math.pi * self.__radius

    def get_area(self):
        """计算圆的面积：S = π * r²"""
        return math.pi * self.__radius ** 2


# ========== 测试代码 ==========
if __name__ == "__main__":
    # 不提供半径，默认为 0
    c1 = Circle()
    print(f"默认圆 半径={c1.radius}, 周长={c1.get_perimeter():.2f}, 面积={c1.get_area():.2f}")

    # 提供半径
    c2 = Circle(5)
    print(f"半径5的圆 半径={c2.radius}, 周长={c2.get_perimeter():.2f}, 面积={c2.get_area():.2f}")

    # 通过属性修改半径
    c2.radius = 10
    print(f"修改后 半径={c2.radius}, 周长={c2.get_perimeter():.2f}, 面积={c2.get_area():.2f}")
