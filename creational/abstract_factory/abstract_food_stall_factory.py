from abc import ABC, abstractmethod


class AbstractFoodStallFactory(ABC):

    @abstractmethod
    def create_ice_cream():
        pass

    @abstractmethod
    def create_burger():
        pass

    @abstractmethod
    def create_pizza():
        pass
