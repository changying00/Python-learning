# Person / Manager：继承 vs 组合，以及显示方法总结

> 基于《Learning Python》相关示例的学习笔记：继承、嵌入（组合+委托）、`__getattr__`、`__repr__` / `__str__`。

---

## 一、两段代码分别在做什么

### 1. 第一段：继承（is-a）

```python
class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)  # 自己就是 Person

    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)
```

- `Manager` **是** `Person` 的子类。
- `pat` 本身就是一个 `Person` 实例（类型更具体）。
- `pat.name`、`pat.pay`、`pat.lastName()` 都直接在 `pat` 上。
- 关系：**Manager is a Person**。
- `isinstance(pat, Person)` → **True**。

### 2. 第二段：嵌入 + 委托（has-a）

```python
from person_10 import Person   # 只导入 Person 当“零件”用

class Manager:                 # 注意：没有 (Person)！
    def __init__(self, name, pay):
        self.person = Person(name, "mgr", pay)  # 里面塞一个 Person

    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)  # 拦截并改写

    def __getattr__(self, attr):
        return getattr(self.person, attr)       # 其他属性/方法转发

    def __repr__(self):
        return str(self.person)                 # 显示也要自己转发
```

- `from person_10 import Person`：只拿 `Person` 类用，**不继承**它。
- `Manager` **拥有**一个 `Person`，不是 Person 本身。
- 关系：**Manager has a Person**。
- `isinstance(pat, Person)` → **False**。

---

## 二、`self.person` 是什么意思？

### 1. 大写 `Person` vs 小写 `person`

```python
self.person = Person(name, "mgr", pay)
```

| 写法 | 含义 |
|------|------|
| `Person`（大写） | **类名**（图纸），用来创建对象 |
| `self.person`（小写） | **实例属性名**（零件的名字），可随便起 |

名字可以随便写，例如：

```python
self.p = Person(...)
self.emp = Person(...)
self.worker = Person(...)
```

只要后面统一用这个名字即可。小写 `person` 只是习惯，符合：

- 类名：`PascalCase` → `Person`
- 属性：`snake_case` → `person`

### 2. 嵌入方向（容易搞反）

**不是** `pat.person` 嵌进 Person，  
**而是** 一个 `Person` 对象嵌进了 `Manager` 实例 `pat` 里。

```
pat  (Manager 实例)
 └── .person  ──►  Person('Pat Jones', 'mgr', 50000)
                    name / job / pay / lastName / giveRaise ...
```

| 写法 | 是什么 |
|------|--------|
| `pat` | 外面的 Manager 盒子 |
| `pat.person` | 盒子里嵌着的那个 Person 对象 |
| `pat.person.name` | 直接访问内部对象 → `'Pat Jones'` |
| `pat.person.pay` | 内部对象的薪水 |

### 3. 调用路径

```python
pat = Manager('Pat Jones', 50000)

# 自己定义的方法：直接走 Manager.giveRaise
pat.giveRaise(.10)
# → self.person.giveRaise(0.10 + 0.10)  # 实际加 20%

# 没有定义的方法：触发 __getattr__ 转发
pat.lastName()
# → getattr(self.person, 'lastName')()  # → 'Jones'

# 直接摸内部对象（绕过 Manager 的 bonus 逻辑）
pat.person.giveRaise(0.10)  # 只加 10%
```

### 4. 为什么必须单独写 `__repr__`？

Python **内置操作**（`print`、`str`、`repr`、`len` 等）**不会**触发 `__getattr__`。

若不写 `__repr__`，`print(pat)` 只会得到：

```text
<Manager object at 0x...>
```

而不是内部 Person 的漂亮显示。

---

## 三、继承 vs 组合对照表

