"""
【封装】编写一个 Role 角色类、并提供 name (角色名), blood(血量) ，skills技能列表, 被动技能列表passive_skills , max_blood (最大血量) 等属性 按照封装的要求、编写类
1) 技能属性 和 被动技能属性 被所有角色共享。技能列表值为
[(“神剑御雷真诀”, “1500”),
 (“八荒六合唯我独尊”,  “1000”) , (“含笑半步颠”,  “500”),  (“风含情水含笑”,  “300”) ,
(“大梵般若”,  “700”),  (“冰心诀”,  “100”) ,  (“天尊法身”,  “200”)]，
  数字代表技能攻击伤害 。
被动技能初始值列表
 [(“黄帝内径” , “1000” ) ,  (“天仙护体” , “800”) ,  (“炼器还神”,  “500”) ,  (“” ,  “0” ) ]
 数字代表 技能防御 抵消 伤害 (如果技能伤害 500， 被动防御 1000， 则实现抵消 500伤害、不允许出现回血现象)
 (“” , “0”)  代表没有使用被动技能

2.提供一个方法  get_rand_skill(self) 随机返回一个 主动技能  提示:  random.choice(seq) 随机返回序列中的一个元素
3.提供一个方法 get_rand_passive_skill(self) 随机返回一个 被动技能
4.提供一个 attack(self,  role) 攻击方法,  role 代表对方

	a)每次攻击 随机获取一个主动技能、并攻击 对方
	b)对方 有  3% 的概率(使用随机数获取概率) 会触发“铜墙铁壁”特殊免疫技能(忽略对方所有伤害)
	c)如果没有触发 “铜墙铁壁”，则 对方 随机 获取一个被动技能进行防御
	d)如果计算后血量 <= 0 , 则 触发 特殊技能 ·起死回生·, 血量回复最大血量5%(取整)
	e)特殊技能 *起死回生* 战斗过程中，只会被触发一次
编写Game类、维护2个角色属性，num 属性记录回合数(一来一往算一回合) 并编写start() 方法，实现回合制小游戏 （打印输出游戏的整合执行过程） 备注： 也可以使用 time.sleep(2) 每回合延迟2秒. 
"""
import random
import time


