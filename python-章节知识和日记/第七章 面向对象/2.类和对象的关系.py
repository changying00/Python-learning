class Cat:
    def __init__(self):
        self.skin = "三花"
        self.sall = "喵喵喵"
        self.ming = "年年"

    def eat(self):
        print(f"一只{self.skin}正在{self.sall}叫，他想找吃的")

    def call(self):
        print(f"一个叫{self.ming}的猫正在{self.sall}叫")

if __name__ == "__main__":
    #实例化对象，
    cat = Cat()
    #调用猫 的eat方法
    cat.call()
    #调用猫 的call方法
    cat.eat()