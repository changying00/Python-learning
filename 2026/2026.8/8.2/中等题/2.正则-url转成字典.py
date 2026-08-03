"""
【字符串】编写一个函数 get_params(url) ,
负责将一个网址中传入的参数转换为字典
例如 https://www.baidu.com/s?wd=图片&e=utf-8&t=1345234234
====> {"wd": "图片", "e": "utf-8", "t": "1345234234"}
提示: 在网址中 请求地址 和 请求参数使用 `?` 进行分割 、
每一个参数采用 key=val 的形式表示、
多个参数之间使用 & 拼接！！！
"""
#导库
import re
def get_params(url):
    """将传入的网址参数转换成字典"""
    result = {}
    params = re.findall(r"(\w+)=([^&]+)", url)
    print(params)
    for key, value in params:
        result[key] = value

    return result

if __name__ == "__main__":
    print(get_params("https://www.baidu.com/s?wd=图片&e=utf-8&t=1345234234"))