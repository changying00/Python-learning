#【函数】编写一个函数 isprime, 判断一个数字是否是质素、完成计算两个质数相加的和为99、求他们的乘积是多少！

#定义一个函数isprime
def isprime(num):
    #小于2的数字不是质数
    if num < 2:
        return False
    #从2开始遍历、判断是否存在因数
    for i in range(2,num):
        #如果能被整除、说明不是质数
        if num % i == 0:
            return False
    #循环结束没有找到因数、说明是质数
    return True

#寻找俩个质数、使他们的和为99
for i in range(2,99):
    #第一数是质数
    if isprime(i):
        #第二个数字
        j  = 99 - i
        #第二个数也是质数
        if isprime(j):
            #输出俩个质数他们的乘积
            print(f"{i}+{j} = 99,乘积为:{i * j}")
             #找到后结束
            break

