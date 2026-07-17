# a  = 1,2,3,4,43,31
#有一种解决变量个数少于元素的个数方法，就是使用星号表达式。通过星号表达式，
# 我们可以让一个变量接收多个值，代码如下所示。需要注意两点：首先，用星号表达式修饰的变量会变成一个列表，
# 列表中有0个或多个元素；其次，在解包语法中，星号表达式只能出现一次。
# i,j,*k  = a
# print(i,j,k)

# a,b,*c = range(1,10)
# print(a,b,c)
# a,b,c = [1,2,34]
# print(a,b,c)

# a,*c,b = "552511"
# print(a,c,b)

# import  timeit
# print("%.3f秒"%timeit.timeit("[1,2,3,4,5,6,7,8,9]",number=10000000))
# print("%.3f秒"%timeit.timeit("(1,2,3,4,5,6,7,8,9)",number=10000000))

lis = ["DGX","19","hx"]
print(tuple(lis) ) #把列表转换为元组
first = ("mubapen","meixi","neimaer")
print(list(first))