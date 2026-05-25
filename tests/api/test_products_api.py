from api.products_api import ProductsAPI


def test_get_all_products_returns_200():
    products_api = ProductsAPI()

    response = products_api.get_all_products()

    assert response.status_code == 200
    assert "products" in response.text


def test_search_product_returns_matching_products():
    products_api = ProductsAPI()

    response = products_api.search_product("top")

    assert response.status_code == 200
    assert "products" in response.text
    assert "top" in response.text.lower()