X = 11 #该模块的全局
def g1():
    print(X)  #11引用模块的全局X
def g2():
    global X
    # 声明：下面的赋值写到模块全局
    X = 22  # 修改模块中的全局
def h1():
    X = 33  # 函数中的局部
    def nested():
        print(X)  # 引用外层作用域中的局部（33）
def h2():
    X = 33  # 函数中的局部
    def nested():
        nonlocal X  # 声明：下面的赋值写到外层函数的局部
        X = 44  # 修改外层作用域中的局部

g1()
g2()
h1()
h2()