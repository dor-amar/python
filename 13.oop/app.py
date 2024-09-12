class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def decription(self):
        return f"{self.title} by {self.author}"
    

my_book = Book("Devops","Dor Amar",7000)
print(my_book.author)
print(my_book.title)
print(my_book.decription())



        


