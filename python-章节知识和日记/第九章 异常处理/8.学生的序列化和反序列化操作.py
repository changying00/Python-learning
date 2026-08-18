from datetime import date, datetime 
import json 


class Student:

    def __init__(self, name: str, gender: str, birth: date):
        self.name = name 
        self.gender = gender 
        self.birth = birth

    def to_json(self):

        return {
            "name": self.name,
            "gender": self.gender, 
            "birth": self.birth.strftime("%Y-%m-%d")
        }

    def __repr__(self) -> str:
        
        return f"{self.__class__.__name__}({self.__dict__})"


def dct_to_student(student_dct):
    """
    将一个字典转成 student 对象
    """
    # 获取 字典 中的 出生日期 
    birth = student_dct.pop("birth")
    # 进行 反格式化
    birth = datetime.strptime(birth, "%Y-%m-%d").date()
    # 将 birth 放入到 字典中 
    student_dct["birth"] = birth 
    return Student(**student_dct)

if __name__ == "__main__":
    
    # 定义一个列表 、列表中存储多个学生信息 
    student_list = [
        Student("张三", "男", date(2000, 10, 10)),
        Student("李四", "女", date(2010, 8, 10)),
        Student("王五", "男", date(2001, 7, 17)),
        Student("赵六", "男", date(2000, 10, 10)),
    ]

    # 将列表 进行序列化 、并存储到 students.json 文件中 
    with open("./students.json", "wt", encoding="utf-8") as f:
        json.dump(student_list, f, default=lambda d: d.to_json(), indent=4, ensure_ascii=False)

    # 读取 数据 并进行反序列化
    with open("./students.json", "rt", encoding="utf-8") as f:
        data = json.load(f, object_hook=dct_to_student)

    print(data)