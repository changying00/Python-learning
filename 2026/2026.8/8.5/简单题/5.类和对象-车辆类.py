"""
【类与对象】车辆类：创建一个代表车辆的类，具有属性（例如品牌、型号、颜色等）和方法（例如启动、停止等）。
"""
"""【类与对象】车辆类：创建一个代表车辆的类，具有属性和方法。"""
class Vehicle:
    """车辆类"""
    def __init__(self, brand, model, color):
        """初始化车辆"""
        self.brand = brand  # 品牌
        self.model = model  # 型号
        self.color = color  # 颜色
        self.speed = 0  # 当前速度
        self.is_started = False  # 启动状态
    def start(self):
        """启动"""
        if not self.is_started:
            self.is_started = True
            print(f"{self.brand} {self.model} 已启动")
        else:
            print(f"{self.brand} {self.model} 已经启动")
    def stop(self):
        """停止"""
        if self.is_started and self.speed == 0:
            self.is_started = False
            print(f"{self.brand} {self.model} 已停止")
        elif self.speed > 0:
            print(f"请先刹车！当前速度：{self.speed}")
        else:
            print(f"{self.brand} {self.model} 已经停止")
    def accelerate(self, speed_up):
        """加速"""
        if not self.is_started:
            print("请先启动车辆")
            return
        self.speed += speed_up
        print(f"当前速度：{self.speed} km/h")
    def brake(self, speed_down):
        """刹车"""
        self.speed -= speed_down
        if self.speed < 0:
            self.speed = 0
        print(f"当前速度：{self.speed} km/h")
    def show_info(self):
        """显示信息"""
        print(f"品牌：{self.brand}")
        print(f"型号：{self.model}")
        print(f"颜色：{self.color}")
        print(f"速度：{self.speed} km/h")
        print(f"状态：{'已启动' if self.is_started else '已停止'}")
# 测试代码
if __name__ == "__main__":
    # 创建车辆
    car = Vehicle("特斯拉", "Model 3", "白色")
    # 测试功能
    car.show_info()
    print("-" * 30)
    car.start()  # 启动
    car.accelerate(30)  # 加速到30
    car.accelerate(50)  # 加速到80
    car.brake(20)  # 减速到60
    car.brake(70)  # 减速到0
    car.stop()  # 停止
    car.show_info()  # 查看最终状态