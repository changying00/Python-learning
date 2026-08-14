"""
【责任链模式】设计一个 用来处理 采购流程的类 采购流程如下：
1.  采购价格在5000以内 、需要自己的直接领导审批
2.  采购价格在30000以内  、需要部门经理审批
3.  采购价格在200000以内、总经理审批
4.  超过200000 、需要 董事长审批。
"""
# price 采购价格
from abc import ABC, abstractmethod

class AbstractLeaveApproval(ABC):

    def __init__(self,price,next_handler =None):
        #设置 采购价格
        self._price = price
        #设置 责任链 中的下一个 任务处理者
        self.__next_handler = next_handler
    @abstractmethod
    def is_support(self):
        """是否需要审批"""
        pass

    def approval(self):
        """审批"""
        if self.is_support():
            #输出一段话
            print(f"当前采购金额为{self._price}，{self.role}准备开始审批")
            if input('1 允许\n2 不允许\n请输入对应的数字:') == '1':
                return True
            else:
                return False
        return self.__next_handler.approval()
#直接领导
class DirectLeaderLeaveApproval(AbstractLeaveApproval):
    def __init__(self,price,next_handler=None):
        super().__init__(price,next_handler)
        self.role = "直接领导"
    def is_support(self):
        return   0 <= self._price < 5000
#部门经理
class DepartManageLeaveApproval(AbstractLeaveApproval):
    def __init__(self, price, next_handler=None):
        super().__init__(price, next_handler)
        self.role = "部门经理"
    def is_support(self):
        return  5000 <= self._price < 30000
#总经理
class ManageLeaveApproval(AbstractLeaveApproval):
    def __init__(self,price, next_handler=None):
        super().__init__(price, next_handler)
        self.role = "总经理"
    def is_support(self):
        return 30000 <= self._price < 200000
#董事长
class BossLeaveApproval(AbstractLeaveApproval):
    def __init__(self,price, next_handler=None):
        super().__init__(price, next_handler)
        self.role = "董事长"
    def is_support(self):
        return True
class LeaveApproval:
    def __init__(self,price):
        # 创建 不同的 审批 角色
        boss = BossLeaveApproval(price)
        # 创建 总经理 橘色
        manage = ManageLeaveApproval(price, boss)
        # 创建 部门主管 角色
        depart = DepartManageLeaveApproval(price, manage)
        # 创建 直接领导 角色
        direct = DirectLeaderLeaveApproval(price, depart)
        # 将 直接 领导 角色 作为 当前审批类的属性
        self.__approval = direct
    def approval(self):
        #进行审批
        return self.__approval.approval()
if __name__ == "__main__":
    money = int(input("请输入采购价格:"))

    if LeaveApproval(money).approval():
        print(f"审批通过")
    else:
        print(f"审批不通过")
