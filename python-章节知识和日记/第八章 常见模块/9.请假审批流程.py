
"""
请假审批

"""
from abc import ABC, abstractmethod


class AbstractLeaveApproval(ABC):

    def __init__(self, day, next_handler=None):
        # 设置 请假的天数
        self._day = day 
        # 设置 责任链中的 下一个任务处理者
        self.__next_handler = next_handler

    @abstractmethod
    def is_support(self):
        """是否需要进行审批"""
        pass

    def approval(self):
        """审批"""
        if self.is_support():
            # 输出 一句话 
            print(f"{self.role} 准备开始审批请假流程") 
            if input("1 允许\n2 拒绝\n 请输入 对应的数字\n") == "1":
                print(f"{self.role} 准许 请假 {self._day} 天")
            else:
                print(f"{self.role} 不同意 请假 {self._day} 天")
                return False
        
        # 无论是否 当前角色 是否支持 审批、审批 流向下一个审批人 
        if self.__next_handler:
            return self.__next_handler.approval()
        # 如果 没有下一个审批人、则代表 允许
        return True 


class DirectLeaderLeaveApproval(AbstractLeaveApproval):

    def __init__(self, day, next_handler=None):
        super().__init__(day, next_handler)
        self.role = "直接领导"

    def is_support(self):
        return True 

    
class DepartManageLeaveApproval(AbstractLeaveApproval):

    def __init__(self, day, next_handler=None):
        super().__init__(day, next_handler)
        self.role = "部门主管"

    def is_support(self):
        return self._day > 1

     
class ManageLeaveApproval(AbstractLeaveApproval):

    def __init__(self, day, next_handler=None):
        super().__init__(day, next_handler)
        self.role = "总经理"

    def is_support(self):
        return self._day > 3


class BossLeaveApproval(AbstractLeaveApproval):

    def __init__(self, day, next_handler=None):
        super().__init__(day, next_handler)
        self.role = "董事长"

    def is_support(self):
        return self._day > 7


class LeaveApproval:

    def __init__(self, day):
        # 创建 不同的 审批 角色 
        boss = BossLeaveApproval(day)
        # 创建 总经理 橘色 
        manage = ManageLeaveApproval(day, boss)
        # 创建 部门主管 角色
        depart = DepartManageLeaveApproval(day, manage)
        # 创建 直接领导 角色 
        direct = DirectLeaderLeaveApproval(day, depart)

        # 将 直接 领导 角色 作为 当前审批类的属性 
        self.__approvalor = direct

    def approval(self):
        # 进行审批 
        return self.__approvalor.approval()


if __name__ == "__main__":

    day = int(input("请输入请假天数\n"))
    # 模拟 请假 1 天 审批流程
    if LeaveApproval(day).approval():
        print("你可以安心休假了")
    else:
        print("牛马， 继续干活吧！")