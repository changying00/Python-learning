try:
    from book.entity import Book
    from book.dao import BookDao
except ImportError:
    from entity import Book
    from dao import BookDao


class BookService:
    def __init__(self):
        self.__dao = BookDao()

    def add_book(self, book: Book):
        books = self.__dao.get_books()
        for b in books:
            if b.name == book.name and b.author == book.author:
                return False
        self.__dao.save_book(book)
        return True

    def borrow_book(self, name, author):
        books = self.__dao.get_books()
        for book in books:
            if book.name == name and book.author == author:
                self.__dao.remove_book(book.id)
                return book
        return None

    def back_book(self, book: Book):
        self.__dao.save_book(book)
        return True


if __name__ == "__main__":
    service = BookService()

    b1 = Book(1, "Python入门", "张三", 59.0)
    b2 = Book(2, "Java实战", "李四", 79.0)
    b3 = Book(3, "Python入门", "张三", 59.0)

    print("添加 b1:", service.add_book(b1))
    print("添加 b2:", service.add_book(b2))
    print("添加 b3(同名同作者):", service.add_book(b3))

    borrowed = service.borrow_book("Python入门", "张三")
    print("借书:", borrowed)

    print("还书:", service.back_book(borrowed))
    print("再次添加同书:", service.add_book(Book(4, "Python入门", "张三", 59.0)))
