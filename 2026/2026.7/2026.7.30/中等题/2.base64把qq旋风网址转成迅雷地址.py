"""
【字符串】编写一个函数 convert_qqdl_to_thunder(qqdl_url) 负责将 任意一个QQ旋风网址 转换成 迅雷地址，
示例: qqdl://aHR0cDovL3Rvb2wubHUvdGVzdC56aXA=

"""
import base64
#定义一个函数convert_qqdl_to_thunde()
def convert_qqdl_to_thunde(qqdl_url):
    """把qq旋风网址 转成迅雷地址"""
    #定义一个变量qqdl_prefix用于存储qq旋风网址的前缀
    qqdl_prefix = "qqdl://"
    #定义一个变量用于接收去掉前缀的网址，result_url_qqdl
    result_url_qqdl = qqdl_url.removeprefix(qqdl_prefix)
    #通过base64对result_url进行解码,
    qqdl_reled = base64.b64decode(result_url_qqdl)
    #再把qqdl_reled进行解码
    result_url  = qqdl_reled.decode()
    print(f"qq旋风转成的原地址{result_url}")
    #加入迅雷的前缀
    thunder_prefix = "thunder://"
    #在result_url 前后加上AA 和 ZZ
    thunder_url  =  "AA" + result_url + "ZZ"
    #对thunder_url进行编码成二进制流
    thunder_bytes= thunder_url.encode()
    #对二进制流在进行base64编码
    thunder_base64 = base64.b64encode(thunder_bytes)
    #在转成字符串
    thunder_last_url = thunder_prefix +  thunder_base64.decode()
    return thunder_last_url

if __name__ == "__main__":
    print(convert_qqdl_to_thunde("qqdl://aHR0cDovL3Rvb2wubHUvdGVzdC56aXA="))