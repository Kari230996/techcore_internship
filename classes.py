class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
       
    def __str__(self):
        return f"'{self.title}' от автора {self.author}"

print(Book("Война и мир", "Лев Толстой"))