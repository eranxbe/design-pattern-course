from abc import ABC, abstractmethod


class ParkElement(ABC):
    @abstractmethod
    def add_component(self):
        pass

    @abstractmethod
    def remove_component(self):
        pass


class Park(ParkElement):
    def __init__(self) -> None:
        self.elements = []

    def add_component(self, component):
        self.elements.append(component)

    def remove_component(self, component):
        self.elements.remove(component)


class Tree(ParkElement):
    def __init__(self, type_: str):
        self.type_ = type_

    def add_component(self):
        print(f"Added Tree: {self.type_}")

    def remove_component(self):
        print(f"Removed Tree: {self.type_}")


class Bird(ParkElement):
    def __init__(self, type_: str):
        self.type_ = type_

    def add_component(self):
        print(f"Added Bird: {self.type_}")

    def remove_component(self):
        print(f"Removed Bird: {self.type_}")


def main():
    park = Park()
    tree1 = Tree("fikus")
    tree2 = Tree("oak")
    bird1 = Bird("eagle")
    bird2 = Bird("seagul")
    park.add_component(tree1)
    park.add_component(tree2)
    park.add_component(bird1)
    park.add_component(bird2)
    print([e.type_ for e in park.elements])


main()
