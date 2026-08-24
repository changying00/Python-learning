# -*- coding: utf-8 -*-
"""
04 · SSL 证书处理 + 异常捕获
=============================
对照学习笔记《HTTPS/SSL 篇》：
HTTPS = HTTP + TLS 加密。访问 https 站点前先要验证证书。
badssl.com 是专门用来测试各种证书问题的合法测试站点。
"""

import requests
import urllib3

# 1. 正常 HTTPS 站点 —— 证书有效，直接访问
r = requests.get("https://httpbin.org/get")
print("1. 正常 https 访问:", r.status_code)

# 2. 证书过期的站点 —— 报 SSLError
try:
    requests.get("https://expired.badssl.com/", timeout=10)
except requests.exceptions.SSLError:
    print("2. 证书过期报错: requests.exceptions.SSLError")

# 3. 自签名证书的站点 —— 也报 SSLError
try:
    requests.get("https://self-signed.badssl.com/", timeout=10)
except requests.exceptions.SSLError:
    print("3. 自签名证书报错: requests.exceptions.SSLError")

# 4. 跳过证书验证（抓测试数据用，生产环境有被中间人攻击的风险）
urllib3.disable_warnings()                 # 屏蔽 InsecureRequestWarning 警告
r4 = requests.get("https://self-signed.badssl.com/",
                  verify=False, timeout=10)
print("4. verify=False 跳过验证:", r4.status_code)

# 5. 通用异常处理：把网络错误兜住，别让程序崩掉
try:
    resp = requests.get("https://httpbin.org/get", timeout=5)
    resp.raise_for_status()                # 状态码不是 2xx 就抛异常
except requests.exceptions.Timeout:
    print("5. 请求超时：网站太慢，或加长 timeout 参数")
except requests.exceptions.ConnectionError:
    print("5. 连接失败：网络不通 / 端口不对 / 被服务器断开")
except requests.exceptions.HTTPError as e:
    print("5. HTTP 错误：", e)
else:
    print("5. 请求成功，状态码:", resp.status_code)

print("\n结论：SSL 报错先分清是证书问题还是代理问题；")
print("verify=False 只在抓测试数据时用，正式环境别关验证。")
