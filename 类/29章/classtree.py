"""
classtree.py: 用命名空间链接攀登继承树，
用缩进显示更高层的超类，表示高度
"""

def classtree(cls, indent):
    print('.' * indent + cls.__name__)  # 在这里打印类名
    for supercls in cls.__bases__:      # 递归到所有超类
        classtree(supercls, indent+3)   # 可能多次访问超类

def instancetree(inst):
    print('Tree of', inst)              # 显示实例
    classtree(inst.__class__, 3)        # 爬到它的类

def selftest():
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(B,C): pass
    class E: pass
    class F(D,E): pass
    instancetree(B())
    instancetree(F())

if __name__ == '__main__': selftest()