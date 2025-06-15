from .fantasy_ice_cream import FantasyIceCream
from .fantasy_pizza import FantasyPizza
from .fantasy_burger import FantasyBurger
from abstract_food_stall_factory import AbstractFoodStallFactory


class FantasyFactory(AbstractFoodStallFactory):

    def create_burger(self):
        return FantasyBurger()

    def create_ice_cream(self):
        return FantasyIceCream()

    def create_pizza(self):
        return FantasyPizza()
