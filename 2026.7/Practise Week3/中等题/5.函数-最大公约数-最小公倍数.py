#【函数】编写一个函数 、计算 2个数的 最大公约数 和 最小公倍数
#定义一个函数max_common_divisor_multiple
def max_common_divisor_multiple(a,b):
        #保留原来的俩个数
        num1 = a
        num2 = b
        #保证  a >= b
        if a < b:
            a , b  = b ,a
        #使用辗转相除求最大公约数
        while b!= 0:
            a, b = b ,a % b
        #最大公约数
        gcd = a
        #最小公倍数
        lcm = num1 * num2 // gcd

        return gcd, lcm
#测试
print(max_common_divisor_multiple(25,10))
