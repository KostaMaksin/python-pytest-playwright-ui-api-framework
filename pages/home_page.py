from playwright.sync_api import expect
import re

class HomePage:
    URL = "https://automationexercise.com/"

    def __init__(self, page):
        self.page = page
    
    def open(self):
        self.page.goto(self.URL)

    def navbar(self):
        return self.page.locator("ul.nav.navbar-nav")
    
    def hero_heading(self):
        return self.page.get_by_role("heading", name="Full-Fledged practice website for Automation Engineers")
    
    def signup_login_link(self):
        return self.page.locator("ul.nav.navbar-nav").get_by_role("link", name=" Signup / Login")
    
    def assert_url(self):
        expect(self.page).to_have_url(re.compile(r"https://automationexercise\.com/?"))

    def assert_homepage_loaded(self):
        expect(self.hero_heading()).to_be_visible()

    def assert_navbar_visible(self):
        expect(self.navbar()).to_be_visible()