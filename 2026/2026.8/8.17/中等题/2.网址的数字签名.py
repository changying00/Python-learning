"""
现有一个网址，例如 https://www.test.com/abc?c=3&b=2&a=1
编写一个函数  add_sign(url,  private_key,  hash_method=None) 方法、
对 请求参数例如 a =1&b=2&c=3 进行数字签名(参数中的键按照升序排列)
并将签名后的数据拼接到 url 中，返回格式例如
https://www.test.com/abc?c=3&b=2&a=1&sign=2354yu5ygfsdgsfayt
hash_method 没有提供默认使用 MD5
"""
from urllib import parse
import rsa
import base64
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
#编写一个函数
def add_sign(url,private_key,hash_method="MD5"):
    #获取url 中的参数列表
    parse_result = parse.urlparse(url)
    #获取请求参数、并转成一个形似 字典的列表
    query_params = parse.parse_qsl(parse_result.query)
    #按照键进行排序
    query_params.sort(key= lambda x:x[0])
    #将排序后的列表转成查询字符串
    query_string = "&".join(["=".join(x) for x in query_params])

    sign_bytes = rsa.sign(query_string.encode(),private_key,hash_method)
    sign_text = base64.b64encode(sign_bytes).decode()
    sign_text = parse.quote(sign_text)
    url = url + "&sign="+sign_text
    return url
with open("private.pem", "rb") as f:
    private_bytes = f.read()
private_key = rsa.PrivateKey.load_pkcs1(private_bytes)

result = add_sign('https://www.test.com/abc?c=3&b=2&a=1',private_key)
print(result)