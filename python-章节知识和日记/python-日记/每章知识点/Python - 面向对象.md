# 面向对象 OOP

面向对象 是一种 编程风格 、常见的编程风格 有 面向过程、 面向对象、指令式编程 和 函数式编程 ！， 面向过程 具有代表性的语言 C 语言！

面向对象 的 三大基石：  `封装` 、 `继承`、 `多态`

## 面向过程 VS 面向对象

面向过程：  任务 按照 某种 特定的顺序 进行执行 、通过 算法 或者 调用 函数 逐步 实现 最终的任务 、 它强调的时候 任务执行的过程 ~ 

目的性非常强 、 任务非常明确 ！！  ， 多应用于 处理简单的任务 

面向对象 ：  任务进行拆分、将不同数据 和行为 组装到 不同类中 、通过类来构建对象， 通过 对象 调用 对应的行为  实现 数据的处理和传递 。面向对象 更加关注程序的设计 、可以让 程序 从一开始 就进行规划 ，后期维护性 更强 。 多用于处理 复杂的任务 

|特性|面向过程|面向对象|
|:--|--|:--|
|**基本单位**|函数或过程|对象（通过类实例化）|
|**数据和行为的关系**|数据和行为分开|数据和行为封装在对象中|
|**设计方式**|强调功能和过程，代码执行是线性的|强调对象及其交互，系统通过对象之间的消息传递进行协作|
|**可扩展性**|较差，难以应对复杂的系统结构|优于面向过程，易于扩展和修改系统|
|**易维护性**|难以维护，尤其是在复杂的系统中|更加易于维护，代码模块化，便于修改|

# 封装

封装：  将一个类中的属性 尽可能的私有化 、而公开它的方法、 从而保证了类中数据的安全、屏蔽了方法的具体实现、使调用者不需要关注 方法的具体实现代码， 通过类中 暴露 的功能 完成最终的任务即可 ！！！

## 类的概念

类 是 用来 描述 自然界 中 具有 相同 `特征`  和 `行为` 的事物统称 ！！！  

类 是 抽象的  、看不见  和 摸不着的 。 研究一个类 就是 研究这个类的 属性 (特征) 和 方法 (行为) 。

狗 类 有 什么特征 ：  有毛、 尾巴 、 四个腿、 鼻子、 眼睛、 耳朵、 嘴巴 、肤色、年龄 、性别 、品种 、 体型 、 ......

狗 类 有什么行为  ： 叫 、 吃 、 喝 、 睡 、 跑、舔 、..... 

**特征是 名词、 行为 是 动词 **

## 类的定义

使用 关键字 class 定义一个类 、 类的名字 是 标识符 、多个单词 要求 采用 大驼峰 命名法 

```python
class Person:
    """定义一个类、用来描述人类"""
    pass 


class Dog:
    """
     定义一个类、用来描述 狗类 
    """
    pass


class Computer:
    """定义一个电脑类"""
    pass
```

## `__init__` 初始化方法

创建对象的时候 ， 会 自动 调用 `__init__` 方法

属性 是 类的重要组成部分 、需要 定义 在 类的 初始化 `__init__` 方法中 、该方法的主要作用 就是 完成 属性的定义 和 初始化数据 。

```python
class Person:
    """
        定义一个类、用来描述人类
        人类有 名字 、 性别 、 年龄 等属性 
            self 代表 当前类的对象、 self 不是关键字 、也可以使用 其它变量名替代 、 建议 使用 self

    """
    def __init__(self):
        """
            a) 定义类的属性 、 b) 给属性设置初始值 
        """
        # 定义 当前类的 名字属性 
        self.name = None
        # 定义 当前类的 性别
        self.gender = None 
        # 定义 当前类的 年龄 
        self.age = 0


class Dog:
    """
     定义一个类、用来描述 狗类 
       肤色 、 年龄 、 性别     
    """
    def __init__(self, color, gender, age=0):
        # 定义一个 color 属性、用来标记 肤色
        self.color = color 
        # 定义一个 gender 属性、 用来标记 狗的性别
        self.gender = gender
        # 定义一个 age 属性、用来标记 狗的年龄
        self.age = age 


class Computer:
    """
        定义一个电脑类 
         brand (品牌) 、 颜色 、 价格
    """
    def __init__(self, brand=None, color=None, price=0):
        # 定义一个属性 brand 描述电脑的品牌
        self.brand = brand 
        # 定义一个属性 color 描述电脑的颜色
        self.color = color 
        # 定义一个属性 price 描述 电脑的价格
        self.price = price 
```

