"""
数字签名 :  可以防止数据在 互联网传播中 被篡改 ~~~

签名 通常 会 和 URL 进行 拼接 、成为 网址的 一部分、 但 URL 中 不能包含 一些特殊字符 、例如 `+`,  ` ` 等符号、否则会进行 URL 编码

例如 + 会被 编码为  %2B ,


私钥 负责 签名 、 公钥 负责 认证 。

"""
from urllib import parse
import rsa
import base64


url = "http://task.qiku.edu/task/enterprise-task-list?page=1&rows=20&a=1"
# 获取 URL 中的查询参数
parse_result = parse.urlparse(url)

# 获取 请求参数 、并转成一个 形似字典的 列表
query_params = parse.parse_qsl(parse_result.query)
# 按照 键 进行 排序
query_params.sort(key=lambda d: d[0])
# 将 排序后的 列表 转成 查询字符串
print(query_params)
query_string = "&".join(["=".join(q) for q in query_params])
# 输出
print(query_string)
# 获取 私钥对象
with open("private.pem", "rb") as f :
    private_bytes = f.read()

private_key = rsa.PrivateKey.load_pkcs1(private_bytes)

# 使用 私钥 进行签名 、并返回 签名后的 流数据
sign_bytes = rsa.sign(query_string.encode(), private_key, "MD5")
# 获取 签名后的字符串 、base64 编码 (签名中 可能出现 URL 不支持的 字符)
sign_text = base64.b64encode(sign_bytes).decode()
# 对 签名后的 结果 进行 URL 编码 、将 特殊字符串 进行 转义、例如 + 转成 %2B
sign_text = parse.quote(sign_text)
print(sign_text)
# 输出 签名后的 网址
url = url + "&sign=" + sign_text
print(url)
