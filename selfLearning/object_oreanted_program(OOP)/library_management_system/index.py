from abc import ABC
from helper import line
from data_manager import save_to_csv, directory_maker_deleter
from exceptions import InvalidLibraryError,InvalidMemberError,InvalidLibrarianError, BookAlreadyBelongsToLibraryError, LibrarianAlreadyBelongsToLibraryError,LibrarianDoesNotBelongsToLibrayError, InvalidBookError, IsNotPartOfLibrary,NotFoundBookInInventory, HasNotBorrowedBookError, KeyNotFountError, EmptyUpdateDetailError, MemberNotPartOfLibraryError, MemberIsAlreadyPartOfLibrary
from validators import is_valid_librarian, is_valid_member, is_valid_book, is_valid_library

def save_all():
    Book.save_books_to_csv()
    Member.save_members_to_csv()
    Librarian.save_librarians_to_csv()
    Library.save_libraries_to_csv()
    Library.save_library_detail()

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
        save_to_csv([book.dict_info() for book in cls._books], "Books/Books.csv")

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
            raise InvalidMemberError(f"{member.name} is not a valid member.")
        self.reserved_list.append(member)
        print(f"{self.title} have bee reserved for {member.name}")
    
    def notify_next_reserve(self) -> None:
        if self.reserved_list:
            next_member = self.reserved_list.pop(0)
            try:
                next_member.borrow_book(book = self, library= book.library)
            except Exception as e:
                print(f"Failed to lend {self.title} to {next_member.name}: {e}")
                
    def dict_info(self) -> dict:
        return {
            "Id" : self.id,
            "Title" : self.title,
            "Isbn" : self.isbn,
            "Available" : self.available,
            "Library": self.library,
            "Borrower": self.borrower
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
        self.emp_active_id = 1
        self.emp_free_id = []
        self.library_free_member_id = []
        self.library_active_member_id = 1

        if Library._free_id:
            self.id = Library._free_id.pop(0)
        else:
            self.id = Library._active_id
            Library._active_id += 1
        Library._libraries.append(self)

    def __str__(self) -> str:
        return f"Library: {self.name} (ID: {self.id})"

    @classmethod  
    def save_libraries_to_csv(self) -> None:
        save_to_csv([library.dict_info() for library in Library._libraries], "Library/libraries.csv")

    @classmethod
    def del_library(cls, library: object) -> None:
        if not is_valid_library(library):
            raise InvalidLibraryError(f"'{library}' is not a valid Library.")
        Library._libraries.remove(library)
        library.books = None
        library.members = None
        library.libraria = None
        # removing library form books
        for book in Book._books:
            if book.library is library:
                book.library = None
        # removeing library form librarian
        for libraraian in Librarian._librarians:
            if libraraian.library is library:
                libraraian.library = None
        print(f"Library '{library.name}' has been deleted.")
        del library
        
    def dict_info(self) -> dict:
        return {
            "Id" : self.id,
            "Name" : self.name,
            "No of Books" : len(self.books) if self.books else 0,
            "No of Librarians" : len(self.librarians) if self.librarians else 0,
            "No of Members" : len(self.members) if self.members else 0,
        }

# MemberIsAlreadyPartOfLibrary
    def add_member(self, member : object) -> None:
        id = None
        if not isinstance(member, Member):
            raise InvalidMemberError(f"'{member}' is not a valid Member.")
        for _, lib in member.library_and_id:
            if lib is self:
                raise MemberIsAlreadyPartOfLibrary(f"'{member.name}' is already member of {self.name}.")
        self.members.append(member)
        if self.library_free_member_id:
            id = self.library_free_member_id.pop(0)
        else:
            id = self.library_active_member_id
            self.library_active_member_id += 1
        member.library_and_id.append((id, self))
        print(f"{member.name} has been added to {self.name}")

    def remove_member(self, member : object) -> None:
        if not is_valid_member(member):
            raise InvalidMemberError(f"'{member}' is not a valid member.")
        if not self.is_part_of(member):
            raise MemberNotPartOfLibraryError(f"'{member.name}' is not part of {self.name}.")
        self.members.remove(member)
        for index,i in enumerate(member.library_and_id):
            if i[1] is self:
                self.library_free_member_id.append(i[0])
                # print(self.library_free_member_id)
                del member.library_and_id[index]
        print(f"{member.name} has been removed for Library {self.name}.")

    def add_librarian(self, librarian : object) -> None:
        if not is_valid_librarian(librarian):
            raise InvalidLibrarianError("'{linrarian} is not Librarian.'")
        if librarian.library is not None:
            raise LibrarianAlreadyBelongsToLibraryError(f"'{librarian.name}' is already lebrarian of Library:{librarian.library.name}.")
        self.librarians.append(librarian)
        librarian.library = self
        if self.emp_free_id:
            librarian.employed_id  = self.emp_free_id.pop(0)
        else:
            librarian.employed_id = self.emp_active_id
            self.emp_active_id += 1
        print(f"{librarian.name} has been added to {self.name}")

    def delete_librarian(self, librarian: object) -> None:
        if not is_valid_librarian(librarian):
            raise InvalidLibrarianError(f"'{librarian}' is not a valid Librarian.")
        if not self.is_part_of(librarian):
            raise LibrarianDoesNotBelongsToLibrayError(f"'{librarian.name}' is not part of Library: {self.name}.")
        self.librarians.remove(librarian)
        librarian.library = None
        librarian.employed_id = None
        print(f"'{librarian.name}' has been removed for Library: {self.name}")

    def add_book(self, book : Book) -> None:
        if not is_valid_book(book):
            raise InvalidBookError(f"'{book}' is not a book.")
        if book.library is None:
            self.books.append(book)
            book.library = self
            print(f"{book.title} has been added in {self.name}")
        else:
            raise BookAlreadyBelongsToLibraryError(f"This book {book.title} - {book.isbn} is already located to another library {book.library.name}.")

    def remove_book(self, book: Book) ->None :
        if not is_valid_book(book):
            raise InvalidBookError(f"'{book}' is not a book.")
        if book in self.books:
            self.books.remove(book)
            book.library = None
            print(f"{book.title} has been removed from {self.name}.")
        else:
            raise NotFoundBookInInventory(f"'{book.title}' not fount in inventory.")

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

    def is_in_library(self, book:Book) -> bool:
        return book in self.books

    def is_part_of(self, obj : object) -> bool:
        return obj in self.members or obj in self.librarians

    @classmethod
    def save_library_detail(self) -> None:
        directory_maker_deleter(len(Library._libraries))
        for obj in Library._libraries:
            save_to_csv([book.dict_info() for book in obj.books], f"Library/library_{obj.id}/books.csv")
            save_to_csv([member.dict_info() for member in obj.members],f"Library/library_{obj.id}/members.csv")
            save_to_csv([librarian.dict_info() for librarian in obj.librarians], f"Library/library_{obj.id}/librarians.csv")

class Person(ABC):

    _person_active_id = 1
    _person_free_id = []

    def __init__(self, name : str, email : str) -> None:
        self.name = name.capitalize().strip()
        self.email = email.strip()
        if Person._person_free_id:
            self.person_id = Person._person_free_id.pop(0)
        else:
            self.person_id = Person._person_active_id
            Person._person_active_id += 1
        
    def display_info(self) -> None:
        print("ID:",self.person_id)
        print("Name:",self.name)
        print("Email:",self.email)

    def update_detail(self, **kwargs) -> None:
        if not kwargs:
            raise EmptyUpdateDetailError("Please send some detail to chanage")
            return
        for key, value in kwargs.items():
            if value is not None and hasattr(self, key):
                setattr(self, key, value)
            else:
                raise KeyNotFountError(f"'{key}' not fount.")

class Librarian(Person):
    
    _librarians = []
    _librarian_active_id = 1
    _librarian_free_id = []

    def __init__(self, name: str, email: str) -> None:
        super().__init__(name, email)
        self.library = None
        self.employed_id = None
        self.librarian_id = None

        if Librarian._librarian_free_id:
            self.librarian_id = Librarian._librarian_free_id.pop(0)
        else:
            self.librarian_id = Librarian._librarian_active_id
            Librarian._librarian_active_id += 1
        Librarian._librarians.append(self)

    def __str__(self) -> str:
        return f"Name: {self.name} (Id: {self.librarian_id})"

    @classmethod
    def save_librarians_to_csv(self):
        save_to_csv(data= [librarian.dict_info() for librarian in Librarian._librarians], file_name="Librarians/libraians.csv")

    def add_book(self, book: Book) -> None:  # noqa: F811
        if is_valid_book(book):
            if self.library is None:
                raise LibrarianDoesNotBelongsToLibrayError(f"{self.name} is not part of any Library.")
            if self.library.is_part_of(self):
                self.library.add_book(book)
            else:
                raise LibrarianDoesNotBelongsToLibrayError(f"'{self.name}' doesnt belong to this library to add books.")
        else:
            raise InvalidBookError(f"'{book}' is not a valid book.")

    def remove_book(self, book : Book) -> None:
        if self.library is None:
            raise LibrarianDoesNotBelongsToLibrayError(f"'{self.name} deos not belong to any library.'")
        if not self.library.is_part_of(self):
            raise IsNotPartOfLibrary(f"'{self.name}' is not part of {self.library}.")
        if book in self.library.books:
            self.library.remove_book(book)
        else:
            raise NotFoundBookInInventory(f"'{book.title, book.isbn}'not fount in inventory to remove form library. ")

    def view_all_book(self) -> None:
        if self.library is None:
            raise LibrarianDoesNotBelongsToLibrayError(f"'{self.name} deos not belong to any library.'")
        if not self.library.is_part_of(self):
            raise IsNotPartOfLibrary(f"'{self.name}' is not part of {self.library}.")
        if self.library.books():
            self.library.list_all_book()
        else:
            print("No Book has been added till now")
        
    def dict_info(self) -> dict:
        return {
            "P.ID" : self.person_id,
            "L.ID" : self.librarian_id,
            "Name" : self.name,
            "Email" : self.email, 
            "Library" : self.library,
            "L.E.ID" : self.employed_id
        }
    
class Member(Person):

    _members = []
    _active_id = 1
    _free_id = []

    def __init__(self, name: str, email: str) -> None:
        super().__init__(name, email)
        self.borrowed_book = []
        self.library_and_id = []
        # self.library_member_id = 
        
        if Member._free_id:
            self.member_id = Member._free_id.pop(0)
        else:
            self.member_id = Member._active_id
            Member._active_id += 1
        Member._members.append(self)
        
    def __str__(self) -> str:
        return f"Member: {self.name} (Prson ID: {self.person_id})"

    def return_book(self, book : Book) -> None:
        if book not in self.borrowed_book:
            raise HasNotBorrowedBookError(f"{self.name} hasn't borrowed a book name {book.title} to return.")   
        self.borrowed_book.remove(book)
        book.available = True
        book.borrower = None
        print(f"{book.title} has been return by {self.name}.")
        book.notify_next_reserve()

    @classmethod
    def del_member(self, m : object) -> None:
        if not is_valid_member(m):
            raise InvalidMemberError(f"'{m}' is not a vlaid Member.")
        while m.borrowed_book:
            m.return_book(m.borrowed_book[0])
        all_library_list = [b for a, b  in m.library_and_id]
        for x in all_library_list:
            x.remove_member(m)
        Member._members.remove(m)

    @classmethod
    def save_members_to_csv(self):
        save_to_csv([member.dict_info() for member in Member._members], file_name= "Members/members.csv")

    def borrow_book(self, book : Book, library: Library) -> None:
        all_library_list = [b for a, b  in self.library_and_id]
        if library not in all_library_list:
            raise IsNotPartOfLibrary(f"'{self.name}' is not part of any Library")
        if not is_valid_book(book):
            raise InvalidBookError("'{book}' is not a valid Book.")
        if not library.is_in_library(book):
            raise NotFoundBookInInventory(f"'{book.title}' cannot be found in inventory. Might be in other Library.")
        if book.available:
            self.borrowed_book.append(book)
            book.available = False
            book.library = library
            book.borrower = self
            print(f"{book.title} has been borrowed by {self.name}")
        else:
            book.add_reserved(self)
            print(f"{book.title} is not available, {self.name} has been added to reserve list.")


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
            "P.ID" : self.person_id,
            "M.ID" : self.member_id,
            "Name" : self.name,
            "Email" : self.email, 
            "Library" : self.library,
            "L.M.ID" : self.library_member_id
        }

