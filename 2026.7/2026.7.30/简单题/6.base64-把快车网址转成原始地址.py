"""
【字符串】定义一个函数 parse_flashget_to_url(url) 负责将 快车地址 解析为 原始网址：
快车地址示例: flashget://W0ZMQVNIR0VUXWh0dHA6Ly90b29sLmx1L3Rlc3QuemlwW0ZMQVNIR0VUXQ==
"""
import base64


#定义一个函数parse_flashget_to_url
def parse_flashget_to_url(url):
    """将快车地址 解析为原始地址"""
    #定义一个变量，用于接收快车地址
    flash_url = url
    #定义一个变量用于储存、快车地址前缀
    flash_prefix = "flashget://"
    #去掉前缀
    flash_data = flash_url.removeprefix(flash_prefix)
    #尝试base64解码
    decode_data = base64.b64decode(flash_data).decode()
    print(decode_data)
    return decode_data.strip("[FLASHGET]")

#测试
if __name__ == '__main__':
    result = parse_flashget_to_url("flashget://W0ZMQVNIR0VUXWh0dHA6Ly90b29sLmx1L3Rlc3QuemlwW0ZMQVNIR0VUXQ==")
    print(result)