## 对象的创建和使用  

对象 是 类 的 具体实现(实例) 、 一个类 可能产生 无数个 对象 。

万物皆为对象 、 类是对象的 模板 、  对象 是 类的 实例 、 在程序中 可以通过 一个类 实例化 一个对象 ~~

```python
if __name__ == "__main__":
    # 创建一个 人类的对象, 一个类型后面 添加 小括号 就会 创建对象、就会 自动执行 __init__ 初始化函数
    person = Person()
    # 获取 person 名字
    print(person.name)
    # 将新建的对象 名字设置为 张三
    person.name = "张三"
    print(person.name)
    # 删除属性
    del person.name
    
    # 再创建一个人类对象
    person2 = Person()
    print(person2.name)
    
    print(person is person2)
    
    
    # 创建一个 狗类对象 
    dog = Dog("黑色", "公")
    
    # 获取狗的颜色
    print(dog.color)
    # 修改狗的颜色
    dog.color = "黄色"
    print(dog.color)
    # 获取狗的年龄
    print(dog.age)
    
    print(dog)
```

## 方法的定义

在 类中 、通过 def 关键字 定义的函数 被称为 方法 、 方法的第一个参数 一定是 `self`  , 当表当前对象 。 其他用法 参考 函数！！！ 

```python
class Computer:
    """
        定义一个电脑类 
         brand (品牌) 、 颜色 、 价格
    """

    def __init__(self, brand=None, color=None, price=0):
        # 定义一个属性 brand 描述电脑的品牌
        self.brand = brand
        # 定义一个属性 color 描述电脑的颜色
        self.color = color
        # 定义一个属性 price 描述 电脑的价格
        self.price = price
        # 定义一个属性 is_open 描述是否 开机
        self.is_open = False

    def open(self):
        """开机"""
        print("开机中.......")
        # 将电脑的状态 更改为 开机 ...
        self.is_open = True

    def close(self):
        """关机"""
        print("关机中.......")
        self.is_open = False

    def computed(self, *args, function):
        """计算方法"""
        return function(*args)

    def add(self, x: int, y: int) -> int:
        """计算 2个数字的和"""
        if self.is_open:
            # 使用 self 调用类中定义的 computed 方法
            return self.computed(x, y, function=lambda a, b: a + b)
        raise Exception("电脑未开机")

    def min(self, x: int, y: int) -> int:
        """计算2个数字的差"""
        if self.is_open:
            return x + y
        raise Exception("电脑未开机")


if __name__ == "__main__":
    # 创建 一个 电脑对象
    computer = Computer("Dell", "黑色", 5000)
    # 获取 电脑 的品牌、颜色 和 价格
    print(computer.brand, computer.color, computer.price)
    # 将电脑 开机
    # 类中定义的方法 可以 使用 对象来调用
    computer.open()
    # 类中定义的方法 也可以使用 类来调用
    # Computer.open(computer)

    # 调用方法、计算 2个数字的和
    ret = computer.add(3, 5)

    print(ret)

```

## `__del__` 析构方法  （不重要）

在 销毁 对象 的时候 ， 会自动 执行 `__del__` 析构方法 

```python
class Computer:
    """
        定义一个电脑类 
         brand (品牌) 、 颜色 、 价格
    """

    def __init__(self, brand=None, color=None, price=0):
        # 定义一个属性 brand 描述电脑的品牌
        self.brand = brand
        # 定义一个属性 color 描述电脑的颜色
        self.color = color
        # 定义一个属性 price 描述 电脑的价格
        self.price = price
        # 定义一个属性 is_open 描述是否 开机
        self.is_open = False
        
    def __del__(self):
        print("正在销毁电脑......")
```

