from abc import ABC, abstractmethod


# like Base Page
class Product(ABC):
    @abstractmethod
    def serve():
        pass


# like page
class Pizza(Product):
    def serve(self):
        print("serving pizza")
        return self


# like different Page
class IceCream(Product):
    def serve(self):
        print("serving ice cream")
        return self


# page factory
class FoodStall(ABC):
    @abstractmethod
    def prepare_food():
        pass

    def take_order(self) -> Product:
        print(f"Order placed: {type(self).__name__}")
        product: Product = self.prepare_food()
        return product.serve()


# template of page
class PizzaStall(FoodStall):
    def prepare_food(self) -> Pizza:
        print("preparing pizza")
        return Pizza()


# template of different page
class IceCreamStall(FoodStall):
    def prepare_food(self) -> IceCream:
        print("preparing ice cream")
        return IceCream()


def main():
    ice_cream_stall = IceCreamStall()
    pizza_stall = PizzaStall()

    ice_cream = ice_cream_stall.take_order()
    pizza = pizza_stall.take_order()

    print(ice_cream)
    print(pizza)


main()
