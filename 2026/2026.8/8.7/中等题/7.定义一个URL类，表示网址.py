"""
定义一个 URL 类、用来表示 网址 、提供 属性 协议 schema、域名/主机 host、端口 port、 请求路径 path 、请求参数 query_params 、锚点 hash 等属性。
1.  提供一个 __init__ 方法、接收一个 字符串 url_path 参数、代表网络地址
 在 __init__ 方法中、完成 协议、域名、端口 等属性的赋值
2.  提供一个 方法  search_params 、 返回 query_params 的字典表示形式
	例如  query_params 为  a=1&b=2&c=3  该方法返回 {"a": "1",  "b": "2",  "c": "3"}

网址的组成规则例如:：https://www.baidu.com/test/abc/xxx?a=1&b=2&c=3#db
协议： https
域名/主机：  www.baidu.com
端口号 ：端口号和域名默认以 冒号 分割，如没有端口号，则 https 协议默认 443，  http协议默认 80
请求路径:  /test/abc/xxx
请求参数 :  a=1&b=2&c=3
锚点 :  db
"""


class URL:
    def __init__(self, url_path: str):
        self.schema = ""
        self.host = ""
        self.port = None
        self.path = ""
        self.query_params = ""
        self.hash = ""

        rest = url_path
        if "://" in rest:
            self.schema, rest = rest.split("://", 1)

        if "#" in rest:
            rest, self.hash = rest.split("#", 1)

        if "?" in rest:
            rest, self.query_params = rest.split("?", 1)

        if "/" in rest:
            host_port, self.path = rest.split("/", 1)
            self.path = "/" + self.path
        else:
            host_port = rest
            self.path = "/"

        if ":" in host_port:
            self.host, port_str = host_port.split(":", 1)
            self.port = int(port_str)
        else:
            self.host = host_port
            if self.schema == "https":
                self.port = 443
            elif self.schema == "http":
                self.port = 80
            else:
                self.port = None

    def search_params(self) -> dict:
        result = {}
        if not self.query_params:
            return result
        for pair in self.query_params.split("&"):
            if not pair:
                continue
            if "=" in pair:
                key, value = pair.split("=", 1)
            else:
                key, value = pair, ""
            result[key] = value
        return result

    def __str__(self):
        return (
            f"URL(schema={self.schema}, host={self.host}, port={self.port}, "
            f"path={self.path}, query_params={self.query_params}, hash={self.hash})"
        )


if __name__ == "__main__":
    u = URL("https://www.baidu.com/test/abc/xxx?a=1&b=2&c=3#db")
    print(u)
    print(u.search_params())
    u2 = URL("http://localhost:8080/api?x=1")
    print(u2)
    print(u2.search_params())
