from abc import ABC, abstractmethod


class BookInterface(ABC):
    @abstractmethod
    def borrow_book(self):
        pass

    @abstractmethod
    def return_book(self):
        pass

    @abstractmethod
    def is_available(self) -> bool:
        pass

    @abstractmethod
    def get_id(self):
        pass
