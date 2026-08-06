"""
【类的定义】编写一个 长方形类 、 定义 长和宽 两个私有化属性、 提供 计算 周长、面积 的行为 、并完成相关功能的测试。要求 构建长方形对象的时候 必须提供 长和宽 两个属性值
"""


class Rectangle:
    """长方形类：长、宽私有化，可计算周长和面积"""

    def __init__(self, length, width):
        """构造方法：必须提供长和宽"""
        self.__length = length  # 私有属性：长
        self.__width = width    # 私有属性：宽

    @property
    def length(self):
        """获取长度"""
        return self.__length

    @length.setter
    def length(self, value):
        """设置长度"""
        if value <= 0:
            raise ValueError("长度必须大于0")
        self.__length = value

    @property
    def width(self):
        """获取宽度"""
        return self.__width

    @width.setter
    def width(self, value):
        """设置宽度"""
        if value <= 0:
            raise ValueError("宽度必须大于0")
        self.__width = value

    def get_perimeter(self):
        """计算周长：C = 2 * (长 + 宽)"""
        return 2 * (self.__length + self.__width)

    def get_area(self):
        """计算面积：S = 长 * 宽"""
        return self.__length * self.__width


# ========== 测试代码 ==========
if __name__ == "__main__":
    rect = Rectangle(5, 3)
    print(f"长={rect.length}, 宽={rect.width}")
    print(f"周长={rect.get_perimeter()}")
    print(f"面积={rect.get_area()}")

    # 修改长宽后重新计算
    rect.length = 10
    rect.width = 4
    print(f"修改后 长={rect.length}, 宽={rect.width}")
    print(f"周长={rect.get_perimeter()}, 面积={rect.get_area()}")
