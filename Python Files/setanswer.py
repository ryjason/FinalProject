class Library:
    def __init__(self):
        self.books = set()

    def add_book(self, book):
        """
        Add a book to the library.
        """
        self.books.add(book)
        print(f"Added '{book}' to the library.")

    def remove_book(self, book):
        """
        Remove a book from the library.
        """
        if book in self.books:
            self.books.remove(book)
            print(f"Removed '{book}' from the library.")
        else:
            print(f"'{book}' is not in the library.")

    def display_books(self):
        """
        Display all the books in the library.
        """
        if self.books:
            print("Books in the library:")
            for book in self.books:
                print("-", book)
        else:
            print("The library is empty.")

    def is_book_available(self, book):
        """
        Check if a specific book is available in the library.
        """
        return book in self.books

    def count_books(self):
        """
        Count the total number of books in the library.
        """
        return len(self.books)

# Example usage:
library = Library()

library.add_book("Harry Potter and the Sorcerer's Stone")
library.add_book("The Great Gatsby")
library.add_book("To Kill a Mockingbird")

print("\nBooks in the library:")
library.display_books()

print("\nRemoving 'The Great Gatsby' from the library.")
library.remove_book("The Great Gatsby")

print("\nBooks in the library after removal:")
library.display_books()

print("\nIs 'To Kill a Mockingbird' available in the library?")
print(library.is_book_available("To Kill a Mockingbird"))

print("\nTotal number of books in the library:", library.count_books())
