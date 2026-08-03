"""
【字符串】编写一个函数 convert_url_to_flash_get(url) 负责将 任意一个网址 转换成 快车地址
"""
import base64

#定义一个函数convert_url_to_flash_get
def convert_url_to_flash_get(url):
    """把任意一个网址转成快车地址"""
    # 定义一个变量用于储存、快车地址前缀
    flash_prefix = "flashget://"
    #定义一个变量,用于存储快车网址的前后要加的，因为前后加的一样
    flash_strip = "[FLASHGET]"
    #定义一个变量用于加上前后快车的标志
    flash_data =flash_strip + url + flash_strip
    #先对flash_data编码获得二进制流数据
    byts  = flash_data.encode()
    #在通过base64编码
    flash_base64 = base64.b64encode(byts)
    #在获得base64编码后转成字符串
    text_flash_base64 = flash_base64.decode()
    #定义一个变量result_flash接收完整的快车地址,加上前缀flash_prxfix
    result_flash =  flash_prefix + text_flash_base64
    return result_flash

#测试
if __name__ == "__main__":
    result = convert_url_to_flash_get("https://chat.openai.com/")
    print(result)

