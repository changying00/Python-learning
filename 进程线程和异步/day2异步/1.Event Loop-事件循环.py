import asyncio

async def main():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

#asyncio.run() 做了以下事情:
#1.创建事件循环
#2.运行main()协程
#3.关闭事件循环
asyncio.run(main())
