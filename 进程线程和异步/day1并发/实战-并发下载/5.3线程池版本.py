"""使用 concurrent.futures.ThreadPoolExecutor - 推荐方式"""
from concurrent.futures import ThreadPoolExecutor,as_completed
import urllib.request
import time 

urls = [
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
]

def download(url):
    data = urllib.request.urlopen(url)
    return url,len(data.read())

start = time.time()

with  ThreadPoolExecutor(max_workers=3) as executor:
    futures = { executor.submit(download,url):url for url in urls}
    for future in as_completed(futures):
        url,size = future.result()
        print(f'下载完成：{url}({size} bytes)')
print(f'总耗时:{time.time() - start:.2f}s')

