"""


【列表】编写一段程序、计算一个数字组成的列表中所有数字的和

"""
#假设一个列表
ls = [1,2,4,23,3,4]
#定义一个变量接收列表数据的和
count = 0
#for循环一个列表的Length长度
for  i in range(len(ls)):
    #遍历列表的，每一个元素然后相加
     count += ls[i]
#循环结束打印，count的值
print(count)