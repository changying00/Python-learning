"""
针对 一些简单的任务、不需要 大模型思考、此时可以禁用思考
"""
import ollama
#构建一个消息
messages = [
    {
        "role":"user",
        "content":"you know python learning 6th this book？"
    }
]
#发起一个 聊天请求、返回一个迭代器
stream = ollama.chat("python-teacher",messages = messages,stream = True,think =  False)
content = ""
#遍历迭代器、并获取 最终结果
for chunk in  stream:
    print(chunk.message.content,end = "",flush = True)
    #将每次得到的内容 进行拼接
    content += chunk.message.content
print("======================================================="*3)

print(content)