
from typing import List

def get_all_comb(string:str) -> List[str]:
    """获取一个字符串的所有组合情况"""
    if(length := len(string)) == 0:
        return []

    #收敛条件
    if length == 1:
        return[string]
    #定义一个变量、用来存储最终的结果
    result = []
    #基于 索引和值的遍历方式
    for index,value in enumerate(string):
        #获取value 之外的剩余字符
        rest_string = string[:index] + string[index+1:]
        #获取 剩余字符的所有组合情况
        for s in get_all_comb(rest_string):
            #获取拼接后的数据
            data = value + s
            if data not in result:
                result.append(data)
    return result

if __name__ == "__main__":
    print(get_all_comb("abc"))