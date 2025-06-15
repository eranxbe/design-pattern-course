from white_teddy_bear_prototype import WhiteTeddyBear
from black_teddy_bear_prototype import BlackTeddyBear


def main():
    white_tb = WhiteTeddyBear()
    black_tb = BlackTeddyBear()

    clone_white = white_tb.clone()
    clone_black = black_tb.clone()

    print(f"Cloned teddy {type(clone_white).__name__}")
    print(f"Cloned teddy {type(clone_black).__name__}")


main()
