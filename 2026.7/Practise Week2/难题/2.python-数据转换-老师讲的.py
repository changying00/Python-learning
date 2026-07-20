data = [
	{"time": "2024-01" ,  "temperature":  "6°C" ,   "city":  "河南省"},
	{"time": "2024-02" ,  "temperature":  "12°C" ,   "city":  "河南省"},
	{"time": "2024-03" ,  "temperature":  "22°C" ,   "city":  "河南省"},
	{"time": "2024-01" ,  "temperature":  "16°C" ,   "city":  "广东省"},
	{"time": "2024-02" ,  "temperature":  "26°C" ,   "city":  "广东省"},
	{"time": "2024-03" ,  "temperature":  "26°C" ,   "city":  "广东省"},
	{"time": "2024-01" ,  "temperature":  "14°C" ,   "city":  "四川省"},
	{"time": "2024-02" ,  "temperature":  "18°C" ,   "city":  "四川省"},
	{"time": "2024-03" ,  "temperature":  "22°C" ,   "city":  "四川省"},
]
group_key = "city"
#定义一个变量、存储最终的结果
result = []
#遍历 原始数据的列表
for dct in data:
    #获取 分组键对应的值
    value = dct[group_key]
    #定义一个变量、用来存储 结果的字典
    result_dct ={}
    #遍历 结果result 列表、 查找group_key是否在里面,
    for d in result:
        if  d[group_key] == value:
             result_dct =d
             break
    else:
        #如果没有执行 break 说明没有找到
        result.append(result_dct)

    if len(result_dct) == 0:
        #如果 result_dct 是空的、则 将group_key 存储
        result_dct [group_key] = value
        #遍历 当前要处理的 中除了group_key之外的键
        for key,value in dct.items():
            if key != group_key:
                result_dct[key] = [value]
    else:
        #如果结果中存在 数据、则将数据追加到列表中即可
        for key,value in dct.items():
            if key != group_key:
                result_dct[key].append(value)
#整个循环结束、打印结果
print(result)