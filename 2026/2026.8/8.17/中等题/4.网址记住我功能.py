"""网站中都有一个"记住我"功能, 现在编写一个函数 generator_remember_token(username, password, key, duration)
用来生成令牌。 duration 代表时间间隔(令牌有效时长) 令牌生成规则为
base64(<username>:<timestamp>:md5(<username>: <timestamp>:<key>: <password>))
username:  账号名
timestamp:  令牌过期的时间戳 (精确到秒即可、去掉小数点后面的值)
key :  密钥
password:  密码
将 username, timestamp, key,  password 四个数据使用 冒号拼接、并使用 md5加密，
将 加密后的 数据 和  username , timestamp 继续使用 冒泡拼接 ，
将 拼接后的内容 进行 base64编码， 编码的结果即为 令牌信息
编写一个函数 check_remember_token(token, username, password, key) , 用来验证令牌的真假
1. 令牌中的 用户名 必须和 传入的用户名 一致
2. 对 令牌中的 MD5 值 进行校验 、比较 密码 是否一致
3. 如果 用户名、密码 均一致， 则 判断 时间戳 是否 过期"""
import time
import hashlib
import base64
def generator_remember_token(username, password, key, duration):
    # 1. 计算过期时间戳，精确到秒
    timestamp = int(time.time()) + duration
    # 2. username:timestamp:key:password
    text = f"{username}:{timestamp}:{key}:{password}"
    # 3. MD5 加密
    md5_value = hashlib.md5(text.encode()).hexdigest()
    # 4. username:timestamp:md5
    token_text = f"{username}:{timestamp}:{md5_value}"
    # 5. Base64 编码
    token = base64.b64encode(token_text.encode()).decode()
    return token
def check_remember_token(token, username, password, key):
    try:
        # 1. Base64 解码  
        token_text = base64.b64decode(token).decode()
        # 2. 拆分
        token_username, timestamp, token_md5 = token_text.split(":")
        # 3. 用户名校验
        if token_username != username:
            return False
        # 4. 根据传入的密码和 key 重新计算 MD5
        text = f"{token_username}:{timestamp}:{key}:{password}"
        md5_value = hashlib.md5(text.encode()).hexdigest()
        # 5. MD5 校验
        if md5_value != token_md5:
            return False
        # 6. 判断是否过期
        if int(timestamp) < int(time.time()):
            return False
        return True
    except Exception:
        return False
token = generator_remember_token(
    "zhangsan",
    "123456",
    "abc123",
    60
)

print(token)

print(check_remember_token(
    token,
    "zhangsan",
    "123456",
    "abc123"
))