# class 语句 允许 global 和 nonlocal 像def 一样修改赋值规则
gvar =111
class C:
    global gvar #修改外层模块中的名字 gvar
    gvar = 222 #否则它会是类属性 c.gvar

print(gvar)

def outer():
    nvar = 111
    class C:
        nonlocal nvar  #修改外层函数中的名字 nvar
        nvar = 222  #否则他会是类的属性 c.nvar

    print(nvar)

print(outer())