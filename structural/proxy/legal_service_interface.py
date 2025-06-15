from abc import ABC, abstractmethod


class LegalServiceInterface(ABC):
    @abstractmethod
    def request_legal_assistance(self):
        pass
