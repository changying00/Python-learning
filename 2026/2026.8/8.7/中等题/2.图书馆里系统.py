"""
使用面向对象完成 简单图书管理系统 ，具体要求如下
a)   新建一个包 book
b)  在 book 包下， 新建一个 entity模块，该模块内容如下
   1）  定义一个 Book 类，该类包含 id(图书编号)、name (书名)、author(作者)、price(价格)
   2）  要求属性 私有化、并提供 对应的 property getter,  setter 属性
   3）  提供 __str__  ，显示格式为 所有属性组成的字典格式字符串
   4）  提供 __eq__ ,  支持 比较 2本书内容是否相等
   5)    提供 __gt__ ,   支持 按照 价格 比较大小
   6）  提供 __hash__ ，  支持计算对象的 hash值

c)  在 book 包下、提供一个 模块 dao.py, 模块中内容如下
   1)  定义一个 BookDao 类 、用来完成对书籍的增删改查
   2）该类中 定义一个 列表属性(私有化) ， 用来存储 所有书籍
   3）提供 save_book(book)  ： 保存书籍方法
   4)  提供 get_book_by_id(id) :  根据书籍编号查找书籍
   5）提供 get_books()  :  获取所有书籍
   6)  提供 get_books_by_name(name)  根据作者查找书籍
   7)  提供 remove_book(id)  :  根据书籍ID 删除数据方法

d)  在 book 包下、 新建一个 模块 service.py 模块内容如下

   1） 定义一个 BookService 类、用来处理 图书馆业务
   2)   维护一个  BookDao 属性（私有化）、用来实现对书籍的增删改查
   3)   定义一个 add_book(book)  添加书籍， 如果书籍名存在，且作者相同，则返回添加失败
   4） 定义一个 borrow_book(name,  author) :  根据 书籍名和作者 编写 借书 业务
   5） 定义一个 back_book(book)  :  编写还书业务代码
   6)   对 这 三个业务 进行 功能测试   
"""

from book.entity import Book
from book.service import BookService


if __name__ == "__main__":
    service = BookService()

    b1 = Book(1, "三体", "刘慈欣", 59.0)
    b2 = Book(2, "活着", "余华", 35.0)
    b3 = Book(3, "三体", "刘慈欣", 59.0)

    print("添加 b1:", service.add_book(b1))
    print("添加 b2:", service.add_book(b2))
    print("添加重复 b3:", service.add_book(b3))

    print("b1 > b2:", b1 > b2)
    print("b1 == b3:", b1 == b3)

    borrowed = service.borrow_book("三体", "刘慈欣")
    print("借书:", borrowed)

    print("还书:", service.back_book(borrowed))
