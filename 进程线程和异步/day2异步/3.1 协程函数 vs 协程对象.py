import asyncio

#协程函数、用 async def 定义的函数
async  def my_coroutine():
    print("我是协程 ")
    await asyncio.sleep(1)
    return 11

#注意 ：调用协程函数不会执行函数体！
#只是返回 一个 协程对象 （coroutine object）
coro = my_coroutine()
print(type(coro)) #<class 'coroutine'>

#必须通过事件 循环来执行 协程
reesult = asyncio.run(coro)# 打印"我是协程"，11
print(reesult)#11