import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="deepseek-v4-pro",
    max_tokens=1000,
    system="你是百科全书",
    messages=[
        {
            "role": "user",
            "content": "给我介绍一下北京大学",
        }
    ],
)

for block in message.content:
    if block.type == "text":
        print(block.text)