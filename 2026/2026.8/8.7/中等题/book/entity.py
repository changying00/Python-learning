class Book:
    def __init__(self, id, name, author, price):
        self.__id = id
        self.__name = name
        self.__author = author
        self.__price = price

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        self.__author = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    def __str__(self):
        return str({
            "id": self.__id,
            "name": self.__name,
            "author": self.__author,
            "price": self.__price,
        })

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return (
            self.__id == other.__id
            and self.__name == other.__name
            and self.__author == other.__author
            and self.__price == other.__price
        )

    def __gt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.__price > other.__price

    def __hash__(self):
        return hash((self.__id, self.__name, self.__author, self.__price))
