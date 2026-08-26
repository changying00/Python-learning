import asyncio
# ✅ 正确：在 async def 中 await 协程
async def good():
    print(f"执行")
    await asyncio.sleep(1)
    print(f"执行完成")
# ❌ 错误：在普通函数中 await 会报 SyntaxError
# def bad():
    # await asyncio.sleep(1)
#错误
#asyncio.run(bad())
# ✅ 正确：用 asyncio.run() 启动
asyncio.run(good())