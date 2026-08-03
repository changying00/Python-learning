"""
1.  temperature 温度  、取值范围 0 ~ 1

    温度值 越低、 生成的内容 越稳定。 值越高、创新性越强。

2.  repeat_penalty 重复惩罚系数 、 取值范围 1.0 ~ 2.0

        1.0  不做任何惩罚、

        1.1 ~ 1.2 :  相对较合适

3.  top-k :

...

"""
import ollama

messages = [
    {"role": "user", "content": "什么是水仙花数"}
]

# 构建请求
stream = ollama.chat("qiku", messages=messages, think=False, stream=True, options={
    "temperature": 0,
    "repeat_penalty": 1.1
})

# 获取 结果
for chunk in stream:
    print(chunk.message.content, end="", flush=True)


