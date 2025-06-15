from book import Book


class Library:
    BOOKS = dict()

    def get_book(self, title, author) -> Book:
        if title not in self.BOOKS.keys():
            self.BOOKS[title] = Book(len(self.BOOKS) + 1, title, author)
        return self.BOOKS[title]

    def borrow_book(self, title, author):
        book = self.get_book(title, author)
        if book._is_available:
            book.borrow_book()
        else:
            # get new copy of book
            new_book = Book(len(self.BOOKS) + 1, title, author)
            self.BOOKS[title] = new_book
            print(f"Ordered a new copy of {new_book.title}, id: {new_book.id}")

            new_book.borrow_book()
            self.BOOKS[f"{new_book.title} # {len(self.BOOKS) + 1}"] = new_book

    def return_book(self, title):
        if self.BOOKS[title]:
            self.BOOKS[title]
