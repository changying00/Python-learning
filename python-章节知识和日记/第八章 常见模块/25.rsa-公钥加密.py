"""
公钥 加密
"""
import rsa
import base64

# 从 磁盘中 获取公钥
with open("./public.pem", "rb") as f:
    public_bytes = f.read()

# 将 公钥流数据转成 公钥对象
public_key = rsa.PublicKey.load_pkcs1(public_bytes)

# 定义一个字符串、用来表示 要加密的明文
raw_password = "123456"

# 使用 公钥 进行加密 、并获取 加密后的 流数据
encrpy_bytes = rsa.encrypt(raw_password.encode(), public_key)

# 将 加密后的密码 进行 base64 编码
text = base64.b64encode(encrpy_bytes).decode()

print(text)