class Role:
    """角色类：封装角色名、血量、技能等属性"""

    # 类属性：所有角色共享的主动技能列表 (技能名, 伤害)
    skills = [
        ("神剑御雷真诀", "1500"),
        ("八荒六合唯我独尊", "1000"),
        ("含笑半步颠", "500"),
        ("风含情水含笑", "300"),
        ("大梵般若", "700"),
        ("冰心诀", "100"),
        ("天尊法身", "200"),
    ]

    # 类属性：所有角色共享的被动技能列表 (技能名, 防御值)
    passive_skills = [
        ("黄帝内径", "1000"),
        ("天仙护体", "800"),
        ("炼器还神", "500"),
        ("", "0"),  # 空技能：未使用被动
    ]

    def __init__(self, name, blood):
        """
        :param name: 角色名
        :param blood: 初始血量（同时作为最大血量）
        """
        self.__name = name
        self.__blood = blood
        self.__max_blood = blood
        # 起死回生是否已触发过（整场战斗只触发一次）
        self.__revive_used = False

    # ---- property 封装 ----
    @property
    def name(self):
        return self.__name

    @property
    def blood(self):
        return self.__blood

    @blood.setter
    def blood(self, value):
        self.__blood = value

    @property
    def max_blood(self):
        return self.__max_blood

    @property
    def revive_used(self):
        return self.__revive_used

    def mark_revive_used(self):
        """标记起死回生已使用"""
        self.__revive_used = True

    def get_rand_skill(self):
        """随机返回一个主动技能 (技能名, 伤害字符串)"""
        return random.choice(self.skills)

    def get_rand_passive_skill(self):
        """随机返回一个被动技能 (技能名, 防御字符串)"""
        return random.choice(self.passive_skills)

    def attack(self, role):
        """
        攻击对方 role
        a) 随机主动技能攻击
        b) 对方 3% 概率触发「铜墙铁壁」免疫全部伤害
        c) 否则对方随机被动技能防御
        d) 血量<=0 时触发「起死回生」（仅一次），回复 max_blood 的 5%（取整）
        """
        # a) 随机主动技能
        skill_name, skill_damage = self.get_rand_skill()
        damage = int(skill_damage)
        print(f"  【{self.__name}】使用主动技能【{skill_name}】，攻击力 {damage}")

        # b) 对方 3% 概率触发铜墙铁壁
        if random.random() < 0.03:
            print(f"  【{role.name}】触发特殊技能【铜墙铁壁】！免疫全部伤害！")
            return

        # c) 对方随机被动技能防御
        p_name, p_defense = role.get_rand_passive_skill()
        defense = int(p_defense)
        if p_name == "":
            print(f"  【{role.name}】未使用被动技能，防御 0")
        else:
            print(f"  【{role.name}】使用被动技能【{p_name}】，防御 {defense}")

        # 实际伤害 = 攻击 - 防御，不允许出现回血（最小为 0）
        actual_damage = max(0, damage - defense)
        role.blood = role.blood - actual_damage
        print(f"  实际造成伤害: {actual_damage}，【{role.name}】剩余血量: {role.blood}")

        # d/e) 血量 <= 0 且未使用过起死回生
        if role.blood <= 0 and not role.revive_used:
            revive_hp = int(role.max_blood * 0.05)  # 最大血量 5%，取整
            role.blood = revive_hp
            role.mark_revive_used()  # 标记已使用（整场仅一次）
            print(f"  【{role.name}】触发特殊技能【起死回生】！血量回复至 {revive_hp}")
        elif role.blood <= 0:
            role.blood = 0
            print(f"  【{role.name}】已阵亡！")

    def is_alive(self):
        """是否存活"""
        return self.__blood > 0

    def __str__(self):
        return f"{self.__name}(血量:{self.__blood}/{self.__max_blood})"


class Game:
    """回合制对战游戏"""

    def __init__(self, role1, role2):
        self.__role1 = role1  # 角色1
        self.__role2 = role2  # 角色2
        self.__num = 0        # 回合数（一来一往算一回合）

    @property
    def num(self):
        return self.__num

    def start(self):
        """开始回合制对战，打印完整过程"""
        print("=" * 50)
        print(f"  战斗开始！ {self.__role1}  VS  {self.__role2}")
        print("=" * 50)

        while self.__role1.is_alive() and self.__role2.is_alive():
            self.__num += 1
            print(f"\n---------- 第 {self.__num} 回合 ----------")

            # role1 攻击 role2
            print(f"→ {self.__role1.name} 发起攻击：")
            self.__role1.attack(self.__role2)
            if not self.__role2.is_alive():
                break

            # role2 攻击 role1
            print(f"→ {self.__role2.name} 发起攻击：")
            self.__role2.attack(self.__role1)
            if not self.__role1.is_alive():
                break

            # 每回合延迟 2 秒（可按需注释掉加快测试）
            time.sleep(2)

        # 战斗结束
        print("\n" + "=" * 50)
        print(f"  战斗结束！共进行 {self.__num} 回合")
        if self.__role1.is_alive():
            print(f"  胜利者: {self.__role1.name}，剩余血量: {self.__role1.blood}")
            print(f"  失败者: {self.__role2.name}")
        else:
            print(f"  胜利者: {self.__role2.name}，剩余血量: {self.__role2.blood}")
            print(f"  失败者: {self.__role1.name}")
        print("=" * 50)


# ========== 测试代码 ==========
if __name__ == "__main__":
    # 创建两个角色，血量设为 3000 便于多回合对战
    r1 = Role("令狐冲", 3000)
    r2 = Role("东方不败", 3000)

    game = Game(r1, r2)
    game.start()
