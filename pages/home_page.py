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
    
    def sign_up_login_link(self):
        return self.page.locator("ul.nav.navbar-nav").get_by_role("link", name=" Signup / Login")
    
    def test_cases_nav_link(self):
        return self.page.locator("ul.nav.navbar-nav").get_by_role("link", name=" Test Cases")
    
    def test_cases_heading(self):
        return self.page.locator("h2.title >> text='Test Cases'")
    
    # Actions
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

    def assert_signup_login_link_visible(self):
        expect(self.sign_up_login_link()).to_be_visible()

    def click_signup_login_link(self):
        self.sign_up_login_link().click()

    def click_test_cases_link(self):
        self.test_cases_nav_link().click()

    def block_google_ad_services(self):
        # 1. Block Google Ad services globally
        self.page.route("**/*googleads*", lambda route: route.abort())
        self.page.route("**/*adsbygoogle*", lambda route: route.abort())

    def assert_test_cases_url(self):
        expect(self.page).to_have_url(re.compile("/test_cases"))

    def assert_test_cases_heading(self):
        expect(self.test_cases_heading()).to_be_visible()