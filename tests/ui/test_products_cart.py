from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

def test_user_can_search_product_and_add_it_to_cart(page):
    home_page = HomePage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    home_page.block_google_ad_services()
    home_page.open()
    home_page.click_products()

    products_page.assert_products_page_loaded()
    products_page.search_product("Blue Top")
    products_page.assert_search_results_visible()
    products_page.add_first_product_to_cart()
    products_page.click_view_cart_from_modal()

    cart_page.assert_cart_page_loaded()
    cart_page.assert_cart_has_item()
    cart_page.assert_first_item_name_contains("Blue Top")
    cart_page.assert_first_item_quantity(1)