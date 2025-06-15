from legal_service_interface import LegalServiceInterface


class LegalService(LegalServiceInterface):
    def request_legal_assistance(self):
        print("Requesting real legal assistance with real legal service")

    def provide_legal_assistance(self):
        self.request_legal_assistance()
