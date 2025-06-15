from abc import ABC, abstractmethod


class ArtworkInterface(ABC):
    @abstractmethod
    def view(self):
        pass

    @abstractmethod
    def purchase(self):
        pass


class NormalArtwork(ArtworkInterface):

    def view(self, passwd=None):
        if passwd != "123456":
            print("no access")
            return
        print("viewing the artwork")

    def purchase(self, passwd=None):
        if passwd != "123456":
            print("no access")
            return
        print("purchasing the artwork")


class ProxyArtwork(ArtworkInterface):
    def __init__(self):
        self.normal_artwork = None

    def view(self):
        if self.normal_artwork is None:
            self.normal_artwork = NormalArtwork()
        pass_ = input("viewing; PASSWORD? ")
        self.normal_artwork.view(pass_)

    def purchase(self):
        if self.normal_artwork is None:
            self.normal_artwork = NormalArtwork()
        pass_ = input("purchasing; PASSWORD? ")
        self.normal_artwork.purchase(pass_)


def main():
    proxy = ProxyArtwork()
    proxy.view()
    proxy.purchase()


main()
