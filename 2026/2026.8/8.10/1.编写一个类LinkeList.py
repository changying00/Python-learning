from __future__ import annotations
from typing import Callable, Any


class LinkedList:
    def __init__(self):
        # 用来存储链表中的 首链
        self.__first = None
        # 用来存储 链表中的 尾链
        self.__last = None
        # 定义一个 属性 ，用来存储链表的真实长度
        self.__size = 0

    def add_last(self, value):
        """向链条的尾部添加数据"""
        new_node = self.Node(self.__last, None, value)
        if self.__last is None:
            self.__first = new_node
        else:
            self.__last.next = new_node
        self.__last = new_node
        self.__size += 1

    def add_first(self, value):
        """向链条的头部添加数据"""
        new_node = self.Node(None, self.__first, value)
        if self.__first is None:
            self.__last = new_node
        else:
            self.__first.prev = new_node
        self.__first = new_node
        self.__size += 1

    def add(self, index, value):
        """向指定索引位置添加数据"""
        if index == self.__size:
            self.add_last(value)
            return
        if index == 0:
            self.add_first(value)
            return
        index = self.__get_index(index)
        node = self.__get_node(index)
        new_node = self.Node(node.prev, node, value)
        node.prev.next = new_node
        node.prev = new_node
        self.__size += 1

    def __get_index(self, index):
        """检查索引范围并返回指定索引的正索引值"""
        if not isinstance(index, int):
            raise TypeError("索引必须是整数")
        if index < 0:
            index += self.__size
        if index < 0 or index >= self.__size:
            raise IndexError("索引超出范围")
        return index

    def __get_node(self, index):
        """获取链表指定索引位置的节点对象 (索引 < 长度 一半 从 链表头部找、否则从链表尾部找)"""
        index = self.__get_index(index)
        if index < self.__size // 2:
            node = self.__first
            for _ in range(index):
                node = node.next
        else:
            node = self.__last
            for _ in range(self.__size - 1, index, -1):
                node = node.prev
        return node

    def get(self, index):
        """获取指定索引位置的元素值"""
        return self.__get_node(index).value

    def pop(self, index):
        """删除指定位置的元素、并返回删除的元素"""
        node = self.__get_node(index)
        self.__unlink(node)
        return node.value

    def __unlink(self, node):
        """从链表中断开指定节点"""
        prev_node = node.prev
        next_node = node.next
        if prev_node is None:
            self.__first = next_node
        else:
            prev_node.next = next_node
            node.prev = None
        if next_node is None:
            self.__last = prev_node
        else:
            next_node.prev = prev_node
            node.next = None
        node.value = None
        self.__size -= 1

    def remove(self, value):
        """删除指定的元素"""
        node = self.__first
        while node is not None:
            if node.value == value:
                self.__unlink(node)
                return True
            node = node.next
        return False

    def set(self, index, value):
        """修改指定位置的元素"""
        node = self.__get_node(index)
        old_value = node.value
        node.value = value
        return old_value

    def __len__(self):
        """获取链表的长度"""
        return self.__size

    def __iter__(self):
        """让链表拥有可迭代的能力、返回一个迭代器即可"""
        node = self.__first
        while node is not None:
            yield node.value
            node = node.next

    def __str__(self):
        """获取链表的字符串表示、例如链表中有三个元素、分别是1， 2， 3， 则返回字符串格式为  (1 <--> 2 <--> 3)"""
        if self.__size == 0:
            return "()"
        return "(" + " <--> ".join(str(v) for v in self) + ")"

    def foreach(self, consumer: Callable[[Any], None]) -> None:
        """链表 可迭代、消费一个元素元素"""
        for value in self:
            consumer(value)

    def map(self, function: Callable[[Any], Any]) -> LinkedList:
        """链表 映射、消费一个元素、返回一个新元素 组成的链表"""
        result = LinkedList()
        for value in self:
            result.add_last(function(value))
        return result

    def filter(self, predicate: Callable[[Any], bool]) -> LinkedList:
        """链表过滤、消费一个元素、返回满足条件的所有元素组成的链表"""
        result = LinkedList()
        for value in self:
            if predicate(value):
                result.add_last(value)
        return result

    def find(self, predicate: Callable[[Any], bool]) -> Any:
        """链表查找 第一个满足条件的元素、返回满足条件的第一个元素、如果找不到，返回None"""
        for value in self:
            if predicate(value):
                return value
        return None

    def index(self, predicate: Callable[[Any], bool]) -> int:
        """链表查找 第一个满足条件的元素、返回满足条件的第一个元素索引、如果找不到、返回 -1"""
        i = 0
        for value in self:
            if predicate(value):
                return i
            i += 1
        return -1

    def remove_if(self, predicate: Callable[[Any], bool]) -> LinkedList:
        """删除聊表中满足条件的元素、并返回删除后的剩余元素组成的新链表"""
        result = LinkedList()
        for value in self:
            if not predicate(value):
                result.add_last(value)
        return result

    def __add__(self, other):
        """支持 2个链表 相加、 合并两个链表中的内容、返回一个新链表 """
        if not isinstance(other, LinkedList):
            return NotImplemented
        result = LinkedList()
        for value in self:
            result.add_last(value)
        for value in other:
            result.add_last(value)
        return result

    def __sub__(self, other):
        """支持 2个链表相减、 返回 第一个链表 和 第二个链表 的差集 组成新链表 """
        if not isinstance(other, LinkedList):
            return NotImplemented
        other_values = set(other)
        result = LinkedList()
        for value in self:
            if value not in other_values:
                result.add_last(value)
        return result

    def __mul__(self, other: int):
        """支持 链表 和一个整数做乘法运算、代表将链表中的数据 重复 other 次"""
        if not isinstance(other, int):
            return NotImplemented
        result = LinkedList()
        if other <= 0:
            return result
        for _ in range(other):
            for value in self:
                result.add_last(value)
        return result

    def __rmul__(self, other: int):
        return self.__mul__(other)

    def take_while(self, predicate: Callable[[Any], bool]) -> LinkedList:
        """获取链表中满足条件的数据、直到不满足条件的数据为止、返回一个新链表"""
        result = LinkedList()
        for value in self:
            if not predicate(value):
                break
            result.add_last(value)
        return result

    def drop_while(self, predicate: Callable[[Any], bool]) -> LinkedList:
        """删除链表中满足条件的数据、直到不满足条件的数据为止、返回一个新链表"""
        result = LinkedList()
        dropping = True
        for value in self:
            if dropping and predicate(value):
                continue
            dropping = False
            result.add_last(value)
        return result

    def clear(self):
        """清空链表中所有的数据"""
        node = self.__first
        while node is not None:
            next_node = node.next
            node.prev = None
            node.next = None
            node.value = None
            node = next_node
        self.__first = None
        self.__last = None
        self.__size = 0

    @classmethod
    def of(cls, *args):
        """支持一次性将传入的多个数据作为 链表中的多个元素，返回一个新链表"""
        result = cls()
        for value in args:
            result.add_last(value)
        return result

    class Node:
        """代表 链表中的节点"""

        def __init__(self, prev, next, value):
            """
            :param prev:  上一个 节点地址
            :param next:  下一个节点地址
            :param value:  当前节点的数据
            """
            self.prev = prev
            self.next = next
            self.value = value
