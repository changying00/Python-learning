import pymysql
"""
    DML 命令 必须在 事务环境下 才能工作、否则 增、删、改 都不会影响表中的数据。
    解决 无法插入问题:
            a) 在创建 连接对象的时候 设置 autocommit=True (自动提交)、不推荐、这种做法每一个SQL 命令都是一个单独的事务环境、
                违背了事务概念。
            b) 手动 提交 或者 回滚事务。
                业务成功提交事务、     
"""
#创建 一个数据库连接对象
conn = None
try:
    conn = pymysql.connect(user='root',password='123456',host='localhost',port=3306,database='py2607b')
    # 定义要执行的 SQL命令
    # 在SQL 命令中、 如果需要数据、必须使用 占位符 代替、防止产生 SQL 注入的风险
    #    数据 通常来自 网页、网页中的数据是由用户输入的、为了解决SQL 注入(工具)、服务器在 定义SQL时候、数据必须用占位符
    #  %s      : 如果 使用 该格式的占位符、那么 传入数据的时候 需要通过 元组的 方式 传入数据
    #  %(name)s: 如果 使用 该格式的占位符、那么 传入数据的时候 需要通过 字典的 方式 传入数据
    sql="""
      
        insert into tb_qiku(name,address) values (%(name)s,%(address)s)
    """
    # insert into tb_qiku(name,address) values (%s,%s)
    #创建一个 SQL 执行器
    with conn.cursor() as cursor:
        params = {'name':'中共郑州',
                  'address':'郑州'}
        # 执行 SQL、并传入数据
        # rows = cursor.execute(sql,args=('中国河南','郑州'))
        rows = cursor.execute(sql, args=params)
        #输出 结果、lastrowid 用来获取 插入成功的 主键(主键必须是自动增长)
        print(f"插入成功、影响行数为{rows},当前数据的主键:{cursor.lastrowid}")
    #业务成功、提交事务
    conn.commit()
except:
    #如果产生异常、业务失败
    conn.rollback()
    #抛出错误
    raise
finally:
    if conn is None:
        conn.close()