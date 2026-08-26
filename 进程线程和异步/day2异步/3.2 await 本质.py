#await 是一个挂起点 (yield point).当执行到 await 时
#1. 协程 暂停 执行
#2. 事件循环  可以去执行 其他协程
#3. 当 await 的操作完成后 、协程恢复执行
import asyncio
async def fetch_url(url):
    print(f'开始请求{url}')
    #这里是挂起点：事件循环可以去处理其他任务
    await asyncio.sleep(2)#模拟网络延迟
    print(f'{url} 请求完成')
    return f'{url}的数据'
async def main():
    #顺序执行
    result1 = await fetch_url("http://a.com")
    result2 = await fetch_url("http://b.com")
    print(result1,result2)

asyncio.run(main())