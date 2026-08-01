"""

    re.findall(pattern,string,flags):

        pattern: 传入 正则表达式 或者 pattern 对象

        string :
"""
import re as  re
#实例一

regex1 = r"\d+"
string2 = "dadadhuafhakhfkshfahjo121fiujaioujfio212"
result = re.findall(regex1,string2)
print(result)

#实例二
string = """
    <dd><a href='https://www.baidu.com'>百度</a></dd>
    <dd><a href='https://www.oppenai.com'>ai</a></dd>
    <dd><a href='https://www.deepseek.com'>deepseek</a></dd>
    

"""
#从字符串中 提取 a标签内 文本"百度" 和对应的超链接
regex = r"<dd><a\s+href='(.*?)'>(.*?)</a></dd>"
result = re.findall(regex,string)
print(result)

