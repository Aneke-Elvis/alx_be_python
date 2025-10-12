# library_system.py

class Book:
    """Base class representing a general book."""
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"


class EBook(Book):
    """Derived class representing a digital book."""
    def __init__(self, title, author, file_size):
        # Call the parent constructor to initialize title and author
        super().__init__(title, author)
        self.file_size = file_size  # in MB

    def __str__(self):
        return f"EBook: '{self.title}' by {self.author} [{self.file_size}MB]"


class PrintBook(Book):
    """Derived class representing a printed book."""
    def __init__(self, title, author, page_count):
        # Call the parent constructor to initialize title and author
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: '{self.title}' by {self.author} [{self.page_count} pages]"


class Library:
    """A class demonstrating composition by managing a collection of books."""
    def __init__(self):
        self.books = []  # holds Book, EBook, and PrintBook objects

    def add_book(self, book):
        """Add a book (Book, EBook, or PrintBook) to the library."""
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Added: {book}")
        else:
            print("Only book objects can be added to the library.")

    def list_books(self):
        """List all books currently in the library."""
        print("\n📚 Library Collection:")
        if not self.books:
            print("No books in the library.")
        else:
            for idx, book in enumerate(self.books, start=1):
                print(f"{idx}. {book}")
