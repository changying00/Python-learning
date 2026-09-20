"""
  操作数据库的工具类

    threadlocal :  本地线程、它的最大特点就是 将它管理的资源 给 每一个线程 克隆一份 。

"""
from db import DBUtils, transcational
@transcational
def test():
    sql = "insert into tb_qiku(name, address) values(%s, %s)"
    pk = DBUtils.insert(sql, args=('AAA', 'BBBB'))
    print(f"插入数据成功、返回的主键是 {pk}")

    sql = "update tb_qiku set name = %s, address = %s where id = %s"
    rowcount = DBUtils.update(sql, args=('AAAA',  'BBBBBB',  4))
    print(f"更新数据成功、影响行数{rowcount}")

    sql = "delete from tb_qiku where id = %s"
    rowcount = DBUtils.delete(sql, args=(3, ))
    print(f"删除数据成功、影响行数是{ rowcount}")

    sql = "select * from tb_qiku where id = %s"
    data = DBUtils.select_one(sql, args=(4, ))
    print(f"查询的单条数据是: {data}")

    # 查询所有数据
    sql = "select * from tb_qiku"
    data = DBUtils.select_all(sql)

if __name__ == "__main__":
    test()