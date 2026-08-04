import ollama
from datetime import datetime


def get_current_clock():
    """获取当前系统时间"""
    return datetime.now()

# 定义一个函数的映射、方便 工具 提取对应的函数对象
function_mapping = {
    "get_current_clock": get_current_clock,
}

messages = [
    {"role": "user", "content": "现在几点了?"}
]

# 定义一个变量，用来控制是否结束
is_over = False

while not is_over:
    # 大模型使用 工具 执行任务
    response = ollama.chat("qiku", messages, think=False, tools=[get_current_clock])

    # 如果 返回中 使用 了 tool_calls , 说明 该次对话 需要 借助工具
    if response.message.tool_calls:
        # 获取 大模型 需要用到的工具
        for toolcall in response.message.tool_calls:
            # 获取 toolcall 中 对应的 函数 和参数
            func_name = toolcall.function.name
            # 会将 所有需要的参数转成 字典
            func_args = toolcall.function.arguments
            # 根据 大模型找到的 工具 、并 使用 工具 获取 对应的结果
            result = function_mapping.get(func_name)(**func_args)

            # 将 大模型 返回的 消息 添加到 messages 中
            messages.append(response.message)

            # 将 工具返回的结果 做成消息 、并标记该消息 是 工具返回的
            messages.append({
                "role": "tool",  # 标记该消息是工具返回的
                "tool_name": func_name, # 设置 工具名称
                "content":  str(result)  # 将 工具返回的结果 强制转成 字符串、作为工具执行的结果
            })

    elif response.message.content:
        print(response.message.content)
        # 说明任务结束了
        is_over = True



