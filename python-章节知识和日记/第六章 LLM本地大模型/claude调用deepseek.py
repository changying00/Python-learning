import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="deepseek-v4-pro",
    max_tokens=1000,
    system="你是百科全书",
    messages=[
        {
            "role": "user",
            "content": "今天郑州天气如何？",
        }
    ],
)

for block in message.content:
    if block.type == "text":
        print(block.text)