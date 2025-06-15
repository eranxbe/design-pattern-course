"""interface for concrete_builder"""

from abc import ABC, abstractmethod


class Builder(ABC):
    @abstractmethod
    def build_part_a(self):
        pass

    @abstractmethod
    def build_part_b(self):
        pass

    @abstractmethod
    def build_part_c(self):
        pass

    @abstractmethod
    def get_product(self):
        pass
