"""
大模型 默认 使用 Markdown 语法 进行 输出 。

"""
import ollama
# 定义一个消息
messages = [
    {"role": "user", "content": "我叫小明, 今年20岁了。从这段文字中提取名字和年龄"}
]
# 设置 响应的格式
stream = ollama.chat("qiku", messages, think=False, stream=True, format="json")

for chunk in stream:
    print(chunk.message.content, end="", flush=True)