from number import Number,Number1 #从模块取出来
#第一种实例 与 数字做 减
X = Number(10)      #Number.__init__(X,10)
Z =  X - 2       #Number.__sub__(X,2)
print(Z.data)
print(Z)

#第二种 实例与 实例做 减法
X1  = Number1(10)  #Number1.__init__(X1,10)
Y1  = Number1(4)   #Number1.__init__(Y1,4)
Z1 = X1 - Y1        #Number1.__sub__(X1,Y1)
print(Z1.data)
print(Z1)

#第二种延申，不同类之间做 运算
X2 = Number1(10)
Z2 =  X2 -Z     #?第一次，这是用哪个类的 __sub__做的减法，Z2类为啥是Number？？？牛逼我在Number1的__sub__ 设置的返回为Number类的实例
                #不同类间做减法， 谁在前用哪个类的__sub__方法，
print(X2)
print(Z2)

