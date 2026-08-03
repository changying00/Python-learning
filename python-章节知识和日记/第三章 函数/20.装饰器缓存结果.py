"""
装饰器 缓存 函数 调用 结果

  当 调用 函数的时候， 会 首先 从 缓存中 查看 是否 有结果  、

    如果 没有结果、则 调用 目标函数获取结果、 并将 结果 写入 到 缓存中

    如果 有 结果、 则 直接返回结果 。


"""
import time


def cache(*, duration=60):
    """对函数执行的结果进行缓存、默认时长 60s """

    def cache_target(func):
        # 定义一个 容器 、用来存储 缓存的结果、cache中存储的数据格式为 (args, kwargs, result, time)
        cache_data = []

        def wrapper(*args, **kwargs):
            nonlocal cache_data
            # 获取 当前 时间戳
            current_time = time.time()
            # 获取 所有没有过期的缓存数据
            cache_data = [(a, k, r, t) for a, k, r, t in cache_data if t + duration > current_time]
            # 检查 a, k 是否 在 缓存中存在， 如果 存在， 则 获取 r
            data = list(filter(lambda d: args == d[0] and kwargs == d[1], cache_data))
            if data:
                # 如果 data 有值、说明 找到缓存
                return data[0][2]
            # 如果 没有找到 缓存、调用目标函数 获取结果
            ret = func(*args, **kwargs)
            # 将 返回的结果 存储到 缓存中
            cache_data.append((args, kwargs, ret, current_time))

            # 返回 目标函数执行的结果
            return ret

        return wrapper

    return cache_target


@cache(duration=10)
def sum(a, b):
    time.sleep(5)
    print(a, b)
    return a + b


def test(a, b):
    return a - b


if __name__ == "__main__":
    # 第一次 调用 sum
    print(sum(3, 5))

    # 调用 test函数
    print(test(3, 5))

    # 睡眠 10秒
    time.sleep(1)
    print("睡眠醒来....................................")

    # 第二次调用 sum
    print(sum(3, 5))

    # 模拟 更改 参数 后的 第三次调用
    print(sum(3, 4))
