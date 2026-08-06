"""
封装要求 属性尽可能私有化

属性一旦私有化， 会导致 在类的外部 无法直接操作私有化属性 、此时 按照封装的要求 可以 通过 提供 公开的 方法 操作私有属性


property 属性 :  专门解决 私有属性 公开访问 方法名随意命名问题的。

Python 官方 推荐:  私有 属性 应该提供 对应的 property 属性

property(fget, fset, fdel, doc):

    fget :  传入 私有属性的 get 访问 方法
    fset :  传入 私有属性的 set 访问 方法
    fdel :  传入 私有属性的 del 访问方法
    doc  :  传入 文档 注释


如果 一个类 给它的 所有 私有属性 提供 了 property 属性 ，那么 在 初始化方法中， 就可以直接 调用 property 属性完成赋值操作


property 属性 配合 get,  set, del 方法 ================优化===========>  采用装饰器 @property 来让代码 更加简洁



"""
import re


class Human:

    def __init__(self,name, age):
        # 给 proerty属性 进行赋值 会自动调用 set_name 方法
        self.name = name
        self.age = age

    def find_name(self):
        """公开方法允许访问私有属性"""
        return self.__name

    def set_name(self, name):
        regex = r"[\u4e00-\u9fa5]{2,4}"
        if re.fullmatch(regex, name) is None:
            raise Exception(f"{name}值必须是2~4位的中文字符")
        self.__name = name

    def del_name(self):
        """删除私有属性"""
        del self.__name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if not isinstance(age, int):
            raise Exception(f"{age} 值类型必须是 int ")

        if age < 0:
            raise Exception(f"{age} 值 不能小于 0")
        self.__age = age

    # 给 当前 类 中的 私有属性 添加 property 属性
    name = property(find_name, set_name, del_name)
    # 给 私有属性 age 添加 property 属性
    age = property(get_age, set_age)


if __name__ == "__main__":
    # 创建一个人类对象
    p = Human("小明1", 20)

    # 修改 对象的名字
    #  p.name 中的 name 是 property 属性，会自动调用 对用的 set_name 方法
    # p.name = "张三"

    # 获取 该对象的名字
    # p.name 中的 name 是 property属性 、会 自动调用 对应的 get_name 方法
    # print(p.name)

    # 删除 当前 对象的 name 属性
    # p.name 中的 name 是 property属性，会 自动调用 del_name 方法
    # del p.name

    # # p.name = "张3"
    # # 将 当前对象的名字 更改为张三
    # p.set_name("张3")

    # # 获取 该对象的姓名
    # print(p.get_name())

