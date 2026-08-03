# def make_incrementor(n):
#     return lambda x: x * n
#
# f = make_incrementor(2)
# print(f(2))
#
import keyword

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
#把列表的每个元素叫 pair 然后按照pair[1]位置的值 进行排序
pairs.sort(key=lambda pair: pair[1])
print(pairs)

