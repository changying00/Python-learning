import base64
import hashlib
import rsa
from urllib import parse
class Security:
    @classmethod
    def md5(cls, text: str) -> str:
        """进行MD5加密、并返回密文"""
        return hashlib.md5(text.encode('utf-8')).hexdigest()

    @classmethod
    def sha256(cls, text: str) -> str:
        """进行sha256加密、并返回密文"""
        return hashlib.sha256(text.encode('utf-8')).hexdigest()

    @classmethod
    def sign(cls, message: str, private_key: str, hash_method='MD5') -> str:
        """
        对 message 字符串进行 签名 、返回 base64编码后的字符串
        :param message : str 要签名的消息
        :param private_key : 字符串格式的私钥
        :param hash_method: hash方法，默认 MD5
        """
        sign_bytes = rsa.sign(message.encode(), private_key, hash_method)
        sign_test = base64.b64encode(sign_bytes).decode()
        return sign_test

    @classmethod
    def sign2(cls, message: str, private_key: str, hash_method='MD5') -> str:
        """
        对 message 字符串进行 签名 、返回 url 编码后的字符串
        :param message : str 要签名的消息
        :param private_key : 字符串格式的私钥
        :param hash_method: hash方法，默认 MD5
        """
        sign_bytes = rsa.sign(message.encode(), private_key, hash_method)
        sign_test = base64.b64encode(sign_bytes).decode()
        sign_text = parse.quote(sign_test)
        return sign_text

    @classmethod
    def verify(cls, message: str, signature: str, public_key: str, hash_method=None) -> bool:
        """
        对字符串进行认证
        :param message : str 要认证的消息
        :param signature : 签名（base64编码后的字符串）
        :param public_key : 字符串格式的公钥
        :param hash_method: hash方法，默认 MD5
        """
        sign_bytes = base64.b64decode(signature.encode())
        try:
            # 认证成功、返回 hash_method 、认证失败 、则 抛出错误
            hash_method = rsa.verify(message.encode(), sign_bytes, public_key)
            return(f"认证成功、hash算法为 {hash_method}")
        except:
            return("认证失败")


    @classmethod
    def encrypt(cls, message: str, public_key: str) -> str:
        """
        对字符串进行公钥加密 、返回 base64编码后的字符串
        """
        encrypt_bytes = rsa.encrypt(message.encode(), public_key)
        encrypt_text = base64.b64encode(encrypt_bytes).decode()
        return encrypt_text

    @classmethod
    def decrypt(cls, secure_text: str, private_key: str) -> str:
        """
        对密文进行私钥解密
        :param secure_text  base64编码后的字符串
        :param private_key rsa私钥
        """
        secure_bytes = base64.b64decode(secure_text.encode())
        message_bytes = rsa.decrypt(secure_bytes, private_key)
        return message_bytes.decode()