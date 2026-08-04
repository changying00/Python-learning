import ollama

"""
Prompt 提示词 采用 RTF 风格 书写

"""


prompt = """
我是一个初学编程的大一新生学生。
刚学习了 Python 中的 判断 和 循环、字符串、列表、函数等等知识还没有学习。
怎么 使用 Python实现 2 + 22 + 222 + 2222 的 编程 
返回的结果以 Markdown 格式表示
"""

# 定义 消息
messages = [
    {"role": "user", "content": prompt}
]

stream = ollama.chat("qiku", messages, think=False, stream=True)

for chunk in stream:
    print(chunk.message.content, end="", flush=True)
