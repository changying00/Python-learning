from urllib import parse
import rsa
import base64
url = "http://task.qiku.edu/task/enterprise-task-list?page=1&rows=20&a=1"
#获取URL中的查询参数
parse_result = parse.urlparse(url)
#获取请求参数、并转成一个 形似字典的列表
query_params = parse.parse_qsl(parse_result.query)
#按照键 进行排序
query_params.sort(key= lambda d:d[0])
#将排序后的 列表 转成 查询字符串
query_string = "&".join(["=".join(q) for q in query_params])
#输出
print(query_string)
#获取 私钥对象
with open('private.pem','rb') as file:
    private_bytes = file.read()
private_key = rsa.PrivateKey.load_pkcs1(private_bytes)
#使用私钥 进行签名、并返回 签名后的流数据
sign_bytes = rsa.sign(query_string.encode(),private_key,'sha256')
#获取 签名后的字符串、 base64 编码（签名中 可能 出现URL 不支持的字符）
sign_text = base64.b64encode(sign_bytes).decode()
#对签名后的结果 进行URL编码、 将特殊字符串 进行转义、例如+转成%2B
sign_text =parse.quote(sign_text)
print(sign_text)
#输出 签名后的网址
url =url + '&sign=' + sign_text
print(url)
