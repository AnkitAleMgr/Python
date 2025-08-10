from abc import ABC

class Book:

    def __init__(self, title : str , author : str, isbn : str , available : bool = True) -> None:
        self.title = title.capitalize().strip()
        self.author = author.capitalize().strip()
        self.isbn = isbn
        self.available = available
        self.reserved_list = []

    def display_info(self) -> None:
        print("Title: ", self.title)
        print("Author: ", self.author)
        print("Isbn: ", self.isbn)
        print(f"Available: {'Yes' if self.available else 'No'}")

    def is_reserved():
        pass

class Library:

    def __init__(self,name : str) -> None:
        self.name = name.capitalize().strip()
        self.books = []

    def add_book(self, book : Book) -> None:
        self.books.append(book)
        print(f"{book.title} has been added in {self.name}")
    
    def remove_book(self, book: Book) ->None :
        if book in self.books:
            self.books.remove(book)
            print(f"{book.title} has been removed form {self.name}.")
        else:
            print(f"No book found name {self.book.title} in library {self.name}.")

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
        print("***********************************")

    def find_book_by_title(self, name: str) -> None:
        found_book = []
        for book in self.books:
            if book.title == name.capitalize().strip():
                found_book.append(book)
        if found_book:
            print("********** Matching Book **********")
            for index,book in enumerate(found_book, start= 1):
                print(f"{index}) {book.title} - {book.inbn} - {book.available}")
            print("***********************************")

class Person(ABC):

    def __init__(self, name : str, email : str, id : int) -> None:
        self.name = name.capitalize().strip()
        self.email = email.strip()
        try:
            self.id = int(id)
        except ValueError:
            raise ValueError(f"Invalid id '{id}'. ID must be an integer.")
        
    def display_info(self) -> None:
        print("ID:",self.id)
        print("Name:",self.name)
        print("Email:",self.email)

    def update_detail(self, **kwargs) -> None:
        if not kwargs:
            print("Please send some detail to chanage")
            return
        for key, value in kwargs.items():
            if value is not None and hasattr(self, key):
                setattr(self, key, value)
            else:
                print(f"Warning: Attribute '{key}' not found or value is None.")

class Librarian(Person):
    
    def __init__(self, name: str, email: str, id : int, employed_id : int) -> None:
        super().__init__(name, email, id)
        try:
            self.employed_id = int(employed_id)
        except ValueError:
            raise ValueError(f"Employed id {employed_id} need to be number")

    def add_book(self, book: Book, library: Library) -> None:  # noqa: F811
        if book:
            library.add_book(book)
        else:
            print(f"No book found name {book.title}")

    def remove_book(self, book : Book, library : Library) -> None:
        library.remove_book(book)

    def view_all_book(self, library : Library) -> None:
        library.list_available_book()
        
    

class Member(Person):

    def __init__(self, name: str, email: str, id : int, ) -> None:
        super().__init__(name, email, id)
        self.borrowed_book = []


    def borrow_book(self, book : Book) -> None:
        if book.available:
            self.borrowed_book.append(book)
            book.available = False
            print(f"{book.title} has been borrowed by {self.name}")
        else:
            print(f"{book.title} is not availabe")
            book.reserved_list.append(self)
            print(f"{self.name} has been a dded in reserve list for {book.title}")

    def return_book(self, book : Book) -> None:
        if book not in self.borrowed_book:
            print(f"{self.name} hasn't borrowed a book name {book.title} to return.")   
            return
        self.borrowed_book.remove(book)
        book.available = True
        print(f"{book.title} has been return by {self.name}.")
        book.is_reserved(book)

    def view_borrowed_book(self) -> None:
        if not self.borrowed_book:
            print("No book has been borrowed")
            return
        print("********** Borrowed Book **********")
        for index, book in enumerate(self.borrowed_book, start= 1):
            print(f"{index}) {book.title} {book.isbn}")
        print("***********************************")



# main entry point
if __name__ == "__main__":
    pass
    # # Create 3 books and add them to the library
    # thor = Book(title="thor", author= "samgam", isbn="1234-5678-90",available= True)
    # spider_man = Book(title="spider man", author= "anup", isbn="1234-5678-900",available= True)
    # wonder_women = Book(title="wonder_women", author= "samir", isbn="1234-5678-89",available= True)

    # universal_library = Library(name="universal_library")
    # universal_library.add_book(thor)
    # universal_library.add_book(spider_man)
    # universal_library.add_book(wonder_women)

    # # Create a member
    # ankit_member = Member("Ankit")

    # # The member borrows one book
    # ankit_member.borrow_book(book= thor)

    # # view membre borrowed book:
    # ankit_member.view_borrowed_book()

    # # Display available books after borrowing
    # universal_library.list_available_book()

    # # The member returns the book
    # ankit_member.return_book(thor)

    # # Display available books after returning
    # universal_library.list_available_book()