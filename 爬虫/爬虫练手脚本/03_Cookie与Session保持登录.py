# -*- coding: utf-8 -*-
"""
03 · Cookie 与 Session：保持登录状态
====================================
对照学习笔记《HTTP 篇 · 无状态 + Cookie》：
HTTP 不记人，服务器靠 Cookie 记住"你登录过"。
裸 requests.get() 每次都是新身份；Session 会自动保存并携带 Cookie。
"""

import requests

# httpbin 提供的登录演示接口：
# 用对用户名/密码 → {"authenticated": true}

# 1. 裸请求：每次都要带一次账号密码，登录状态不保留
r = requests.get("https://httpbin.org/basic-auth/user/passwd",
                 auth=("user", "passwd"))
print("裸请求登录:", r.json())

# 2. 正确示范：用 Session，模拟"先登录、再访问需要登录的页面"
session = requests.Session()

# 设置 Cookie（相当于登录成功后服务器发你的凭证）
session.cookies.set("sessionid", "abc123", domain="httpbin.org")

# 再次访问，Session 会自动带上这个 Cookie
r2 = session.get("https://httpbin.org/cookies")
print("Session 携带的 Cookie:", r2.json()["cookies"])

# 3. 用 Session 统一设置请求头，爬多个页面不用重复写
session.headers.update({"User-Agent": "my-crawler/1.0"})
r3 = session.get("https://httpbin.org/headers")
print("Session 统一 UA:", r3.json()["headers"]["User-Agent"])

# 4. 真实网站流程一般是：先 POST 提交账号密码 → 拿到 Cookie → 带 Cookie 爬
#    用 requests 模拟大概长这样（伪代码，站点不同写法不同）：
#       session.post("https://example.com/login", data={"user": "...", "pwd": "..."})
#       resp = session.get("https://example.com/user")   # 自动带登录态
print("\n结论：爬需要登录的网站，一定要用 requests.Session()。")
