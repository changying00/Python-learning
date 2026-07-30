"""
【字符串】 编写一个函数 count_num_sum(string) 统计字符串中所有的数字和。 例如 sdkhf34kg456 中的数字为 34 和 456 ，结果为 490

"""
#定义一个函数count_num_sum
def count_num_sum(string):
    """ 统计字符串所有的数字之和"""
    #用来保存最终的总和
    total =  0
    #用来临时拼接连续的数字字符
    current_num = ""
    for char in string:
        if char.isdigit():
            current_num += char
        else:
            #如果current_num不为空、说明刚刚结束了一段数字
            if current_num:
                #转换为整数并累加
                total += int(current_num)
                #清空、为下一个数字做准备
                current_num = ""
    #如果字符串 是以数字结尾的、循环结束后还需要把最后一段数字加上
    if current_num:
         total += int(current_num)
    return total
if __name__ == '__main__':
    print(count_num_sum("sdhf34kg456"))

