X = 1
def nester():
    X = 2                 # 隐藏全局
    print(X)              # 局部：2
    class C:
        X = 3             # 类局部隐藏 nester 的：C.X 或 I.X（不是作用域）
        print(X)          # 局部：3
        def method1(self):
            print(X)      # 在外层 def 中（不是类里的 3！）：2
            print(self.X) # 继承的类局部：3
        def method2(self):
            X = 4         # 隐藏外层（nester，不是类）
            print(X)      # 局部：4
            self.X = 5    # 隐藏类的
            print(self.X) # 定位在实例中：5
    I = C()
    I.method1()
    I.method2()
print(X)                  # 全局：1
nester()                  # 其余输出：2, 3, 2, 3, 4, 5