## `__str__`  将 对象以字符串的形式表示

将 对象 以 更加 友好的 方式 使用 字符串 进行标识 、该魔术方法 必须返回 字符串类型 ， 内置 函数 str  在 转换对象为字符串的时候，会自动调用 `__str__` 方法

```python
class Computer:
    """
        定义一个电脑类 
         brand (品牌) 、 颜色 、 价格
    """

    def __init__(self, brand=None, color=None, price=0):
        # 定义一个属性 brand 描述电脑的品牌
        self.brand = brand
        # 定义一个属性 color 描述电脑的颜色
        self.color = color
        # 定义一个属性 price 描述 电脑的价格
        self.price = price
        # 定义一个属性 is_open 描述是否 开机
        self.is_open = False

    def __str__(self):
        # 可以通过 self.__dict__ 获取 当前对象的所有属性 组成的 字典 
        # 可以通过 self.__class__ 获取当前对象的类型 、self.__class__.__name__ 获取当前类的名字

        return f"{self.__class__.__name__}({self.__dict__})"
```

## `__eq__`  比较 两个对象的内容是否相等 

自定义的类 默认 `__eq__`  比较的是 2个对象的 地址 、如果 希望 比较 内容， 则需要在对象所在的类中 添加 `__eq__`  方法、并自定义比较规则

```python
# class Dog:
    """狗类"""
    def __init__(self, color, age):
        # color 表示肤色
        self.color = color
        # age 表示 年龄
        self.age = age 

    def __eq__(self, other): 
        # 如果 要比较的对象是 None 
        if other is None:
            return False
        # 如果 要比较的对象 和当前对象地址相同
        if self is other:
            return True 
        # 判断 other 是不是 当前类型 Dog 
        if not isinstance(other, self.__class__):
            return False 
        
        # 追个比较 属性是否相同
        return self.color == other.color and self.age == other.age


if __name__ == "__main__":

    # 创建一个狗的对象
    dog1 = Dog("黑色", 2)
    # 创建一个狗的对象 
    dog2 = Dog("黑色", 2)

    # 判断 2只狗 是不是同一个对象 
    print(dog1 is dog2)

    # 判断 2只狗的内容是否相同 
    print(dog1 == dog2)
        
```

## 属性私有化

如果 希望 类中的定义的属性 或者 方法 进行 私有化， 可以在属性名/方法名的 前面 添加  `_`  或者  `__`  

`_`   代表的是 受保护的 、 受保护的属性/方法 可以在 本类或者 子类 中使用 ，其它地方 不推荐使用、这是一种 君子协议 

`__`  代表的是 私有的 、  私有的属性/方法 只能在 本类中使用， 其他地方 不能使用 ， 私有化的属性/方法 也不是 完全私有的、如果确实需要在 类的外面时候，  可以使用  `__类名__私有属性名`   方式 进行访问 ！！！

### 私有属性的 getter, setter  

```python
class Cat:

    def __init__(self, name, age) -> None:
        self.__name = name 
        self.__age = age 

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name 

    def set_age(self, age):
        if not isinstance(age, int):
            raise Exception("传入的age值必须是 int 类型")

        if age < 0 or age > 20:
            raise Exception("age值得范围不正确, 正确得区间应该是 0 ~ 20")    
    
        self.__age = age 

    def get_age(self):
        return self.__age

    def del_age(self):
        del self.__age


if __name__ == "__main__":

    # 创建一个 猫的对象
    cat = Cat("小白", 2)

    # 调用 set 方法、完成私有属性的修改
    cat.set_name("小黑")
    cat.set_age(20)
    cat.del_age()
    print(cat)
```

**getter,  setter 方法不是 python的规范、可能会导致实际开发中 方法名 不规范问题**

### 私有属性 property 类属性

