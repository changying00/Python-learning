"""

    re.findall(pattern, string, flags):

        pattern :  传入 正则表达式 或者 pattern 对象

        string :  要处理的 字符串

        flags :  正则 需要使用的 模式 、常见 模式 re.I,  re.S,  re.M

    返回一个列表、 列表中 存储 正则匹配的 内容

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


# 示例三
string = "1353653365354212611156145112521151151565616212771"

# 尝试 从字符串中 提取 满足 手机号 格式的数据
regex = r"(1[3-9]\d{5})\d{4}"

result = re.findall(regex, string)
print(result)
