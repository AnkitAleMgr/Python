from abc import ABC
from helper import line
from data_manager import save_to_csv
from exceptions import BookUnavailableError, InvalidMemberError, NotBookError, AlreadyBelongsToLibraryError
from validators import is_valid_librarian, is_valid_member, is_valid_book

class Book:

    _books = []
    _free_id = []
    _active_id = 1

    def __init__(self, title : str , author : str, isbn : str , available : bool = True) -> None:
        self.title = title.capitalize().strip()
        self.author = author.capitalize().strip()
        self.isbn = isbn
        self.available = available
        self.reserved_list = []
        self.library = None
        self.borrower = None

        if Book._free_id:
            self.id = Book._free_id.pop(0)
        else:
            self.id = Book._active_id
            Book._active_id += 1
        Book._books.append(self)

    def __str__(self) -> str:
        return f"{self.title} by {self.author} ({'Available' if self.available else 'Checked out'})"

    @classmethod
    def save_books_to_csv(cls):
        if Book._books:
            save_to_csv([book.dict_info() for book in cls._books], "Books.csv")
        else:
            print("No Book has been created to save in csv.")

    def del_book(self) -> None:
            Book._books.remove(self)
            if self.library:
                self.library.remove_book(self)
            if self.borrower:
                self.borrower.borrowed_book.remove(self)
    
    def display_info(self) -> None:
        print("Title: ", self.title)
        print("Author: ", self.author)
        print("Isbn: ", self.isbn)
        print(f"Available: {'Yes' if self.available else 'No'}")

    def add_reserved(self, member : object) -> None:
        if not is_valid_member(member):
            raise InvalidMemberError(f"No such member found named {member.name}")
        self.reserved_list.append(member)
        print(f"{self.title} have bee reserved for {member.name}")
    
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

    @classmethod  
    def save_libraries_to_csv(self) -> None:
        if Library._libraries:
            save_to_csv([library.dict_info() for library in Library._libraries], "libraries.csv")
        else:
            print("No library has created to save in csv")

    def del_library(self):
        pass

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
        if is_valid_book(book):
            if book.library == None:
                self.books.append(book)
                book.library = self
                print(f"{book.title} has been added in {self.name}")
            else:
                raise AlreadyBelongsToLibraryError(f"This book {book.title} - {book.isbn} is already located to another library.")
        else:
            raise NotBookError(f"{book} is not a book.")

    def remove_book(self, book: Book) ->None :
        if book in self.books:
            self.books.remove(book)
            book.library = None
            print(f"{book.title} has been removed from {self.name}.")
        else:
            print(f"No book found name {book.title} in library {self.name}.")

    def list_all_book(self) -> None:
        if not self.books:
            print("No book has been added till now")
            return
        count = 1
        print("************ All Book ************")
        for book in self.books:
            print(f"{count}) {book.title} {book.isbn} {book.available}")
            count += 1
        print("***********************************")

    def list_available_book(self) -> None:
        if not self.books:
            print("No book has been added till now")
            return
        count = 1
        print("********** Available Book **********")
        for book in self.books:
            if book.available:
                print(f"{count}) {book.title} {book.isbn}")
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

    def is_part_of(self, obj : object) -> bool:
        return obj in self.members or obj in self.librarians

    def save_library_detail(self):
        if self.books:
            save_to_csv([book.dict_info() for book in self.books], f"book_{self.id}.csv")
        else:
            print("No book has been added till now.")
        if self.members:
            save_to_csv([member.dict_info() for member in self.members],f"member_{self.id}.csv")
        else:
            print("No member has been added till now")
        if self.librarians:
            save_to_csv([librarian.dict_info() for librarian in self.librarians], f"librarian_{self.id}.csv")
        else:
            print("No librarians has been added till now")


    # def save_books(self) -> None:
    #     if self.books:
    #         save_to_csv([book.dict_info() for book in self.books], f"book_{self.id}.csv")
    #     else:
    #         print("No book has been added till now.")

    # def save_members(self) ->None:
    #     if self.members:
    #         save_to_csv([member.dict_info() for member in self.members],f"member_{self.id}.csv")
    #     else:
    #         print("No member has been added till now")
        
    # def save_librarians(self) -> None:
    #     if self.librarians:
    #         save_to_csv([librarian.dict_info() for librarian in self.librarians], f"librarian_{self.id}.csv")
    #     else:
    #         print("No librarians has been added till now")

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
            if library.is_part_of(self):
                library.add_book(book)
            else:
                print(f"{self.name} is not part of {library.name}.")
        else:
            print(f"No book found name {book.title}")

    def remove_book(self, book : Book, library : Library) -> None:
        if library.is_part_of(self):
            library.remove_book(book)

    def view_all_book(self, library : Library) -> None:
        if library.is_part_of(self):
            library.list_available_book()
        else:
            print(f"{self.name} is not part of {library.name}")
        
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
            book.library = library
            book.borrower = self
            print(f"{book.title} has been borrowed by {self.name}")
        else:
            book.add_reserved(self)
            # raise BookUnavailableError(f"{book.title} is not available, added to reserve list.")

    def return_book(self, book : Book) -> None:
        if book not in self.borrowed_book:
            print(f"{self.name} hasn't borrowed a book name {book.title} to return.")   
            return
        self.borrowed_book.remove(book)
        book.available = True
        book.borrower = None
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
    # #region creating library:
    # united_library = Library(name= "United library")
    # oxford_library = Library(name = "Oxford library")
    # Legex_library = Library(name = "legex library")
    # #endregion

    # #region creating book:
    # book_1 = Book(title="The Last Horizon", author="Evelyn Harper", isbn="200-300-101", available=True)
    # book_2 = Book(title="Shadows of the Deep", author="Marcus Reid", isbn="200-300-102", available=True)
    # book_3 = Book(title="The Clockmaker's Paradox", author="Isabella Monroe", isbn="200-300-103", available=True)
    # book_4 = Book(title="Whispers in the Fog", author="Liam Blackwood", isbn="200-300-104", available=True)
    # book_5 = Book(title="Crimson Skies", author="Sofia Winters", isbn="200-300-105", available=True)
    # book_6 = Book(title="Echoes of Eternity", author="Noah Carter", isbn="200-300-106", available=True)
    # book_7 = Book(title="The Glass Labyrinth", author="Ava Sterling", isbn="200-300-107", available=True)
    # book_8 = Book(title="Beneath the Silver Moon", author="Ethan Sinclair", isbn="200-300-108", available=True)
    # book_9 = Book(title="The Forgotten Kingdom", author="Clara Davenport", isbn="200-300-109", available=True)
    # book_10 = Book(title="Storms of the Midnight Sea", author="James Aldridge", isbn="200-300-110", available=True)
    # #endregion
    
    # #region creating member:
    # ankit_member_1 = Member(name="Ankit Ale", email="anmolankit00@gmail.com")
    # sophia_member_2 = Member(name="Sophia Reed", email="sophia.reed@example.com")
    # liam_member_3 = Member(name="Liam Brooks", email="liam.brooks@example.com")
    # olivia_member_4 = Member(name="Olivia Carter", email="olivia.carter@example.com")
    # ethan_member_5 = Member(name="Ethan Smith", email="ethan.smith@example.com")
    # ava_member_6 = Member(name="Ava Johnson", email="ava.johnson@example.com")
    # noah_member_7 = Member(name="Noah Bennett", email="noah.bennett@example.com")
    # mia_member_8 = Member(name="Mia Robinson", email="mia.robinson@example.com")
    # lucas_member_9 = Member(name="Lucas Turner", email="lucas.turner@example.com")
    # isabella_member_10 = Member(name="Isabella Foster", email="isabella.foster@example.com")
    # #endregion
    
    # #region creating librarian:
    # ankit_librarian_1 = Librarian(name="Ankit Ale", email="anmolankit00@gmail.com")
    # sophia_librarian_2 = Librarian(name="Sophia Reed", email="sophia.reed@example.com")
    # liam_librarian_3 = Librarian(name="Liam Brooks", email="liam.brooks@example.com")
    # olivia_librarian_4 = Librarian(name="Olivia Carter", email="olivia.carter@example.com")
    # ethan_librarian_5 = Librarian(name="Ethan Smith", email="ethan.smith@example.com")
    # mia_librarian_6 = Librarian(name="Mia Robinson", email="mia.robinson@example.com")
    # lucas_librarian_7 = Librarian(name="Lucas Turner", email="lucas.turner@example.com")
    # #endregion

    # line()
    # #region adding book into library so that they can be lended and stored
    # united_library.add_book(book_1)
    # oxford_library.add_book(book_2)
    # #endregion

    # line()
    # #region adding member and librarian to library:
    # # member
    # united_library.add_member(ankit_member_1)
    # united_library.add_member(sophia_member_2)
    # united_library.add_member(liam_member_3)
    # oxford_library.add_member(olivia_member_4)
    # oxford_library.add_member(ethan_member_5)
    # oxford_library.add_member(ava_member_6)
    
    # # libraraian
    # united_library.add_librarian(ankit_librarian_1)
    # united_library.add_librarian(sophia_librarian_2)
    # oxford_library.add_librarian(liam_librarian_3)
    # oxford_library.add_librarian(mia_librarian_6)
    # oxford_library.add_librarian(lucas_librarian_7)
    # #endregion

    # line()
    # #region trying to add books with librarina:
    # ethan_librarian_5.add_book(book_3, united_library)
    # ankit_librarian_1.add_book(book_4, united_library)
    # ankit_librarian_1.add_book(book_5, united_library)
    # lucas_librarian_7.add_book(book_6, oxford_library)
    # lucas_librarian_7.add_book(book_7, oxford_library)
    # lucas_librarian_7.add_book(book_8, oxford_library)
    # #endregion

    # line()
    # # checking if book has been added to library or not
    # united_library.list_available_book()
    # oxford_library.list_available_book()
    
    # # line()
    # # checking for mathcing title
    # # united_library.find_book_by_title("iron man")

    # line()
    # # borrowing few books 
    # ankit_member_1.borrow_book(book=book_1, library=united_library)
    # sophia_member_2.borrow_book(book=book_2, library=united_library)
    # ethan_member_5.borrow_book(book_6, oxford_library)
    # ava_member_6.borrow_book(book_5, oxford_library)

    # line()
    # # looking it borrowed book are showing false
    # united_library.find_book_by_title("the last horizon")

    # line()
    # # returnign few book:
    # ankit_member_1.return_book(book_1)

    # line()
    # # checking it after returning the book it is set to available
    # united_library.find_book_by_title("the last horizon")

    # line()
    # # checking if brrowing system works properly
    # ankit_member_1.borrow_book(book=book_1, library=united_library)
    # sophia_member_2.borrow_book(book=book_1, library=united_library)
    # ankit_member_1.return_book(book_1)

    # line()
    # # check if list all book works
    # oxford_library.list_all_book()

    # line()
    # # checking if data are retrive proerly from every class
    # Library.save_libraries()
    # united_library.save_books()
    # united_library.save_librarians()
    # united_library.save_members()

    # line()
    # Library.save_libraries()
    # oxford_library.save_books()
    # oxford_library.save_librarians()
    # oxford_library.save_members()


    united_library = Library(name= "United library")
    oxford_library = Library(name= "Oxford library")
    book_1 = Book(title="The Last Horizon", author="Evelyn Harper", isbn="200-300-101", available=True)
    ankit_librarian_1 = Librarian(name="Ankit Ale", email="anmolankit00@gmail.com")
    # ankit_member_1 = Member(name="Ankit Ale", email="anmolankit00@gmail.com")

    # united_library.add_librarian(ankit_librarian_1)
    # united_library.add_member(ankit_member_1)
    # ankit_librarian_1.add_book(book_1, united_library)
    # ankit_member_1.borrow_book(book= book_1, library=united_library)
    # # book_1.del_book()
    # ankit_member_1.view_borrowed_book()
    

    book_2 = Book(title="The Last Horizon", author="Evelyn Harper", isbn="200-300-102", available=True)
    book_3 = Book(title="The Last Horizon", author="Evelyn Harper", isbn="200-300-103", available=True)

    united_library.save_libraries_to_csv()