if __name__ == "__main__":
    library1 = Library(name="united")
    library2 = Library(name="saurav")
    library3 = Library(name="nigga")

    book = Book(title="book1", author="saureav",isbn="12321", available=True)
    book2 = Book(title="book2", author="saureav",isbn="12321", available=True)
    book3 = Book(title="book3", author="saureav",isbn="12321", available=True)
    book4 = Book(title="book4", author="saureav",isbn="12321", available=True)
    book5 = Book(title="book5", author="saureav",isbn="12321", available=True)
    book6 = Book(title="book6", author="saureav",isbn="12321", available=True)

    library1.add_book(book=book)
    library1.add_book(book=book2)
    library1.add_book(book=book3)
    library1.add_book(book=book4)
    library1.add_book(book=book5)
    library1.add_book(book=book6)

    line()
    member1 = Member("member1", "fdaf")
    library1.add_member(member1)

    line()
    member1.borrow_book(book, library1)
    member1.borrow_book(book2, library1)
    member1.borrow_book(book3, library1)
    member1.borrow_book(book4, library1)
    member1.borrow_book(book5, library1)
    member1.borrow_book(book6, library1)


    line()
    Member.del_member(member1)
    # print(book, book2)

    library1.list_all_book()





# main entry point
# if __name__ == "__main__":
#     # =======================================================================
#     #region creating libraries:
#     library_1 = Library(name="Central Library")
#     library_2 = Library(name="City Library")
#     library_3 = Library(name="Village Library")
#     library_4 = Library(name="Coastal Library")
#     #endregion

