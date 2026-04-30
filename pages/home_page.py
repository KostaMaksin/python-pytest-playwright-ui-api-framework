from playwright.sync_api import expect
import re

class HomePage:
    URL = "https://automationexercise.com/"
    PAGE_TITLE = "Automation Exercise"

    def __init__(self, page):
        self.page = page

    # Selectors
    def navbar(self):
        return self.page.locator("ul.nav.navbar-nav")
    
    def hero_heading(self):
        return self.page.get_by_role("heading", name="Full-Fledged practice website for Automation Engineers")
    
    def test_cases_nav_link(self):
        return self.page.locator("ul.nav.navbar-nav").get_by_role("link", name=" Test Cases")
    
    def test_cases_heading(self):
        return self.page.locator("h2.title >> text='Test Cases'")
    
    def sign_up_login_link(self):
        return self.page.locator("ul.nav.navbar-nav").get_by_role("link", name=" Signup / Login")
    
    def logged_in_as_text(self):
        return self.page.locator("a").filter(has_text="Logged in as")
    
    def logout_link(self):
        return self.page.get_by_role("link", name="Logout")
    
    def delete_account_link(self):
        return self.page.get_by_role("link", name=" Delete Account")
    
    def account_deleted_heading(self):
        return self.page.get_by_text("Account Deleted!")
    
    def continue_button(self):
        return self.page.locator("a[data-qa='continue-button']")
    
    def contact_us_link(self):
        return self.page.get_by_role("link", name="Contact us")
    
    # Actions
    def block_google_ad_services(self):
        # 1. Block Google Ad services globally
        self.page.route("**/*googleads*", lambda route: route.abort())
        self.page.route("**/*adsbygoogle*", lambda route: route.abort())

    def open(self):
        self.page.goto(self.URL)
    
    def assert_url(self):
        expect(self.page).to_have_url(re.compile(r"https://automationexercise\.com/?"))

    def assert_homepage_loaded(self):
        expect(self.hero_heading()).to_be_visible()

    def assert_homepage_title(self):
        expect(self.page).to_have_title(self.PAGE_TITLE)

    def assert_navbar_visible(self):
        expect(self.navbar()).to_be_visible()

    def click_test_cases_link(self):
        self.test_cases_nav_link().click()

    def assert_test_cases_heading(self):
        expect(self.test_cases_heading()).to_be_visible()

    def assert_test_cases_url(self):
        expect(self.page).to_have_url(re.compile("/test_cases"))

    def assert_signup_login_link_visible(self):
        expect(self.sign_up_login_link()).to_be_visible()

    def click_signup_login_link(self):
        self.sign_up_login_link().click()

    def assert_logged_in(self):
        expect(self.logged_in_as_text()).to_be_visible()
        expect(self.logout_link()).to_be_visible()

    def click_logout(self):
        self.logout_link().click()

    def click_delete_account(self):
        self.delete_account_link().click()

    def assert_account_deleted(self):
        expect(self.account_deleted_heading()).to_be_visible()

    def click_continue(self):
        self.continue_button().click()

    def products_link(self):
        return self.page.get_by_role("link", name="Products")
    
    def click_products(self):
        self.products_link().click()

    def click_contact_us(self):
        self.contact_us_link().click()