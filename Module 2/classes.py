class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
       

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.title == other.title and self.author == other.author

class Ebook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __repr__(self):
        return f"Ebook(title='{self.title}', author='{self.author}', file_size={self.file_size}MB)"

    def __eq__(self, other):
        if not isinstance(other, Ebook):
            return NotImplemented
        return (
            self.title == other.title
            and self.author == other.author
            and self.file_size == other.file_size
        )


book1 = Book("Война и мир", "Лев Толстой")
book2 = Book("Война и мир", "Лев Толстой")
book3 = Book("Анна Каренина", "Лев Толстой")

ebook1 = Ebook("1984", "Джордж Оруэлл", 5)
ebook2 = Ebook("1984", "Джордж Оруэлл", 5)
ebook3 = Ebook("1984", "Джордж Оруэлл", 10)


print(book1)
print(repr(book1))

print(ebook1)          
print(repr(ebook1))  


print(book1 == book2)
print(book1 == book3)

print(ebook1 == ebook2)  
print(ebook1 == ebook3)  