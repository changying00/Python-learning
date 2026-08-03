import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="deepseek-v4-pro",
    max_tokens=1000,
    system="你是一个python专家，帮我我学习python",
    messages=[
        {
            "role": "user",
            "content": "给我说说你的用法",
        }
    ],
)

for block in message.content:
    if block.type == "text":
        print(block.text)