```python
class Cat:

    def __init__(self, name, age) -> None:
        self.__name = name 
        self.__age = age 

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name 

    def set_age(self, age):
        if not isinstance(age, int):
            raise Exception("传入的age值必须是 int 类型")

        if age < 0 or age > 20:
            raise Exception("age值得范围不正确, 正确得区间应该是 0 ~ 20")    
    
        self.__age = age 

    def get_age(self):
        return self.__age

    def del_age(self):
        del self.__age
    
    # 在 类中定义一个 类属性 name 
    name = property(get_name, set_name)
    # 在 类中定义一个 类属性 age 
    age = property(get_age, set_age, del_age)
    

if __name__ == "__main__":

    # 创建一个 猫的对象
    cat = Cat("小白", 2)

    # 修改 name 属性的值为 小黑 、调用 cat.name 并进行赋值操作、会自动调用 property 的 set方法
    # cat.set_name("小黑")
    cat.name = "小黑"

    cat.age = 20

    # 使用 cat 对象 调用 类中的 property 属性 ，会自动调用 property 的 get 方法
    print(cat.name)

    print(cat.age)

    # 删除 age 属性 、 会自动调用 property中的 del 方法
    del cat.age

    print(cat)
```

**解决 setter ,  getter 函数名不规范问题、 使用 property 类属性替代、 但该写法 需要同时 定义函数 和对应的 property类属性 **

### property 装饰器 （终版）

```python
class Cat:

    def __init__(self, name, age) -> None:
        self.__name = name 
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age) -> None:
        if not isinstance(age, int):
            raise Exception("传入的age值必须是 int 类型")

        if age < 0 or age > 20:
            raise Exception("age值得范围不正确, 正确得区间应该是 0 ~ 20")    
    
        self.__age = age 

    @age.deleter
    def age(self) -> None:
        del self.__age


if __name__ == "__main__":

    # 创建一个 猫的对象
    cat = Cat("小白", 2)

    # 将 猫的名字更改为 小黑
    # 当 调用 cat.name 进行 赋值的时候，会 自动调用 被 name.setter 装饰器 装饰器的 name 函数
    cat.name = "小黑"

    # 会自动调用 被 property 装饰器的 name 函数
    print(cat.name)

    cat.age = 10

    print(cat.age)

    del cat.age

    print(cat.__dict__)
```

## 静态/类 方法

 静态/类 方法 和 类 有关、 和 对象没有关系 、静态/类 方法 可以直接使用 类 来调用， 也支持 使用 对象来调用，但不推荐使用对象调用 

```python
from typing import List, Callable, Any


class Utils:
    """工具类"""

    @staticmethod
    def findindex(predicate: Callable[[Any], Any], lst: List[Any]):
        """查找列表中第一个满足条件的数据的索引, 如果找不到 、返回 -1"""
        for index, item in enumerate(lst):
            if predicate(item):
                return index

        return -1

    @classmethod
    def find(cls, predicate: Callable[[Any], Any], lst: List[Any]):
        # 调用 findindex 方法、查找 满足条件的索引，在根据索引 找到满足条件的数据
        index = cls.findindex(predicate, lst)
        return lst[index] if index != -1 else None



if __name__ == '__main__':
    ls = [12, 43, 6769, 98, 3456]
    # 查找第一个 大于 100的数据
    index = Utils.findindex(lambda x: x > 100, ls)

    # 创建一个对象，调用 find 方法
    data = Utils.find(lambda x: x > 100, ls)

    print(index, data)

```

## 类属性 

定义在 类 中的 属性 叫 类 属性 、 和 类 有直接关系 、可以通过 类 来调用 ， 也可以 被 对象 调用， 类属性和对应的值 被 所有类的 对象 共享

当 使用 对象 调用 属性的时候, 首先 会查找 是否存在对应的 成员属性， 如果 找不到 成员属性 、 则 继续 找 类属性， 如果 找到成员成员 、 则 操作 成员属性

如果 给 对象的指定属性 进行赋值运算、那么 这个属性 一定是 成员属性， 属性存在 则 覆盖原值 、 不存在 则动态添加属性 并设置值

