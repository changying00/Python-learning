"""
使用多线程 完成笔趣阁 https://www.52xbq.com/xiaoshuo/238687/ 某小说的抓取和下载。(网站可随意)
"""
from random import random
import requests
import time
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib import parse

#获取整个网页的Response 里的text内容，然后找每个章节的(title章名) 和 (网址链接)==》然后进入爬取章节内容)
def load_url(url,retry = 0):
    try:
        headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,am;q=0.7,sq;q=0.6',
        'cache-control': 'max-age=0',
        'priority': 'u=0, i',
        'referer': 'https://www.52xbq.com/',
        'sec-ch-ua': '"Not=A?Brand";v="99", "Google Chrome";v="151", "Chromium";v="151"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36',
        }
        response = requests.get(url,headers=headers)
        #获取网页的内容
        return response.text
    except:
        #如果上面的请求，出现异常进行的处理，对此重新请求访问
        #延迟200 ~ 500毫秒
        time.sleep(random.uniform(0.2, 0.5))
        if retry< 3:
            retry += 1
            print(f'网址{url}当前解析失败、准备下次重新请求、当前重试次数为{retry}')
            return load_url(url,retry)
        else:
            raise
#编写一个函数，对主页面先进行爬取 获取 章节名 和 章节链接
def home_page(url):
    #调用load_url 对当前网址 获取 reponse 返回的text 内容
    home_text = load_url(url)

    #编写一个正则表达式、匹配小说的名字
    regex = r'<meta\s+property="og:novel:book_name"\s+content="(.*?)"/>'
    match = re.search(regex, home_text)
    #获取第一个分组就是 小说名字
    name = match.group(1)

    #编写一个正则表达式、用来提取 小说的所有章节文本
    regex = r'<ul\s+class="fen_4">(.*?)</ul>'
    #提取匹配的唯一章节内容
    match = re.search(regex, home_text,re.S)
    #获取组内容
    cap_text =match.group(1)

    #编写正则表达式、提取每个章节的 URL 和 章节标题
    regex = r"<li>\s+<a\s+href=\"(.*?)\"\s+title=\"(.*?)\">(.*?)</a>\s+</li>"
    # 提取 所有的连接地址 和 标题
    cap_list = re.findall(regex, cap_text)
    return cap_list,name

def parse_caputer(url,title,index):
    """负责解析小说章节正文内容"""
    time.sleep(random.uniform(0.01, 0.05))
    print(f"正在抓取章节 {title}、对应的 URL是 {url} ....")
    # 读取 url 对应的 源代码
    html_text = load_url(url)
    regex = r'<div\s+id="txt">(.*?)</div>'
    match = re.search(regex, html_text, re.S)
    # 获取 正文内容
    text1 = match.group(1)
    # 去除标签 、 去除 &nbsp;  去除 <br/>
    regex = r"<a(.*?)>(.*?)</a>|&nbsp;|<br/>"
    text = re.sub(regex,"",text1)
    return index, title, text
if __name__ == "__main__":
        url = "https://www.52xbq.com/xiaoshuo/10631/"
        capt_list = home_page(url)
        #构建一个30个线程的线程池
        executor = ThreadPoolExecutor(max_workers=20)
        # 定义一个容器、存储所有的 futuer 对象
        futuers = []
        # 创建一个 index 表示 索引、 方便 数据抓取成功 排序

        index = 0
        for href, title in capt_list[0]:
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

        print(f"小说 {capt_list[1]} 抓取完成、正在排序中....")
        # 排序
        results.sort(key=lambda d: d[0])
        print(f"小说 {capt_list[1]}  排序完成、正在写入磁盘 ...")
        # 将小说 内容存储的磁盘中
        with open(f"./{capt_list[1]}.txt", "wt", encoding="utf-8") as f:
            for index, title, content in results:
                f.write(title)
                f.write("\n")
                f.write(content)
                f.write("\n")
                # 每写入一章、强制写入到文件中
                f.flush()
        print(f"小说 {capt_list[1]} 抓取成功")