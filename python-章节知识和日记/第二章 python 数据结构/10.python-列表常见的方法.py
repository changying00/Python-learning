"""
列表 中常见的方法  

  -  append(value) :  向列表的尾部添加数据 value
  -  insert(index, value) :  向 指定的 index 索引位置前 添加数据 value

  -  pop(index=-1) :  删除 指定索引位置的元素、并返回被删除的元素、 索引越界会产生错误 。 如果不传入索引、默认删除列表中最后一个元素
  -  remove(value) :  删除 第一个 value 元素 、 当 value 不存在的时候 会报错 
  -  clear()  : 清空 列表 


  -  index(value) :  获取 value 元素 在 列表中 第一次 出现的索引位置 、value 不存在， 会报错 。
  -  count(value) :  统计 value 元素 在 列表中 出现的次数 

  -  reverse()  :  将 列表中的所有元素 进行反转 、该方法 没有返回值 
  -  extend(iterable) :  将 可迭代对象中的 数据 合并到 列表中 

  -  copy() :  采用 浅克隆 技术 复制 当前 列表 、返回一个 新的 列表

"""

ls = [12, 54, 87, 6, 54, 2, 7, 2]

# ls.clear()
# 统计 54 元素在 列表中出现的次数
# print(ls.count(541)) 

# ls.reverse() 

ls.extend("abc") 

new_ls = ls.copy()

print(ls == new_ls)
print(ls is new_ls)