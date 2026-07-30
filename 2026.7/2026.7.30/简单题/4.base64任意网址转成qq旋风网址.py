"""
【字符串】编写一个函数 convert_url_to_qqdl(url) 负责将 任意一个网址 转换成 QQ旋风地址
"""
#定义一个函数convert_url_to_qqdl
import base64
def convert_url_to_qqdl(url):
    #定义一个变量存储qq旋风地址的前缀
    qqdl_prefix = "qqdl://"
    #把传入的地址进行编码成二进制流
    qqdl_btyes = url.encode()
    #再通过base64把二进制流进一步转换
    qqdl_base64 = base64.b64encode(qqdl_btyes)
    #再把base64编码后的二进制流解码为字符串
    qqdl_rest = qqdl_base64.decode()
    #最后加上前缀
    qqdl_result = qqdl_prefix + qqdl_rest
    return qqdl_result

#测试
if __name__== "__main__":
    result = convert_url_to_qqdl("http://task.qiku.edu/")
    print(result)