# math 数学模块

- math.ceil(x) :  向上取整(离它最近的整数) 
- math.floor(x) :  向下取整 
- math.fabs(x) :   获取 x 的绝对值, 返回 一个浮点数 
- math.fsum(seq) :  将一个可迭代对象中的数据 进行求和 , 返回一个 浮点数, 序列中的数据 必须是 数字类型
- math.gcd(*integers) :  求多个整数的 最大公约数 
- math.pow(x, y)  :  求 x 的 y 次幂 , 返回一个 浮点数
- math.remainder(x, y) : 求 x % y , 返回一个 浮点数  math.sqrt(x) :  求 x 的算术平方根, 返回一个小数
- math.isqrt(x) :  求 x 的算术平方根, 返回小数的整数部分
- math.isnan(x) :  判断 x 是否是 非数 ,  float("nan") ,  x 必须是数字类型 math.isinf(x) :  判断 x 是否是 无穷 
- math.isfinite(x) :  判断 x 是否是 有穷的 , nan 既不是有穷的, 也不是 无穷的 
- math.sin(x)  :  获取 三角形 某个 角度的 正弦值   x 指的是 弧度    1° =  Π / 180 弧度 
- math.cos(x)  :  获取 三角形 某个 角度的 余弦值 , x 指的是 弧度 
- math.tan(x)  :  获取 三角形 某个 角度的 正切值 , x 指的是 弧度

```python
def get_clock_location12(radius, center=(0, 0)):
    """获取钟表中 12个刻度的坐标"""
    result = []
    # 定义一个循环, 遍历 12次 
    for x in range(12):
        # 计算 x 刻度 和 12点方向的 夹角度数 
        deg = x * 30 
        loc_x = center[0] + math.sin(deg * math.pi / 180) * radius
        loc_y = center[1] - math.cos(deg * math.pi / 180) * radius 

        result.append((round(loc_x,2), round(loc_y,2)))

    return result 
```

# random 随机模块

- random.random() : 随机返回一个 [0, 1)  的 浮点数 
- random.randint(m, n) :  随机返回一个 [m, n]  的 整数 ,  m  <= n 
- random.randrange(m, n) :  随机返回一个 [m, n)  的 整数 ,  m  < n 
- random.choice(seq) :  随机从一个 序列对象中 返回一个值 
- random.choices(seq, *, k=1) : 随机从 序列中 返回 k 个数据, 数据可能会重复出现
- random.sample(seq, *,  k=1) :   随机从 列表中 返回 k 个不重复的数据
- random.uniform(a, b) : 随机生成 [a,  b] 区间的 浮点数
- random.shuffle(ls) : 将一个列表随机打乱，返回值为None

**思考 ：  如何 使用  random.random()  方法  生成一个 [m ,  n)  的随机整数**

```
math.floor(random.random() * (n - m)) + m
```

# uuid 模块

- uuid.uuid1()  :   使用 时间戳 +  MAC 地址 + 随机数 生成 
- uuid.uuid3(namespace,  name) :  使用 命名空间 + 名字 采用 MD5 加密生成 
- uuid.uuid4()  :  随机生成、 最常用
- uuid.uuid5(namespace, name)  :  使用 命名空间 + 名字 采用 sha1 加密生成

```python
import uuid 

# 基于 时间戳 + mac 地址 + 随机值 
x = uuid.uuid1()
print(x)

# 基于名称 和命名空间 采用 md5 算法
x = uuid.uuid3(x, "py2502") 
print(x)

# 采用随机生成
x = uuid.uuid4() 
print(x)

# 使用 命名空间 + 名字 采用 sha1 算法
x = uuid.uuid5(x, "py2502")
print(x.hex, str(x))
```

## time 时间模块

