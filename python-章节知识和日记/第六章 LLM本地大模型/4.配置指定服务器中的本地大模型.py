"""
ollama 支持 连接远程的本地大模型



#创建 一个 连接指定服务器的客户端
"""
import ollama
client = ollama.Client("http://192.168.10.107:11434")

response = client.chat("qiku",[{
    "role":"user",
    "content":"简单介绍下什么是勾股定理"
}])
#
print("think:",response.message.thinking)
print("content:",response.message.content)