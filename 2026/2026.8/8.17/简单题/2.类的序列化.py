"""
定义一个 Student类、包含 name, age , birth (date类型) 属性、
定义一个列表、存储多个学生对象、要求使用 json 序列化 技术 对列表数据进行序列化，
使用 json.dump(obj, fd) 方式 尝试 将 数据写入到 文件中、且对结果进行 简单美化！
使用 json.load(fd) 读取文件的内容，并进行反序列化、且数据的格式为 Student ，
属性值 类型和原类型保持一致。
"""
from datetime import date,datetime
import json
#定义一个类
class Student:
    def __init__(self,name,age,birth):
        self.name = name
        self.age = age
        self.birth = birth

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

student1= Student('小明',22,date(2004,6,19))
student2= Student("小雪",20,date(2006,9,20))
student3= Student("小樱",10,date(2015,7,12))
class Json_student(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, date):
            return o.strftime("%Y-%m-%d")
        if hasattr(o, "__dict__"):
            return o.__dict__
ls_student = [student1,student2,student3]
with open("./student.txt",'wt',encoding="utf-8") as file:
    json.dump(ls_student,file,ensure_ascii=False,indent=4,cls =Json_student)

def convetor_student(dct):
    # 获取 dct 中的  birth
    birth = dct.pop("birth")
    # 进行日期的反格式化
    time = date.fromisoformat(birth)
    #也可以这样写time = datetime.strptime(birth,"%Y-%m-%d").date()
    dct["birth"] = time
    return Student(**dct)

with open("student.txt",'rt',encoding="utf-8") as file:
        # 从 json 文件中 读取数据
        dct = json.load(file,object_hook=convetor_student)
print(dct)
