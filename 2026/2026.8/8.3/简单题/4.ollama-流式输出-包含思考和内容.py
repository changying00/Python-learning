"""
【Ollama】编写一段代码、使用 ollama 本地大模型 介绍一下 北京大学、采用 stream 流式输出、响应结果要包含思考和内容
"""
import ollama

messages = [{
    "role":"user",
    "content":"给我介绍一下北京大学"}
]
# 使用 stream = True, 采用 流式输出 、返回的是一个 迭代器、迭代器中 每一个数据是 一个 ChatResponse
stream = ollama.chat("qwen3.5:0.8b", messages=messages, stream=True)

# 定义 一个 变量， 用来 控制 当前是否在 思考
in_thinking = False

# 使用 for 循环 遍历输出 迭代器中 中的数据
for chunk in stream:
    # 获取 它的思考过程
    if chunk.message.thinking:
        # 判断 in_thinking 是否为 False
        if not in_thinking:
            print("thinking: ", end="", flush=True)
            in_thinking = True
        # 如果正在 思考中、输出 思考的内容
        print(chunk.message.thinking, end="", flush=True)

    elif chunk.message.content:
        if in_thinking:
            in_thinking = False
            print()  # 强制输出一个空白行、分隔思考和内容
            print("content: ", end="", flush=True)

        print(chunk.message.content, end="", flush=True)