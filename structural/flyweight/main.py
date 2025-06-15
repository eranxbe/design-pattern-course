from library import Library


def main():
    library = Library()

    library.borrow_book("Harry Potter", "J. K. Rowling")  # user 1 borrows a book

    library.borrow_book("Harry Potter", "J. K. Rowling")  # user 2 borrows the same book

    library.return_book("Harry Potter")  # user 1 returns the book

    library.borrow_book("Harry Potter", "J. K. Rowling")  # user 3 borrows the book


main()
