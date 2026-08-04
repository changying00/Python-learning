import ollama
from datetime import datetime


def get_current_clock():
    """
    获取当前系统时间
    """
    return datetime.now()



def get_weather(location: str) -> str:
    """
    获取 指定 地区 的 天气情况
    Args:
        location :  地区

    Return : 返回 该地区的天气情况
    """
    data = {
        "北京": "晴",
        "郑州": "小雨",
        "南京": "大到暴雨"
    }

    return data.get(location, "未知")


tools_map = {"get_current_clock": get_current_clock, "get_weather": get_weather}

messages = [
    {"role": "user",  "content": "现在几点了, 南京和北京的天气如何?"}
]

print("====================Human=====================")
print(messages[-1]["content"])

response = ollama.chat("qwen3.5:0.8b", messages, think=False, tools=tools_map.values())

print("======================AI====================")
print(response.message.tool_calls)

for toolcall in response.message.tool_calls:
    messages.append(response.message)
    # 获取 工具 名 和参数
    func_name = toolcall.function.name
    func_args = toolcall.function.arguments
    # 调用 工具 获取 结果
    print("=====================tool=====================")
    result = tools_map.get(func_name)(**func_args)
    # 输出 工具计算的结果
    print(result)
    # 将 结果放入到 消息体中
    messages.append({
        "role": "tool", "content": str(result), "tool_name": func_name
    })

# 发起请求
response = ollama.chat("qwen3.5:0.8b", messages, think=False, tools=tools_map.values())

print("=================================AI=========================")
print(response.message.content)
