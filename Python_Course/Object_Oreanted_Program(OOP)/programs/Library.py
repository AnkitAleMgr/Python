class Library:
    # constructor
    def __init__(self, no_of_books, *books):
        self.__books = list(books)
        # checking if no of book accurate
        if len(self.__books) != no_of_books:
            raise ValueError("No of books is invalid.")
        else:
            self.__no_of_books = no_of_books

    # for printing
    def __str__(self):
        books_str = ", ".join(self.__books)
        return f"No of books: {self.__no_of_books}\nBooks: {books_str}"

    # getter for books
    @property
    def books(self):
        return self.__books
    
    # setter for changing books name
    @books.setter
    def books(self, value):
        index, new_book = value
        self.__books[index] = new_book
        print(self.__books)

    # getter for no of books 
    @property
    def no_of_books(self):
        return self.__no_of_books
    
# instances
library1 = Library(3 , "Harry porter", "Spider man", "Avenger")
library2 = Library(5, "Harry porter", "Black Panther", "Jhon Wick", "Avenger", "Avatar")

print(library1)
print()
print(library2)
print()
library2.books = (0 , "Captain America")

