"""
re.split(regex,string,flags=0,maxsplit=-1):

        按照 正则表达式 匹配的内容 进行 字符串的拆分


"""
import re
import string
strings = "1,2,3,4,5,6,7"
#按照 逗号 对字符串 进行拆分、并返回一个列表
ls = strings.split(",")
print(ls)

strings = "1,2.3/4'6"
#将上述字符串 进行拆分、并获取 数字字符串 组成的列表
#编列一个正则表达式、用来匹配 分隔符
regex  = r"[,./']"
#使用 正则中的分割方法
ls2 = re.split(regex,strings)
print(ls2)

#定义一个字符串、统计字符串中 单词出现的个数
strings = "Also shown in Table 4-1, program units such as functions, modules, and classes"\
"—which you’ll meet in later parts of this book—are objects in Python too; they"\
"are created with statements and expressions such as def, class, import, and"

regex  = f"[{string.whitespace + string.punctuation}]"
ls3 = re.split(regex,strings)

new_ls = [i for i in ls3 if len(i)>0]
print(len(new_ls))
