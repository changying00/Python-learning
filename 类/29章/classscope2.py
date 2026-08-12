X = 1
def nester():
    X = 2                 # 隐藏全局
    print(X)              # 局部：2
    class C:
        print(X)          # 在外层 def（nester）中：2
        def method1(self):
            print(X)      # 在外层 def（nester）中：2
        def method2(self):
            X = 3         # 隐藏外层（nester）
            print(X)      # 局部：3
    I = C()
    I.method1()
    I.method2()
print(X)                  # 全局：1
nester()                  # 其余输出：2, 2, 2, 3