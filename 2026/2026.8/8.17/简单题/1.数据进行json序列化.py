"""一、将 python 中如下格式的数据、进行JSON序列化

data = {
    "name": "张三",
    "age": 30,
    "city": "河南郑州",
    "skills": ["Python", "JavaScript", "Data Science"],
"is_student": False,
(1,  ):  1
}
要求序列化后，能正常显示中文、 观察序列化后的数据和原数据有何区别 10分钟
def dumps(obj: Any,
          *,
          skipkeys: bool = False,
          ensure_ascii: bool = True,
          check_circular: bool = True,
          allow_nan: bool = True,
          cls: type[JSONEncoder] | None = None,
          indent: None | int | str = None,
          separators: tuple[str, str] | None = None,
          default: (Any) -> Any | None = None,
          sort_keys: bool = False,
          **kwds: Any) -> str
"""
#导入json库
import json
data = {
    "name": "张三",
    "age": 30,
    "city": "河南郑州",
    "skills": ["Python", "JavaScript", "Data Science"],
"is_student": False,
(1,  ):  1
}
ret = json.dumps(data,ensure_ascii=False,skipkeys=True,indent=2)
print(ret)