- time.sleep(n)  :  将程序 睡眠 n 秒 、 n 可以一个 浮点数 
- time.time() :  获取 距离 1970年 1月 1日 经过的 秒数 (时间戳) , 精确到 纳秒 
- time.localtime() :  获取一个本地时间 对应的 时间元组对象 (由 9 部分组成, 分别是 年, 月, 日, 时, 分, 秒, 星期, 1年中的第几天, 是否采用夏令时)      星期 :  0 代表 周一 ,  1 代表 周二 ,  6 代表 周日
- time.localtime(timestamp) :  构建一个 时间元组对象, 返回一个 距离 1970年 1月1日的 时间元组对象  timestamp : 时间戳, 单位是 秒 
- time.mktime(timetuple)  :  传入 一个 时间元组 对象, 获取 对应的时间戳, 精确到秒
  ```python
  # 将时间元组 转成时间戳
  print(time.mktime(time.localtime()))
  # 也可以传入一个 包含 9个值的 元组， 顺序必须保证 年、月、日、 时 、 分、秒、星期、 一年中的第几天、 夏令时
  # 后三个值 可以任意
  print(time.mktime( (2000, 10, 10, 10 , 10, 10, 0, 0, 0) ))
  ```
- time.strftime(pattern , timetuple) :  将一个时间元组对象 转成 指定的 字符串格式
  ```python
  # 输出 当前系统时间, 且希望时间 以  2000年03月15号 12点11分24秒 格式 表示
  now = time.localtime()
  time_str = time.strftime("%Y年%m月%d号 %H点%M分%S秒", now)
  
  print(time_str)
  
  print(time.strftime("%m/%d/%Y %H:%M", time.localtime()))
  
  time_str = "2000年10-20 12:24 30秒" 
  ```
- time.strptime(string,  pattern) :  将一个 字符串 格式的 时间 转成 时间元组
  ```python
  time_str = "2000年10-20 12:24 30秒" 
  # 将上述的 字符串 转成 时间元组 对象 
  time_tp = time.strptime(time_str, "%Y年%m-%d %H:%M %S秒") 
  
  print(time_tp)
  ```

### 时间元组

时间元组 由 9 部分组成 、分别代表  年, 月, 日, 时, 分, 秒, 星期, 1年中的第几天, 是否采用夏令时) 

时间元组 对象中的数据 可以 基于 索引的方式 进行 获取 、也可以使用 时间元组 对象中的 9个属性 获取

分别是  tm_year ,   tm_mon,  tm_mday,  tm_hour,  tm_min,  tm_sec, tm_wday ,  tm_yday ,  tm_isdst

# datetime 日期和时间模块

## date 日期类 

> 用来 表示 年、月、 日 的  日期 类 

- 创建日期对象

```python
from datetime import date, datetime

# 1. 创建 一个 日期对象
d1 = date(2000, 10, 10)

# 创建一个 当前 日期对象
d2 = date.today()
# 基于 时间戳 构建一个日期对象
d3 = date.fromtimestamp(3000)
# 基于 ISO8601 日期格式 构建一个日期对象  ISO8601 日期和时间规范  %Y-%m-%dT%H:%M:%S , 格式中的 T 可以替换成空格
d4 = date.fromisoformat("2000-10-10")

print(d1, type(d1))
print(d2)
print(d3)
print(d4)
```

- 获取 日期对象的 年、月、日 、星期

```python
# 获取 日期中的年、 月、  日
print(d4.year)
print(d4.month)
print(d4.day)
# 获取 星期 ， 0 代表 周一 、 1代表 周二、 ... 6 代表周日
print(d4.weekday())
```

- 日期转时间元组

```python
# 获取当前日期 对应的时间元组对象
print(d4.timetuple())
```

- 日期格式化

```python
# 日期对象的格式化
print(d4.strftime("%Y/%m/%d"))

# 定义一个日期格式的字符串
strings = "2000年10月10日"
print(datetime.strptime(strings, "%Y年%m月%d日").date())
```

## datetime 日期和时间类

> 用来 表示 年、月、 日 、 时、 分、 秒 的  日期和时间 类 、精确到 微妙 

- 创建日期和时间对象
  ```python
  from datetime import datetime 
  
  # 创建日期和时间对象 (年, 月, 日, 时, 分, 秒, 微妙), 至少需要传入 年,月,日
  d1 = datetime(2000, 10, 10, 12, 10, 10, 23456)
  print(d1)
  
  # 获取当前系统时间 
  d2 = datetime.now()
  print(d2) 
  
  # 根据时间戳 构建一个 日期和时间对象 
  d3 = datetime.fromtimestamp(1000)
  print(d3) 
  
  # 基于 iso8601 日期规范 构建 
  d4 = datetime.fromisoformat("2025-03-24T17:12:03")
  
  print(d4)
  ```
