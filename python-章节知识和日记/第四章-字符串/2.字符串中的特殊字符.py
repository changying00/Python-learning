"""
 字符串 中的 特殊字符 :
        引号 

        \  :  

在 定义 字符串的时候， 如果 出现了 编程中 具有特殊含义的 字符、那么 可能会导致 字符串定义 产生问题 。


针对 `\`  产生的 特殊 含义 、 如果 希望 保持 普通文本 、需要对 \ 进行 转义 

"""

# 使用 单引号 定义 一个字符串 、输出 一个  I'm Chinese
# string = 'I'm Chinese' 

string = "I'm Chinese" 
print(string)

# 使用 双引号 定义一个字符串、 输出  你是一个 "好人"
string2 = '你是一个 "好人"'
print(string2)

# 定义一个字符串、 内容为  I'm Chinese， 你是一个 "好人"
string3 = '''I'm Chinese， 你是一个 "好人"'''
print(string3)

# 要求必须使用 双引号 定义字符串、且 输出内容  你是一个 "好人"
#  如果 冲突、 可以 在 冲突的 位置上 使用 `\`  进行 转义 
string4 = "你是一个 \"好人\""
print(string4)

# 定义一个 文件 磁盘路径 
file_path = "C:\\Users\\Administrator\\pip"
print(file_path)

string5 = "你好\\n世界!"

print(string5)

# 如果 在 字符串 中 定义的 字符 \  希望 代表普通的 字符 、则 可以直接 在 字符串前 添加一个 前缀 r
path = r"\\192.168.10.55\ublic\share\Python2607B\第一阶段\第4章 字符串\视频"

print(path)
