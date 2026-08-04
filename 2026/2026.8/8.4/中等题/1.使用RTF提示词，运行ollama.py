"""
【Ollama】使用 RTF 风格 Prompt 规划河南三日游旅游攻略

要求包含：
1. 角色
2. 背景
3. 任务及任务要求
4. 输出结果要求
"""


import ollama


"""
Prompt 提示词采用 RTF（Role-Task-Format）结构
"""


prompt = r"""
# Role（角色）

你是一名资深河南旅游规划师，
熟悉河南省内历史文化景点、自然景观、
交通路线、美食特色以及旅游时间安排。


# Context（背景）

用户计划进行一次河南三日游。

旅游条件：

- 出行方式：自驾游
- 时间：3天
- 旅游目标：体验河南历史文化和特色美食
- 避免安排过于普通、重复、商业化严重的景点
- 优先选择具有代表性的景点
- 考虑景点之间距离，避免每天长时间驾驶
- 需要合理安排住宿、餐饮和交通路线


# Task（任务）

请规划一份详细的河南三日旅游攻略。


# Task Requirements（任务要求）

攻略必须包含：

1. 总体旅游路线规划

2. 每一天详细安排：
   - 上午行程
   - 中午餐饮推荐
   - 下午行程
   - 晚上住宿建议

3. 每个景点介绍：
   - 景点特色
   - 推荐游玩时间
   - 游玩理由

4. 河南特色美食推荐：
   - 美食名称
   - 推荐地点

5. 自驾路线建议：
   - 城市之间距离
   - 大概驾驶时间


# Output Format（输出格式）

要求：

- 只输出旅游攻略内容
- 不输出分析过程
- 不解释自己的思考过程
- 使用 Markdown 格式
- 使用标题和列表增强可读性

"""


messages = [
    {
        "role": "user",
        "content": prompt
    }
]


stream = ollama.chat(
    model="qwen3.5:0.8b",
    messages=messages,
    think=False,
    stream=True
)


for chunk in stream:
    print(chunk.message.content, end="", flush=True)