- 获取 日期和时间对象中的 年、月、日、时、分、秒、微秒、星期
  ```python
  # 获取 日期和时间对象中 的年, 月, 日,  时, 分, 秒, 星期 
  print(d4.year, d4.month, d4.day, d4.hour, d4.minute, d4.second, d4.microsecond, d4.weekday())
  ```
- 日期和时间对象 转 时间元组
  ```python
  # 获取 时间元组
  print(d4.timetuple())
  ```
- 日期和时间对象的格式化
  ```python
  # 日期和时间的格式化
  print(d4.strftime('%Y/%m/%d %H:%M:%S'))
  
  strings = "2025年10月20号 22点12分"
  
  print(datetime.strptime(strings, "%Y年%m月%d号 %H点%M分"))
  ```

 ## timedelta 时间间隔类

- 创建时间间隔
  ```python
  from datetime import timedelta
  
  # 创建一个时间间隔对象、用来表示 2周
  week2 = timedelta(weeks=2)
  print(week2)
  # 创建一个 时间间隔对象、用来表示 2天
  day2 = timedelta(days=2)
  print(day2)
  
  # 创建一个时间间隔、用来表示 2小时
  hour2 = timedelta(hours=2)
  print(hour2)
  
  # 创建一个时间间隔、用来表示 2周零3天 5小时 30分钟 20秒
  duration = timedelta(weeks=2, days=3, hours=5, minutes=30, seconds=20, microseconds=3000)
  
  print(duration)
  ```
- 获取时间间隔的 天数、秒、 总秒数
  ```python
  # 获取时间间隔的秒 (时、分、秒 转换的总秒数)
  print(duration.seconds)
  # 获取间隔的天数
  print(duration.days)
  # 获取整个时间间隔的 总秒数
  print(duration.total_seconds())
  ```
- 日期 和 时间间隔的运算
  ```python
  # 两个日期对象 支持 减法运算 、返回 时间间隔
  d1 = date(2000, 10, 10)
  d2 = date(2010, 2, 3)
  
  # 计算 2个日期 间隔多少天
  duration = d2 - d1
  print(duration.days)
  
  # 日期 和 时间 间隔间隔 支持 加法 和 减法运算
  now = datetime.now()
  # 获取 昨天的这个时间
  yesterday = now - timedelta(days=1)
  
  # 获取明天的这个时间
  tor = now + timedelta(days=1)
  
  print(yesterday)
  print(tor)
  
  ```

# copy 拷贝模块

- copy.copy(obj)  :  将一个对象 进行 浅克隆( 将 对象中的数据  不可变类型 进行 值拷贝 ， 可变类型 进行地址 拷贝 ) 
  ```python
  import copy 
  
  class Teacher:
      def __init__(self, name) -> None:
          self.name = name 
  
  class Student:
  
      def __init__(self, name, age, teacher) -> None:
          self.name = name 
          self.age = age 
          self.teacher = teacher 
  
  
  
  stu = Student("张三", 20, Teacher("张三丰")) 
  
  # 克隆一个学生
  stu2 = copy.copy(stu)
  
  print(stu2.name, stu2.age, stu2.teacher) 
  
  stu2.teacher.name = "李四" 
  
  print(stu.teacher.name)
  
  ```
- copy.deepcopy(obj) :  将一个对象 进行 深克隆 ( 将一个对象中的数据 不可变类型  值拷贝， 可变类型 进行 递归的浅拷贝)  
  ```python
  import copy 
  
  ls = [1, 2, 3, 4 ,5 , [5, 31]]
  
  ls2 = copy.deepcopy(ls)
  
  print(ls is ls2)
  
  print(ls[-1] is ls2[-1])
  
  ls[-1].append(100)
  
  print(ls2)
  
  ```

# os 模块

- os.name :  获取操作系统的名字   （nt :  window操作系统 ，  posix : linux 操作系统 ）
- os.environ :  获取操作系统对应的环境变量 组成的字典 
- os.getcwd() : 获取 当前模块的工作目录  
- os.mkdir(path) :  根据指定的创建 创建一个 目录, a) 要创建的目录不存在， b) 父级路径必须存在
- os.makedirs(path, exist_ok=False) :  递归的创建多级目录, 默认如果目录存在，会产生一个错误，如果 设置 exist_ok为 true, 则 目录存在也不产生错误
- os.rmdir(path) :  删除 指定的 空目录
- os.removedirs(path) :  递归的删除 多层 空目录
- os.listdir(path) :  获取 指定 目录下的所有一级内容
- os.remove(path)  : 删除 指定的 文件

