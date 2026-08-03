"""
【Ollama】编写一段代码、从一段文字中 提取所有的 地名、并采用流式输出、以 json 格式进行返回、并存储最终的结果
"""
import ollama
messages = [
    {"role": "user",
     "content": "从一段文字中提取所有的地名'河南商丘夏邑县的旁边是安徽亳州还有江苏徐州‘并以json格式返回并存储最终的结果"}

]
stream = ollama.chat("qwen3.5:0.8b", messages=messages, stream=True)

content = ""
#遍历迭代器、并获取 最终结果
for chunk in  stream:
    print(chunk.message.content,end = "",flush = True)
    #将每次得到的内容 进行拼接
    content += chunk.message.content
print("======================================================="*3)
print(content)