"""
大模型 默认 使用 Markdown 语法 进行 输出 。

在 LLM 中、 大模型 如果 返回 JSON 格式的数据、它 采用 字典结构 进行数据组装。


如果要 设置 LLM 返回的数据格式 、通常可以使用 Pydantic 模块 来定义 响应的数据结构

    http://192.168.17.37:11434/

"""
import ollama
from pydantic import BaseModel, Field
from typing import List


# 可以 让 LLM 按照 预设的 模式 返回 相关的数据
class Goods(BaseModel):
    """用来描述 商品的类 """
    id: str = Field("", description="商品的唯一编号")
    name: str = Field("", description="商品名称")
    price: int = Field("", description="商品价格")


class GoodsList(BaseModel):
    items: List[Goods] = Field(description="商品列表")

# 获取 Goods类型 对应的 json schema 信息
# print(GoodsList.model_json_schema())
messages = [
    {
        "role": "user",
        "content": """
            请从下面的 XML 中， 提取 和 商品相关的信息 、并进行数据组装

            <root>
                <Goods>
                    <id>S10000</id>
                    <name>笔记本电脑</name>
                    <price>￥4000</price>
                </Goods>

                <Goods>
                    <id>S10001</id>
                    <name>机械键盘</name>
                    <price>￥200</price>
                </Goods>

            </root>
        """
    }
]

stream = ollama.chat(
        "qiku",
        messages,
        think=False,
        stream=True,
        format=GoodsList.model_json_schema()
)

for chunk in stream:
    print(chunk.message.content, end="", flush=True)