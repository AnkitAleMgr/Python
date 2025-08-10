class Book:

    def __init__(self, title : str , author : str, isbn : str , available : bool = True) -> None:
        self.title = title.capitalize().strip()
        self.author = author.capitalize().strip()
        self.isbn = isbn
        self.available = available

    def display_info(self) -> None:
        print("Title: ", self.title)
        print("Author: ", self.author)
        print("Isbn: ", self.isbn)
        print(f"Available: {'Yes' if self.available else 'No'}")

class Member:

    def __init__(self, name: str) -> None:
        self.name = name.capitalize().strip()
        self.borrowed_book = []


    def borrow_book(self, book : Book) -> None:
        if book.available:
            self.borrowed_book.append(book)
            book.available = False
            print(f"{book.title} has been borrowed by {self.name}")
        else:
            print(f"{book.title} is not availabe")

    def return_book(self, book : Book) -> None:
        if book not in self.borrowed_book:
            print(f"{self.name} hasn't borrowed a book name {book.title} to return.")   
            return
        self.borrowed_book.remove(book)
        book.available = True
        print(f"{book.title} has been return by {self.name}.")

    def view_borrowed_book(self) -> None:
        if not self.borrowed_book:
            print("No book has been borrowed")
            return
        print("********** Borrowed Book **********")
        for index, book in enumerate(self.borrowed_book, start= 1):
            print(f"{index}) {book.title} {book.isbn}")
        print("***********************************")

class Library:

    def __init__(self,name : str) -> None:
        self.name = name.capitalize().strip()
        self.books = []

    def add_book(self, book : Book) -> None:
        self.books.append(book)
    
    def list_available_book(self) -> None:
        if not self.books:
            print("No book has been added till now")
            return
        count = 1
        print("********** Available Book **********")
        for book in self.books:
            if book.available:
                # print(f"{Book.__name__}")
                print(f"{count}) {book.title}")
                count += 1
        print("********** Available Book **********")

# main entry point
if __name__ == "__main__":

    # Create 3 books and add them to the library
    thor = Book(title="thor", author= "samgam", isbn="1234-5678-90",available= True)
    spider_man = Book(title="spider man", author= "anup", isbn="1234-5678-900",available= True)
    wonder_women = Book(title="wonder_women", author= "samir", isbn="1234-5678-89",available= True)

    universal_library = Library(name="universal_library")
    universal_library.add_book(thor)
    universal_library.add_book(spider_man)
    universal_library.add_book(wonder_women)

    # Create a member
    ankit_member = Member("Ankit")

    # The member borrows one book
    ankit_member.borrow_book(book= thor)

    # view membre borrowed book:
    ankit_member.view_borrowed_book()

    # Display available books after borrowing
    universal_library.list_available_book()

    # The member returns the book
    ankit_member.return_book(thor)

    # Display available books after returning
    universal_library.list_available_book()