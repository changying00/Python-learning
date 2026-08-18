"""
按照要求完成代码编写
1. 读取 student.json (保存某个学生信息的 JSON数据)
2. 转为 json 字符串
3. 对 json 字符串进行 base64 编码
4.将 base64 结果写入 encode_result.txt 读取 encode_result.txt 文件 并 获取对应的 学生信息
"""
import json
import base64
from encodings.base64_codec import base64_decode

#1读取保存的学生信息JSON信息
with open('students.json',"rt",encoding="utf-8") as file:
    result = json.load(file)
print(result)

#2.转成json字符串
result = str(result)
#3对json 字符串进行 base64编码
base64_str = base64.b64encode(result.encode()).decode()
print(base64_str)

#4将base64写入encode_result.txt
with open("encode_result.txt ","wt",encoding="utf-8") as file:
    file.write(base64_str)
with open("encode_result.txt","rt",encoding="utf-8") as file:
    strings = file.read()
    base64_decode = base64.b64decode(strings.encode()).decode()
    print(base64_decode)