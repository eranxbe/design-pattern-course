from .lego_ice_cream import LegoIceCream
from .lego_pizza import LegoPizza
from .lego_burger import LegoBurger
from abstract_food_stall_factory import AbstractFoodStallFactory


class LegoFactory(AbstractFoodStallFactory):

    def create_burger(self):
        return LegoBurger()

    def create_ice_cream(self):
        return LegoIceCream()

    def create_pizza(self):
        return LegoPizza()