| | 继承版 Manager | 嵌入版 Manager |
|--|----------------|----------------|
| 类定义 | `class Manager(Person)` | `class Manager:` |
| 数据在哪 | 直接在 `self` 上 | 在 `self.person` 上 |
| 改写 raise | `Person.giveRaise(self, ...)` | `self.person.giveRaise(...)` |
| 其他方法 | 自动继承 | 靠 `__getattr__` 委托 |
| `__repr__` | 可继承父类 | **必须自己写** |
| 设计意图 | is-a | has-a（更松耦合） |
| `isinstance(pat, Person)` | True | False |

**一句话**：

- 继承：Manager **是** Person。
- 组合：Manager **有一个** Person；`giveRaise` 自己拦截，其余用 `__getattr__` 转发，显示用 `__repr__` 单独转发。

---

## 四、AttrDisplay：`__repr__` 改成 `__str__` 会怎样？

### 相关代码结构（概念）

```python
class AttrDisplay:
    def _gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append(f'{key}={getattr(self, key)}')
        return ', '.join(attrs)

    def __repr__(self):  # 工具类更推荐用这个
        return f'{self.__class__.__name__}({self._gatherAttrs()})'
```

### 调用规则

```
print(obj) / str(obj)
    → 先找 __str__
    → 没有就用 __repr__

repr(obj) / 交互环境输入对象回车 / 列表字典等容器
    → 只用 __repr__
    → 没有就用默认 <Class object at 0x...>
```

### 对比结果

| 场景 | 只写 `__repr__` | 只写 `__str__` |
|------|-----------------|----------------|
| `print(X)` | 自定义显示 | 自定义显示 |
| `str(X)` | 有（回退到 `__repr__`） | 有 |
| `repr(X)` | 有 | **默认地址形式** |
| 交互环境直接看 `X` | 有 | **默认地址形式** |
| 容器 `[X, Y]` | 有 | **默认地址形式** |

### 建议

- 调试/工具类 mixin（如 `AttrDisplay`）：继续用 **`__repr__`**，一次覆盖打印、交互、容器。
- 若需要“给人看”和“给开发看”两套文案，可以两个都写：

```python
def __str__(self):
    return f'{self.__class__.__name__} 实例'

def __repr__(self):
    return f'{self.__class__.__name__}({self._gatherAttrs()})'
```

### 注意：方法名要一致

若定义了 `__gatherAttrs`（双下划线），调用却写 `gatherAttrs()`，会报错。

- 双下划线会变成名称改写：`_AttrDisplay__gatherAttrs`
- 建议统一成 `_gatherAttrs`（单下划线，表示内部方法）

---

## 五、核心要点速记

1. **`Person`（类）** ≠ **`self.person`（属性）**；属性名可随便取。
2. **`pat.person`** = Manager 里面嵌着的那个 Person 实例。
3. **继承** = is-a；**组合+委托** = has-a。
4. **`__getattr__`** 只处理“实例上找不到的普通属性/方法”，**不管** 内置的 `__repr__` / `__str__` 等。
5. **只写 `__repr__`** 最省事；**只写 `__str__`** 时，`repr` 和容器显示会变丑。

---

## 六、最小可运行对照（概念示例）

```python
# --- 继承 ---
class Person:
    def __init__(self, name, job=None, pay=0):
        self.name, self.job, self.pay = name, job, pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def __repr__(self):
        return f'[Person:{self.name} ${self.pay:,}]'

class ManagerInherit(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)

# --- 组合 ---
class ManagerEmbed:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)
    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)
    def __getattr__(self, attr):
        return getattr(self.person, attr)
    def __repr__(self):
        return str(self.person)
```

两种写法对外用法可以很像：

```python
pat1 = ManagerInherit('Pat Jones', 50000)
pat2 = ManagerEmbed('Pat Jones', 50000)
pat1.giveRaise(.10)
pat2.giveRaise(.10)
print(pat1.lastName(), pat1)  # Jones [Person:Pat Jones $60,000]
print(pat2.lastName(), pat2)  # Jones [Person:Pat Jones $60,000]
```

但内部机制不同：一个靠继承，一个靠嵌入 + 委托。
