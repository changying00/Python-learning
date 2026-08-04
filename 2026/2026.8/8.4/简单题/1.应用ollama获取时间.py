"""
【Ollama】编写一段代码、使用工具获取某个城市的天气情况和当前系统时间、并输出 该相关的结果！
"""
"""
【Ollama】
使用工具获取城市天气和当前系统时间
"""
import ollama
from datetime import datetime
# 获取当前时间
def get_current_clock():
    """
    获取当前系统时间
    """
    return datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )
# 获取天气
def get_weather(location:str):

    city_map = {

        "Hangzhou":"杭州",
        "Beijing":"北京",
        "Shanghai":"上海",
        "Tianjin":"天津"

    }


    location = city_map.get(
        location,
        location
    )


    weather = {

        "杭州":"多云",
        "北京":"晴",
        "上海":"大到暴雨",
        "天津":"晴"

    }


    return weather.get(
        location,
        "暂无天气信息"
    )
# 工具映射
tools_map = {
    "get_current_clock":get_current_clock,
    "get_weather":get_weather
}
messages=[
    {
        "role":"user",
        "content":
        "现在几点了，杭州和北京天气如何？"
    }

]
print("================Human================")
print(messages[-1]["content"])
# 第一次请求，让模型选择工具
response = ollama.chat(
    model="qwen3.5:0.8b",
    messages=messages,
    think=False,
    tools=tools_map.values()

)
print("================AI Tool Call================")
print(response.message.tool_calls)
# 保存AI工具调用信息
messages.append(response.message)
# 执行工具
for toolcall in response.message.tool_calls:
    func_name = toolcall.function.name
    func_args = toolcall.function.arguments
    print("================Tool================")
    result = tools_map[func_name](**func_args)
    print(result)
    messages.append(
        {
            "role":"tool",
            "content":str(result)
        }

    )
# 第二次请求，让模型总结
response = ollama.chat(
    model="qwen3.5:0.8b",
    messages=messages,
    think=False
)
print("================AI================")
print(response.message.content)