```python
import os 


# os.mkdir(r"D:\PycharmProjects\pythonProject\abc\xyz")

os.makedirs(r"D:\PycharmProjects\pythonProject\abc\xyz", exist_ok=True)

# os.rmdir(r"D:\PycharmProjects\pythonProject\abc")
os.removedirs(r"D:\PycharmProjects\pythonProject\abc\xyz")

dirs = os.listdir(r"D:\PycharmProjects\pythonProject")

print(dirs)
# print(os.name)

# print(os.environ.get("JAVA_HOME"))

# print(os.environ.get("PATH")) 

# print(os.getcwd()) 
```

## os.path 子模块 

- os.path.basename(path) :  获取 指定路径 最后一级的 名字 
- os.path.dirname(path) :  获取 指定路径的 父级 路径 
- os.path.abspath(path) :  获取一个路径的 绝对路径
- os.path.exists(path) :  判断路径是否存在 
- os.path.isfile(path) :  判断指定的路径是否 是 文件
- os.path.isdir(path)  :  判断 指定的路径是否 是 目录 
- os.path.isabs(path) :  判断 路径是否是 绝对路径
- os.path.getsize(filename) : 获取 文件的大小、如果是 目录，结果可能和预期的不一致
- os.path.join(basedir, *path) :  将 basedir 和 path 进行路径拼接、 path 如果是绝对路径， 则 会忽略 basedir
- os.path.split(path) :  将 指定的路径 进行拆分 、获取 一个 长度为 2 的元组 (父级路径、 名字)

# open函数 

>  `open(path, mode, encoding) `
> 
> path:  要读取/写入 的 文件 路径
> 
> mode :  默认值 是 rt
> 
> ```
> r :  读           w :  覆盖写        a :  追加写      t :  字符 (默认值)     b :  字节
> ```
> 
> encoding:  读取文件的编码方式， 只能在 字符文件读取的时候生效 、字节模式不能传入该参数

## 读取字符文件

- readable()  :  判断 文件是否 可读
- read() 如果不传入任何参数、则直接将文件中的所有数据 读取到内存中。 (适应于小文件的读取)
- read(n) :  n 代表 读取的 字符数量 , 当读取完成后 再次读取 、返回一个 空字符串
- readline() :  一次读取 1行数据, 当读取完成后 再次读取 、返回一个 空字符串
- readlines() :  一次性将文件中的所有行 读取完成、返回一个列表
- close()  :  关闭 通道

### 读取大文件

```python
f = open(r"C:\Users\admin\Desktop\test.txt", encoding="utf-8")
# 读取大文件、需要使用 循环读取， 1次 读取 1000个字符
while (text := f.read(1000)) != '':
    print(text)
# 关闭 通道
f.close()
```

### 读取小文件

```python
f = open(r"C:\Users\admin\Desktop\test.txt", encoding="utf-8")
data = f.read()
print(data)
# 关闭 通道
f.close()
```

## 读取字节文件

- read(n) :  n 代表 读取的 字节数量 , 当读取完成后 再次读取 、返回一个 空字节

```python
import io

with open(r"C:\Users\admin\Desktop\test.txt", "rb") as f:
    # data = f.read()
    # # 获取读取的结果、结果是 字符串流数据
    # print(data)
    
    bytes = io.BytesIO()
    # 一次性读取 8kb 数据到内存中
    while (binary := f.read(8 << 10)) != b'':
        bytes.write(binary)
    
    # 设置 seek 为 值 0
    bytes.seek(0)
    # 获取 流中的数据
    print(bytes.read())
```

**在使用 字节流 对文件读取的时候，不允许传入 encoding 编码**

## 写入 字符 到 文件

- write(str) :  将指定的字符串 写入到文件中 
- writelines(iterable) :  将一个 可迭代对象中的 数据 一次性写入到 文件中 （可迭代对象中的数据必须是 字符串类型） 
- writeable()  :  判断文件是否可写
- close()  :   关闭通道

```python
# 字符写入
with open(r"C:\Users\admin\Desktop\test2.txt", "wt", encoding="utf-8") as f:
    # 写入
    f.write("hello")
```

