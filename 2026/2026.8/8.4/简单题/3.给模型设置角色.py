"""
【Ollama】需求：给模型固定人设，三种角色切换：代码纠错工程师， 口语化解说员， 严谨文档撰写者
在代码里通过设置不同角色进行提问，观察回答风格变化。
"""
"""
【Ollama】
固定模型人设，
实现三种角色切换：

1. 代码纠错工程师
2. 口语化解说员
3. 严谨文档撰写者

观察不同角色回答风格变化。
"""


import ollama


# 定义角色库
roles = {

    "代码纠错工程师": """
你是一名资深软件工程师。

你的职责：
- 分析代码错误原因
- 指出具体问题位置
- 提供修改方案
- 给出优化建议

回答风格：
专业、技术化、直接。
优先展示代码和解决步骤。
""",


    "口语化解说员": """
你是一名优秀的科普解说员。

你的职责：
- 将复杂概念简单化
- 使用生活中的例子解释
- 避免过多专业术语

回答风格：
轻松、有趣、容易理解。
像朋友聊天一样解释问题。
""",


    "严谨文档撰写者": """
你是一名专业技术文档工程师。

你的职责：
- 编写结构清晰的技术说明
- 使用规范术语
- 保持逻辑严谨

回答风格：
正式、准确、适合写入文档。
使用标题和列表组织内容。
"""
}


# 选择角色
role_name = "代码纠错工程师"


# 用户问题
question = """
下面Python代码为什么报错？

numbers = [1,2,3]

print(numbers[5])
"""


# 构造消息
messages = [

    {
        "role": "system",
        "content": roles[role_name]
    },

    {
        "role": "user",
        "content": question
    }

]


# 调用 Ollama
stream = ollama.chat(
    model="qwen3.5:0.8b",
    messages=messages,
    think=False,
    stream=True
)


# 输出结果
for chunk in stream:
    print(chunk.message.content, end="", flush=True)