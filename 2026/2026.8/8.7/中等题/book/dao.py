try:
    from book.entity import Book
except ImportError:
    from entity import Book


class BookDao:
    def __init__(self):
        self.__books = []

    def save_book(self, book: Book):
        self.__books.append(book)

    def get_book_by_id(self, id):
        for book in self.__books:
            if book.id == id:
                return book
        return None

    def get_books(self):
        return list(self.__books)

    def get_books_by_name(self, name):
        return [book for book in self.__books if book.name == name]

    def remove_book(self, id):
        for i, book in enumerate(self.__books):
            if book.id == id:
                return self.__books.pop(i)
        return None
