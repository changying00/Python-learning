"""

"""
import base64
def encode(string: str, encoding: str="utf-8") -> str:
    """将一个字符串进行base64编码、并返回编码后的字符串"""
    #使用base64编码
    byts = base64.b64encode(string.encode(encoding))
    # base64 编码后的结果 又A-Z、a-z、0-9、+、/、=符号组成
    # 将 二进制流 转成字符串
    ret = byts.decode()
    return ret
def decode(string: str, encoding: str="utf-8") -> str:
    """将一个字符串进行base64解码、并返回解码后的字符串"""
    byts = base64.b64decode(string.encode(encoding))
    ret = byts.decode()
    return ret

#测试
if __name__ == '__main__':
    result = encode(string = "hello 董国旋")
    print(result)
    result1 = decode(result)
    print(result1)

import base64


def encode(text: str, encoding: str = "utf-8") -> str:
    """将一个字符串进行base64编码，并返回编码后的字符串"""
    # 1. 将普通字符串按指定编码转为二进制字节流
    byte_data = text.encode(encoding)
    # 2. 进行 base64 编码（返回的依然是字节流）
    b64_bytes = base64.b64encode(byte_data)
    # 3. base64 包含的都是 ASCII 字符，直接用 ascii 解码成字符串返回即可
    return b64_bytes.decode("ascii")


def decode(b64_text: str, encoding: str = "utf-8") -> str:
    """将一个字符串进行base64解码，并返回原始字符串"""
    # 1. python3 中，b64decode 其实可以直接接收 ASCII 字符串，
    # 但严谨一点，我们把它转成 base64 字节流
    b64_bytes = b64_text.encode("ascii")
    # 2. 进行 base64 解码，还原出最原始的二进制字节流
    original_bytes = base64.b64decode(b64_bytes)
    # 3. 将原始字节流按指定的编码格式还原成普通字符串
    return original_bytes.decode(encoding)


# 测试
if __name__ == '__main__':
    # 测试 UTF-8
    result = encode(text="hello 徒步的骑手")
    print(f"编码后: {result}")

    result1 = decode(result)
    print(f"解码后: {result1}")