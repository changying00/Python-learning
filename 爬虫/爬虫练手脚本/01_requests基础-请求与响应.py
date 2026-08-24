# -*- coding: utf-8 -*-
"""
01 · requests 基础：发请求、看响应
=================================
对照学习笔记《HTTP 篇》：认识一次请求/响应的每个部分。
运行前提：已安装 requests 库
    pip install requests
"""

import requests

# 1. 最基本的 GET 请求
url = "https://httpbin.org/get"
resp = requests.get(url)

# 2. 状态码 —— 200 才是成功
print("状态码:", resp.status_code)          # 200
print("是否成功:", resp.ok)                 # True

# 3. 响应头（服务器告诉我们的信息，对应学习笔记里的 Content-Type 等字段）
print("\n===== 响应头 Headers =====")
for key, value in resp.headers.items():
    print(f"{key}: {value}")

# 4. 响应内容
print("\n===== 响应内容 =====")
print(resp.text[:300])                     # 原始文本

# 5. 如果内容是 JSON，直接 .json() 解析成字典
data = resp.json()
print("\n--- .json() 解析后 ---")
print("服务器看到的 User-Agent:", data["headers"]["User-Agent"])

# 6. 请求头（这是我们可以控制的，下一脚本的主角）
print("\n===== 注意 =====")
print("上面那个 User-Agent 是 python-requests，不是浏览器——")
print("很多网站靠它认出爬虫，这就是 02 脚本要解决的问题。")
