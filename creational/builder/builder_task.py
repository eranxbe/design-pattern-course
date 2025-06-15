from abc import ABC, abstractmethod
from typing import Optional


class Builder(ABC):
    @abstractmethod
    def set_url(self):
        pass

    @abstractmethod
    def set_method(self):
        pass

    @abstractmethod
    def set_headers(self):
        pass

    @abstractmethod
    def set_query_params(self):
        pass

    @abstractmethod
    def set_body(self):
        pass


class ApiRequestBuilder(Builder):
    def __init__(self):
        self.api_request = ApiRequest()

    def set_url(self, url: str):
        self.api_request.add_property("URL", url)

    def set_method(self, method: str):
        allowed_methods = ["GET", "POST", "PUT", "DELETE", "PATCH"]
        if method not in allowed_methods:
            raise ValueError("Method not allowed")
        self.api_request.add_property("Method", method)

    def set_headers(self, headers: Optional[dict] = None):
        if not headers:
            return
        if not isinstance(headers, dict):
            raise ValueError("Invalid headers format")
        self.api_request.add_property("Headers", headers)

    def set_query_params(self, params: Optional[dict] = None):
        if not params:
            return
        if not isinstance(params, dict):
            raise ValueError("Invalid params format")
        self.api_request.add_property("Query Parameters", params)

    def set_body(self, body: Optional[dict] = None):
        if not body:
            return
        self.api_request.add_property("Body", body)

    def get_request_obj(self):
        return self.api_request


class Director:
    def __init__(self, builder: Builder):
        self.builder = builder

    def construct_api_request(
        self,
        url,
        method,
        headers: Optional[dict] = None,
        params: Optional[dict] = None,
        body: Optional[dict] = None,
    ):
        self.builder.set_url(url)
        self.builder.set_method(method)
        self.builder.set_headers(headers)
        self.builder.set_query_params(params)
        self.builder.set_body(body)


class ApiRequest:
    def __init__(self):
        self.properties = {}

    def add_property(self, property, value):
        self.properties[property] = value

    def show(self):
        print("API Request:")
        for k, v in self.properties.items():
            print(f"{k} - {v}")


def main():
    builder = ApiRequestBuilder()
    director = Director(builder)
    director.construct_api_request("https://youtube.com", "GET", {"hello": "world"})
    request = builder.get_request_obj()
    request.show()


main()
