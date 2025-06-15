from prototype import Prototype


class BlackTeddyBear(Prototype):

    def clone(self):
        print("Creating Black Teddy Bear")
        return BlackTeddyBear()
