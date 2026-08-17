"""
计算机中 常见的加解密技术有哪些 ?

- 不可逆加密 : 主要采用 hash混淆算法、特点 只能加密、无法解密， 主要代表性算法 MD5, sha1, sha256

- 对称加密算法:  通过 密钥 实现 加密、 通过 同一把密钥 实现 解密 , 主要代表性算法 AES,  DES

- 非对称加密算法 :  通过 公钥 进行 加密 、使用 私钥 进行解密 (公钥和私钥是一对钥匙)、主要代表性算法 rsa

    pip install rsa
"""
import rsa

# 创建 公钥 和私钥 对象 、需要传入一个 生成公钥和私钥的因子数
# 因子数 通常使用 2 的幂次方 、个人推荐使用 1024 或者 2048
public_key, private_key = rsa.newkeys(2048)

# 将 生成的 公钥对象 存储到 磁盘中
public_bytes = public_key.save_pkcs1()

# 将 返回的 公钥 流数据存储到 磁盘文件中
with open("./public.pem", "wb") as f:
    f.write(public_bytes)

# 将生成的私钥对象 存储到磁盘中
private_bytes = private_key.save_pkcs1()

with open("./private.pem", "wb") as f:
    f.write(private_bytes)




