# 函数

> 是一组有机的代码组合、能够实现某个特定的功能 。函数可以屏蔽掉代码的具体实现，调用者只需要关心函数的作用，而不需要关心函数的具体实现。  
> 
> 函数 可以 理解为 是一个 存储 多个任务(指令) 的容器 ~~~

## 函数的特点

1. 函数有非常强的复用性 ~~~ 
2. 函数有非常强的独立性 ~~~

## 函数的定义方式

> 函数 使用 关键字 `def`  进行定义 。
> 
> 函数名：  是一个标识符、需要遵循 标识符的命名规则
> 
> 函数名 后面 必须 紧跟 一个 小括号 ，这个小括号 是用来标记 该标识符 是一个函数的 。 
> 
> 小括号 中 可以设置 函数 需要使用的 额外数据 (参数列表)
> 
> `:`  代表 一个函数块的开始 、函数的具体实现代码 被称为 函数体  
> 
> ```python
> def  函数名(参数列表):
>     函数体
> ```

```python
def sum_1_to_100():
    """
    实现  1 + 2 + 3 + 4 + ... 100 的和
    :return:
    """
    s = 0
    for x in range(1, 101):
        s += x

    print("1 + 2 + 3 + 4 + ... + 100 = " ,  s)
```

## 函数的返回值

> 一个函数在执行任务完成后、可能会产生一个任务的结果、 如果任务的结果 需要返回给 调用者 、那么 函数 必须设置 返回值 
> 
> 在函数中 可以使用  `return` 关键字 返回 指定的数据 ~~~  
> 
> 函数 一旦执行了 return , 函数会立马结束调用、并返回结果，  如果一个函数 没有执行 return 且 结束了，那么这个函数会返回一个         None 。  一个函数在执行完 任务的时候，可以返回多个结果 、多个返回值 之间使用 逗号分隔。 此时 函数返回的多个结果 会自动封装一个元组 返回给调用者 

```python
def sum_1_to_100():
    """
    实现  1 + 2 + 3 + 4 + ... 100 的和
    :return:
    """
    s = 0
    for x in range(1, 101):
        s += x

    return s
```

## 函数的参数类型

- 位置参数 :    调用函数的时候，必须给 位置参数 按照 位置传递 数据 、不能少传、 也不能多传
  ```python
  def sum_range(m, n):
      """
      实现  m ~ n 所有的连续自然数的和
      :return:
      """
      s = 0
      for x in range(m, n + 1):
          s += x
  
      return s
  ```
- 默认参数 ： 带有 默认值的参数 被称为 默认参数 ， 默认参数在调用的时候 可传 可不传， 默认参数出现 必须定义在所有 位置参数的 后面
  ```python
  def sum_range(m, n=None, step=1):
      """
      实现  m ~ n 所有的自然数的和 (步长 默认为 1)
      :return:
      """
      if n is None:
          m, n = 0, m
  
      s = 0
      for x in range(m, n + 1, step):
          s += x
  
      return s
      
    
  print(sum_range(10)) 
  print(sum_range(10, 100))
  print(sum_range(10, 100, 2))
  ```
- 关键字参数 :   在 `*`  后面的参数 是 关键字参数、关键字参数在调用函数的时候，必须通过 关键字传入参数 ！！！ 
  ```python
  def sum_range(m, n=None, *, step=1):
      """
      实现  m ~ n 所有的自然数的和 (步长 默认为 1)
      :return:
      """
      if n is None:
          m, n = 0, m
  
      s = 0
      for x in range(m, n + 1, step):
          s += x
  
      return s
  
  
  print(sum_range(10, 100, step=2))
  ```
