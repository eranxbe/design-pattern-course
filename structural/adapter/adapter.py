from abc import ABC, abstractmethod


class ElectricalOutlet(ABC):
    @abstractmethod
    def request():  # charge an electrical device
        pass


class MobilePhone:
    def specific_request(self):
        print("Charging mobile phone")


class UniversalAdapter(ElectricalOutlet):
    def __init__(self, device: MobilePhone) -> None:
        self.device = device

    def request(self):
        print("Charging phone with electricity")
        self.device.specific_request()


def main():
    iphone = MobilePhone()
    adapter = UniversalAdapter(iphone)
    adapter.request()


main()
