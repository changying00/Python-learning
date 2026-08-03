"""
【字符串】编写一个函数 isanagram，接受两个字符串参数，然后判断它们是否为互为 Anagram（即由相同的字母但以不同的顺序组成）
"""
#定义一个函数、判断字符是否互为Anagram
def  isanagram(str1:str,str2:str)->bool:
    """判断俩个字符串是否互为Anagram"""
    #判断俩个字符串的长度是否相同，不相同则为False
    if len(str1) != len(str2):
        return False
    #列表推导式 把字符串str2的元素放到ls1
    ls1 = [i for i in str2]
    #遍历一个字符串str1
    for i in str1:
        #判断i是否在ls1中，如果不在返回false
        if i not in ls1:
            return False
        #如果在就继续删除
        ls1.remove(i)
    #如果ls1里面的元素删除完了，就返回True
    if ls1 == [] :
        return True
    return False

if __name__ == '__main__':
        print(isanagram("aab","baa"))
