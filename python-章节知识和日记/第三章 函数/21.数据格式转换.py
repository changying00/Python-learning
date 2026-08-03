from typing import List, Dict, Any


def convert_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """数据格式转换
        data : 要转换的数据
    """
    # 定义一个 列表、用来存储最终的结果
    result = []

    for d in data:
        # 获取 并删除 名字
        name = d.pop("name")

        for key, value in d.items():
            dct = {}
            # 负责 获取字典
            for dictionary in result:
                if key == dictionary["lang"]:
                    dct = dictionary
                    break
            else:
                result.append(dct)
            # 如果 字典是空的，则更新数据
            if len(dct) == 0:
                dct.update({"lang": key, "name": [name], "value": [value]})
            else:
                dct["value"].append(value)
                dct["name"].append(name)

    return result


if __name__ == "__main__":
    data = [
        {"name": "张三", "chinese": 90, "math": 85, "english": 67},
        {"name": "李四", "chinese": 50, "math": 30, "english": 95},
        {"name": "王五", "chinese": 82, "math": 77, "english": 45},
        {"name": "赵六", "chinese": 62, "math": 81, "english": 76},
    ]

    print(convert_data(data))