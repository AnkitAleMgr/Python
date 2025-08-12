# excaption errors
class BookUnavailableError(Exception):
    pass
class InvalidMemberError(Exception):
    pass
class InvalidLibrarianError(Exception):
    pass
class NotBookError(Exception):
    pass
class BookAlreadyBelongsToLibraryError(Exception):
    pass
class LibrarianAlreadyBelongsToLibraryError(Exception):
    pass