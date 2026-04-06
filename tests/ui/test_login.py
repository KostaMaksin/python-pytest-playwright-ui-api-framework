from pages.home_page import HomePage
from pages.login_page import LoginPage

def test_login_with_invalid_credentials(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)

    home_page.open()
    home_page.click_signup_login_link()

    login_page.login("wrong@example.com", "wrongpassword")
    login_page.assert_login_error_message_visible()