```python
class Dog:
    # 在 类中定义的属性 被称为 类属性
    # 在 __init__ 初始化方法中 定义的属性 叫 成员属性
    val = 0

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    # 获取 类中的 val 属性
    dog = Dog("小黑")
    Dog.val = 100
    # 输出 类属性 val 的值
    print(dog.val)

    # 如果 给 对象的指定属性 进行赋值运算、那么 这个属性 一定是 成员属性
    #   属性存在 则 覆盖原值 、 不存在 则添加属性 并设置值
    dog.val = 1000
    
    # 类属性的值仍旧是 100
    print(Dog.val)

    dog2 = Dog("小白")
    # 对象中 没有 成员属性，仍旧输出 类属性的值 100
    print(dog2.val)
```

# 常见的魔术方法

`__init__`   :   定义成员属性 和 赋初值操作 

`__del__`   :   析构方法、 用来 在 对象 销毁前 执行的逻辑 

`__str__`   :   将 对象以  字符串的形式 表示 

`__repr__`  :   将 对象以  字符串的形式 表示 , 主要解决在 容器中对象 的字符串表示形式， 通常返回的字符串可以通过 eval函数还原为对象

`__eq__`	 :   用来比较两个对象内容是否相等 

`__hash__`  :   用来 获取 对象的 hash值、 通常 和 字典，集合 存储的数据相关 ~~

```python
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if other is None:
            return False

        if self is other:
            return True

        if not isinstance(other, self.__class__):
            return False

        return self.name == other.name and self.age == other.age

    def __hash__(self):
        """相同内容的hash值必须相同，尽可能保证不同内容的hash值不同"""
        return hash(self.name) + hash(self.age)
    
    def __str__(self) -> str:
        return str(self.__dict__)

if __name__ == '__main__':
    dog1 = Dog("小白", 2)
    dog2 = Dog("小白", 2)

    print(dog1 is dog2)

    print(dog1 == dog2)
    # set 去重 必须保证 对象 提供 __eq__ 和 __hash__ 两个魔术方法
    set1 = {dog1, dog2}

    print(set1)

```

`__new__`  :    构造方法 、 创建对象、控制对象创建的行为

```python
class Singleton:
    """ 单例模式 """"
    # 定义一个类属性、表示 唯一对象
    __instance = None

    def __new__(cls, *args, **kwargs):

        if not cls.__instance:
            # 真正创建对象的方式
            obj = super().__new__(cls)
            cls.__instance = obj

        return cls.__instance
```

`__add__ ,  __sub__ ,  __mul__ ,  __truediv__ ,  __floordiv__ ,  __mod__,   __pow__` :  算术运算符重载

```python
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if not isinstance(other, int):
            raise Exception(f"{self.__class__.__name__}类 加法 运算支持的类型是 int")

        return Dog(self.name, self.age + other)

    def __sub__(self, other):
        if not isinstance(other, int):
            raise Exception(f"{self.__class__.__name__}类 减法 运算支持的类型是 int")

        return Dog(self.name, self.age - other)

    def __mul__(self, other):
        # 将 狗重复 other 次、 返回一个列表
        if not isinstance(other, int):
            raise Exception(f"{self.__class__.__name__}类 乘法 运算支持的类型是 int")

        return [Dog(**self.__dict__) for _ in range(other)]


if __name__ == '__main__':
    # 创建一个 狗的对象
    dog = Dog("小黑", 2)
    # 希望 dog 支持 算术运算 ，可以 将 dog 的年龄 进行加、减、乘、等计算
    print(dog - 1)

    print(dog * 3)

```

`__gt__,  __ge__,  __lt__,  __le__,   __eq__ ,  __ne__`  关系运算符重载 

```python
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Dog({self.name}, {self.age})'

    def __gt__(self, other):
        """重写 大于运算符"""
        if not isinstance(other, self.__class__):
            raise TypeError("类型不正确")

        return self.age >= other.age
        
    def __eq__(self, other):
        if other is None:
            return False
        if other is self:
            return True
        if not isinstance(other, self.__class__):
            return False 
        return self.age == other.age


if __name__ == "__main__":

    # 创建 5只小狗
    dog1 = Dog("小黑", 2)
    dog2 = Dog("小白", 1)
    dog3 = Dog("小红", 2)
    dog4 = Dog("小兰", 4)
    dog5 = Dog("小绿", 3)
    # 将 五只 小狗存储到 列表中
    ls = [dog1, dog2, dog3, dog4, dog5]

    # 将 五只小狗 默认按照 年龄 升序排序
    ret = sorted(ls)

    print(ret)
```

