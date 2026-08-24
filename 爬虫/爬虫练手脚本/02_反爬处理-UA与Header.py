# -*- coding: utf-8 -*-
"""
02 · 反爬处理：User-Agent 与 Header 伪装
========================================
对照学习笔记《HTTP 篇 · Header》：很多网站靠 UA 判断"你是不是浏览器"。
不带 UA 可能返回 403；带上像浏览器一样的 Header，就能正常访问。
"""

import requests

url = "https://httpbin.org/headers"

# 1. 不带任何 Header —— 服务器看到的 UA 是 python-requests
resp1 = requests.get(url)
ua = resp1.json()["headers"].get("User-Agent")
print("1. 默认 UA:", ua)

# 2. 伪装成 Chrome 浏览器
headers = {
    # 从你浏览器的 "网络面板" 里复制一个真实的 UA 也行
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/120.0.0.0 Safari/537.36"),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Referer": "https://www.google.com/",   # 有的站会检查来源，防止盗链
}

resp2 = requests.get(url, headers=headers)
print("2. 伪装后 UA:", resp2.json()["headers"].get("User-Agent"))

# 3. 实战结论：被 403 时，第一步先检查 / 伪装 User-Agent 和 Referer
print("\n结论：被 403 时，第一步先检查 / 伪装 User-Agent 和 Referer。")
print("用法：requests.get(url, headers=headers)")

# 4. 加一个延时，别把服务器打爆（对应学习笔记状态码 429 限速）
import time
time.sleep(1)
print("每个请求之间 sleep 一下，降低被反爬的概率。")
