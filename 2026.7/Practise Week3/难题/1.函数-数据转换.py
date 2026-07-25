"""
【函数】现有数据(示例数据、实际数据格式一致)格式如下
# 基本数据
phone = {"name":  "华为Meta30",  "price":  7000}
# 商品属性字典
attr_dict = {
        "color": [{"name":"黑曜石",  "price": 0} ,   {"name": "银白色",  "price": 20} , {"name":"土豪金",  "price": 50}  ],
        "memory": [ {"name":  "256G",  "price": 300} , {"name":  "128G",  "price":  150} ,  {"name": "64G",  "price": 0} ],
        "time": [{"name":  "1年",  "price":  100},  {"name":  "2年",  "price": 180}, {"name":  "永久",  "price": 800}]
    }
现编写一段程序、获取某产品所有组合情况，列表的个数不确定。例如

[
  {"name": "华为Meta30",  "color":  "银白色",   "memory" :  "256G",  "time":  "1年",  "price":  7420}
   ....
]
"""
# 基本数据
phone = {"name": "华为Meta30", "price": 7000}

# 商品属性
attr_dict = {
    "color": [
        {"name": "黑曜石", "price": 0},
        {"name": "银白色", "price": 20},
        {"name": "土豪金", "price": 50}
    ],
    "memory": [
        {"name": "256G", "price": 300},
        {"name": "128G", "price": 150},
        {"name": "64G", "price": 0}
    ],
    "time": [
        {"name": "1年", "price": 100},
        {"name": "2年", "price": 180},
        {"name": "永久", "price": 800}
    ]
}


def get_all_phone(phone, attr_dict):
    # 保存所有组合结果
    result = []
    # 取出所有属性名
    # ['color', 'memory', 'time']
    keys = list(attr_dict.keys())
    def dfs(index, current, total_price):
        """
        index       ：当前正在处理第几个属性
        current     ：已经选择好的属性组合
        total_price ：当前组合的总价格
        """
        # =====================
        # 递归结束条件
        # =====================
        # 当 index 等于属性个数时
        # 说明 color、memory、time 都已经选择完成
        if index == len(keys):
            # 创建最终商品信息
            data = {
                "name": phone["name"],
                "price": total_price
            }
            # 将已选择好的属性加入字典
            data.update(current)
            # 保存结果
            result.append(data)
            return
        # 当前要处理的属性名
        # 第一次：color
        # 第二次：memory
        # 第三次：time
        key = keys[index]
        # 遍历当前属性所有可选项
        for item in attr_dict[key]:
            # 保存当前选择
            # 例如：
            # {"color":"黑曜石"}
            current[key] = item["name"]
            # 递归处理下一个属性
            dfs(
                index + 1,                  # 处理下一种属性
                current.copy(),             # 拷贝当前组合，避免相互影响
                total_price + item["price"] # 累加价格
            )
    # 从第0个属性开始
    dfs(
        0,                  # 从color开始
        {},                 # 当前还没有任何选择
        phone["price"]      # 初始价格就是手机价格
    )
    return result
phones = get_all_phone(phone, attr_dict)

print("组合数量：", len(phones))

for phone in phones:
    print(phone)






