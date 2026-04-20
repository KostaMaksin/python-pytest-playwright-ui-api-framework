from playwright.sync_api import expect

class LoginPage:
    def __init__(self, page):
        self.page = page

    # Selectors
    # Login
    def login_input_email(self):
        return self.page.locator("input[data-qa='login-email']")
    
    def login_input_password(self):
        return self.page.locator("input[data-qa='login-password']")
    
    def login_button(self):
        return self.page.locator("button[data-qa='login-button']")
    
    def login_error_message(self):
        return self.page.get_by_text("Your email or password is incorrect!")
    
    def logged_in_as_text(self):
        return self.page.locator("a").filter(has_text="Logged in as")
    
    def logout_link(self):
        return self.page.get_by_role("link", name="Logout")
    
    # Signup
    def signup_name_input(self):
        return self.page.locator("input[data-qa='signup-name']")
    
    def signup_email_input(self):
        return self.page.locator("input[data-qa='signup-email']")
    
    def signup_button(self):
        return self.page.locator("button[data-qa='signup-button']")
    
    def enter_account_information_heading(self):
        return self.page.get_by_text("Enter Account Information")
    
    # Actions
    # Login
    def enter_login_email(self, email):
        self.login_input_email().fill(email)

    def enter_login_password(self, password):
        self.login_input_password().fill(password)

    def login(self, email, password):
        self.enter_login_email(email)
        self.enter_login_password(password)
        self.login_button().click()

    def assert_login_error_message_visible(self):
        expect(self.login_error_message()).to_be_visible()

    def assert_login_successful(self):
        expect(self.logged_in_as_text()).to_be_visible()
        expect(self.logout_link()).to_be_visible()

    # Signup
    def fill_signup_name(self, name):
        self.signup_name_input().fill(name)

    def fill_signup_email(self, email):
        self.signup_email_input().fill(email)

    def click_signup(self):
        self.signup_button().click()

    def start_signup(self, name, email):
        self.fill_signup_name(name)
        self.fill_signup_email(email)
        self.click_signup()

    def assert_signup_page_opened(self):
        expect(self.enter_account_information_heading()).to_be_visible()
