import sys


ls = [1, 2, 3, 4, 5]

try:
    # 从键盘上输入一个索引值 、用来获取 列表中的数据 
    index = int(input("请输入一个要获取数据对应的索引值"))

    # 获取 指定位置的元素 并输出 
    print(ls[index])

    # print(ls[index] / 0)
    print(ls * "3")


except ZeroDivisionError as e:
    # 可以使用 e.args[0] 获取 异常产生的原因， 也可以 直接 str(e) 获取原因 
    print("除数不能为0 异常已解决", e.args[0])

except ArithmeticError as e:
    print("计算错误 已解决")

except (ValueError, IndexError) as e:
    print("捕获值 或者 索引 异常、并处理完成")

except:
    # 如果 不指定 异常对象， 可以通过 sys.exception() 获取 异常对象 
    print("捕获剩余 其它所有异常、并进行处理", str(sys.exception()))

print("程序执行结束")

import  sys

ls = [1,2,3,44.5,6,6]
try:
    index = int(input("请输入一个要获取的数据对应的索引值:"))

    print(ls[index])
    print(ls * "3")
#捕获所有异常 except + 类型错误 例如（IndexError,....）+ as e(获取类型错误的原因)
# -》3种方式 1. e.args[0] 2.str(e) 3.str(sys.exception())
except:
    print('捕获所有异常',str(sys.exception()))
