##16. Library Management System (Constructor & Inheritance) 
##A library stores information about books and digital books. Create a base class Book 
##with a constructor to initialize book details. Create a derived class EBook that adds file 
##size information.


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("File Size:", self.file_size)


b = EBook("Python", "John", "5 MB")
b.display()
