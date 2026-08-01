"""
    在python 中、使用re 模块操作 正则表达式、 使用Pattern 类型表示 正则表达式！！！

        re.compile(pattern,flags): 将 字符串 格式的正则表达式 转成 Pattern(模式)对象

        pattern: 正则表达式

        flags:设置 正则表达式 需要使用的模式、例如 i、s、m 模型

                -re.I : 忽略大小写
                -re.S : 点 可以 匹配 任意字符
                -re.M : 配合 限定符 可以实现 多行匹配
        flags 支持 同时使用 多模式 工作、使用 | 运算
"""
import re
#正则表达式 如果 包含\，通常需要在 字符串 前添加 前缀r
pattern = re.compile(r'(\w+)')