# excaption errors
class InvalidBookError(Exception):
    pass
class IsNotPartOfLibrary(Exception):
    pass
class InvalidMemberError(Exception):
    pass
class InvalidLibrarianError(Exception):
    pass
class InvalidLibraryError(Exception):
    pass
class BookAlreadyBelongsToLibraryError(Exception):
    pass
class LibrarianAlreadyBelongsToLibraryError(Exception):
    pass
class LibrarianDoesNotBelongsToLibrayError(Exception):
    pass
class NotFoundBookInInventory(Exception):
    pass
class HasNotBorrowedBookError(Exception):
    pass
class KeyNotFountError(Exception):
    pass
class EmptyUpdateDetailError(Exception):
    pass
class MemberNotPartOfLibraryError(Exception):
    pass
class MemberIsAlreadyPartOfLibrary(Exception):
    pass