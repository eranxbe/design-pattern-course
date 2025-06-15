from book_interface import BookInterface


class Book(BookInterface):
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author
        self._is_available = True
