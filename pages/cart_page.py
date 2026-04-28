from playwright.sync_api import expect

class CartPage:
    def __init__(self, page):
        self.page = page

    # Selectors
    def cart_table(self):
        return self.page.locator("#cart_info_table")
    
    def cart_items(self):
        return self.page.locator("#cart_info_table tbody tr")
    
    def first_cart_item_name(self):
        return self.cart_items().first.locator(".cart_description a")
    
    def first_cart_item_quantity(self):
        return self.cart_items().first.locator(".cart_quantity button")
    
    # Actions
    def assert_cart_page_loaded(self):
        expect(self.cart_table()).to_be_visible() 

    def assert_cart_has_item(self):
        expect(self.cart_items().first).to_be_visible()

    def assert_first_item_name_contains(self, expected_text):
        expect(self.first_cart_item_name()).to_contain_text(expected_text)
    
    def assert_first_item_quantity(self, expected_quantity):
        expect(self.first_cart_item_quantity()).to_have_text(str(expected_quantity))