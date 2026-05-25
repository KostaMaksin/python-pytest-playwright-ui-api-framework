from api.api_client import APIClient


class ProductsAPI:
    def __init__(self):
        self.client = APIClient()

    def get_all_products(self):
        return self.client.get("/productsList")

    def search_product(self, search_product):
        return self.client.post(
            "/searchProduct",
            data={"search_product": search_product}
        )