- 不定项位置参数 (可变位置参数) ：  通常使用  `*args`  来表示 ~~~, 调用的时候可以传 0 ~ n 个参数，参数被组装成元组类型
  ```python
  def sum_numbers(*args):
      """
      实现 多个数字求和
      :param args:
      :return:
      """
      s = 0
      for x in args:
          s += x
  
      return s
  
  
  print(sum_numbers(1, 2, 3, 4, 5, 6, 7))
  ```
  ```
    **不定项位置参数 出现在 默认参数的后面 、关键字参数的 前面 **
  ```
- 不定项关键字参数 ： 通常使用 `**kwargs` 来表示 ,  调用的时候 可以传入0 ~ n 个 关键字参数、关键字参数会被组装成 字典类型
  ```python
  def test(*args, key=None, **kwargs):
     print("args:", args)
     print("kwargs:", kwargs)
  
  
  test(1, 2, 3, 4, c=3, key="123")
  ```
  ```
   **kwargs 参数后面 只能出现在 所有参数的 尾部 **
  ```

## 不可变类型值传递

> 不可变类型 作为参数 进行传递 、传递的是 值、 在函数内部 对 值得任何修改 ，都不会影响函数 外部定义的变量 ~~~

```python
def increment(a):
    """将 a 的值 自增 1"""
    a += 1
    
# 整数是 不可改变的数据类型 
a = 10 
# 调用 increment函数、将 a 的值 进行自增 
increment(a)

# 输出 a 的值 
print(a)     #  10
```

## 可变类型引用地址传递

```python
def increment(ls):
    """将列表中的第一个元素增加1"""
    ls[0] += 1
    


# 整数是 不可改变的数据类型 
ls = [10] 
# 调用 increment函数、将 ls 的值 进行自增 
increment(ls)

# 输出 ls 的值 
print(ls)

```

# 匿名（lambda）函数

> 匿名函数是一种 非常特殊的函数 、 没有名字的函数 ~~~ 。
> 
> 在 python 语言中，  只有 简单函数(函数体中有且只有1行代码)才可以 使用 匿名函数的形式来表示。
> 
> 万物皆为对象，所以 python中的函数 也可以理解为是一个对象，可以将一个函数 赋值给 一个变量、那么就可以通过变量来调用匿名函数
> 
> ```
> lambda 参数列表: 函数体
> ```

**如果函数体中包含 return 关键字 、 必须 省略 return **

# 函数的种类 

> 函数 根据 返回值 和 参数 的不同， 可以分为 5大类 函数 、分别是 任务型函数、生产型函数、消费性函数、功能型函数、断言型函数。

##  任务型函数

如果 一个函数 既没有 参数 、也没有 返回值 、那么这个函数 被称为 任务型函数 

```python
"""
    编写一个 execute 函数、 该函数可以用来执行任务 ~~~

        1.  怎么 让 execute 执行 任务 ？？？
              使用 任务型函数  (   )
        2.  任务型函数 execute 有 吗 ？？？
               没有 
        3.  怎么 让 execute 有 任务型函数 ？？？
               将 任务型函数 作为 execute 函数的参数 

        4.  现在 execute 有任务型函数了吗 ？？？
              有 
        5.  可以执行任务吗 ？？？
             可以 
"""


def execute(task_func):
    """
       执行任务 
    """
    task_func()


# execute 函数 怎么去执行任务 ？？？

# 1. 使用 execute 函数 打印 一个 hello world !!!

execute(lambda: print("hello world")) 

# 2. 使用 execute 函数 发送一个邮件 给张三 
execute(lambda: print("正在发送邮件给张三"))

```

## 生产型函数

如果 一个函数 没有 参数 、但有 返回值 、那么这个函数 被称为 生产型函数 

```python
import random 

def generator_ramdom_number():
    return random.random()

```

## 消费型函数

如果 一个函数 有 参数 、但没有返回值 、那么这个函数 被称为 消费型函数 

