def times(x,y):
        return = x * y
        
#等价于下面
times1 = lambda x,y: x * y

#函数调用
times(2,3)

#调用后的结果进行保存
x = times(2,3.14)

#传入不同类型的数据,计算方法不一样
times("py",5)