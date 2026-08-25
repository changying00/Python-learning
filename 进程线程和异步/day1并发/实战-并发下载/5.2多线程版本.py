"""多线程下载"""
import urllib.request
import time
from threading import Thread,Lock
urls = [
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
]
results = {}
lock = Lock()

def download(url):
    try:
        data = urllib.request.urlopen(url)
        with lock:
            results[url] =len(data.read())
    except Exception as e:
        with lock:
            results[url] = str(e)

start = time.time()
threads =[Thread(target = download,args= (url,)) for url in urls]

for t in threads:t.start()
for t in threads:t.join()
print(f"多线程下载：{time.time() - start:.2f}s")
