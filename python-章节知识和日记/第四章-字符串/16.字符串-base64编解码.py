"""
    b64encode(bytes):将一个 二进制流 转成base64编码后的二进制流
    好处: 将 非 ascii范围内字符串 转成 全部在 ascii范围的字符串

    b64decode(str|bytes):将一个字符串或者流 进行base64解码、并返回 解码后的 二进制流数据

"""
import base64

#定义一个 字符串
string = "hello 徒步的骑手"

#将原始 字符串 进行base64 编码
bytes =  base64.b64encode(string.encode())
# base64 编码后的结果 又A-Z、a-z、0-9、+、/、=符号组成
#将 二进制流 转成字符串
ret = bytes.decode()


#解码，传bytes 和ret 都行并返回一个流
bytes = base64.b64decode(bytes)
print(bytes.decode())