"""
【类与对象】图书馆类：创建一个图书馆类，其中包含书籍和读者对象，具有借书、还书等方法。
"""
# #定义一个图书馆类
# class Library:
#     #定义类的属性
#     Books = ["平凡的世界","活着","三体1"]
#     def __init__(self,author,book_name=Books):
#         self.book_name=book_name
#         self.author=author
#
#     #定义借书方法
#     def borrowing_books(self,borrow_book):
#         if borrow_book in self.book_name:
#             self.book_name.remove(borrow_book)
#             print(f"恭喜读者:{self.author}借书成功，名为:{borrow_book}")
#         else:
#             print("抱歉图书馆没有这本书")
#     #定义还书方法
#     def return_book(self,return_book_name):
#         self.book_name+=return_book_name
#         print("恭喜你还书成功")
#
# if __name__=="__main__":
#     lib1= Library("董国旋")
#     #借书
#     lib1.borrowing_books("平凡界")
#
#     #还书
#     lib1.return_book("平凡的世界")
"""【类与对象】图书馆类：创建一个图书馆类，具有借书、还书、查询等方法。"""

class Library:
    """图书馆类"""
    def __init__(self, library_name, books=None):
        """
        初始化图书馆
        :param library_name: 图书馆名称
        :param books: 书籍列表（默认为空）
        """
        self.library_name = library_name
        # 如果没传入书籍列表，就创建一个空列表
        if books is None:
            self.books = []
        else:
            self.books = books.copy()  # 使用copy避免共享列表
        self.borrowed_books = []  # 记录已借出的书
    def add_book(self, book_name):
        """添加新书"""
        if book_name not in self.books and book_name not in self.borrowed_books:
            self.books.append(book_name)
            print(f"《{book_name}》已添加到{self.library_name}")
        else:
            print(f"《{book_name}》已存在")
    def borrowing_books(self, book_name):
        """借书方法"""
        if book_name in self.borrowed_books:
            print(f"《{book_name}》已被借走")
            return False
        if book_name in self.books:
            self.books.remove(book_name)
            self.borrowed_books.append(book_name)
            print(f"借书成功！《{book_name}》")
            return True
        else:
            print(f"抱歉，{self.library_name}没有《{book_name}》这本书")
            return False

    def return_book(self, book_name):
        """还书方法"""
        if book_name in self.borrowed_books:
            self.borrowed_books.remove(book_name)
            self.books.append(book_name)
            print(f"还书成功！《{book_name}》")
            return True
        else:
            print(f"《{book_name}》不在借出记录中")
            return False

    def show_books(self):
        """显示所有书籍状态"""
        print(f"\n {self.library_name} 的藏书：")
        print(f"可借书籍：{self.books if self.books else '无'}")
        print(f"已借书籍：{self.borrowed_books if self.borrowed_books else '无'}")
        print(f"总计：{len(self.books) + len(self.borrowed_books)} 本")

# 测试代码
if __name__ == "__main__":
    # 创建图书馆（带初始书籍）
    lib = Library("城市图书馆", ["平凡的世界", "活着", "三体1"])
    # 查看初始状态
    lib.show_books()
    # 借书
    print("\n【借书测试】")
    lib.borrowing_books("平凡的世界")  # 成功
    lib.borrowing_books("平凡的世界")  # 已被借走
    lib.borrowing_books("三体1")  # 成功
    # 查看借书后的状态
    lib.show_books()
    # 还书
    print("\n【还书测试】")
    lib.return_book("平凡的世界")  # 成功
    lib.return_book("哈利波特")  # 不存在
    # 查看最终状态
    lib.show_books()