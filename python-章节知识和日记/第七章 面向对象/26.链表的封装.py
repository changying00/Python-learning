from __future__ import annotations
from typing import Callable, Any


class LinkedList:
    """链表"""

    def __init__(self):
        # 定义一个属性 、用来表示 首节点
        self.__head = None
        # 定义一个属性、用来表示 尾节点
        self.__tail = None
        # 定义一个属性、用来表示 节点长度
        self.__size = 0

    def add_first(self, value):
        """向链表头部添加数据"""
        # 获取 原首节点 
        node = self.__head
        # 创建 一个 新节点、它的上一个节点指向 None, 下一个节点指向 node 
        new_node = self.Node(None, value, node)
        # 判断 原首节点是否为 None 
        if node is None:
            # 说明 添加的值 是第一个值、将 新节点作为 尾节点 
            self.__tail = new_node
        else:
            # 如果 源节点不为None, 则将 原首节点的上一个节点指向 新节点
            node.prev = new_node
            # 将 新节点 作为 首节点
        self.__head = new_node
        # 长度 + 1 
        self.__size += 1

    def add_last(self, value):
        """向链表的尾部添加数据"""
        # 获取 原尾节点 
        node = self.__tail
        # 创建一个 新节点、它的 上一个节点指向 node, 下一个指向 None 
        new_node = self.Node(node, value, None)
        # 判断 原尾节点是否为None 
        if node is None:
            # 将 新节点作为 首节点
            self.__head = new_node
        else:
            # 将 原尾节点的 下一个节点指向 新节点 
            node.next = new_node
            # 将 新节点作为 尾节点
        self.__tail = new_node
        # 长度 + 1
        self.__size += 1

    def add(self, value, index=None):
        """向指定索引位置前添加数据、 index 如果为 None, 默认向尾部追加"""
        if index is None:
            self.add_last(value)
            return
            # 获取 正索引
        index = self.__get_index(index)
        if index == 0:
            self.add_first(value)
            return
            # 向 中间添加元素 、获取 index 索引位置的 节点 node_b
        node_b = self.__get_node(index)
        # 获取 node_b 的上一个节点 
        node_a = node_b.prev
        # 创建一个 新节点 、它的上一个节点指向 node_a, 下一个节点指向 node_b 
        new_node = self.Node(node_a, value, node_b)
        # 将 node_a 的下一个 节点 和 node_b 的上一个节点 同时指向 new_node 
        node_a.next = node_b.prev = new_node
        # 长度 + 1
        self.__size += 1

    def __unlink(self, node):
        """删除指定的节点"""
        # 获取 它的 上一个 节点 和 下一个节点、分别赋值给 node_a, node_b 两个变量 
        node_a, node_b = node.prev, node.next
        # 将 node 节点的 上一个 和 下一个节点 全部设置为 none 
        node.prev = node.next = None
        # 将 node_a 的 下一个节点 设置为 node_b 
        if node_a is None:
            # 说明 删除的节点是 第一个节点、将原来的第二个节点设置为 首节点
            self.__head = node_b
        else:
            node_a.next = node_b

            # 将 node_b 的上一个节点 设置为 node_a
        if node_b is None:
            # 说明 删除的是最后一个节点、需要将 node_a 作为 尾节点 
            self.__tail = node_a
        else:
            node_b.prev = node_a
            # 将 长度 减少 1
        self.__size -= 1
        return node.value

    def pop(self, index=-1):
        """删除指定索引位置的元素、并返回被删除的数据"""
        # 获取 指定索引的 的 node 节点 
        node = self.__get_node(index)
        # 删除指定的 node 节点 
        return self.__unlink(node)

    def remove(self, value):
        """删除指定的第一个元素"""
        # 遍历 链表 、找到 value 对应的 Node 节点 
        node = self.__head
        while node is not None:
            if node.value == value:
                break
            node = node.next

        if node is not None:
            # 删除 node 节点 
            self.__unlink(node)

    def __get_index(self, index):
        _index = index
        if index < 0:
            # 将 负索引 转成 正索引
            _index = self.__size + index
        # 检查 索引的取值范围 
        if _index < 0 or _index >= self.__size:
            raise IndexError(f" 索引 {index} 超出范围")
        # 返回 计算后的正索引
        return _index

    def __get_node(self, index):
        """获取指定索引位置的节点"""
        # 检查索引的取值范围、并返回正索引
        _index = self.__get_index(index)
        # 判断 索引 是否超出了 长度 的一半 
        if _index <= self.__size >> 1:
            # 获取 第一个节点 
            node = self.__head
            # 定义一个遍历、循环次数为 index 
            for _ in range(_index):
                node = node.next
            return node
            # 如果 索引 超过了一般、则 从 后 向前移动
        node = self.__tail
        # 获取 要 循环的次数 
        count = self.__size - 1 - _index
        for _ in range(count):
            node = node.prev
        return node

    def get(self, index):
        """获取指定索引位置的数据"""
        node = self.__get_node(index)
        return node.value

    def set(self, index, value):
        """修改指定位置的元素"""
        node = self.__get_node(index)
        node.value = value

    def __len__(self):
        return self.__size

    def __iter__(self):
        """返回一个迭代器"""
        # 获取 第一个节点 
        node = self.__head
        while node is not None:
            # 返回 对应的数据
            yield node.value
            # 将 数据指向 下一个节点 
            node = node.next

    def clear(self):
        """清空链表"""
        while self.__size > 0:
            self.pop(0)

    def __repr__(self):
        # 返回格式为  LinkedList(1 <-> 2 <-> 3 <-> 4)
        # 将 链表 转成 列表 
        data = " <-> ".join([str(v) for v in self])
        return f"{self.__class__.__name__}({data})"

    def foreach(self, consumer: Callable[[Any], None]) -> None:
        """链表 可迭代、消费一个元素元素"""
        for v in self:
            consumer(v)

    def map(self, function: Callable[[Any], Any]) -> LinkedList:
        """链表 映射、消费一个元素、返回一个新元素 组成的链表"""
        # 创建一个 新的链表对象 
        new_linked = self.__class__()
        # 遍历 链表 
        for v in self:
            new_linked.add(function(v))
        return new_linked

    def filter(self, predicate: Callable[[Any], bool]) -> LinkedList:
        """链表过滤、消费一个元素、返回满足条件的所有元素组成的链表"""
        new_linked = self.__class__()
        # 遍历 链表 
        for v in self:
            if predicate(v):
                new_linked.add(v)
        return new_linked

    def find(self, predicate: Callable[[Any], bool]) -> Any:
        """链表查找 第一个满足条件的元素、返回满足条件的第一个元素、如果找不到，返回None"""
        for v in self:
            if predicate(v):
                return v
        return None

    def index(self, predicate: Callable[[Any], bool]) -> int:
        """链表查找 第一个满足条件的元素、返回满足条件的第一个元素索引、如果找不到、返回 -1"""
        for index, v in enumerate(self):
            if predicate(v):
                return index
        return -1

    def remove_if(self, predicate: Callable[[Any], bool]) -> LinkedList:
        """删除聊表中满足条件的元素、并返回删除后的剩余元素组成的新链表"""
        new_linked = self.__class__()
        # 遍历 链表 
        for v in self:
            if not predicate(v):
                new_linked.add(v)
        return new_linked

    def __add__(self, other):
        """支持 2个链表 相加、 合并两个链表中的内容、返回一个新链表 """
        if not isinstance(other, self.__class__):
            raise TypeError("链表 只支持 和 链表 做 加法 运算")

        new_linked = self.__class__()
        # 将 两个链表中的数据 进行 合并 
        for v in self:
            new_linked.add(v)

        for v in other:
            new_linked.add(v)

        return new_linked

    def __sub__(self, other):
        """支持 2个链表相减、 返回 第一个链表 和 第二个链表 的差集 组成新链表 """
        if not isinstance(other, self.__class__):
            raise TypeError("链表 只支持 和 链表 做 加法 运算")

        new_linked = self.__class__()
        # 将 两个链表中的数据 进行 合并 
        for v in self:
            if v not in other:
                new_linked.add(v)
        return new_linked

    def __mul__(self, other: int):
        """支持 链表 和一个整数做乘法运算、代表将链表中的数据 重复 other 次"""
        if type(other) != int:
            raise TypeError("链表 只支持 和 整数 做 乘法 运算")

        new_linked = self.__class__()
        # 遍历 other 次 
        for _ in range(other):
            for v in self:
                new_linked.add(v)

        return new_linked

    def take_while(self, predicate: Callable[[Any], bool]) -> LinkedList:
        """获取链表中满足条件的数据、直到不满足条件的数据为止、返回一个新链表"""
        new_linked = self.__class__()
        # 遍历 链表 
        for v in self:
            if predicate(v):
                new_linked.add(v)
            else:
                break
        return new_linked

    def drop_while(self, predicate: Callable[[Any], bool]) -> LinkedList:
        """删除链表中满足条件的数据、直到不满足条件的数据为止、返回一个新链表"""
        new_linked = self.__class__()
        # 定义一个变量，用来控制 是否找到了 不满足条件的数据 
        flag = False
        # 遍历 链表 
        for v in self:
            if not flag and not predicate(v):
                flag = True
                # 如果 flag 为 True, 说明 找到了 不满足条件的数据
            if flag:
                new_linked.add(v)
        return new_linked

    @classmethod
    def of(cls, *args):
        """支持一次性将传入的多个数据作为 链表中的多个元素，返回一个新链表"""
        new_linked = cls()
        for v in args:
            new_linked.add(v)
        return new_linked

    class Node:
        """节点类"""
        def __init__(self, prev, value, next):
            self.prev = prev
            self.value = value
            self.next = next

        def __repr__(self):
            return f"{self.__class__.__name__}({self.value})"

