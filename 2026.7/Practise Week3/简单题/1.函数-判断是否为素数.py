#【函数】编写一个函数 is_prime(n)，判断给定整数 n 是否为素数，并返回 True 或 False。
#定义一个名为is_prime的函数，判断给定整数是否为素数
def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(7))