## 写入字节 到文件

```python
with open(r"C:\Users\admin\Desktop\test2.txt", "wb") as f:
    # 写入
    f.write("hello".encode())
```

### 实现文件的拷贝

```python
def copy_file(src, dest):
    """
    拷贝文件
    :param src:  文件的原始路径
    :param dest:  文件拷贝的目的地
    :return:
    """
    # 如果 dest 是目录
    if os.path.isdir(dest):
        # 获取 存储的为止
        dest = os.path.join(dest, os.path.basename(src))
    elif not os.path.exists(os.path.dirname(dest)):
        # 如果 父级路径不存在，则创建
        os.makedirs(os.path.dirname(dest))
    # 实现文件的拷贝
    with open(src, "rb") as f:
        with open(dest, "wb") as w:
            # 边读 边写
            while (binary:= f.read(8 << 10)) != b'':
                w.write(binary)
```

### 实现目录的拷贝

```python
def copy_dir(src, dest):
    """将 src 目录下的内容 拷贝到 dest 目录下"""
    if not os.path.exists(dest):
        # 创建目录
        os.makedirs(dest)

    # 遍历 目录下的所有数据
    all_files = os.listdir(src)

    for file in all_files:
        # 获取 file 的路径
        file_path = os.path.join(src, file)

        if os.path.isfile(file_path):
            # 拷贝文件到 dest/ 下
            copy_file(file_path, dest)
        else:
            copy_dir(file_path, os.path.join(dest, file))
```

# shutil 模块

- shutil.rmtree(path) :  删除一个目录 
- shutil.copyfile(src, dest) :  拷贝一个文件 到 指定的文件中 
- shutil.copy(src, dest) : 
  1. 可以实现 将一个文件 拷贝到 一个 指定的目录中
  2. 可以实现 将一个文件 拷贝到一个指定的文件中
- shutil.move(src, dest): 
- 1. 实现 将一个文件 重命名
  2. 实现 将一个文件 剪切到 指定的目录中 
  3. 实现 将一个目录 剪切到 指定的目录中 
  4. 实现 将一个 目录 重命名

# json 模块

- json.dumps(obj, skipkeys=False, ensure_ascii=True, allow_nan=True, cls=None, indent=None, default=None)
  - obj :  要序列化的对象 
  - skipkeys :  是否要跳过 不能序列化的键、 支持的键类型包含 int, float, str, bool, None
  - ensure_ascii : 是否将 非 ascii 范围内的 字符 以 unicode 表示, 默认 True
  - allow_nan : 是否支持处理 非数， 默认支持
  - indent :  设置缩进的空格数， 默认没有缩进, 以更加优雅的方式 展示数据
  - default : 是一个功能性函数、处理无法序列化的数据 , 消费的参数代表 无法序列化的数据对象， 返回 一个支持序列化的数据
用面向过程的方式 处理
  ```python
  class Dog:
      def __init__(self, name, age) -> None:
          self.name = name 
          self.age = age 
  
  class Tudou:
  
      def __init__(self, name) -> None:
          self.name = name 
          
  # 定义一个字典
  dct = {"name": "张三", "age": 20, (1, 2): "元组",  None: None, "pet": dog, "food": tudou}
  
  json_str = json.dumps(dct, skipkeys=True, ensure_ascii=False, indent=4, lambda: x: x.__dict__)
  
  print(json_str)
  ```
  - cls :  是一个继承 JSONEncoder 类的 子类 、该类 负责 处理无法序列化的数据， 和 default 的职责相同
用卖你想对象的方式 处理
  ```python
  import json 
  from datetime import date, datetime, time, timedelta
  
  
  class CustomTypeSerializer(json.JSONEncoder):
  
      def default(self, o):
          if isinstance(o, date):
              return o.strftime('%Y/%m/%d')
          if isinstance(o, datetime):
              return o.strftime("%Y/%m/%d %H:%M:%S")
          if isinstance(o, time):
              return o.strftime("%H:%M:%S")
          if hasattr(o, "__dict__"):
              return o.__dict__
          return str(o)
  
  
  # 定义一个列表 
  ls = [1, 2, 3, 4, 5, 6, float("nan"),  float("inf"),  (32, 6)]  
  # 对 列表 进行 json 序列化 
  json_str = json.dumps(ls, indent=4)  
  
  print(json_str) 
  
  dog = Dog("小黑", 2)
  
  dct = {"name": "张三", "age": 20, (1, 2): "元组",  None: None, "pet": dog,  "birth": date(2000, 10, 10)}
  
  json_str = json.dumps(dct, skipkeys=True, ensure_ascii=False, indent=4, cls=CustomTypeSerializer)
  
  print(json_str)
  ```
