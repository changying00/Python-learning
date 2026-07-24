"""
难题 【函数】现有如下格式的数据 , 已知 name 代表 姓名、其它均代表成绩。
[
	{“name” : “张三” ,  “chinese”:  90 ,  “math”:  85,  “english”:  67} ,
	{“name” : “李四” ,  “chinese”:  50 ,  “math”:  30,  “english”:  95} ,
	{“name” : “王五” ,  “chinese”:  82 ,  “math”:  77,  “english”:  45} ,
	{“name” : “赵六” ,  “chinese”:  62 ,  “math”:  81,  “english”:  76} ,
]
定义一个函数 convert_data 、实现将 上述 数据的格式转换为 如下格式：
[
	{
	    "lang":  "chinese" ,
            "name":  [“张三” ,  “李四”,  “王五”,  “赵六”],
            "value":  [90,  50,  82,  62]
        },
       {
	    "lang":  "math" ,
            "name":  [“张三” ,  “李四”,  “王五”,  “赵六”],
            "value:  [85, 30 ,77 , 81]
        },
	{
	    "lang":  "english" ,
            "name":  [“张三” ,  “李四”,  “王五”,  “赵六”],
            "value":  [67,  95,  45,  76]
        }
]
"""
#



def convert_data(ls_data):
    result = {}
    for item in ls_data:
        name = item["name"]
        for lang, score in item.items():
            # 跳过姓名
            if lang == "name":
                continue
            # 第一次出现科目，创建结构
            if lang not in result:
                result[lang] = {
                    "lang": lang,
                    "name": [],
                    "value": []
                }
            result[lang]["name"].append(name)
            result[lang]["value"].append(score)
    return list(result.values())
ls1 = [
    {"name":"张三","chinese":90,"math":85,"english":67},
    {"name":"李四","chinese":50,"math":30,"english":95},
    {"name":"王五","chinese":82,"math":77,"english":45},
    {"name":"赵六","chinese":62,"math":81,"english":76},
]
print(convert_data(ls1))




