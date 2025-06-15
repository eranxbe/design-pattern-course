"""constructs parts of the product and assembles them"""

from builder import Builder
from product import Product
from director import Director


class ConcreteBuilder(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add_part("Whole wheat bread")

    def build_part_b(self):
        self.product.add_part("Turkey")

    def build_part_c(self):
        self.product.add_part("Lettuce, Tomato, Onion")

    def get_product(self):
        return self.product


def main():
    builder = ConcreteBuilder()
    director = Director(builder)
    director.construct_sandwich()
    sandwich = builder.get_product()
    sandwich.show()


main()
