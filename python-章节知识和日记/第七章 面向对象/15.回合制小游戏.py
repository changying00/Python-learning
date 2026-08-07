"""
Role :
    属性  name,  blood ,  skill,  pass_skill,  max_blood

    方法  get_skill,  get_pass_skill,  attach...

"""
import random
import time


class Role:

    def __init__(self, name, blood):
        self.__name = name
        self.__blood = blood
        self.__maxblood = blood
        self.__skills = [
            ("神剑御雷真诀", 1500),
            ("八荒六合唯我独尊", 1000),
            ("含笑半步颠", 500),
            ("风含情水含笑", 300),
            ("大梵般若", 700),
            ("冰心诀", 100),
            ("天尊法身", 200)
        ]

        self.__pass_skills = [
            ("黄帝内径", 700),
            ("天仙护体", 400),
            ("炼器还神", 100),
            ("", 0)
        ]

    @property
    def blood(self):
        return self.__blood

    def get_rand_skill(self):
        """随机返回一个 主动攻击技能"""
        return random.choice(self.__skills)

    def get_rand_passskill(self):
        """随机返回一个 被动防御技能"""
        return random.choice(self.__pass_skills)

    def attack(self, role) -> bool:
        # 随机获取一个 攻击技能
        skill, value = self.get_rand_skill()
        print(f"{self.__name} 使用技能 {skill} 攻击 {role.__name}")
        # 判断 概率为 3%
        if random.random() <= 0.03:
            print(f"{role.__name}触发了铜墙铁壁免疫本次所有伤害")
            return False

        # 对方 随机产生一个 防御技能
        pass_skill, pass_value = role.get_rand_passskill()
        # 计算 需要扣除血量
        blood = value - pass_value

        if blood <= 0:
            print(f"{role.__name} 使用了 {pass_skill} 防御技能、本次伤害值为 0")
            return False

        # 判断 对方血量
        if blood < role.__blood:
            print(f"{role.__name} 使用了 {pass_skill} 防御技能、本次伤害值为 {blood}")
            role.__blood -= blood
            return False
        # 说明 给了 对方 致命一击
        if not hasattr(role, "_deaded"):
            role.__blood = int(role.__maxblood * 0.05)
            # 对方可以 触发 假死 技能、且 血量 恢复为 5%
            print(f"{role.__name} 使用了 {pass_skill} 防御技能、触发 起死回生 技能、血量恢复为 {role.__blood}")
            # 将 role 标记为 _deaded
            setattr(role, "_deaded", True)
            return False

        print(f"{role.__name} 使用了 {pass_skill} 防御技能、血量为 0、已死亡!!!")

        return True


class Game:
    """游戏类"""

    def __init__(self, me, you):
        self.__me_role = me
        self.__you_role = you
        # 存储回合数
        self.__num = 1

    def start(self):
        """
        血量小的 优先发起进攻
        """
        if self.__me_role.blood > self.__you_role.blood:
            self.__me_role, self.__you_role = self.__you_role, self.__me_role

        # 模拟 不断攻击
        while True:
            print(f"======================第 {self.__num} 回合======================")
            # me 先主动 发起攻击
            result = self.__me_role.attack(self.__you_role)
            if result:
                break
                # 睡眠、模拟攻击的过程
            time.sleep(2)
            # you 发起攻击
            result = self.__you_role.attack(self.__me_role)

            if result:
                break
            time.sleep(2)
            # 如果 都没赢 、一回合结束了、 将回合数 增加  1
            self.__num += 1


if __name__ == "__main__":
    # 创建 2 个角色
    role1 = Role("张三", 2000)
    role2 = Role("李四", 2100)

    # 创建一个 游戏对象
    game = Game(role1, role2)
    # 开启游戏
    game.start()
