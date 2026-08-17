"""
私钥解密
"""
import rsa
import base64

with open("./private.pem", "rb") as f:
    private_bytes = f.read()

# 获取 私钥对象
private_key = rsa.PrivateKey.load_pkcs1(private_bytes)

# 定义一个 密文
security_text = "OlHput9pnlf16ggGyLd0g7jcWwmFDdKGYGNuF8Cx7oUA4W1cTERFlxRGWs+faMR0t6h+zXFCImGVwf1DKh4zb/Y2G35J9Y/vvpBnvWPZbDSKrlsE8D5ugnCRLIZQKuplZUvEkih3V6zPdqkDXdGSgtfgFC6Ewl4pzFwoKqCIYjkq2LZArfID3KhUPBkjBp/st4axcQWd16Q6n3yxkGgYpa/0jVijBQ02infIdCBCDWyEP8tCwZdhIY0YSEd/JpcCQN3G4wKbEnmcWH/JzPBPmHV2Gi0kgoC9O14XdD3OC2pnn9GXdTyUPXSzkz+tUJRlE/cQR8ehW/vFq1/AVhUFBQ=="

# 对 密码 进行 base64 解码
encrpy_bytes = base64.b64decode(security_text)

# 使用 私钥 进行 解密 、获取明文
text = rsa.decrypt(encrpy_bytes, private_key).decode()

print(text)
