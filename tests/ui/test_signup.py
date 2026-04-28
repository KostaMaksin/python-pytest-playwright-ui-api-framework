from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from utils.data_generator import generate_signup_user
from test_data.users import VALID_USER

def test_user_can_signup_successfully_and_delete_account(page):
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

    home_page.click_continue()
    home_page.assert_logged_in()
    home_page.click_delete_account()
    home_page.assert_account_deleted()

def test_signup_with_existing_mail_shows_error(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)

    home_page.open()
    home_page.click_signup_login_link()

    login_page.start_signup("Existing test user", VALID_USER["email"])
    login_page.assert_signup_error_message_visible()
    login_page.assert_signup_error_text("Email Address already exist!")