#【字符串&递归】编写一个函数 get_all_comb(string)，然后输出所有可能的由该字符串中字符组成的排列。
# 例如 abc ==> ["abc", "acb", "bac", "bca", "cab", "cba"]
#思考，我没看要用递归，我想的是随机打乱，
#定义一个函数 get_all_comb(string):
def get_all_comb(string):
    """输出所有可能的由该字符串中字符组成的排列"""
    #递归的结束条件
    if len(string) == 1:
        return [string]

    result = []
    #每次选择一个字符作为开头
    for i in range (len(string)):
        #当前选择的字符
        current = string[i]
        #剩余没有选择的字符
        rest = string[:i] + string[i + 1:]
        #递归获取剩余字符的排列
        for item in get_all_comb(rest):
            #当前字符 + 后面的排列
            result.append(current + item)
    return result
if __name__ == "__main__":
    print(get_all_comb("abc"))