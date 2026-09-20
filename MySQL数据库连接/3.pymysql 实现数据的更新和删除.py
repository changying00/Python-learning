import pymysql

#创建数据库连接对象
conn = None

try:
    #创建数据库连接对象
    conn = pymysql.connect(user='root',password='123456',host='localhost',port=3306,database='py2607b')

    id = 4
    #获取 SQL 执行器
    with conn.cursor() as cursor:
        #定义 要执行的 SQL
        sql = """
            delete from tb_qiku where id = %s
        """
        # 执行SQL 并获取 影响的行数
        rows = cursor.execute(sql,args=(id,))
        # 删除 成功
        print(f'删除成功,影响{rows}行')
    #提交事务
    conn.commit()
except:
    if conn is not None:
        conn.rollback()
    raise
finally:
    if conn is not None:
        conn.close()