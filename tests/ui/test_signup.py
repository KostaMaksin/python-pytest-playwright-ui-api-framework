from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from utils.data_generator import generate_signup_user

def test_user_can_signup_successfully(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    signup_page = SignupPage(page)

    user = generate_signup_user()

    home_page.open()
    home_page.click_signup_login_link()

    login_page.start_signup(user["name"], user["email"])
    login_page.assert_signup_page_opened()

    signup_page.fill_account_details(user)
    signup_page.click_create_account()
    signup_page.assert_account_created()