```python
"""
    消费型函数： 有参数、但没有返回值 , 职责是 消费数据 

     编写一个 foreach 函数 、遍历可迭代对象中的 数据 、并消费 每一个数据  

     1.  如何 消费 可迭代对象中的 每一个数据  ？？？

            让 消费型函数 负责 消费 可迭代对象中的数据 

    2.   foreach 函数中 有消费型函数吗 ？？？

            没有 

    3.   怎么 让 foreach 函数 拥有 消费性函数 

            给 foreach 添加一个 参数 、该参数 是一个消费型函数

    4.   当有 消费型函数后，怎么 办？？？
            让 消费型 函数 负责 消费 可迭代对象中的每一个数据 

"""

def foreach(iterable, consumer_func):

    # 使用 for ... in 遍历 可迭代对象 
    for val in iterable:
        # 消费 val 
        consumer_func(val)


# 怎么使用 foreach 函数 消费数据 

# 1. 使用 foreach 函数 打印 列表中的每一个元素 

ls = [23, 65, 86, 67]
foreach(ls, lambda x: print(x))

```

## 功能型函数

如果 一个函数 有 参数 、且有返回值 、那么这个函数 被称为 功能函数 。

功能型函数 既是生产型函数 、也是 消费型函数 ~~~ 

```python
"""
功能型函数： 既有参数、又用返回值 。 消费数据并生产数据 ~~~ 


编写一个 computed 函数 、完成 2个数字 的计算 ~~~~

    1. computed 函数 不知道 该对 2个数字 做什么运算 ， 怎么办 ？？？

        需要 使用 一个 功能型函数 完成 2个数字的运算、并返回一个运算结果 

    2. computed 函数 需要添加一个 功能型函数 作为 参数 


"""

def computed(a, b, function):
    """完成 2个数字 的计算"""
    return function(a, b)


# 怎么使用该函数 
# 1. 使用 computed 函数 完成 2个数字求和 
ret = computed(3, 5, lambda x, y: x + y)

print(ret)

# 2. 使用 computed 函数 完成 2个数字 求幂次方 

ret = computed(3, 5, lambda x, y: x ** y)
print(ret) 

# 3. 使用 computed 函数 比较 2个数字的大小 
ret = computed(3, 5, lambda x, y: x > 5)

print(ret)
```

## 断言型函数

是一种特殊的功能性函数 、 消费数据 并返回一个 boolean 类型的结果 ~~~ 、可以实现数据过滤和筛选！！！

```python
"""
 断言型函数：  消费数据并返回 bool 


 编写一个 filter 函数 , 可以将 可迭代对象 进行 过滤并保留 满足条件的数据、返回一个列表 ~~~ 

    1. 过滤条件怎么写 ？？？

         可以给 filter 提供一个 断言型函数 
 
"""
import inspect


def check_function_params(function, item, index):
    # 获取 消费者 函数 传入的参数个数
    sign = inspect.signature(function)
    # 获取参数的个数
    params_count = len(sign.parameters)
    # 如果 消费者 只消费 1 个参数、则 默认消费 item
    if params_count == 1:
        return function(item)
    elif params_count == 2:
        # 如果 消费者 消费 2 个参数、 则 默认 消费 item 和 index
        return function(item, index)
    else:
        raise Exception("消费的参数个数是1 ~ 2个、实际得到的个数是" + str(params_count))


def filter(iterable, predicate):
    """过滤并保留满足条件的元素"""
    new_ls = []
    for index, item in enumerate(iterable):
        # 调用 check_function_params 函数
        if check_function_params(predicate, item, index):
            new_ls.append(item)

    return new_ls


# 怎么使用 filter 
# 1. 定义一个元素、并使用 filter 过滤并 保留 元组中 大于 3 的所有数据 
tp = (1, 2, 3, 4, 5, 6)

ret = filter(tp, lambda x: x > 3)

print(ret)

# 2. 定义一个 列表 ，存储多种类型的数据 、使用 filter函数 过滤并保留 列表中所有的 字符串 
ls = [1, 2, "abc", "yxy", True,  lambda x: print(x),  {1, "2", 3},  "ttt"]

ret = filter(ls, lambda x: type(x) == str)

print(ret)
```

