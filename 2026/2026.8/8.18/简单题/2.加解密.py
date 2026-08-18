"""用户配置字典 {"uid":2002,"token":"abc123secret","notify":True} 将字典转 json 字符串，
使用 RSA 加密 将 密文写入文件 config.enc 并读取 config.enc，解密得到原始配置字典
"""
import base64
import rsa
import json
data = {"uid":2002,"token":"abc123secret","notify":True}
json_str = json.dumps(data)
#使用rsa 生成公钥和私钥
public_key,private_key = rsa.newkeys(1024)

encrypt_bytes = rsa.encrypt(json_str.encode(),public_key)

#把经过rsa 加密的字节流写进文件
with open("./config.enc","wb") as file:
    file.write(encrypt_bytes)
#从文件读取加密的字节流
with open("config.enc","rb")  as file:
     bytes = file.read()
json_str = rsa.decrypt(bytes, private_key).decode()
#得到反格式化得到字典
data = json.loads(json_str)
print(data)
