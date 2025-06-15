from fantasy.fantasy_factory import FantasyFactory
from lego.lego_factory import LegoFactory
from pixar.pixar_factory import PixarFactory


def main():
    print("let's go to the theme park!")
    print("first, fantasy!")
    fantasy_theme = FantasyFactory()
    fantasy_burger = fantasy_theme.create_burger()
    fantasy_burger.enjoy()
    fantasy_ice_cream = fantasy_theme.create_ice_cream()
    fantasy_ice_cream.enjoy()
    fantasy_pizza = fantasy_theme.create_pizza()
    fantasy_pizza.enjoy()

    print("now, pixar")
    pixar_theme = PixarFactory()
    pixar_burger = pixar_theme.create_burger()
    pixar_burger.enjoy()
    pixar_ice_cream = pixar_theme.create_ice_cream()
    pixar_ice_cream.enjoy()
    pixar_pizza = pixar_theme.create_pizza()
    pixar_pizza.enjoy()

    print("finnaly - lego!")
    lego_theme = LegoFactory()
    lego_burger = lego_theme.create_burger()
    lego_burger.enjoy()
    lego_ice_cream = lego_theme.create_ice_cream()
    lego_ice_cream.enjoy()
    lego_pizza = lego_theme.create_pizza()
    lego_pizza.enjoy()

    print("was fun")


main()