# 参数类型/返回值标注

类型标注 可以 对 函数 起到 两个作用 。 1)  对编写函数体中的代码起到 `代码提示` 作用，  2)  对调用函数的 地方 起到 `警告` 作用 

- 真实类型标注 :   直接在 参数的后面 标记它的数据类型  (多适用于 简单类型、例如 int , float,  str,  bool  等类型)
  ```python
  def sum(a: int,  b: int) -> int:
    
    return a + b
  ```
- 列表类型标注：
  
  a)  list :  只能标注是一个列表 、无法标注 列表中元素的类型
  
  b)  typing.List , 该标注 可以限定元素的类型
  ```python
  from typing import Any
  
  # list 类型标注
  def sort(ls:  list) -> Any:
     pass
  
  
  # 限定列表中元素的类型标注
  from typing import List
  
  def sort(ls:  List[int]):
      pass
  ```
- 元组类型标注:
  
  a)  tuple:  只能标注是一个元组 、无法标注 元组 中元素的类型
  
  b)  typing.Tuple :  该标注 可以限定元素的类型
  ```python
  # tuple 类型标注
  def test(tp: tuple) -> None:
      pass
    
  
  #  限定元组中元素的类型标注
  from typing import Tuple
  #  限定元组中数据 的个数 和类型
  def test(tp: Tuple[int, str]) -> None:
      pass
        
  # 限定元组中数据 类型
  def test(tp: Tuple[int, ...]):
      pass
  ```
- 集合类型标注 
  
  a)  set ：  只能标注 是一个 集合 、无法标注 集合中数据的类型 
  
  b）typing.Set  :  可以标记 集合 和 集合中元素的类型 
  ```python
  # set 类型标注
  def test(collect:  set):
     pass
  
  
  # 限定集合中元素的类型标注
  from typing import Set
  
  def test(collect:  Set[int]):
      pass
  ```
- 字典类型标注 
  
  a)  dict :  只能标注 是一个 字典 、无法标注 字典中 键和值的类型 
  
  b)  typing.Dict  :  可以标注字典类型 和 字典中的 键和值的类型 
  ```python
  # dict 类型标注
  def test(dct:  dict):
     pass
  
  
  # 限定集合中元素的类型标注
  from typing import Dict
  
  def test(dct:  Dict[str, int]):
      pass
  ```
- 可迭代类型标注 
  
  a)  typing.Iterable  :  可以标注 类型是 可迭代的、且支持标记 可迭代对象中的数据类型 
  ```python
  from typing import Iterable
  
  def test(iterable:  Iterable[str]):
      pass
  ```
- 可调用类型标注
a)  typing.Callable  :  可以标注 类型是 可调用的 (函数) 、且支持 标记 函数的 参数类型 和 返回值类型 
  ```python
  
  from typing import Callable, Any
  
  def test(func:  Callable[[int, str], Any]):
      pass
  ```
- 多类型标注 
  
  a)  typing.Union :   可以让某一个参数 同时支持 多种数据类型 
  ```python
  from typing import Union,  List,  Tuple , Any
  
  # 限定函数的参数类型是 int 或者 str
  def test(arr:  Union[int, str]):
      pass
    
  
  # 限定函数的参数类型是列表(列表中的数据类型任意)或者元组 (长度为2，且第一个数据是 int, 第2个数据任意类型)  
  def test(arr:  Union[List[Any],  Tuple[int, Any]]):
      pass
  ```

# 函数-递归调用

> 是一种 函数 调用 行为 ， 描述的是 函数 自己调用 自己的过程 ~~~ 。
> 
> 递归调用 默认是 有深度限制的， 值为 1000 ，可以通过 系统模块中的方法  `sys.setrecursionlimit(n)`  进行 修改限制
> 
> 递归 的性能是 非常 差的 、在实际应用中， 能不用递归解决问题的， 尽量不要使用 递归 ~~~ 