`__iter__`，  `__len__`  ：  将 类产生的 对象 做成 可迭代对象 

```python
class Collection:

    def __init__(self, *args):
        self.__values = args

    def __iter__(self):
        """重载 iter 魔术方法可以让当前对象 变成 可迭代对象, 该方法 必须返回一个迭代器 """
        return (x for x in self.__values)
    
    def __len__(self):
        return len(self.__values)

if __name__ == '__main__':
    col = Collection(1, 2, 3, 5, 6, 89)

    # 希望 col 支持 for ... in ， 可以在对应的类中 提供 __iter__ 魔术方法
    for x in col: 
        print(x)

    print("=================================")

    for x in col:
        print(x)
```

`__iter__` , `__next__`  :  将类产生的对象 做成 迭代器

```python
————class Collection:
    """
      创建一个对象、并返回对应的 迭代器
    """

    def __init__(self, *args):
        self.__value = args
        # 定义一个变量、记录当前数据的索引位置
        self.__index = 0

    def __iter__(self):
        """返回 self. 代表 标记当前对象为 迭代器、具体如何迭代由 __next__ 完成"""
        return self

    def __next__(self):
        # 如果 索引越界、必须抛出 StopIteration 错误！
        if self.__index >= len(self.__value):
            raise StopIteration
        # 获取当前索引位置的元素
        val = self.__value[self.__index]
        # 将索引增加 1
        self.__index += 1
        return val


if __name__ == '__main__':

    col = Collection(1, 2, 3, 4)

    print(next(col))
    print(next(col))

    for x in col:
        print(x)
    # print("==========")
    for x in col:
        print(x)
```

`__call__`  :   将 对象 变成 可调用对象 

```python
class Log:
    """不带参数的装饰器"""

    def __init__(self, func):
        self.__func = func
        # 将目标函数名绑定到当前对象中
        self.__name__ = func.__name__

    def __call__(self, *args, **kwargs):
        # 记录 目标函数的执行时间
        start = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # 记录调用的目标函数名
        func_name = self.__func.__name__
        # 调用目标函数
        ret = self.__func(*args, **kwargs)

        print(f"{start} 执行了函数 {func_name}, 执行的结果是 {ret}")

        return ret
        
        
class LimitCallCount:
    """带参数的装饰器"""

    def __init__(self, *, max_count):
        self.__max_count = max_count

    def __call__(self, func):
        # 定义一个变量、用来存储该函数调用的次数
        count = 0

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal count

            if count >= self.__max_count:
                raise Exception("函数的调用次数超出限制")

            # 调用目标函数
            ret = func(*args, **kwargs)

            count += 1

            return ret
        return wrapper
```

`__getitem__`  `__setitem__` `__delitem__`  :  实现切片技术

## 反射函数

反射:  在程序运行期间 ，可以动态的 根据 字符串名字 来获取 类中的属性、方法、对象的属性、方法等信息 。

- hasattr(obj,  str)  :   判断 obj 对象中 是否 有 str （字符串） 的属性 
- getattr(obj,  str)   :  获取 obj 对象中的  str 字符串对应的 属性值  
- setattr(obj,   str,  val)  :   修改  obj 对象中 str 字符串 对应的 属性值 为 val 
- delattr(obj,  str)  :  删除 对象中指定的 str 字符串对应的属性

# 继承

继承（Inheritance）是面向对象编程（OOP）中的一个基本特性，它允许一个类（子类）继承另一个类（父类）的属性和方法，从而实现代码的复用、扩展和层次化。

## 继承的基本用法

```python
class Dog:
    pass
    
class VipDog(Dog):
    pass
```

**python语言采用多继承方式、 继承多个类使用 逗号进行分割**

## 子类属性的初始化

```python
class Dog:
    """狗类"""

    def __init__(self, color, age):
        self.color = color
        self.age = age

    def eat(self):
        print(f"颜色为{self.color}的小狗正在吃饭....")


class VipDog(Dog):
    """贵宾犬"""

    def __init__(self, name, color, age):
        # 子类 需要 调用 父类 中 __init__ 方法，完成 父类中定义的属性初始化工作 
        super().__init__(color, age)
        self.name = name
```