- json.loads(strings,  object_hook=None)
  ```python
  import json 
  
  class Person:
      def __init__(self, name, age):
          self.name = name 
          self.age = age 
  
      def __repr__(self) -> str:
          return f"{self.__class__.__name__}({self.__dict__})"
  
  
  strings = """
      [
          {
              "name": "张三",
              "age": 20
          } ,
          {
              "name": "李四",
              "age": 22
          } ,
          {
              "name": "王五",
              "age": null
          }    
      ]
  """
  #  默认 [] 转 列表，  {} 转字典 、如果希望字典转成其它格式对象，可以提供 object_hook
  # object_hook : 是一个可选的 功能性函数、 消费一个 字典 、返回一个 对象
  obj = json.loads(strings, object_hook=lambda x:  Person(**x) ) 
  ```

# hashlib 加密模块

```python
## 对字符串 进行 md5 加密
md5 = hashlib.md5("admin".encode())
# 获取 加密后的密文
print(md5.hexdigest())

# # 对字符串 进行 sha256 加密
sha256 = hashlib.sha512("admin".encode())
print(sha256.hexdigest())
```

## 对网址进行数字签名

```python
url = "http://www.baidu.com/s?w=python&page=1"

# 可以将网址中的参数 进行数字签名 、获取一个签名后的结果
params = url.split("?")[-1]

# 将参数转成字典
dct = dict([entry.split("=") for entry in params.split("&")])
# 添加格外参数、增加破解难度
# dct["com"] = "QIKU"
# 按照 字典中的键 进行排序
sorted_list = sorted(dct.items(), key=lambda x: x[0])
# 将 排序后的列表 转成字符串 a=1&b=2&c=3 ....
params = "&".join(map(lambda tp: f"{tp[0]}={tp[1]}" , sorted_list))
# 对参数进行 md5 / sha256 加密
sign_text = hashlib.sha256(params.encode()).hexdigest()

# 给网址 添加一个 签名信息
url += "&sign=" + sign_text
print(url)
```

## 对网址进行数字认证

```python
url = "http://www.baidu.com/s?w=python&page=1&sign=fe08beaf9432bade091533e0994d679e1333f4c587eb44b49d5e429c29a5d708"

# 数字认证
params = url.split("?")[-1]
dct = dict([entry.split("=") for entry in params.split("&")])
# 去掉 签名信息
sign_text = dct.pop("sign")

# 将 参数 进行排序
sorted_list = sorted(dct.items(), key=lambda x: x[0])
params = "&".join(map(lambda tp: f"{tp[0]}={tp[1]}" , sorted_list))
sign_text2 = hashlib.sha256(params.encode()).hexdigest()

if sign_text == sign_text2:
    print("网址合法")
else:
    print("网址不合法")
```

# rsa 模块

该模块不是 python 标准模块，需要安装第三方库 `pip  install  rsa`

## rsa生成公钥和私钥

```python
import rsa


# 生成 公钥 和 私钥
public_key, private_key = rsa.newkeys(2048)

# 获取公钥对象 对应的 流数据
public_bytes = public_key.save_pkcs1()

# 将对应的公钥流数据存储到 磁盘文件中
with open("public.pem", "wb") as w:
    w.write(public_bytes)

print("公钥存储成功")

# 获取 私钥对象对应的 流数据
private_bytes = private_key.save_pkcs1()

# 打开一个文件、并存储私钥
with open("private.pem", "wb") as w:
    w.write(private_bytes)

print("私钥存储成功")
```

## rsa公钥加密

```python
import rsa
import base64

# 获取 公钥对应的 流数据
with open("public.pem", "rb") as f:
    public_bytes = f.read()

# 获取公钥对象
public_key = rsa.PublicKey.load_pkcs1(public_bytes)

# 定义一个要加密的 明文内容
message = "我喜欢你"

# 使用 公钥加密
encrypt_bytes = rsa.encrypt(message.encode(), public_key)

# print(encrypt_bytes.decode("unicode_escape"))
# 将 加密后的 密文 流数据 进行 base64 编码
secure_text = base64.b64encode(encrypt_bytes).decode()

print(secure_text)

```

