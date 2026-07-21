#【lambda】编写一个函数 remove_if , 删除列表中满足条件的所有数据

def remove_if(ls_num,predicate):
    return[ v for v in ls_num if not predicate(v)]
#定义一个列表
ls1 = [1,2,3,4,5,6]
print(remove_if(ls1,lambda x: x < 5)) #[5, 6]