**初始化子类属性必须初始化父类中定义的属性**

## 对象的创建过程

会首先 调用 当前类的 `__new__` 构造方法， 在 `__new__` 会递归的调用 父类中的 `__new__` 完成对象创建 ，当 对象创建完成后 ， 在 调用 当前类的 `__init__` 初始化方法、 在 `__init__` 会递归的调用 父类中的 `__init__` 完成 所有父类中属性的初始化工作 

```python
class Dog:
    """狗类"""

    def __new__(cls, *args, **kwargs):
        print("super dog new ....")
        # 负责创建对象 
        return super().__new__(cls)

    def __init__(self, color, age):
        self.color = color
        self.age = age

    def eat(self):
        print(f"颜色为{self.color}的小狗正在吃饭....")


class VipDog(Dog):
    """贵宾犬"""

    def __init__(self, name, color, age):
        # 子类 需要 调用 父类 中 __init__ 方法，完成 父类中定义的属性初始化工作 
        super().__init__(color, age)
        self.name = name

```

## 继承实现单例模式

```python
class Singleton:
    """定义一个单例类、谁继承该类、谁就是单例"""
    def __new__(cls, *args, **kwargs):
        instance_name = f'_{cls.__name__}__instance'
        if not hasattr(cls, instance_name):
            setattr(cls, instance_name, super().__new__(cls))
        return getattr(cls, instance_name)


class Sun(Singleton):
    pass


class Moon(Singleton):
    pass
```

## 方法的重写

当 父类中定义的方法 实现 不满足 子类的需求的时候， 子类 可以重写 父类中的方法

重写的原则：  a) 方法名和 父类必须保持完全相同 ，  b) 参数也要求和父类保持一致

调用 父类 中的 方法 可以使用  super()  进行 调用 

```python
class Rectangle:
    """长方形"""

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def perimeter(self):
        return 2 * self.width + 2 * self.length

    def area(self):
        return self.width * self.length


class Square(Rectangle):
    """正方形"""
    def __init__(self, side):
        super().__init__(side, side)
        
        
class Cuboid(Rectangle):
    """长方体"""
    def __init__(self, width, length, height):
        super().__init__(width, length)
        self.height = height

    def perimeter(self):
        return 4 * (self.width + self.length + self.height)

    def area(self):
        pass
```

## 多继承问题

如果 一个 类 继承了 多个类 、且 多个 类 均有 相同的方法，  当在 子类中 使用  super() 调用 这个方法的时候，  会 默认 先从 所有 父类 中 

一次 查找 这个方法、 如果 找不到 ，再从 父类 的 父类 中 继续查找、直到 找到为止 。

解决方案：

1.  继承类的时候  考虑 类的继承顺序 、优先继承的 类，类中的方法优先调用 
2.  使用 类 直接调用 方法、传入 当前对象 

```python
class Cylinder(Circle, Stereograph):
    """圆柱体"""

    def __init__(self, radius, height) -> None:
        super().__init__(radius)
        self.__height = height

    def perimeter(self):
        raise TypeError("该图形不支持求周长...")
    
    def area(self):
        return Circle.area(self) * 2 + super().perimeter() * self.__height
    
    def volume(self):
        return super().area() * self.__height
```

## 抽象类

当一个类 中 存在 一些 方法是这个类的标准、但没有具体实现， 那么 这些 方法可以 做成 抽象方法 

如果一个类中 包含 抽象方法、 这个类 就必须 作为  抽象类  ~

**什么情况下，需要将一个类做成抽象类  ？**  

当一个类 不允许创建 对象 的时候 

在 python 中 抽象类 中 必须保证 至少要有 1个抽象方法 才能实现 禁止 创建对象 效果 

将一个类 做成 抽象类 、只需要 让它 继承 abc.ABC （abstract class） 类 即可

如果要将 某一个方法做成 抽象方法， 只需要 在 方法上添加一个 装饰器 abc.abstractmethod 

