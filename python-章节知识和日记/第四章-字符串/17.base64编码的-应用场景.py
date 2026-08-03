"""

thunder://QUFtYWduZXQ6P3h0PXVybjpidGloOjMyYWIwNmI0NTI2M2I1NGJlNWY4YjQ1M2M2ZTMyNTM1MGMwMjM5ZmEmYW1wO2RuPSU1QiVFNyU5NCVCNSVFNSVCRCVCMSVFNSVBNCVBOSVFNSVBMCU4Mnd3dy5keXR0ODkuY29tJTVEJUU0JUJBJThDJUU1JTg4JTg2JUU0JUI5JThCJUU0JUI4JTgwJUU3JTlBJTg0JUU5JUFEJTk0JUU2JUIzJTk1QkQlRTQlQjglQUQlRTglOEIlQjElRTUlOEYlOEMlRTUlQUQlOTcubXA0Wlo=

magnet:?xt=urn:btih:2ac97178f89f5bbd7a25559ae6acd0ffc0f3cce8&amp;dn=%5B%E7%94%B5%E5%BD%B1%E5%A4%A9%E5%A0%82www.dytt89.com%5D%E4%BA%8C%E5%88%86%E4%B9%8B%E4%B8%80%E7%9A%84%E9%AD%94%E6%B3%95BD%E5%9B%BD%E7%B2%A4%E8%8B%B1%E4%B8%89%E8%AF%AD%E4%B8%AD%E8%8B%B1%E5%8F%8C%E5%AD%97.mp4

迅雷地址的生成规则：

    1) 将 原始地址 前拼接 AA, 后拼接 ZZ

    2) 将 拼接后的 字符串 进行 BASE64 编码 、返回一个编码后的 字符串

    3）在 编码后的字符串 前 添加前缀 thunder:// 形成 迅雷下载地址 ~~

"""
import base64

# 定义一个变量、存储要解码的 迅雷地址
thunder_url = "thunder://QUFtYWduZXQ6P3h0PXVybjpidGloOjMyYWIwNmI0NTI2M2I1NGJlNWY4YjQ1M2M2ZTMyNTM1MGMwMjM5ZmEmYW1wO2RuPSU1QiVFNyU5NCVCNSVFNSVCRCVCMSVFNSVBNCVBOSVFNSVBMCU4Mnd3dy5keXR0ODkuY29tJTVEJUU0JUJBJThDJUU1JTg4JTg2JUU0JUI5JThCJUU0JUI4JTgwJUU3JTlBJTg0JUU5JUFEJTk0JUU2JUIzJTk1QkQlRTQlQjglQUQlRTglOEIlQjElRTUlOEYlOEMlRTUlQUQlOTcubXA0Wlo="

# 定义一个变量，用来存储 迅雷前缀
thunder_prefix = "thunder://"

# 去掉 前缀
thunder_data = thunder_url.removeprefix(thunder_prefix)
# 尝试 使用 base64 解码
decode_data = base64.b64decode(thunder_data).decode()

print(decode_data.removeprefix("AA").removesuffix("ZZ"))