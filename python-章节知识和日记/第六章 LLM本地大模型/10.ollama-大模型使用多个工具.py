import ollama


def sub(a: int, b: int) -> int:
    """计算 2个数字的差"""
    return a - b


def mul(a: int, b: int) -> int:
    """计算 2个数字的乘积"""
    return a * b


func_map = {
    "sub": sub,
    "mul": mul
}
# http://192.168.17.37:11434/

messages = [
    {"role": "user", "content": "计算 (3 - 5) * 6 的结果是多少 ?\n 要求: 整个计算过程 必须严格使用工具、禁止使用大模型计算！"}
]

print("=============================Human============================")
print(messages[-1]["content"])

while True:
    # 发请求
    response = ollama.chat("qwen3.5:0.8b", messages, think=False, tools=func_map.values())
    # 判断 当前是否 是否了工具
    if response.message.tool_calls:
        print("============================AI============================")
        print([tool.function.name for tool in response.message.tool_calls])
        # 遍历 用到的所有工具
        for toolcall in response.message.tool_calls:
            # 获取 函数名
            func_name = toolcall.function.name
            func_args = toolcall.function.arguments
            # 根据 函数名、获取 函数 并 调用函数 获取结果
            result = func_map.get(func_name)(**func_args)
            # 将 消息存储到 messages 中 、把工具计算的结果 也添加进入
            messages.append(response.message)
            messages.append({
                "role": "tool",
                "content": str(result),
                "tool_name": func_name
            })
            print("============================tool============================")
            print("工具名:", func_name)
            print("工具参数:", func_args)
            print("工具调用结果:", result)

    elif response.message.content:
        print("====================================AI=========================")
        print(response.message.content)
        break
