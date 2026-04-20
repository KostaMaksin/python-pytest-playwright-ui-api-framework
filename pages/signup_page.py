from playwright.sync_api import expect

class SignupPage:
    def __init__(self, page):
        self.page = page

    # Selectors
    def title_mr_radio(self):
        return self.page.locator("#id_gender1")
    
    def password_input(self):
        return self.page.locator("input[data-qa='password']")
    
    def days_dropdown(self):
        return self.page.locator("select[data-qa='days']")
    
    def months_dropdown(self):
        return self.page.locator("select[data-qa='months']")
    
    def years_dropdown(self):
        return self.page.locator("select[data-qa='years']")
    
    def first_name_input(self):
        return self.page.locator("input[data-qa='first_name']")
    
    def last_name_input(self):
        return self.page.locator("input[data-qa='last_name']")
    
    def company_input(self):
        return self.page.locator("input[data-qa='company']")
    
    def address1_input(self):
        return self.page.locator("input[data-qa='address']")
    
    def address2_input(self):
        return self.page.locator("input[data-qa='address2']")
    
    def country_dropdown(self):
        return self.page.locator("select[data-qa='country']")
    
    def state_input(self):
        return self.page.locator("input[data-qa='state']")
    
    def city_input(self):
        return self.page.locator("input[data-qa='city']")

    def zipcode_input(self):
        return self.page.locator("input[data-qa='zipcode']")

    def mobile_number_input(self):
        return self.page.locator("input[data-qa='mobile_number']")

    def create_account_button(self):
        return self.page.locator("button[data-qa='create-account']")
    
    def account_created_heading(self):
        return self.page.get_by_text("Account Created!")
    
    def continue_button(self):
        return self.page.locator("a[data-qa='continue-button']")
    
    # Actions
    def fill_account_details(self, user):
        self.title_mr_radio().check()
        self.password_input().fill(user["password"])
        self.days_dropdown().select_option("10")
        self.months_dropdown().select_option("5")
        self.years_dropdown().select_option("1990")

        self.first_name_input().fill(user["first_name"])
        self.last_name_input().fill(user["last_name"])
        self.company_input().fill(user["company"])
        self.address1_input().fill(user["address1"])
        self.address2_input().fill(user["address2"])
        self.country_dropdown().select_option(user["country"])
        self.state_input().fill(user["state"])
        self.city_input().fill(user["city"])
        self.zipcode_input().fill(user["zip_code"])
        self.mobile_number_input().fill(user["mobile_number"])

    def click_create_account(self):
        self.create_account_button().click()

    def assert_account_created(self):
        expect(self.account_created_heading()).to_be_visible()
