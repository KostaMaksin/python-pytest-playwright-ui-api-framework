from pages.home_page import HomePage
from pages.login_page import LoginPage
from test_data.users import INVALID_USER, VALID_USER

def test_login_with_invalid_credentials(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)

    home_page.open()
    home_page.click_signup_login_link()

    login_page.login(INVALID_USER["email"], INVALID_USER["password"])
    login_page.assert_login_error_message_visible()

def test_login_with_valid_credentials(page):
    home_page= HomePage(page)
    login_page = LoginPage(page)

    home_page.open()
    home_page.click_signup_login_link()

    login_page.login(VALID_USER["email"], VALID_USER["password"])
    login_page.assert_login_successful()