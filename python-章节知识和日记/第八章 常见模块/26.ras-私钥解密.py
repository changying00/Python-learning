"""私钥解密"""
import  rsa
import  base64

with open('./private.pem','rb') as file:
    private_bytes = file.read()

#获取 私钥对象
private_key = rsa.PrivateKey.load_pkcs1(private_bytes)

#定义一个密文
security_text = ""

#对密码进行base64解码
encrpy_bytes = base64.b64encode(security_text)

#使用 私钥 进行解密、获取明文
text = rsa.decrypt(encrpy_bytes,private_key).decode()

