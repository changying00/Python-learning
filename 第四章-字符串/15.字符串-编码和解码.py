"""
字符串编解码：
    字符串 编码：将字符串 按照 某种编码方法 例如 UTF-8、GBK、Unicode等方式 格式转换、返回一个 转换后的 二进制流数据~~
        encode(encoding = "utf-8"):将 字符串 按照 指定的编码方式 转成 二进制流

    字符串解码 ：将一个 二进制流 按照 某种编码方式 还原成 字符串的过程
        decode(encoding = "utf-8")
    编解码对应的方式要一样
"""
#定义 一个文本内容
string = "DGX 徒步的骑手"
#默认utf-8编码一个字占三个字节、十六进制
print(string.encode())#b'DGX \xe5\xbe\x92\xe6\xad\xa5\xe7\x9a\x84\xe9\xaa\x91\xe6\x89\x8b'
#在gbk编码下一个字占俩个字节、十六进制
print(string.encode("gbk"))#b'DGX \xcd\xbd\xb2\xbd\xb5\xc4\xc6\xef\xca\xd6'
#unicode编码一个字占一个字节
print(string.encode("unicode_escape"))#b'DGX \\u5f92\\u6b65\\u7684\\u9a91\\u624b'

s1 = string.encode()
s2 = s1.decode()
print(s2)