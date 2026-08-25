"""同步下载 — 串行等待，效率低"""
import urllib.request
import time

urls = [
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
]

start = time.time()

for url in urls:
    urllib.request.urlopen(url)

print(f"同步下载:{time.time() - start:.2f}s")