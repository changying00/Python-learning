"""
现有一个网址格式为 https://www.test.com/abc?a=1&b=2&c=3&sign=2354yu5ygfsdgsfayt
编写一个函数 verify(url, public_key, hash_method=None) 方法、
对 请求参数a=1&b=2&c=3 进行认证 返回 True/False
"""
import rsa
from urllib import parse
import base64
def verify(url, public_key, hash_method=None):
    parse_result = parse.urlparse(url)
    # 将 请求地址中的 参数 进行解析、获取 对应的 字典
    params = dict(parse.parse_qsl(parse_result.query))
    # 先去掉 sign
    sign_text = params.pop("sign")
    # 按照 字典中的 键 进行排序 、并生成 排序后的查询字符串
    query_params = list(params.items())
    # 排序
    query_params.sort(key=lambda d: d[0])
    print(query_params)
    # 组装 认证的 字符串
    query_string = "&".join(["=".join(q) for q in query_params])
    # 对 sign_text 进行 url 解码 （得到的字符串 包含 特殊字符 + 和 =）
    sign_text = parse.unquote(sign_text)
    # 获取 签名后的 流数据
    sign_bytes = base64.b64decode(sign_text)
    try:
        # 认证成功、返回 hash_method 、认证失败 、则 抛出错误
        hash_method = rsa.verify(query_string.encode(), sign_bytes, public_key)
        return (f"认证成功、hash算法为 {hash_method}")
    except:
        return("认证失败")
with open("public.pem", "rb") as f:
    public_bytes = f.read()
public_key = rsa.PublicKey.load_pkcs1(public_bytes)

url ="https://www.test.com/abc?c=3&b=2&a=1&sign=U3F5KyBIZppY22NN3L1n8BbDGB%2B/A/bGhTGJJtXkaa5fyMIxlBti0t5zVo5w726jyRrN57PYOSucNyBhs%2BWQvNx/DeqByZCORPyPIBvMbAFXVRnIQofLPCNeerUOh1iYVxp38SdoDE/AOtVRPx5mb/IIJ6dpAzkCHGpuK1Mh06Ht4eV/CXFEdyfDpxm/2fQRPmHQHoypZPNK0kChgtGnEk9EYtaGtqhJK2kiRMnb3lrch0i0nO743j78vcjMTzZUBRYwtDuw5ejUNeWn76YpmFFmHSytry/fOSxlr2PeGl49bZLeFZsgcVfo72CK7WonQBK8x4W15tGfcehbk%2BfLXg%3D%3D"

result= verify(url,public_key)
print(result)