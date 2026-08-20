"""
requests 是专门用来 发送 网络请求的库、 它可以 获取 网页 对应的对应

"""

import requests
import re 
import time, random 
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib import parse


def load_url(url, retry=0):
    try:
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'priority': 'u=0, i',
            'sec-ch-ua': '"Not=A?Brand";v="99", "Google Chrome";v="151", "Chromium";v="151"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36',
        }

        response = requests.get(url, headers=headers)
        # 获取 网页的内容
        return response.text 
    except:
        # 延迟 200 ~ 500 毫秒
        time.sleep(random.uniform(0.2, 0.5)) 
        if retry < 3:
            retry += 1
            print(f"网址 {url} 解析失败、准备重试、当前重试次数 {retry}")
            return load_url(url, retry)
        else:
            raise


def parse_caputer(url, title, index):
    """负责解析小说章节正文内容"""
    time.sleep(random.uniform(0.01, 0.05))
    print(f"正在抓取章节 {title}、对应的 URL是 {url} ....")
    # 读取 url 对应的 源代码 
    html_text = load_url(url)
    regex = r'<div\s+id="txt">(.*?)</div>' 
    match = re.search(regex, html_text, re.S)
    # 获取 正文内容 
    text = match.group(1)
    # 去除标签 、 去除 &nbsp;  去除 <br/>
    regex = r'<(.*?)\s.*?>(.*?)</\1>|&nbsp;|<br/>|\s+'
    text = re.sub(regex, "", text)
    return index, title, text


if __name__ == "__main__":
    url = "https://www.52xbq.com/xiaoshuo/87386/"
    # 获取 抓取网址的 内容 
    html_text = load_url(url)
    # 编写一个正则表达式、匹配小说的名字 
    regex = r'<meta\s+property="og:novel:book_name"\scontent="(.*?)"\s*/>'
    match = re.search(regex, html_text)
    name = match.group(1) 
    # print(name)

    # 编写一个正则表达式 、用来提取 小说的所有章节文本 
    regex = r"<ul\s+class=\"fen_4\">(.*?)</ul>"
    # 提取 匹配的唯一章节内容 
    match = re.search(regex, html_text, re.S) 
    # 获取 内容 
    cap_text = match.group(1)

    # 编写正则表达式、提取 URL 和 标题 
    regex = r"<li><a\shref=\"(.*?)\"\stitle=\"(.*?)\">\2</a></li>"
    # 提取 所有的连接地址 和 标题 
    cap_list = re.findall(regex, cap_text)


    # print(cap_list)


    # 构建一个 20个线程的 线程池
    executor = ThreadPoolExecutor(max_workers=20)

    # 定义一个容器、存储所有的 futuer 对象 
    futuers = []
    # 创建一个 index 表示 索引、 方便 数据抓取成功 排序
    index = 0 
    for href, title in cap_list:
        # 获取 href 对应的完整路径 
        cap_url = parse.urljoin(url, href)
        # 使用 线程池 负责 解析 cap 章节 
        futuer = executor.submit(parse_caputer, cap_url, title, index)
        futuers.append(futuer)
        index += 1
    
    results = []
    # 获取任务执行的结果 
    for futuer in as_completed(futuers):
        # 获取 任务执行的结果 index, title, content
        result = futuer.result()
        results.append(result)

    print(f"小说 {name} 抓取完成、正在排序中....")

    # 排序 
    results.sort(key=lambda d: d[0])

    print(f"小说 {name}  排序完成、正在写入磁盘 ...")

    # 将小说 内容存储的磁盘中 
    with open(f"./{name}.txt", "wt", encoding="utf-8") as f:

        for index, title, content in results:
            f.write(title)
            f.write("\n")
            f.write(content)
            f.write("\n")
            # 每写入一章、强制写入到文件中 
            f.flush()

    print(f"小说 {name} 抓取成功")




