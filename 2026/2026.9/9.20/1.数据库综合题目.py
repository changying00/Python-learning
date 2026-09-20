"""
数据库综合练习】完成用户注册功能、要求如下
1.  设计一张 用户表 （ID,  用户名、密码（要求MD5加密）、手机号、邮箱、注册时间）
2.  定义一个 User 类、并提供 和 表字段相关的属性、提供一个 to_dict(self) 方法，可以将对象转成字典
	要求 属性私有化， 并提供对应的 property 属性
3.  定义一个 Result 类、提供 状态status（成功/失败）， message （成功/失败消息）,  data（存储额外数据）属性
	 要求 status , message， data 属性 私有化，并提供对应的  property 属性
	 data 可传可不传
4.  在 模块下 编写一个 用户注册 函数、并提供一个参数 user(代表 User对象) ，完成用户的注册
      a)  用户名 如果在表中已经存在、则 返回 失败状态的 Result 对象、消息为 用户名已被注册
      b)  如果用户名不存在，  则 密码 存储到数据库时候进行 MD5 加密、
      c)  如果 存储影响 1行、则返回成功状态的 Result  消息为 注册成功 ，并返回注册成功的用户ID
	否则 返回 失败状态的Result 、消息为  数据库异常
5.  在  __main__ 中 进行 注册 功能测试 ！！！
"""
import pymysql
import hashlib
from datetime import datetime


conn = pymysql.connect(
    user='root', password='123456',
    host='localhost', port=3306,
    database='py2607b', charset='utf8mb4'
)
try:
    with conn.cursor() as cursor:
        sql = """
            CREATE TABLE IF NOT EXISTS t_user(
                id            BIGINT PRIMARY KEY AUTO_INCREMENT,
                username      VARCHAR(20)  COMMENT '用户名',
                password      CHAR(32)     COMMENT 'MD5密码',
                phone         VARCHAR(11)  COMMENT '手机号',
                email         VARCHAR(50)  COMMENT '邮箱',
                register_time DATETIME     COMMENT '注册时间'
            )
        """
        cursor.execute(sql)
    conn.commit()
    print("建表成功")

    # 验证
    with conn.cursor() as cursor:
        cursor.execute("SHOW TABLES")
        print("当前库中的表:", cursor.fetchall())
finally:
    conn.close()



# ============ 1. User 类 ============
class User:
    def __init__(self, username=None, password=None, phone=None, email=None,
                 id=None, register_time=None):
        self.__id = id
        self.__username = username
        self.__password = password
        self.__phone = phone
        self.__email = email
        self.__register_time = register_time

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        self.__phone = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def register_time(self):
        return self.__register_time

    @register_time.setter
    def register_time(self, value):
        self.__register_time = value

    def to_dict(self):
        """将对象转成字典"""
        return {
            "id": self.__id,
            "username": self.__username,
            "password": self.__password,
            "phone": self.__phone,
            "email": self.__email,
            "register_time": str(self.__register_time) if self.__register_time else None
        }

    def __str__(self):
        return f"User({self.to_dict()})"


# ============ 2. Result 类 ============
class Result:
    def __init__(self, status, message, data=None):
        self.__status = status
        self.__message = message
        self.__data = data

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        self.__message = value

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    def __str__(self):
        return f"Result(status={self.__status}, message={self.__message}, data={self.__data})"


# ============ 3. 数据库工具 ============
def get_connection():
    return pymysql.connect(
        user='root',
        password='123456',
        host='localhost',
        port=3306,  # 修正：post -> port
        database='py2607b',
        charset='utf8mb4'  # 建议加，防止中文乱码
    )


def md5_encrypt(text: str) -> str:
    """MD5 加密"""
    return hashlib.md5(text.encode("utf-8")).hexdigest()


# ============ 4. 用户注册函数 ============
def register(user: User) -> Result:
    """
    用户注册
    :param user: User 对象
    :return: Result 对象
    """
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # a) 判断用户名是否已存在
        check_sql = "SELECT id FROM t_user WHERE username = %s"
        cursor.execute(check_sql, (user.username,))
        if cursor.fetchone():
            return Result(False, "用户名已被注册")

        # b) 密码 MD5 加密
        encrypted_pwd = md5_encrypt(user.password)

        # c) 插入数据
        insert_sql = """
            INSERT INTO t_user(username, password, phone, email, register_time)
            VALUES (%s, %s, %s, %s, %s)
        """
        now = datetime.now()
        rows = cursor.execute(
            insert_sql,
            (user.username, encrypted_pwd, user.phone, user.email, now)
        )
        conn.commit()

        if rows == 1:
            new_id = cursor.lastrowid
            return Result(True, "注册成功", new_id)
        else:
            conn.rollback()
            return Result(False, "数据库异常")

    except Exception as e:
        if conn:
            conn.rollback()
        print("异常信息:", e)
        return Result(False, "数据库异常")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


# ============ 5. 测试 ============
if __name__ == "__main__":
    # 测试1：正常注册
    u1 = User(username="zhangsan", password="123456",
              phone="13800000001", email="zs@qq.com")
    r1 = register(u1)
    print("测试1:", r1)

    # 测试2：重复用户名
    u2 = User(username="zhangsan", password="abcdef",
              phone="13900000002", email="zs2@qq.com")
    r2 = register(u2)
    print("测试2:", r2)

    # 测试3：另一个用户
    u3 = User(username="lisi", password="654321",
              phone="13700000003", email="ls@qq.com")
    r3 = register(u3)
    print("测试3:", r3)

    # 验证对象转字典
    print("u1.to_dict() =>", u1.to_dict())