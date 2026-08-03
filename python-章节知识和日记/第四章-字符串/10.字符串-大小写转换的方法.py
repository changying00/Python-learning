"""
字符串 中所有的方法都有返回值！！！
因为字符串是不可变的，用方法之后会产生一个新的返回值
"""
result  ="hello dgx!!!"
#字符串变小写
print(result.lower())
#字符串变大写
print(result.upper())
#字符串每个单词首字母大写
print(result.title())
#字符串首字母大写,如果第一个汉字，后面的不变
print(result.capitalize())