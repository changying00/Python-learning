import ollama

"""
    chat(model, messages)

        - model : 设置模型名称 
        - messages : 设置 要发送的消息列表
        - options:  可选项、 配置 大模型的一些 可选参数 , 例如

            base_url :  设置 本地大模型对应的 API 接口地址, 默认值为 http://localhost:11434

               如果本地比较卡， 推荐使用  http://192.168.10.107:11434, 模型为 qiku


Response 对象 常见的 属性 

    - model :  任务使用的模型名
    - created_at :  任务开始时间
    - done : 任务是否完成 

    -  message:  返回的 消息对象 
        -  role :  返回的消息角色、 如果 是 AI 返回的结果、通常为 assistant
        -  content :  返回的 结果文本内容 
        -  thinking : 返回 思考的过程
        -  images :  返回相关的图片信息
        -  tool_name :  使用的工具名
        -  tool_calls :  使用的 可调用工具对象


"""

messages = [
    # 每一条消息 必须是一个 字典格式
    {
        "role": "user",  # 代表 用户
        "content": "1 + 1 等于几?",  # 设置 聊天的内容
    }
]
# 使用 ollama 发起一次 聊天请求
response = ollama.chat(model="qwen3.5:2b", messages=messages)

# 获取 思考过程
print("thinking: ", response.message.thinking)

# 获取 最终返回的内容
print("content:", response.message.content)