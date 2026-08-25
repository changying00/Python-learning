"""带进度显示的并发下载器"""
import urllib.request
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

class ProgressDownloader:
    def __init__(self, max_workers=3):
        self.max_workers = max_workers
        self.completed = 0
        self.lock = threading.Lock()
        self.total = 0
    
    def download_one(self, url):
        """下载单个文件"""
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            response = urllib.request.urlopen(req, timeout=10)
            data = response.read()
            
            with self.lock:
                self.completed += 1
                progress = f"[{self.completed}/{self.total}]"
                print(f"{progress} ✓ {url} ({len(data)} bytes)")
    
            return {"url": url, "size": len(data), "status": "ok"}
        except Exception as e:
            with self.lock:
                self.completed += 1
                print(f"[{self.completed}/{self.total}] ✗ {url} ({e})")
            return {"url": url, "size": 0, "status": "error", "error": str(e)}
    
    def download_all(self, urls):
        """并发下载所有文件"""
        self.total = len(urls)
        results = []
        
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_url = {
                executor.submit(self.download_one, url): url 
                for url in urls
            }
            
            for future in as_completed(future_to_url):
                result = future.result()
                results.append(result)
        
        # 统计
        ok = sum(1 for r in results if r["status"] == "ok")
        total_size = sum(r["size"] for r in results)

        print(f"\n📊 完成: {ok}/{self.total} 成功, 总大小: {total_size:,} bytes")
        return results

# 使用示例
if __name__ == "__main__":
    urls = [
        "https://httpbin.org/delay/0.5",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1.5",
        "https://httpbin.org/status/200",
        "https://httpbin.org/bytes/1024",
    ]
    
    downloader = ProgressDownloader(max_workers=3)
    start = time.time()
    results = downloader.download_all(urls)
    print(f"⏱️ 总耗时: {time.time() - start:.2f}s")