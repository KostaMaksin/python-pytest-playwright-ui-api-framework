from playwright.sync_api import expect

class LoginPage:
    def __init__(self, page):
        self.page = page

    # Selectors
    def login_input_email(self):
        return self.page.locator("input[data-qa='login-email']")
    
    def login_input_password(self):
        return self.page.locator("input[data-qa='login-password']")
    
    def login_button(self):
        return self.page.locator("button[data-qa='login-button']")
    
    def login_error_message(self):
        return self.page.get_by_text("Your email or password is incorrect!")
    
    # Actions
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
