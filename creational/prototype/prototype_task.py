from abc import ABC, abstractmethod


class Toy(ABC):
    @abstractmethod
    def clone():
        pass


class PlushToy(Toy):
    def clone():
        print("New Plush Toy")
        return PlushToy()


class TeddyBear(Toy):
    def clone():
        print("New teddy bear")
        return TeddyBear()


class Bunny(Toy):
    def clone():
        print("New bunny")
        return Bunny()


class Kitten(Toy):
    def say_meow(self):
        print("MEOW")

    def clone(self):
        print("New kitten")
        return Kitten()


def main():
    kittens = []
    kitten_proto = Kitten()
    for _ in range(5):
        kittens.append(kitten_proto.clone())
    for k in kittens:
        k.say_meow()


main()
