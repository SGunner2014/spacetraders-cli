import requests
from collections.abc import Mapping

class Dict2Obj(object):
    def __init__(self, dict_data):
        for key in dict_data:
            # recursively convert dict_data
            if isinstance(dict_data[key], list):
                self.__setattr__(key, [Dict2Obj(item) if isinstance(item, dict) else item for item in dict_data[key]])
            elif isinstance(dict_data[key], dict):
                self.__setattr__(key, Dict2Obj(dict_data[key]))
            else:
                self.__setattr__(key, dict_data[key])

class __GenericClient():
    token = None
    root_url = "https://api.spacetraders.io/v2"

    def __init__(self, token):
        self.token = token

    def make_request(self, url, method, data=None, expected: type = None) -> object:
        response = requests.request(
            method,
            f"{self.root_url}{url}",
            headers={
                "Authorization": f"Bearer {self.token}"
            },
            data=data,
        )

        json = response.json()

        # Transform dict to object
        return Dict2Obj(json)