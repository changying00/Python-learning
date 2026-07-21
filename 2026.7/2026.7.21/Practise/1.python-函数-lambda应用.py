#【lambda】编写一个 find函数、实现从列表中获取第一个满足条件的元素、如果找不到对应的元素、则返回 None
# 完成如下功能
# 定义一个列表、列表中的每一个元素是一个字典、例如 {"id": 1, "name": "xxx"} 格式， 查找 id < 10 的 第一条数据
#定义一个列表ls_id
#定义一个列表
ls_id = [{"id":1,"name":"dgx"},
         {"id":2,"name":"hanxu"},
         {"id":11,"name":"dx"},
         {"id":21,"name":"hx"},
         {"id":8,"name":"dx"}]

#创建一个函数
def find(id_count,predicate):
    for v in id_count:
        if predicate(v):
            return v
    return None
print(find(ls_id,lambda v:v["id"] < 10  ))