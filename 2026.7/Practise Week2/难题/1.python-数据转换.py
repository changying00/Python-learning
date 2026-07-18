"""
数据转换】现有如下格式的数据 time 代表时间、 temperature 代表平均气温、 city 代表省份
[
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
编写一段代码、将上述数据转换为 如下格式
[
	{
		"city":  "河南省",
		"time":  ["2024-01" ,  "2024-02",  "2024-03"] ,
		"temperature":  [ "6°C",  "12°C",  "22°C"]
	},
	{
		"city":  "广东省",
		"time":  ["2024-01" ,  "2024-02",  "2024-03"] ,
		"temperature":  [ "16°C",  "26°C",  "26°C"]
	},
	{
		"city":  "四川省",
		"time":  ["2024-01" ,  "2024-02",  "2024-03"] ,
		"temperature":  [ "14°C",  "18°C",  "22°C"]
	},
]
写数据处理题时，先分析输入和输出的数据结构，确定数据应该存在哪里（列表、字典、嵌套关系），再写循环；需要长期保存的数据放循环外，临时变量放循环内。
"""

# #定义一个变量存储列表数据，
city_tem = [
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

# #我的解法绕迷了
# or i in range(len(city_tem)):
# for key,value in city_tem[i].items():
#     city_sort = []
#     dir_sort = {}
#     count = []
#     count1 = []
#     if city_tem[i]["city"] == "河南省":
#         count.append(city_tem[i]["time"])
#         count1.append(city_tem[i]["temperature"])
#         dir_sort["city"] = "河南省"
#         dir_sort["time"] = count
#         dir_sort["temperature"] = count1
#         city_sort.append(dir_sort)
#     elif city_tem[i]["city"] == "广东省":
#         count2 = []
#         count3 = []
#         count2.append( city_tem[i]["time"])
#         count3.append(city_tem[i]["temperature"])
#         dir_sort["city"] = "广东省"
#         dir_sort["time"] = count2
#         dir_sort["temperature"] = count3
#         city_sort.append(dir_sort)
#     else:
#            count3 = []
#            count4 = []
#            count3.append( city_tem[i]["time"])
#            count4.append(city_tem[i]["temperature"])
#            dir_sort["city"] = "四川省"
#            dir_sort["time"] = count3
#            dir_sort["temperature"] = count4
#            city_sort.append(dir_sort)
#            city_sort.append(dir_sort)
# print(city_sort)

#第一种解法
henan_time = []
henan_temp = []

guangdong_time = []
guangdong_temp = []

sichuan_time = []
sichuan_temp = []
city_sort = []
for item in city_tem:
        if item["city"] == "河南省":
            henan_time.append(item["time"])
            henan_temp.append(item["temperature"])
        elif item["city"] == "广东省":
            guangdong_time.append(item["time"])
            guangdong_temp.append(item["temperature"])
        else:
            sichuan_time.append(item["time"])
            sichuan_temp.append(item["temperature"])
city_sort.append({
    "city":"河南省",
    "time":henan_time,
    "temperature":henan_temp
})


city_sort.append({
    "city":"广东省",
    "time":guangdong_time,
    "temperature":guangdong_temp
})


city_sort.append({
    "city":"四川省",
    "time":sichuan_time,
    "temperature":sichuan_temp
})
print(city_sort)
#第二种解法
# city_sort = []
# result= {}
# for item in city_tem:
#     city = item["city"]
#     if city not in result:
#         result[city] = {
#             "city": city,
#             "time": [],
#             "temperature": []
#         }
#     result[city]["time"].append(item["time"])
#     result[city]["temperature"].append(item["temperature"])
# city_sort=list(result.values())
#
# print(city_sort)