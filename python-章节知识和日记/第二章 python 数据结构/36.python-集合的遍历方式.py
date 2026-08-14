"""
集合 常见的 遍历方式 :

    a)  值遍历  

        for var in iterable:
            pass

    b)  基于值 和索引的 遍历方式  enumerate 

"""

s1 = {"xyz", "1234", "abc"}

# for v in s1:
#     print(v)

for index, v in enumerate(s1):
    print(index, v)