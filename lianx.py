# 错误1：遍历列表时删除元素
L = [1, 2, 3, 4, 5]
for x in L:
    if x % 2 == 0:
        L.remove(x)      # 危险！迭代器会跳过元素
# 结果：[1, 3, 5] — 但 4 被跳过了！

# # 正确做法1：遍历副本
# for x in L[:]:
#     if x % 2 == 0:
#         L.remove(x)
#
# # 正确做法2：从后往前遍历
# for i in range(len(L) - 1, -1, -1):
#     if L[i] % 2 == 0:
#         del L[i]
#
# # 正确做法3：列表推导式
# L = [x for x in L if x % 2 != 0]
#
# # 错误2：混淆 sort() 和 sorted()
# L = [3, 1, 2]
# result = L.sort()      # result 是 None！
# print(result)          # None
#
# # 正确做法
# L.sort()               # L 被修改
# print(L)               # [1, 2, 3]
# # 或者
# new_L = sorted(L)      # L 保持不变，new_L 是新列表