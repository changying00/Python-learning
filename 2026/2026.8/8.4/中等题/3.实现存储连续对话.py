"""
【Ollama】用列表保存历史 user 和 assistant 对话记录，每次提问把历史全部传给模型，实现连贯对话
"""
"""
【Ollama】
使用列表保存历史 user 和 assistant 对话记录，
每次提问把历史消息全部传递给模型，
实现连续对话。
"""
import ollama
# 保存历史对话
messages = []
while True:
    # 获取用户输入
    user_input = input("\n用户：")
    # 退出程序
    if user_input.lower() in ["exit", "quit", "退出"]:
        print("对话结束")
        break
    # 保存用户消息
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )
    # 调用 Ollama
    response = ollama.chat(
        model="qwen3.5:0.8b",
        messages=messages,
        think=False
    )
    # 获取模型回复
    assistant_message = response.message.content
    # 输出回复
    print("\n助手：", assistant_message)
    # 保存 assistant 回复
    messages.append(
        {
            "role": "assistant",
            "content": assistant_message
        }
    )