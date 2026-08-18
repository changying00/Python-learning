"""
如何 手动抛出异常  

raise exception 

"""
import re 
import sys


try:
    string = input("请输入一个手机号\n")

    if re.fullmatch(r"1[3-9]\d{9}", string) is None:
        # 手动抛出一个错误、并设置 错误的消息
        raise ValueError("手机号格式不正确")

except:
    # 让 产生的异常 继续抛给 上层调用者
    raise 