## 递归函数编写三要素

- 必须 非常 清楚的了解 递归函数 的含义 ~~~
- 找到 递归的解题思路 ~~~
- 必须 找到 递归的 收敛(终止递归)条件

```python
"""
使用 递归 实现 1 + 2 + 3 + ... + 100 求和 ！！！

  1 + 2 + 3 + ... 100  =  100 +  前 99 项的和

  前 99项的 和 =  99 + 前 98 项的 和
  前 98项的 和 =  98 +  前 97 项的和
  ...
  前 2项的 和  =  2 + 前 1项的 和
  前 1项的 和  =  1  (收敛条件)

  结论 ：  前 n 项 的和  =  n + 前 n - 1 项的和
  
"""
def recu_sum(n):
    """求 前 n 项的 和"""
    # 定义递归的收敛条件
    if n == 1:
        return 1

    return n + recu_sum(n - 1)
```

# 函数的嵌套

在函数体中定义函数 

## 变量的作用范围

全局变量： 在 模块 上下文环境中 定义的变量。  作用范围:  从 定义的位置开始 、都能使用 该变量 ~~~ 

局部变量:  在 函数 上下文环境中 定义的变量。  作用范围： 从 定义位置开始， 到函数结束。

非局部变量:  是一种 特殊的局部变量， 在 嵌套函数中，外部函数中的定义 被称为 非局部变量

内置变量 :  是 python 官方 天生自带的变量 。 

在 函数中 使用一个变量 ，默认查找顺序 :  局部变量 ->  非局部变量 -> 全局变量  -> 内置变量 --> ERROR

global : 可以在函数内部中 用来标记 某个变量 来自 全局变量 

nonlocal : 可以在内部函数 用来标记 某个变量 来自 非局部变量 

```python
y = 10


def test():
    # 用来标记 在函数中使用的变量 y 来自 全局变量
    global y
    y = y + 20
    print(y)


test()
# 值是多少？？？？
print(y)
```

```python
y = 10


def test():
    y = 100

    def inner():
        # 使用 nonlocal 标记 y 来自 非局部变量
        nonlocal y
        y += 10
        print(y)

    inner()


test()
```

## 闭包

> 闭包 是一种特殊的 函数嵌套 。 外部函数 返回 内部函数 的 引用对象， 这种现象 就被成为 闭包 。

### 作用

- 延长非局部变量的作用范围 
  ```python
  def generator_unique_id():
     """生成一个唯一连续的数字"""
      # 非局部变量 
      k = 0
  
      def inner():
          nonlocal k
          k += 1
          return k 
  
      return inner
  
  
  out = generator_unique_id()
  
  print(out())
  print(out())
  print(out())
  print(out())
  print(out())
  ```
  
  **滥用闭包技术 可能会导致 内存溢出风险~~~**
- 装饰器 decorator

## 装饰器 decorator

装饰器 本质上 是 一个 闭包技术 , 在 不更改 原有的 函数 代码 基础上 ， 对 函数的 功能 进行增强的一种操作 ~~~ 

### 编写装饰器 的 步骤

1. 定义一个外部 函数 、 该函数 需要提供 1个参数(要装饰的目标函数对象)
2. 定义一个内部 函数 、内部函数 的参数 是 要装饰的目标函数参数列表, 通常 可以使用 *args 和 **kwargs 表示所有参数
3. 内部函数中 编写 在 调用 目标函数 前 的 装饰代码  (非必须代码)
4. 内部函数中 调用 目标 函数 、并 获取 目标函数的执行结果  
5. 内部函数中 编写 在 调用 目标函数 后的 装饰 代码 (非必须代码) 
6. 内部函数 必须 返回 目标函数 执行的结果 
7. 外部函数 返回 内部函数的 引用对象 (构成 闭包技术)