if __name__ == "__main__":
    # 创建一个链表 

    ll = LinkedList.of(1, 2, 3, 4, 5, 6, 7)

    print(ll)

    # ll = LinkedList()
    # # 向尾部添加一个数据 
    # ll.add_last(20)
    # ll.add_last(30)
    # ll.add_first(10)
    # ll.add_last(40)
    # ll.add_last(50) 
    # # 向索引为 2 的位置 添加一个元素 25
    # ll.add(25, 2) 
    # ll.add(10)

    # ll = ll.drop_while(lambda v: v <= 20)

    # # ll.add_last(40)
    # # ll.remove(40)

    # print(ll)

    # for v in ll:
    #     print(v)

    # 删除 第一个元素 
    # ll.pop(0)
    # 删除 最后一个元素 
    # print(ll.pop(0))
    # ll.clear()

    # for i in range(len(ll)):
    #     print(i,  ll.get(i))

    # print(ll.get(0))
    # print(ll.get(1))
    # print(ll.get(2))
    # print(ll.get(3))
    # print(ll.get(4))

    # 10, 20, 30, 40, 50 
    # print(ll.get_node(-5))
    # print(ll.get_node(-4))
    # print(ll.get_node(-3))
    # print(ll.get_node(-2))
    # print(ll.get_node(-1))
    # print(ll.get_node(-6))
