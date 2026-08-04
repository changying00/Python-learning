"""【Ollama】粘贴一段长文本(文章、笔记等)、对 内容进行 总结概括，100 字精简摘要 + 3 条核心关键点。"""

"""
【Ollama】
粘贴一段长文本（文章、笔记等），
对内容进行总结概括，
生成100字精简摘要 + 3条核心关键点。
"""
import ollama
# 长文本内容
text = """
Apart from these string types, Unicode processing often reduces to transferring
text data to and from files—which automatically encode text to bytes when
stored in a file and decode it to characters (a.k.a. code points) when read back
into memory. Once loaded, we usually process text as strings in decoded form
only. To make this work, text files implement encodings and accept and return
text strings, but binary files instead deal in bytes strings for raw data.
You’ll meet Unicode again in the files coverage later in this chapter, but we will
save the rest of the Unicode story for later in this book. It crops up briefly in
Chapters 7, 9, and 15, but for the most part is postponed until this book’s
advanced topics part, in Chapter 37. Unicode is crucial in many (or most)
domains today, but many Python newcomers can get by with just a passing
acquaintance until they’ve mastered string basics.
In addition to its built-in string objects, Python’s standard toolset includes
support for text pattern matching with its re module, as well as parsing textual
data like JSON, CSV, XML, and HTML. You’ll meet additional examples of
some of these tools later in this book, but this tutorial intro has already said
enough about strings and must move on.
"""
# RTF 风格 Prompt
prompt = f"""
# Role（角色）

你是一名专业的信息分析师，
擅长阅读长篇文章，并提取核心信息。
# Context（背景）
用户提供一段长文本，
内容可能来自：
- 技术文章
- 学习笔记
- 新闻资料
- 文档说明
需要快速理解文本含义，
提炼重要信息。
# Task（任务）
请分析下面的文本内容，
生成简洁准确的总结。
# Requirements（任务要求）
1. 生成一段100字左右的摘要：
要求：
- 概括文章主要内容
- 保留核心观点
- 删除无关细节
2. 提取3条核心关键点：
要求：
- 每条关键点简洁明确
- 使用列表形式
- 突出重要信息
# Input Text（输入文本）
{text}
# Output Format（输出格式）
严格按照以下格式输出：
## 摘要
（100字左右总结）
## 核心关键点
1. xxx
2. xxx
3. xxx
禁止输出：
- 分析过程
- 思考过程
- 额外解释
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