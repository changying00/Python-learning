"""
【正则表达式】现有一段字符串、例如
insert into tb_user(name, sex, age) values ( #{name} , #{sex} , #{age} )

编写一段程序、将其替换为
insert into tb_user(name, sex, age) values ( %(name)s , %(sex)s , %(age)s )
"""
import re
def convert_sql(sql):
    """
    将 #{xxx} 转换成 %(xxx)s
    """
    regex = r"#\{(\w+)\}"
    return re.sub(regex, r"%(\1)s", sql)
if __name__ == "__main__":

    sql = "insert into tb_user(name, sex, age) values ( #{name} , #{sex} , #{age} )"
    print(convert_sql(sql))