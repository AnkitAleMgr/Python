from abc import ABC
from re import U
from data_manager import save_to_csv
from exceptions import BookUnavailableError, InvalidMemberError
from validators import is_valid_librarian, is_valid_member, is_valid_book

class Book:

    def __init__(self, title : str , author : str, isbn : str , available : bool = True) -> None:
        self.title = title.capitalize().strip()
        self.author = author.capitalize().strip()
        self.isbn = isbn
        self.available = available
        self.reserved_list = []
        self.library = None

    def __str__(self) -> str:
        return f"{self.title} by {self.author} ({'Available' if self.available else 'Checked out'})"

    def display_info(self) -> None:
        print("Title: ", self.title)
        print("Author: ", self.author)
        print("Isbn: ", self.isbn)
        print(f"Available: {'Yes' if self.available else 'No'}")

    def add_reserved(self, member : object) -> None:
        if not is_valid_member(member):
            raise InvalidMemberError(f"No such member found named {member.name}")
        self.reserved_list.append(member)
    
    def notify_next_reserve(self) -> None:
        if self.reserved_list:
            next_member = self.reserved_list.pop(0)
            try:
                next_member.borrow_book(book = self, library = self.library)
            except Exception as e:
                print(f"Failed to lend {self.title} to {next_member.name}: {e}")
                
    def dict_info(self) -> dict:
        return {
            "Title" : self.title,
            "Author" : self.author,
            "Isbn" : self.isbn,
            "Available" : self.available
        }

class Library:

    _libraries = []
    _free_id = []
    _active_id = 1

    def __init__(self,name : str) -> None:
        self.name = name.capitalize().strip()
        self.books = []
        self.members = []
        self.librarians = []

        if Library._free_id:
            self.id = Library._free_id.pop(0)
        else:
            self.id = Library._active_id
            Library._active_id += 1
        Library._libraries.append(self)

    def __str__(self) -> str:
        return f"Library: {self.name} with {len(self.books)} books and {len(self.members)} members and {len(self.librarians)} librarians."

    def dict_info(self) -> dict:
        return {
            "Id" : self.id,
            "Name" : self.name
        }

    def add_member(self, member : object) -> None:
        if not isinstance(member, Member):
            print("Error: Only Member instances can be added.")
            return
        self.members.append(member)
        print(f"{member.name} has been added to {self.name}")

    def add_librarian(self, librarian : object) -> None:
        if not isinstance(librarian, Librarian):
            print("Error: Only Librarian instances can be added.")
            return
        self.librarians.append(librarian)
        print(f"{librarian.name} has been added to {self.name}")

    def add_book(self, book : Book) -> None:
        self.books.append(book)
        self.books = self
        print(f"{book.title} has been added in {self.name}")
    
    def remove_book(self, book: Book) ->None :
        if book in self.books:
            self.books.remove(book)
            print(f"{book.title} has been removed from {self.name}.")
        else:
            print(f"No book found name {book.title} in library {self.name}.")

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
                print(f"{index}) {book.title} - {book.isbn} - {book.available}")
            print("***********************************")
        else:
            print(f"No book found named {name} in {self.name}")

    def is_part_of(self, person: object) -> bool:
        return person in self.members or person in self.librarians

    def save_books(self) -> None:
        if self.books:
            save_to_csv([book.dict_info() for book in self.books], f"book_{self.id}.csv")
        else:
            print("No book has been added till now.")
        
    def save_libraries(self) -> None:
        if Library._libraries:
            save_to_csv([library.dict_info() for library in Library._libraries], "libraries.csv")
        else:
            print("No library has been added till now")

    def save_members(self) ->None:
        if self.members:
            save_to_csv([member.dict_info() for member in self.members],f"member_{self.id}.csv")
        else:
            print("No member has been added till now")
        
    def save_librarians(self) -> None:
        if self.librarians:
            save_to_csv([librarian.dict_info() for librarian in self.librarians], f"librarian_{self.id}.csv")
        else:
            print("No librarians has been added till now")

class Person(ABC):

    _person_active_id = 1
    _person_free_id = []

    def __init__(self, name : str, email : str) -> None:
        self.name = name.capitalize().strip()
        self.email = email.strip()
        if Person._person_free_id:
            self.id = Person._person_free_id.pop(0)
        else:
            self.id = Person._person_active_id
            Person._person_active_id += 1
        
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
    
    _librarian_active_id = 1
    _librarian_free_id = []

    def __init__(self, name: str, email: str) -> None:
        super().__init__(name, email)
        if Librarian._librarian_free_id:
            self.employed_id = Librarian._librarian_free_id.pop(0)
        else:
            self.employed_id = Librarian._librarian_active_id
            Librarian._librarian_active_id += 1

    def __str__(self) -> str:
        return f"Name: {self.name} (Id: {self.id})"

    def add_book(self, book: Book, library: Library) -> None:  # noqa: F811
        if is_valid_book(book):
            library.add_book(book)
        else:
            print(f"No book found name {book.title}")

    def remove_book(self, book : Book, library : Library) -> None:
        library.remove_book(book)

    def view_all_book(self, library : Library) -> None:
        library.list_available_book()
        
    def dict_info(self) -> dict:
        return {
            "ID" : self.id,
            "Employed ID" : self.employed_id, 
            "Name" : self.name,
            "Email" : self.email, 
        }
    
class Member(Person):

    def __init__(self, name: str, email: str) -> None:
        super().__init__(name, email)
        self.borrowed_book = []

    def __str__(self) -> str:
        return f"Member: {self.name} (ID: {self.id})"

    def borrow_book(self, book : Book, library : Library) -> None:
        if not library.is_part_of(self):
            raise Exception(f"{self.name} is not part of {library.name}")
        if not is_valid_book(book):
            raise TypeError("borrow_book expects a Book object")
        if book.available:
            self.borrowed_book.append(book)
            book.available = False
            print(f"{book.title} has been borrowed by {self.name}")
        else:
            book.add_reserved(self)
            raise BookUnavailableError(f"{book.title} is not available, added to reserve list.")

    def return_book(self, book : Book) -> None:
        if book not in self.borrowed_book:
            print(f"{self.name} hasn't borrowed a book name {book.title} to return.")   
            return
        self.borrowed_book.remove(book)
        book.available = True
        print(f"{book.title} has been return by {self.name}.")
        book.notify_next_reserve()

    def view_borrowed_book(self) -> None:
        if not self.borrowed_book:
            print("No book has been borrowed")
            return
        print("********** Borrowed Book **********")
        for index, book in enumerate(self.borrowed_book, start= 1):
            print(f"{index}) {book.title} {book.isbn}")
        print("***********************************")

    def dict_info(self) -> dict:
        return {
            "ID" : self.id,
            "Name" : self.name,
            "Email" : self.email, 
        }

# main entry point
if __name__ == "__main__":

    # creating library:
    united_library = Library(name= "United_library")
    
    # creating book:
    thor_book_1 = Book(title="Thor", author="Thomes selvi", isbn="100-100-100", available= True)
    thor_book_2 = Book(title="Thor", author="Thomes selvi", isbn="100-100-101", available= True)
    thor_book_3 = Book(title="Thor", author="Thomes selvi", isbn="100-100-102", available= True)
    spider_man_book_1 = Book(title="smider man", author="Alisha Beath", isbn="100-100-200", available= True)

    # creating member:
    ankit_member_1 = Member(name= "Ankit Ale", email="anmolankit00@gmail.com")

    # creating librarian:
    ankit_librarian_1 = Librarian(name= "Ankit Ale", email="anmolankit00@gmail.com")

    ankit_librarian_1.


    
    
    