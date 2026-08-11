"""
 网址的组成 :

    协议 :  https,  http   (网络数据传输规范)

    用户名/密码:  username:password

    域名/IP :  www.baidu.com ,  www.qiku.edu  (代表一台服务器主机)

    端口号 :
        https 协议 默认端口号 443
        http 协议 默认端口号 80

    请求地址:   /s

    查询参数:   a=1&b=2&c=3

    锚点 :   #xyz   (网页定位的)


协议 后面 ://

如果 存在 用户名:密码 它和 域名使用  @分隔

域名 和 端口号 使用 : 分隔

请求地址 和 查询参数 使用 `?` 分隔


https://www.baidu.com:3467/s?wd=图片#qiku

https://admin:123456@www.baidu.com:3467/s?wd=图片#qiku

"""
from urllib.parse import urlparse


class URL:

    def __init__(self, url: str):
        # 解析网址
        scheme, netloc, path, params, query, fragment = urlparse(url)
        self.__url = url
        self.__schema = scheme
        self.__netloc = netloc
        self.__path = path
        self.__params = params
        self.__query = query
        self.__fragment = fragment

    @property
    def schema(self):
        return self.__schema

    @property
    def host(self):
        array = self.__netloc.split(":")
        return array[0]

    @property
    def port(self):
        if ":" in self.__netloc:
            return self.__netloc.split(":")[-1]

        if self.schema == "https":
            return "443"

        if self.schema == "http":
            return "80"

        return 0

    @property
    def path(self):
        return self.__path

    @property
    def query(self):
        return self.__query

    @property
    def hash(self):
        return self.__fragment

    def query_params(self):
        if self.query == "":
            return {}

        dct = {}
        for entry in self.query.split("&"):

            entries = entry.split("=", maxsplit=1)
            if len(entries) == 1:
                dct[entries[0]] = ""
            else:
                dct[entries[0]] = entries[1]
        return dct


if __name__ == "__main__":
    url = "https://www.baidu.com?a=1&b=1&c=3"

    u = URL(url)

    print(u.schema)
    print(u.host)
    print(u.port)
    print(u.path)
    print(u.query)
    print(u.query_params())
    print(u.hash)