如果 一个类 它 继承了抽象类 、那么这个 类 就必须 重写 抽象类中的 所有 抽象方法 ， 否则 这个类 也是一个 抽象类

```python
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def perimeter(self):
        """求周长方法"""
        pass 

    @abstractmethod
    def area(self):
        """求面积方法"""
        pass 
      
      
class Rectangle(Shape):
    """长方形"""
    def __init__(self, length, width) -> None:
        super().__init__()
        self.__length = length 
        self.__width = width 

    def perimeter(self):
        return (self.__length + self.__width) * 2 
    
    def area(self):
        return self.__length * self.__width
```

# 多态

针对一个方法(接口) 、通过 不同的对象 进行调用 、拥有不同的效果 ， 这种现象被称为多态 。

多态的主要实现手段 :  方法重写 。

Python 语言 具有 天然 的多态性 、这种特性 被 成为  鸭子模型 ~~~ 

# 元类

元 ：  代表 万物的开始 、 元类  描述的 就是 python语言中 所有事物的来源 

元类 是 类 的类型 、  元类 是用来  `创建` 或者 `控制类创建过程` 的 。所有 元类的 父类 是 type 

元类 也是 一个类 、 它的父类 是 object 

object  也是 一个对象 、它的类型是 type 

## 使用 type 创建一个类

```python
"""
    type(name, bases, dict)
        name : 要创建的类的 名字 、格式是一个字符串
        bases : 是一个元组 、创建类 对应的 父类 
        dict :  存放的是 构建类 需要的 类属性 和 方法 

class Dog:
    # 类属性 abc
    abc = 123

    def __init__(self, name):
        self.name = name 

    def __str__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

"""

# 使用 type 创建一个 注释中的 Dog 类 
Dog = type("Dog", (), {"abc": 123, "__init__":  lambda self, name: setattr(self, "name", name), 
                       "__str__": lambda self: f"{self.__class__.__name__}({self.__dict__})"}) 

print(Dog,  Dog.abc) 

dog = Dog("小黑")

print(dog)
```

## 使用 元类 控制 类的创建行为

>  如果 一个类  继承了 type  或者  type 的 子类 、那么 这个类 也是 一个元类 。
> 
> 继承 type 的元类 可以 控制 类的创建行为、 对象的创建行为 。。。

```python
class DogMeta(type):
    """
    DogMeta 可以 控制 Dog 的创建过程 
        1.  将 Dog 类 中 的所有 公开的 类属性 全部更改为 私有属性
        2.  将 Dog 的类名 更改为 全大写、 (需要修改 __qualname__ 中的名字)
        3.  自动 给 Dog 类 添加一个 __str__ 魔术方法
        4.  在 __call__ 中 可以 控制 对象的创建过程、实现单例模式 
    """

    def __new__(cls, name, bases, dct):
        """创建类的"""
        new_dct = {}
        name = name.upper()
        # 遍历 dct ， 并 获取 所有的公开的类属性
        for key, val in dct.items():
            if not key.startswith("_") and not key.endswith("__"):
                new_key = f"_{name}__{key}"
                new_dct[new_key] = val
            elif key == "__qualname__":
                new_dct[key] = name
            else:
                new_dct[key] = val
                # 使用 处理后的 字典 做成 对象的 类属性
        return super().__new__(cls, name, bases, new_dct)

    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        # 初始化一个 __str__ 魔术方法
        setattr(cls, "__str__", lambda self: f"{cls.__name__}({self.__dict__})")

    def __call__(cls, *args, **kwargs):
        """可以控制 对象的创建过程"""
        field_name = f"_{cls.__name__}__instance"
        if not hasattr(cls, field_name):
            # 创建对象
            instance = super().__call__(*args, **kwargs)
            setattr(cls, field_name, instance)
        return getattr(cls, field_name)


class Dog(metaclass=DogMeta):
    abc = "123"

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


if __name__ == "__main__":
    print(Dog._DOG__abc)

    # 创建一个 Dog对象
    dog = Dog("小黑", 2)

    print(dog)

    dog2 = Dog("小白", 2)

    print(dog2)

    print(dog is dog2)
```
