"""
【魔术方法】编写一个 猫类、并提供 名字和 年龄 2个属性 ，要求如下:
a、私有化属性、并提供公开的访问方式
b、2只猫 可以比较 是否相同 (如果名字和年龄相同，则认为两只猫内容相同)
c、2只猫 可以比较大小 (按照年龄 比较大小)
d、多只猫 可以放到 set集合中，且能够对内容相同的猫 进行去重 。
	（hash算法要求 将 名字的hash值 和 年龄的 hash值相加即可）
"""


class Cat:
    """猫类：名字、年龄私有化，支持比较与 set 去重"""

    def __init__(self, name, age):
        self.__name = name  # 私有属性：名字
        self.__age = age    # 私有属性：年龄

    # ---- 公开访问方式 (property) ----
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("年龄不能为负数")
        self.__age = value

    # ---- 比较是否相同 ----
    def __eq__(self, other):
        """名字和年龄都相同则认为两只猫相同"""
        if not isinstance(other, Cat):
            return False
        return self.__name == other.__name and self.__age == other.__age

    # ---- 比较大小（按年龄）----
    def __lt__(self, other):
        """按年龄比较：小于"""
        if not isinstance(other, Cat):
            return NotImplemented
        return self.__age < other.__age

    def __le__(self, other):
        """按年龄比较：小于等于"""
        if not isinstance(other, Cat):
            return NotImplemented
        return self.__age <= other.__age

    def __gt__(self, other):
        """按年龄比较：大于"""
        if not isinstance(other, Cat):
            return NotImplemented
        return self.__age > other.__age

    def __ge__(self, other):
        """按年龄比较：大于等于"""
        if not isinstance(other, Cat):
            return NotImplemented
        return self.__age >= other.__age

    # ---- hash：名字 hash + 年龄 hash，用于 set 去重 ----
    def __hash__(self):
        return hash(self.__name) + hash(self.__age)

    def __repr__(self):
        return f"Cat(name={self.__name}, age={self.__age})"


# ========== 测试代码 ==========
if __name__ == "__main__":
    cat1 = Cat("小花", 3)
    cat2 = Cat("小白", 5)
    cat3 = Cat("小花", 3)  # 与 cat1 相同
    cat4 = Cat("小黑", 2)

    # b. 比较是否相同
    print(f"cat1 == cat2: {cat1 == cat2}")
    print(f"cat1 == cat3: {cat1 == cat3}")

    # c. 比较大小（按年龄）
    print(f"cat1 < cat2: {cat1 < cat2}")   # 3 < 5
    print(f"cat2 > cat4: {cat2 > cat4}")   # 5 > 2
    print(f"排序: {sorted([cat1, cat2, cat4])}")

    # d. 放入 set 去重
    cat_set = {cat1, cat2, cat3, cat4}
    print(f"set 去重后数量: {len(cat_set)} (原4只，相同的去重后应3只)")
    print(f"set 内容: {cat_set}")
