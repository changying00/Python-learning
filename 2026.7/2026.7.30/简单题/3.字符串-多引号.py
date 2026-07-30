"""
【字符串】将一个使用 三引号 定义的多行 字符串、按照 换行符 进行拆分、
并保留所有去除前后空格后长度大于0的内容

"""
text = """ "1123"
"  "
"2 "
"DGX  "
"12312312  "
" "
"""
result = text.splitlines(keepends=False)
ls = []
for i in result:
    # strip(' "') 表示：只要最外侧是空格或双引号，通通剥掉！
    stripped_i= i.strip(' "')
    # 剥完后，'"  "' 变成了空字符串 ""，长度为 0，就会被成功过滤！
    if len(stripped_i) > 0:
        # 或者追加 stripped_i
        ls.append(stripped_i)
print(ls)


text1 = '  ""hello""  '
text2 = '""  hello  ""'

# 无论空格和双引号谁在外层、谁在内层，都会被剥干净
print(text1.strip(' "'))  # 输出: hello
print(text2.strip(' "'))  # 输出: hello