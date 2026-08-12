
class Rectangle:
    """
    长方形
    """
    def __init__(self, length, width):
        # 长方形 提供 2 个属性、 长和宽
        self.__length = length
        self.__width = width

    def permiter(self):
        """计算周长"""
        return 2 * (self.__length + self.__width)

    def area(self):
        """计算面积"""
        return self.__length * self.__width


class Square(Rectangle):
    """正方形"""
    def __init__(self, slide):
        super().__init__(slide, slide)


class Cube(Square):
    """正方体"""
    def __init__(self, slide):
        super().__init__(slide)
        self.__height = slide

    def permiter(self):
        return super().permiter() * 3

    def area(self):
        return 6 * super().area()

    def volume(self):
        return super().area * self.__height 