#     # =======================================================================
#     #region creating books:
#     books = [
#         Book("The Silent River", "Helen Woods", "300-400-201"),
#         Book("Winds of Tomorrow", "Carl Summers", "300-400-202"),
#         Book("The Dragon's Oath", "Jade Green", "300-400-203"),
#         Book("Beyond the Horizon", "Oliver Grant", "300-400-204"),
#         Book("Midnight Echo", "Sienna Blake", "300-400-205"),
#         Book("The Golden Compass", "Philip Bright", "300-400-206"),
#         Book("Whispers of the Forest", "Emily Rose", "300-400-207"),
#         Book("The Last Ember", "Daniel White", "300-400-208"),
#         Book("Frozen Tides", "Clara Frost", "300-400-209"),
#         Book("Echo in the Canyon", "Mark Rivers", "300-400-210"),
#         Book("Hidden Truth", "Zara Lane", "300-400-211"),
#         Book("Shadow Veil", "Liam Moore", "300-400-212"),
#         Book("Crimson Shadows", "Olivia Green", "300-400-213"),
#         Book("Emerald Dreams", "Noah Gray", "300-400-214"),
#         Book("Secrets of the Deep", "Ava Bell", "300-400-215"),
#         Book("The Silver Path", "Sophia Moon", "300-400-216"),
#         Book("Twilight Mirage", "Lucas Hart", "300-400-217"),
#         Book("Broken Crown", "Mia Frost", "300-400-218"),
#         Book("Ashes and Embers", "Ethan West", "300-400-219"),
#         Book("Cursed Flames", "Lara Bright", "300-400-220"),
#         Book("The Lost Voyage", "Oscar Knight", "300-400-221"),
#         Book("The Endless Hunt", "Nora Scott", "300-400-222"),
#         Book("Flame of Eternity", "Henry Cole", "300-400-223"),
#         Book("Veil of Ice", "Amelia Stone", "300-400-224"),
#         Book("The Hidden Fortress", "Jack Black", "300-400-225"),
#         Book("Winter's Grasp", "Ella Frost", "300-400-226"),
#         Book("The Forgotten Realm", "William Chase", "300-400-227"),
#         Book("Moonlit Shores", "Grace Blue", "300-400-228"),
#         Book("Steel Tempest", "Leo Storm", "300-400-229"),
#         Book("Starbound Legacy", "Ivy Sky", "300-400-230"),
#     ]
#     #endregion

