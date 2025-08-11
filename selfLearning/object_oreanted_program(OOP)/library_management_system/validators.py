# from index import Book, Member, Librarian

def is_valid_librarian(obj) -> bool:
    # return isinstance(obj, Librarian)
    return obj.__class__.__name__ == "Librarian"

def is_valid_book(obj) -> bool:
    # return isinstance(obj, Book)
    return obj.__class__.__name__ == "Book"

def is_valid_member(obj) -> bool:
    # return isinstance(obj, Member)
    return obj.__class__.__name__ == "Member"

if __name__ == "__main__":
    pass