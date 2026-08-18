import hashlib
import base64
import time 
from datetime import timedelta


class RemeberMe:
    """
    记住我
    """
    @staticmethod
    def generator_remember_token(username, password, key, duration: timedelta=None):
        """
        生成 记住我 令牌 
        规则:  base64(<username>:<timestamp>: md5(<username>: <timestamp>:<key>: <password>))
        """
        if duration is None:
            # 默认 令牌存活时间 5分钟 
            duration = timedelta(minutes=5)

        # 获取 过期的时间戳 
        timestamp = int(time.time() + duration.total_seconds())
        # 将 用户名、时间戳 、key 和 密码 组成的 字符回传 继续 MD5 加密 
        md5_text = hashlib.md5(f"{username}:{timestamp}:{key}:{password}".encode()).hexdigest()
        # 进行 base64 编码 
        return base64.b64encode(f"{username}:{timestamp}:{md5_text}".encode()).decode()

    @staticmethod
    def check_remember_token(token, username, password, key):
        """
        校验令牌 是否可用 
        """
        # 对 token 令牌 进行 base64解码 (解码后 该字符串由 三部分组成 、分别是 用户ing、时间戳 和 MD5)
        try:
            decode_text = base64.b64decode(token).decode()
        except:
            return False, "token令牌不可用"

        # 按照 : 将 字符串 进行拆分 
        array = decode_text.split(":")

        if len(array) != 3:
            return False, "token令牌不可验证"

        # 令牌长度 是 合法 的 
        if array[0] != username:  
            return False, "token令牌认证失败"  # 用户名不正确

        # 检验 令牌是否 过期 
        if int(array[1]) < int(time.time()):
            return False, "token令牌已过期"

        # 将 用户名、 时间戳、密码 、密钥 进行 MD5加密
        md5_text = hashlib.md5(f"{username}:{array[1]}:{key}:{password}".encode()).hexdigest()

        if md5_text != array[-1]:
            return False, "token令牌认证失败" # 密码 / 密钥不正确

        return True, "token认证成功"
        



if __name__ == "__main__":
    
    key = "egsea&^%TG"

    token = RemeberMe.generator_remember_token("admin", "123456", key, duration=timedelta(seconds=2))

   

    status, message = RemeberMe.check_remember_token(token, "admin", "123456", key)

    print(status, message)