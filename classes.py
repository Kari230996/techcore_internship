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
        

book1 = Book("Война и мир", "Лев Толстой")
book2 = Book("Война и мир", "Лев Толстой")
book3 = Book("Анна Каренина", "Лев Толстой")

print(book1)
print(repr(book1))

print(book1 == book2)
print(book1 == book3)