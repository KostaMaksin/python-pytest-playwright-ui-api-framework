from playwright.sync_api import expect
from pages.home_page import HomePage

def test_homepage_loads(page):
    homepage = HomePage(page)
    homepage.open()
    homepage.assert_url()
    homepage.assert_homepage_loaded()
    homepage.assert_navbar_visible()
    expect(page).to_have_title("Automation Exercise")

def test_homepage_has_signup_login_link(page):
    homepage = HomePage(page)
    homepage.open()
    expect(homepage.signup_login_link()).to_be_visible()

def test_homepage_button(page):
    # 1. Block Google Ad services globally
    page.route("**/*googleads*", lambda route: route.abort())
    page.route("**/*adsbygoogle*", lambda route: route.abort())

    page.goto("https://automationexercise.com/")

    page.locator("ul.nav.navbar-nav").get_by_role("link", name=" Test Cases").click()
    
    page.wait_for_url("**/test_cases")  

    heading = page.locator("h2.title >> text='Test Cases'")
    expect(heading).to_be_visible() 
