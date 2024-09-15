class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        for library_book in self.books:
            if book.title == library_book.title and book.author == library_book.author:
                self.books.remove(library_book)

    def search_books(self, search_string):
        matching_books = []

        for book in self.books:
            if search_string in book.title.lower() or search_string in book.author.lower():
                matching_books.append(book)

        return matching_books
