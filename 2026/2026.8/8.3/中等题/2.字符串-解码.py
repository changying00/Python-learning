"""
【字符串】给定一个编码字符串，按照规则将其解码。
规则是 k[encoded_string]，
表示重复 k 次 encoded_string。 例子：输入 "3[a]2[bc]"，输出 "aaabcbc"。
"""
#我没有考虑[也成了字符串的部分
#定义一个函数 get_encoded_string
def get_encoded_string(s:str)->str:
     #通过索引和值的遍历
     stack = []
     num = 0
     current = ""
     for char in s:
         # 数字
         if char.isdigit():
             num = num * 10 + int(char)
         # [
         elif char == "[":
             stack.append((current, num))
             current = ""
             num = 0
         # ]
         elif char == "]":
             last, count = stack.pop()
             current = last + current * count
         # 字母
         else:
             current += char
     return current
if __name__ == "__main__":
    print(get_encoded_string("3[a]2[bc]"))