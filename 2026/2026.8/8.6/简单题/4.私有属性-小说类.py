"""

【私有属性】编写一个 小说类、包含 作者、小说名、小说类型、出售价格、 要求所有的属性全部私有化、 并提供对应的 property 属性 进行访问。 完成如下测试代码： 1. 创建 5本小说， 将5本小说存储到列表中、并按照 出售价格 进行降序排列。 2. 将 5本小说 存储到 集合中， 如果 小说名、作者相同、则认为是相同小说，需要set集合自动完成去重 30
"""


class Novel:
    """小说类：作者、小说名、类型、价格全部私有化"""

    def __init__(self, author, name, novel_type, price):
        self.__author = author          # 作者
        self.__name = name              # 小说名
        self.__novel_type = novel_type  # 小说类型
        self.__price = price            # 出售价格

    # ---- property 访问器 ----
    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        self.__author = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def novel_type(self):
        return self.__novel_type

    @novel_type.setter
    def novel_type(self, value):
        self.__novel_type = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("价格不能为负数")
        self.__price = value

    def __eq__(self, other):
        """小说名和作者相同则认为是相同小说"""
        if not isinstance(other, Novel):
            return False
        return self.__name == other.__name and self.__author == other.__author

    def __hash__(self):
        """hash 值由小说名和作者决定，用于 set 去重"""
        return hash((self.__name, self.__author))

    def __repr__(self):
        return f"Novel(作者={self.__author}, 书名={self.__name}, 类型={self.__novel_type}, 价格={self.__price})"


# ========== 测试代码 ==========
if __name__ == "__main__":
    # 1. 创建 5 本小说，存入列表，按出售价格降序排列
    novels = [
        Novel("金庸", "射雕英雄传", "武侠", 45.0),
        Novel("古龙", "小李飞刀", "武侠", 38.5),
        Novel("刘慈欣", "三体", "科幻", 68.0),
        Novel("东野圭吾", "白夜行", "推理", 42.0),
        Novel("金庸", "射雕英雄传", "武侠", 45.0),  # 与第一本相同，用于去重测试
    ]

    # 按价格降序排列
    novels_sorted = sorted(novels, key=lambda n: n.price, reverse=True)
    print("按价格降序排列：")
    for n in novels_sorted:
        print(f"  {n}")

    # 2. 存入 set 集合，小说名+作者相同则自动去重
    novel_set = set(novels)
    print(f"\n存入集合后数量: {len(novel_set)} (原列表 {len(novels)} 本，去重后应少1本)")
    print("集合中的小说：")
    for n in novel_set:
        print(f"  {n}")
