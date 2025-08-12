# excaption errors
class InvalidBookError(Exception):
    pass
class IsNotPartOfLibrary(Exception):
    pass
class InvalidMemberError(Exception):
    pass
class InvalidLibrarianError(Exception):
    pass
class BookAlreadyBelongsToLibraryError(Exception):
    pass
class LibrarianAlreadyBelongsToLibraryError(Exception):
    pass
class LibrarianDoesNotBelongsToLibrayError(Exception):
    pass
class NotFoundBookInInventory(Exception):
    pass