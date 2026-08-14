"""
hashlib :  提供了 常见的 hash 混淆算法 

hash 混淆算法 :  
    底层 采用 hash 算法 进行 数据处理 、该算法是不可逆的、只能加密 不能进行解密 

    hash 混淆算法针对 相同的 字符串 加密后的 结果 永远相同 。

常见的不可逆加密算法有: 

    md5

    sha-1

    sha-256

"""
import hashlib

raw_password = "har$edot" 

# 将 密码 进行 MD5 加密、返回 一个加密后的 字符串 
# 32
print(hashlib.md5(raw_password.encode()).hexdigest(), len(hashlib.md5(raw_password.encode()).hexdigest()))  # e10adc3949ba59abbe56e057f20f883e
# 40
print(hashlib.sha1(raw_password.encode()).hexdigest(), len(hashlib.sha1(raw_password.encode()).hexdigest())) # 7c4a8d09ca3762af61e59520943dc26494f8941
# 64
print(hashlib.sha256(raw_password.encode()).hexdigest(), len(hashlib.sha256(raw_password.encode()).hexdigest())) # 8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92
# 128
print(hashlib.sha512(raw_password.encode()).hexdigest(), len(hashlib.sha512(raw_password.encode()).hexdigest())) # ba3253876aed6bc22d4a6ff53d8406c6ad864195ed144ab5c87621b6c233b548baeae6956df346ec8c17f5ea10f35ee3cbc514797ed7ddd3145464e2a0bab413