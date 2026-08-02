"""
正则表达式】已知一个多行字符串、每一行字符串均代表一个网络请求地址、
现要求编写一段程序、从字符串中提取所有表示图片的请求地址
https://www.baidu.com/images/xx.jpg
https://www.baidu.com/images/xx.jpg2
https://www.baidu.com/images/xx.jpeg
https://www.baidu.com/images/xx.gif
https://www.baidu.com/images/xx.doc
https://www.baidu.com/images/xx.pdg
https://www.baidu.com/images/xx.txt
"""
import re
#定义一个函数
def extract_photo(strings):
    """提取多行字符串中符合照片的请求地址"""
    #编写正则表达式
    regex =  r"^.+\.(?:jpe?g|png|gif|bmp)$"
    #获取匹配的结果
    result = re.findall(regex, strings, re.M)
    #返回结果
    return result

if __name__ == '__main__':
    print(extract_photo("""
    https://www.baidu.com/images/xx.jpg
    https://www.baidu.com/images/xx.jpg2
    https://www.baidu.com/images/xx.jpeg
    https://www.baidu.com/images/xx.gif
    https://www.baidu.com/images/xx.doc
    https://www.baidu.com/images/xx.pdg
    https://www.baidu.com/images/xx.txt"""))