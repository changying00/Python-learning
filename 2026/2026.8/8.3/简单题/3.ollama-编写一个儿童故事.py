"""【Ollama】编写一段代码、输入 3 ~ 5 个关键字、并生成一个 儿童故事、长度小于2000字。
 禁止思考、并采用 、流式输出结果"""
import ollama
#构建一个消息
messages = [
    {
        "role":"user",
        "content":"关键词1:12岁，关键词2:男孩，关键词3:河南商丘，关键词4:农村，关键词5:上学并生成一个 儿童故事、长度小于2000字"
    }]
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