from legal_service import LegalService
from legal_service_interface import LegalServiceInterface


class LegalServiceProxy(LegalServiceInterface):
    def __init__(self):
        self.real_legal_service = None

    def request_legal_assistance(self):
        if self.real_legal_service is None:
            self.real_legal_service = LegalService()

        print("proxy serving legal assistance")
        self.real_legal_service.provide_legal_assistance()
