from typing import List, Dict, Any


def get_goods_combine(base: Dict[str, Any], attrs: Dict[str, List[Dict[str, Any]]]) -> List[Dict[str, Any]]:
    """
    根据 商品 基本信息 和 属性 、生成 该商品的所有 配置
    """

    # 构建一个 列表、存储 多列表 交叉组合的结果
    temp_list = [{**base}]

    for key, value_list in attrs.items():
        temp_list = [
            {**dct, key: value["name"], "price": value["price"] + dct["price"]}
            for value in value_list
            for dct in temp_list
        ]

    return temp_list


if __name__ == "__main__":

    base_goods = {"name": "华为Meta30", "price": 7000}
    attr_dict = {
        "color": [{"name":"黑曜石",  "price": 0} ,   {"name": "银白色",  "price": 20} , {"name":"土豪金",  "price": 50}  ],
        "memory": [ {"name":  "256G",  "price": 300} , {"name":  "128G",  "price":  150} ,  {"name": "64G",  "price": 0} ],
        "time": [{"name":  "1年",  "price":  100},  {"name":  "2年",  "price": 180}, {"name":  "永久",  "price": 800}]
    }

    result = get_goods_combine(base_goods, attr_dict)

    for data in result:
        print(data)