```python
import time
import functools


def logs(func):

    @functools.wraps(func)
    def logs_wrapper(*args, **kwargs):
        # 记录 访问时间 、 目标函数名， 参数 
        visit_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        # 获取 要装饰的 目标函数的名字
        func_name = func.__name__
        # 调用 目标函数、并获取目标函数的执行结果
        ret = func(*args, **kwargs)
        # 输出 日志信息 
        print(f"{visit_time}访问了{func_name}函数，参数是{args}和{kwargs}, 执行结果是{ret}")
        
        return ret

    return logs_wrapper


def timer(func):
    @functools.wraps(func)
    def timer_wrapper(*args, **kwargs):
        # 在目标函数执行前 获取当前时间
        start = time.time()
        # 调用 目标函数
        ret = func(*args, **kwargs)
        # 调用函数后 记录当前时间
        end = time.time()
        print(f"函数{func.__name__}执行时长是{end - start}秒")

        return ret

    return timer_wrapper
```

### 使用装饰器

在要装饰的目标函数对象上、使用 @ + 装饰器名字 即可

```python
@logs
def sum_num(a, b):
    """求2个数字的和"""
    return a + b


@logs
@timer
def max_num(a, b):
    """求2个数字的最大值"""
    return a if a > b else b
```

### 装饰器的本质  

> 装饰器 是 python 语言 提供的一种 代码语法糖 ， 一个函数中 添加了 一个装饰器 、等价于 调用 装饰器函数 传入 目标函数
> 
> `sum_num` 函数 上添加了 `logs` 装饰器， 当程序 遇到 `sum_num` 的时候，会自动被解析为  `logs(sum_num)`
> 
> 所以 当 打印  `sum_num` 对象的时候， 会返回  `logs_wrapper` 函数对象, 且此时 调用 `__name__`  获取函数名时，得到的是 `logs_wrapper`
> 
> 如果希望  `__name__`  返回真正的 函数名，需要在 `logs_wrapper` 函数上 添加一个   `@functools.wraps(func)` 装饰器

### 装饰器外部函数特点

一个目标函数 一旦使用 装饰器 ，例如 sum 函数 添加了一个装饰器 @logs ，那么 当 python解析器 解析到 sum 函数定义的时候，

会 将 sum 函数 转成  `sum =  logs(sum)`

> 装饰器外部函数 对 同一个目标函数 永远 只执行一次 ，  那么就意味着 装饰器 外部函数中的定义的变量和数据  对 同一个目标函数 而言共享数据 ， 针对 不同的目标函数 、外部函数中的变量 是 相互独立的 ~~~

```python
import functools

def counter(func):
    """ 记录函数执行的次数"""
    count = 0

    @functools.wraps(func)
    def counter_wrapper(*args, **kwargs):
        # 使用 外部函数中定义的变量 
        nonlocal count
        # 调用目标函数
        ret = func(*args, **kwargs)

        count += 1
        # 将函数的调用次数 添加到 counter_wrapper 对象中 
        setattr(counter_wrapper, "counter", count) 

        return ret 
    
    return counter_wrapper


@counter
def test():
    print("hello")

@counter
def test2():
    print("world")


test()
test()
# 获取调用次数
print(test.counter)

# 获取 目标函数 test2 调用次数
test2()
print(test2.counter)

test()
# 获取调用次数
print(test.counter)

```

### 带参数的装饰器

在 装饰器 的 外层 再定义 一个 函数 、该函数 可以 定义装饰器 需要的参数 ~~~

