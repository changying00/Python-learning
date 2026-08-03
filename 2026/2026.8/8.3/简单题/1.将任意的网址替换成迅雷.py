"""
【字符串】编写一个函数 convert_url_to_thunder(url) 负责将 任意一个网址 转换成 迅雷地址
"""
import base64
#定义一个函数
def convert_url_to_thunder(url:str)->str:
    # 加入迅雷的前缀
    thunder_prefix = "thunder://"
    # 在 url 前后加上AA 和 ZZ
    thunder_url = "AA" + url + "ZZ"
    #对thunder_url进行编码成二进制流
    thunder_bytes = thunder_url.encode()
    # 对二进制流在进行base64编码
    thunder_base64 = base64.b64encode(thunder_bytes)
    # 在转成字符串
    thunder_last_url = thunder_prefix + thunder_base64.decode()
    return thunder_last_url

if __name__ == "__main__":
    print(convert_url_to_thunder("https://chatgpt.com/g/g-p-6a4df066c9648191957781b465454482-learn-python-pan/c/6a707b39-2f90-83ee-b078-d95cfa8d447f"))