#     # =======================================================================
#     #region creating members:
#     members = [
#         Member("John Smith", "john.smith@example.com"),
#         Member("Emily Clark", "emily.clark@example.com"),
#         Member("Michael Johnson", "michael.johnson@example.com"),
#         Member("Laura Wilson", "laura.wilson@example.com"),
#         Member("David Brown", "david.brown@example.com"),
#         Member("Sarah Davis", "sarah.davis@example.com"),
#         Member("James Lee", "james.lee@example.com"),
#         Member("Olivia Taylor", "olivia.taylor@example.com"),
#         Member("Ethan Harris", "ethan.harris@example.com"),
#         Member("Sophia Adams", "sophia.adams@example.com"),
#         Member("Daniel Carter", "daniel.carter@example.com"),
#         Member("Mia Walker", "mia.walker@example.com"),
#         Member("Liam Perez", "liam.perez@example.com"),
#         Member("Ava Young", "ava.young@example.com"),
#         Member("Noah King", "noah.king@example.com"),
#         Member("Chloe Hill", "chloe.hill@example.com"),
#         Member("Lucas Allen", "lucas.allen@example.com"),
#         Member("Isabella Wright", "isabella.wright@example.com"),
#         Member("Benjamin Scott", "benjamin.scott@example.com"),
#         Member("Amelia Torres", "amelia.torres@example.com"),
#     ]
#     #endregion

