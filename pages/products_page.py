from playwright.sync_api import expect

class ProductsPage:
    def __init__(self, page):
        self.page = page

    # Selectors
    def all_products_heading(self):
        return self.page.get_by_role("heading", name="All Products")
    
    def search_input(self):
        return self.page.locator("#search_product")
    
    def search_button(self):
        return self.page.locator("#submit_search")
    
    def searched_products_heading(self):
        return self.page.get_by_role("heading", name="Searched Products")
    
    def product_cards(self):
        return self.page.locator(".features_items .product-image-wrapper")

    def first_product_add_to_cart_button(self):
        return self.product_cards().first.locator("a.add-to-cart").first
    
    def view_cart_link_in_modal(self):
        return self.page.get_by_role("link", name="View Cart")
    
    # Actions
    def assert_products_page_loaded(self):
        expect(self.all_products_heading()).to_be_visible()

    def search_product(self, product_name):
        self.search_input().fill(product_name)
        self.search_button().click()
    
    def assert_search_results_visible(self):
        expect(self.searched_products_heading()).to_be_visible()
        expect(self.product_cards().first).to_be_visible()
    
    def add_first_product_to_cart(self):
        self.first_product_add_to_cart_button().click()

    def click_view_cart_from_modal(self):
        self.view_cart_link_in_modal().click()
