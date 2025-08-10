from index import Book, Member, Librarian

def is_valid_book(obj : Book) -> bool:
    return isinstance(obj, Book)

def is_valid_member(obj : Member) -> bool:
    return isinstance(obj, Member)

def is_valid_Librarian(obj : Librarian) -> bool:
    return isinstance(obj, Librarian)
