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
        pass

    def add_first(self, value):
        """向链条的头部添加数据"""
        pass

    def add(self, index, value):
        """向指定索引位置添加数据"""
        pass

    def __get_index(self, index):
        """检查索引范围并返回指定索引的正索引值"""
        pass

    def __get_node(self, index):
        """获取链表指定索引位置的节点对象 (索引 < 长度 一半 从 链表头部找、否则从链表尾部找)"""
        pass

    def get(self, index):
        """获取指定索引位置的元素值"""
        pass

    def pop(self, index):
        """删除指定位置的元素、并返回删除的元素"""
        pass

    def remove(self, value):
        """删除指定的元素"""
        pass

    def set(self, index, value):
        """修改指定位置的元素"""
        pass

    def __len__(self):
        """获取链表的长度"""
        pass

    def __iter__(self):
        """让链表拥有可迭代的能力、返回一个迭代器即可"""
        pass

    def __str__(self):
        """获取链表的字符串表示、例如链表中有三个元素、分别是1， 2， 3， 则返回字符串格式为  (1 <--> 2 <--> 3)"""
        pass

    def foreach(self, consumer: Callable[[Any], None]) -> None:
        """链表 可迭代、消费一个元素元素"""
        pass

    def map(self, function: Callable[[Any], Any]) -> LinkedList:
        """链表 映射、消费一个元素、返回一个新元素 组成的链表"""
        pass

    def filter(self, predicate: Callable[[Any], bool]) -> LinkedList:
        """链表过滤、消费一个元素、返回满足条件的所有元素组成的链表"""
        pass

    def find(self, predicate: Callable[[Any], bool]) -> Any:
        """链表查找 第一个满足条件的元素、返回满足条件的第一个元素、如果找不到，返回None"""
        pass

    def index(self, predicate: Callable[[Any], bool]) -> int:
        """链表查找 第一个满足条件的元素、返回满足条件的第一个元素索引、如果找不到、返回 -1"""
        pass

    def remove_if(self, predicate: Callable[[Any], bool]) -> LinkedList:
        """删除聊表中满足条件的元素、并返回删除后的剩余元素组成的新链表"""
        pass

    def __add__(self, other):
        """支持 2个链表 相加、 合并两个链表中的内容、返回一个新链表 """
        pass

    def __sub__(self, other):
        """支持 2个链表相减、 返回 第一个链表 和 第二个链表 的差集 组成新链表 """
        pass

    def __mul__(self, other: int):
        """支持 链表 和一个整数做乘法运算、代表将链表中的数据 重复 other 次"""
        pass

    def take_while(self, predicate: Callable[[Any], bool]) -> LinkedList:
        """获取链表中满足条件的数据、直到不满足条件的数据为止、返回一个新链表"""
        pass

    def drop_while(self, predicate: Callable[[Any], bool]) -> LinkedList:
        """删除链表中满足条件的数据、直到不满足条件的数据为止、返回一个新链表"""
        pass

    def clear(self):
        """清空链表中所有的数据"""
        pass

    @classmethod
    def of(cls, *args):
        """支持一次性将传入的多个数据作为 链表中的多个元素，返回一个新链表"""
        pass

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