```python
def check_params_type(*args, **kwargs):
    """检查参数类型"""
    def check_type_outer(func):
      
        @functools.wraps(func)
        def check_type_wrapper(*func_args, **func_kwargs):
            # 校验参数类型 
            if len(args) != len(func_args) or len(func_kwargs) != len(kwargs):
                raise Exception("参数个数错误")

            # 遍历 args 
            for index, arg_type in enumerate(args): 
                # 获取 index 位置传入的值 
                val = func_args[index]

                if not isinstance(val, arg_type):
                    raise Exception(f"{val}的类型和 {arg_type.__name__}不兼容")

            # 遍历 kwargs
            for key, val_type in kwargs.items():
                # 获取 key 对应的值 
                val = func_kwargs.get(key, None)

                if not isinstance(val, val_type):
                    raise Exception(f"{val}的类型和 {val_type.__name__}不兼容")

            # 调用目标函数、并返回执行的结果
            return func(*func_args, **func_kwargs)
        
        return check_type_wrapper
    
    return check_type_outer


@check_params_type(int, int)
def sum(a: int, b: int):

    return a + b


print(sum(1, 2)) 
```

# 生成器

## 迭代器 iterator

迭代器是一种 特殊的可迭代对象 ， 每调用一次 next 内置函数 可以获取 迭代中的一条数据 并移除该数据、当 迭代器中所有的数据获取完成后、再次使用 next 函数 会产生一个 StopIteration 错误！！！

**可以使用 iter 内置函数 将 任意可迭代 对象转成 迭代器 ,  迭代器不能使用 len函数获取长度**

## 生成器 generator

生成器 是一种 特殊的 迭代器 、生成器拥有迭代器的所有特点 。

生成器 可以 节省空间内存 、 生成器 可以 表示 无穷个数据 ~~~

## 生成器的实现方式 

- 元组 生成 推导式 
  ```python
  # 使用元组生成推导式 构建一个生成器
  gen = (x for x in range(1, 101))
  
  # 获取生成器中的数据 
  print(next(gen))
  print(next(gen))
  
  # 不能使用 len函数 获取生成器的数据个数
  print(len(gen))
  ```
- yield 函数
  
  在函数中 使用 yield 关键字、当调用 next 的时候，会返回数据 并挂起程序 、直到 下一次的 next 调用 从挂起位置 继续向下执行 ~~~
  ```python
  def test(): 
      i = 0
      while True:
          yield i 
          i += 1
  
  # 调用 test 函数 构建一个 生成器, 此时不会执行函数体中的代码
  gen = test()
  
  for x in gen:
      print(x)
  ```

# 内置函数

- abs(x) :  求 一个数字的绝对值
  ```python
  a = -3.1
  print(abs(a))
  ```
- all(iterable) :  判断一个可迭代对象中的数据是否全部是 True (包含隐式转换)
  ```python
  ls = [1, 2, 3, 4, 5]
  # 使用 all 验证 列表是否是 已排序的
  is_sorted = all([ls[x] < ls[x+1] for x in range(len(ls[:-1]))])
  print(is_sorted)
  ```
- any(iterable) :  判断一个可迭代对象中的数据是否包含 True (包含隐式转换)

<br/>

- bin(x) : 将一个数字 转成 二进制、返回字符串
- oct(x) : 将一个数字转成 八进制 、返回字符串
- hex(x) : 将一个数字转成 十六进制 、返回字符串
- int(x) :  将一个数字转成 整数
- int(str, radio=10) : 将一个指定进制的 字符串 转成整数
  
  <br/>
- pow(x, y) :  求 x 的 y 次幂 、等价于  `x ** y`
- round(x, n) :  将 x 小数 保留 n 位 小数

> 银行算法：  四舍六入五成双
如果要保留的 位数 后面的数字 是 <=4 , 则 舍去
如果要保留的 位数 后面的数字是 >=6,  则 进 1
如果要保留的 位数 后面的数字 是 5，
如果 5 后面 还有 非0数字， 则 进 1
如果 5 后面 没有任何数字 或者 全是 0， 那么 需要 看 5 前面的数字
> 
> 5前面的数字 如果 是 <= 6, 则 偶数 进 1， 奇数 舍去
如果 是 > 6 , 则 奇数 进 1，  偶数 舍去 ~~

