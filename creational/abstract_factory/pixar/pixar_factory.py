from .pixar_ice_cream import PixarIceCream
from .pixar_pizza import PixarPizza
from .pixar_burger import PixarBurger
from abstract_food_stall_factory import AbstractFoodStallFactory


class PixarFactory(AbstractFoodStallFactory):

    def create_burger(self):
        return PixarBurger()

    def create_ice_cream(self):
        return PixarIceCream()

    def create_pizza(self):
        return PixarPizza()
