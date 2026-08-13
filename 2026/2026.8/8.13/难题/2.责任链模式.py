"""
【责任链模式】

使用抽象类完成请假审批流程：

1. 请假 1 天以内：
   直接领导审批

2. 请假 3 天以内：
   直接领导审核
   部门经理审批

3. 请假 7 天以内：
   直接领导审核
   部门经理审批
   总经理审批

4. 超过 7 天：
   直接领导审核
   部门经理审批
   总经理审批
   董事长审批
"""
from abc import ABC, abstractmethod
# 审批人抽象类
class Leader(ABC):
    def __init__(self, name):
        # 领导姓名
        self.name = name
        # 下一个审批人
        self.next_leader = None
    # 设置下一个审批人
    def set_next(self, leader):
        self.next_leader = leader
    # 抽象方法
    @abstractmethod
    def approve(self, request):
        pass
# 直接领导
class DirectLeader(Leader):
    def approve(self, request):
        print(f"直接领导 {self.name} 审核请假申请")
        # 1天以内，直接领导可以审批
        if request.days <= 1:
            print("审批通过")
        # 超过1天，交给部门经理
        else:
            self.next_leader.approve(request)
# 部门经理
class DepartmentManager(Leader):
    def approve(self, request):
        print(f"部门经理 {self.name} 审批请假申请")
        # 3天以内，部门经理可以审批
        if request.days <= 3:
            print("审批通过")
        # 超过3天，交给总经理
        else:
            self.next_leader.approve(request)
# 总经理
class GeneralManager(Leader):
    def approve(self, request):
        print(f"总经理 {self.name} 审批请假申请")
        # 7天以内，总经理可以审批
        if request.days <= 7:
            print("审批通过")
        # 超过7天，交给董事长
        else:
            self.next_leader.approve(request)
# 董事长
class Chairman(Leader):
    def approve(self, request):
        print(f"董事长 {self.name} 审批请假申请")
        # 董事长是最终审批人
        print("审批通过")
# =========================
# 创建审批人
# =========================
leader = DirectLeader("张主管")
manager = DepartmentManager("李经理")
general_manager = GeneralManager("王总")
chairman = Chairman("赵董事长")
# 建立责任链
leader.set_next(manager)
manager.set_next(general_manager)
general_manager.set_next(chairman)
# 请假申请类
class LeaveRequest:
    def __init__(self, name, days):
        # 请假人
        self.name = name
        # 请假天数
        self.days = days
# 创建请假申请
if __name__ == '__main__':
    request = LeaveRequest( "小明", 5)
    leader.approve(request)