- ord(c) :  获取一个字符对应的码点
- chr(x) :  将一个码点数字 转成对应的字符
- ascii(str) : 将一个字符串中的字符 以 asciii形式表示、如果字符超出了 ascii范围， 以 \u 后跟 16进制数 来表示字符
- dir(obj) : 查看指定对象的属性信息
- help(obj.attr) : 查看 对象属性信息的帮助文档
- divmod(x, y) :  获取 x 和 y 的 商 和 余数
- hash(x) :  获取 指定数据的 hash值 、 数据必须是 不可变类型
- id(x) : 查看 某个数据的 地址信息
- isinstance(obj, Type_or_Tuple) :  判断 一个 对象是否是 指定的数据类型
- iter(iterable) : 将可迭代对象转成 迭代器
- next(iterator) : 获取迭代器中的数据

<br/>

- max(iterable, key=None) : 获取可迭代对象中的最大值
  > key 如果传入 ，是一个功能性函数 、可以用来设置 比较大小的规则
功能性 函数 消费 可迭代对象中的数据 , 返回一个 权重值 、根据权重值 比大小
- min(iterable, key=None) : 获取可迭代对象中的最小值
  ```python
  ls = [
      {"name": "张三", "age": 20, "gender": "男", "score": 75},
      {"name": "李四", "age": 20, "gender": "男", "score": 85},
      {"name": "王五", "age": 20, "gender": "男", "score": 65},
      {"name": "赵六", "age": 33, "gender": "男",  "score": 95},
      {"name": "陆奇", "age": 16, "gender": "男", "score": 35},
  ]
  
  # 使用 max函数 获取列表中 年龄最大的人
  print(max(ls, key=lambda dct: dct.get("age")))
  ```
- sorted(iterable,  key=None,  reverse=False) :  将可迭代对象进行 排序、并返回排序后的 列表
  > key 如果传入 ，是一个功能性函数 、可以用来设置 比较大小的规则
功能性 函数 消费 可迭代对象中的数据 , 返回一个 或多个 权重值 、根据权重值 比大小
  ```python
  ls = [
      {"name": "张三", "age": 20, "gender": "男", "score": 75},
      {"name": "李四", "age": 20, "gender": "男", "score": 85},
      {"name": "王五", "age": 20, "gender": "男", "score": 65},
      {"name": "赵六", "age": 33, "gender": "男",  "score": 95},
      {"name": "陆奇", "age": 16, "gender": "男", "score": 35},
  ]
  
  # 将列表 中的数据 按照 年龄 从大到小排列 , 如果年龄相同，则按照 成绩升序排列
  print(sorted(ls, key=lambda dct: (-dct["age"], dct["score"])))
  ```
- globals() :  获取 当前上下文中 全局变量组成的 字典 信息
- locals() :   获取 当前上下文中 局部变量组成的 字典 信息
- map(funcation ,  *iterable)  :  将 多个可迭代对象 进行 映射、并返回一个 map 对象(可迭代对象)   
  ```python
  ls1 = [1, 2, 3, 4]
  ls2 = [5, 6, 7, 8]
  
  # 编写一段程序、将2个列表中的元素 组装成[(1, 5) , (2, 6), (3, 7), (4, 8)]
  print(list(map(lambda x, y: (x, y) ,  ls1, ls2)))
  # 同位 相加  [6, 8, 10 , 12]
  print(list(map(lambda x, y: x + y ,  ls1, ls2)))
  ```
- filter(predicate, iterable)  :  将 可迭代对象中的数据 进行 过滤， 并返回满足条件的 filter 对象 (可迭代对象)
  ```python
  ls1 = [1, 2, 3, 4, 5, 6,7, 8]
  
  # 将 列表 1 中的数据 保留 大于 3 的数据 
  print(list(filter(lambda x: x > 3, ls1)))
  ```
