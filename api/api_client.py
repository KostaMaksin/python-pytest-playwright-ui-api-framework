import requests


class APIClient:
    BASE_URL = "https://automationexercise.com/api"

    def get(self, endpoint):
        return requests.get(f"{self.BASE_URL}{endpoint}")

    def post(self, endpoint, data=None):
        return requests.post(f"{self.BASE_URL}{endpoint}", data=data)

    def delete(self, endpoint, data=None):
        return requests.delete(f"{self.BASE_URL}{endpoint}", data=data)