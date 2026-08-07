"""
【魔术方法】创建基于类的装饰器 GeneratorKey(*, seq=1) 、当使用某个类创建对象的时候、 如果创建对象的时候，用户传入了 id 属性、则检查 id 的值 是否 大于等于 seq 对应的值, seq 默认为 1 ， 如果大于等于 seq, 则将 seq 设置为 用户传入的值+1 、否则 raise 抛出异常 如果创建对象的时候， 用户没有传入 id 属性、 则自动给创建的对象 添加一个 id 属性、且值为 seq , seq使用后 自动 + 1 提示： 判断一个对象是否有某个属性，使用 hasattr(obj , prop) 判断 obj 对象中是否 有 prop 属性， prop 是一个字符串，代表属性名。

@GeneratorKey(seq=1)
class A:

    def __init__(self, name) -> None:
        self.name = name


    def __str__(self) -> str:
        return str(self.__dict__)


if __name__ == "__main__":
    a = A("张三")
    print(a)      # {id: 1,  name: "张三"}
    b = A("李四")
    print(b)      # {id: 2,  name: "李四"}
    c = A("王五", id=10)
    print(c)      # {id: 10,  name: "王五"}
    d = A("赵六")
    print(d)      # {id: 11,  name: "赵六"}

    f = A("陆奇", id=9) # 报错
    print(f) 
"""


class GeneratorKey:
    def __init__(self, *, seq=1):
        self.seq = seq

    def __call__(self, cls):
        decorator = self
        original_init = cls.__init__

        def new_init(self, *args, **kwargs):
            user_id = kwargs.pop("id", None)
            original_init(self, *args, **kwargs)
            if user_id is not None:
                if user_id >= decorator.seq:
                    self.id = user_id
                    decorator.seq = user_id + 1
                else:
                    raise ValueError(f"id={user_id} 必须大于等于当前 seq={decorator.seq}")
            else:
                self.id = decorator.seq
                decorator.seq += 1

        cls.__init__ = new_init
        return cls


@GeneratorKey(seq=1)
class A:

    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return str(self.__dict__)


if __name__ == "__main__":
    a = A("张三")
    print(a)
    b = A("李四")
    print(b)
    c = A("王五", id=10)
    print(c)
    d = A("赵六")
    print(d)

    try:
        f = A("陆奇", id=9)
        print(f)
    except Exception as e:
        print(e)