## rsa私钥解密

```python
import rsa
import base64


# 从文件中读取私钥对应的流数据
with open("private.pem", "rb") as f:
    private_bytes = f.read()

# 是要私钥类 创建一个私钥对象
private_key = rsa.PrivateKey.load_pkcs1(private_bytes)

# 定义一个密文
secure_text = "HEhubUOOHUl2kmVJGrrVQclmaKNHGxvets8dzMf6Lt3qun8jwn/rTlWcjlmzZcmet6OwY59Bhye7jNjWBZYPzclGiqhON2hyNWrEBZC3PG++LUJDM9XKoYjfT2k5e5mG6f/u6MLZN9JGy5bPFis/6iGsQDMPUqZG/rM2SeuSonzevk5HdxFPrMjwcZ3RnFXecVNJR9B73VR2KRpAbJnyxU4FXKAhS6pcHyIhqZUC7mWCQJLod1xOklRpeP9KmIsUfvid3ubI9RPLH5X4g+6EpnHhggJonEH4UMTJkmcZZRZi9C3TRUnQ8Prmb6opf6YmCpwVGEHrbP2+2VrBDAq97A=="

# 对 密文 先进行 base64 解码、获取 解码后的 流数据
secure_bytes = base64.b64decode(secure_text.encode())
# 使用 私钥 解密
message = rsa.decrypt(secure_bytes, private_key).decode()

print(message)
```

## rsa私钥签名

数字签名：  防止数据在互联中进行数据传输的时候 被 篡改 ~

```python
import rsa
import base64
from urllib.parse import quote

# 获取私钥对象
with open("private.pem", "rb") as f:
    private_bytes = f.read()

private_key = rsa.PrivateKey.load_pkcs1(private_bytes)

message = "我喜欢你"

# 使用 私钥签名
sign_bytes = rsa.sign(message.encode(), private_key, "SHA-1")

# 将 签名进行 base64编码
sign_text = base64.b64encode(sign_bytes).decode()

print(sign_text)
# 签名后的结果 中 可能包含一些 网址 上的特殊字符，例如 `+` ,
# 当在网址中拼接 sign=xxxxxxxxx的时候，服务器得到的签名会出问题
# 解决该问题 可以使用 urllib.parse.quote 函数 对网址中的特殊字符转义
sign_text = quote(sign_text)

print(sign_text)
```

## rsa公钥认证

```python
import rsa
import base64
from urllib.parse import unquote

# 获取公钥对象
with open("public.pem", "rb") as f:
    public_bytes = f.read()

public_key = rsa.PublicKey.load_pkcs1(public_bytes)

# 获取消息
message = "我喜欢你"

# 获取签名值
sign_text = "Cl9o0FRI4NCxot%2BnqJl/GHm4qAOvEQJjVc852rZdXasg0ivrKAa0Z5qIlgOIhaBvdf4BS4SrR8CMMEUnh7WUrz%2BEV8G8ZjAK0JpS%2BzovcUGF480%2BLPQ2Wbiw7UhiJU%2B4h/zPw%2Bhvavm3Jd4R/7T4ob2%2BemH5QWZEmjSXp6cEJdtowYwHyUN7Kf2LOVVcsoHYd/AEb%2Bc0DWOgZ9szJArB5%2BAkCRvNhKOjErcTELL63Z8EeUmkS0qFvrPud0q7A9se22vd5KyKdFNasQceQSSR2NUS6GrYlvRr6YOrI5N0BFM0Mf9tvduGqjj5y6yCFBZ1fiMQYfoQG4jX8jwSqbFNXg%3D%3D"

# 对 签名 进行 url 解码
sign_text = unquote(sign_text)

print(sign_text)

# 使用 base64 进行解码
sign_bytes = base64.b64decode(sign_text.encode())

# 使用 rsa 进行公钥认证, 如果认证失败、则程序 抛出一个 VerificationError 错误
try:
    hash_method = rsa.verify(message.encode(), sign_bytes, public_key)
    print("认证成功", hash_method)
except:
    print("认证失败")
```
