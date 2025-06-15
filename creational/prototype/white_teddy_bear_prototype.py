from prototype import Prototype


class WhiteTeddyBear(Prototype):

    def clone(self):
        print("Creating White Teddy Bear")
        return WhiteTeddyBear()