#     # =======================================================================
#     #region creating librarians:
#     librarians = [
#         Librarian("Henry Parker", "henry.parker@example.com"),
#         Librarian("Anna Scott", "anna.scott@example.com"),
#         Librarian("George Turner", "george.turner@example.com"),
#         Librarian("Clara Brooks", "clara.brooks@example.com"),
#         Librarian("Ethan Cole", "ethan.cole@example.com"),
#         Librarian("Maya Lopez", "maya.lopez@example.com"),
#         Librarian("Oliver Hayes", "oliver.hayes@example.com"),
#         Librarian("Sophia Reed", "sophia.reed@example.com"),
#         Librarian("Noah Bennett", "noah.bennett@example.com"),
#         Librarian("Ava Johnson", "ava.johnson@example.com"),
#     ]
#     #endregion

#     # =======================================================================
#     line()
#     #region distribute members to libraries:
#     for i, member in enumerate(members):
#         if i % 4 == 0:
#             library_1.add_member(member)
#         elif i % 4 == 1:
#             library_2.add_member(member)
#         elif i % 4 == 2:
#             library_3.add_member(member)
#         else:
#             library_4.add_member(member)
#     #endregion

#     # =======================================================================
#     line()
#     #region distribute librarians to libraries:
#     for i, librarian in enumerate(librarians):
#         if i % 4 == 0:
#             library_1.add_librarian(librarian)
#         elif i % 4 == 1:
#             library_2.add_librarian(librarian)
#         elif i % 4 == 2:
#             library_3.add_librarian(librarian)
#         else:
#             library_4.add_librarian(librarian)
#     #endregion

#     # =======================================================================
#     line()
#     #region assign books to libraries via librarians:
#     for i, book in enumerate(books):
#         # assigned_lib = [library_1, library_2, library_3, library_4][i % 4]
#         librarian = librarians[i % len(librarians)]
#         librarian.add_book(book)

#     # for i, book in enumerate(books):
#     #     assigned_lib = [library_1, library_2, library_3, library_4][i % 4]
#     #     librarian = librarians[i % len(librarians)]
#     #     librarian.add_book(book, assigned_lib)
#     #endregion

#     # =======================================================================
#     line()
#     #region borrow books in bulk:
#     borrow_ops = [
#         (members[0], books[0], library_1),
#         (members[1], books[1], library_2),
#         (members[2], books[2], library_3),
#         (members[3], books[3], library_4),
#         (members[4], books[4], library_1),
#         (members[5], books[5], library_2),
#         (members[6], books[6], library_3),
#         (members[7], books[7], library_4),
#         (members[8], books[8], library_1),
#         (members[9], books[9], library_2),
#     ]

#     for m, b, l in borrow_ops:
#         m.borrow_book(b)
#     #endregion

#     # =======================================================================
#     line()
#     #region return some books:
#     return_ops = [
#         (members[0], books[0]),
#         (members[3], books[3]),
#         (members[7], books[7]),
#     ]
#     for m, b in return_ops:
#         m.return_book(b)
#     #endregion

#     # =======================================================================
#     line()
#     #region search for some books:
#     library_1.find_book_by_title("The Silent River")
#     library_2.find_book_by_title("Midnight Echo")
#     library_3.find_book_by_title("Cursed Flames")
#     library_4.find_book_by_title("Nonexistent Book")  # should fail
#     #endregion

#     # =======================================================================
#     line()
#     #region final listing:
#     library_1.list_available_book()
#     library_2.list_available_book()
#     library_3.list_available_book()
#     library_4.list_available_book()

#     #endregion

#     # =======================================================================
#     line()
#     #region save everything:
#     save_all()
#     #endregion
