from playwright.sync_api import expect
from pages.home_page import HomePage

def test_homepage_loads(page):
    homepage = HomePage(page)
    homepage.open()
    homepage.assert_url()
    homepage.assert_homepage_loaded()
    homepage.assert_navbar_visible()
    homepage.assert_homepage_title()

def test_homepage_has_signup_login_link(page):
    homepage = HomePage(page)
    homepage.open()
    homepage.assert_signup_login_link_visible()

def test_homepage_test_cases_button(page):
    homepage = HomePage(page)
    homepage.block_google_ad_services()
    homepage.open()
    homepage.click_test_cases_link()
    homepage.assert_test_cases_url()  
    homepage.assert_test_cases_heading()
