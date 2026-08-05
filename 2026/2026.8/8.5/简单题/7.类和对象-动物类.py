"""
【类与对象】创建一个简单的类：编写一个代表动物的类，它具有属性（例如名字、年龄等）和方法（例如发出声音）。创建几个不同的动物对象，设置它们的属性，并调用它们的方法。
"""

"""【类与对象】动物类：创建代表动物的类，具有属性和方法"""
class Animal:
    """动物类"""
    def __init__(self, name, age, species):
        """初始化动物"""
        self.name = name  # 名字
        self.age = age  # 年龄
        self.species = species  # 种类
    def make_sound(self):
        """发出声音"""
        # 根据种类不同发出不同声音
        if self.species == "狗":
            sound = "汪汪汪！"
        elif self.species == "猫":
            sound = "喵喵喵！"
        elif self.species == "牛":
            sound = "哞哞哞！"
        elif self.species == "羊":
            sound = "咩咩咩！"
        elif self.species == "鸡":
            sound = "咯咯咯！"
        else:
            sound = "叫了一声"
        print(f"{self.name}（{self.species}）{sound}")
    def show_info(self):
        """显示动物信息"""
        print(f"名字：{self.name}")
        print(f"年龄：{self.age} 岁")
        print(f"种类：{self.species}")
        print("-" * 20)
# 测试
if __name__ == "__main__":
    # 创建几个动物对象
    dog = Animal("旺财", 3, "狗")
    cat = Animal("咪咪", 2, "猫")
    cow = Animal("大黄", 5, "牛")
    sheep = Animal("小绵", 1, "羊")
    # 显示信息并发出声音
    print("\n第一只动物：")
    dog.show_info()
    dog.make_sound()
    print("\n第二只动物：")
    cat.show_info()
    cat.make_sound()
    print("\n第三只动物：")
    cow.show_info()
    cow.make_sound()
    print("\n 第四只动物：")
    sheep.show_info()
    sheep.make_sound()