"""
数字认证 :
    1. 获取 请求的所有参数

http://task.qiku.edu/task/enterprise-task-list?page=1&rows=20&a=1&sign=XOhYVZVP8EK7ipkR7SPbu2Af0eN9IpzF6Cj%2BKvz8gZD2W3%2BOPLZNDd%2BPTVLn4uFmVzITVmJiCwX6y%2BoIJ9o6hWg%2BMa8ZLmszoBaV1vo2w9sdRGRo4hL/DEMjRtnnOjnwYkpb9s4Dday2kN4J8d64U4qUkZLgM1mfX04ln78DhWVyZJd19ryxI72lfVmqq4s6I71nkhs7zYelV42ahKsEyFrvCBa9vcYgPvdRIjEebVIeuxgUZwyQTlIQWgNChb8QTHreaEI4T1Mlfyapk0zIAgbm09SodYfHeOA6fTW6SaXeg/%2BDXJVaEO0LwA6BnxPYKHkIDf8z43SE9gyRItrl/g%3D%3D

"""
import rsa
from urllib import parse
import base64

url = "http://task.qiku.edu/task/enterprise-task-list?page=1&rows=20&a=1&sign=XOhYVZVP8EK7ipkR7SPbu2Af0eN9IpzF6Cj%2BKvz8gZD2W3%2BOPLZNDd%2BPTVLn4uFmVzITVmJiCwX6y%2BoIJ9o6hWg%2BMa8ZLmszoBaV1vo2w9sdRGRo4hL/DEMjRtnnOjnwYkpb9s4Dday2kN4J8d64U4qUkZLgM1mfX04ln78DhWVyZJd19ryxI72lfVmqq4s6I71nkhs7zYelV42ahKsEyFrvCBa9vcYgPvdRIjEebVIeuxgUZwyQTlIQWgNChb8QTHreaEI4T1Mlfyapk0zIAgbm09SodYfHeOA6fTW6SaXeg/%2BDXJVaEO0LwA6BnxPYKHkIDf8z43SE9gyRItrl/g%3D%3D"

parse_result = parse.urlparse(url)
# 将 请求地址中的 参数 进行解析、获取 对应的 字典
params = dict(parse.parse_qsl(parse_result.query))
# params = {
#     "page": "1",
#     "rows": "20",
#     "a": "1",
#     "sign": "XOhYVZVP8EK7ipkR7SPbu2Af0eN9IpzF6Cj%2BKvz8gZD2W3%2BOPLZNDd%2BPTVLn4uFmVzITVmJiCwX6y%2BoIJ9o6hWg%2BMa8ZLmszoBaV1vo2w9sdRGRo4hL/DEMjRtnnOjnwYkpb9s4Dday2kN4J8d64U4qUkZLgM1mfX04ln78DhWVyZJd19ryxI72lfVmqq4s6I71nkhs7zYelV42ahKsEyFrvCBa9vcYgPvdRIjEebVIeuxgUZwyQTlIQWgNChb8QTHreaEI4T1Mlfyapk0zIAgbm09SodYfHeOA6fTW6SaXeg/%2BDXJVaEO0LwA6BnxPYKHkIDf8z43SE9gyRItrl/g%3D%3D"
# }
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
# 获取 公钥对象
with open("public.pem", "rb") as f:
    public_bytes = f.read()

public_key = rsa.PublicKey.load_pkcs1(public_bytes)

try:
    # 认证成功、返回 hash_method 、认证失败 、则 抛出错误
    hash_method = rsa.verify(query_string.encode(), sign_bytes, public_key)
    print(f"认证成功、hash算法为 {hash_method}")
except:
    print("认证失败")

