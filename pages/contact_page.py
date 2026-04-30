from playwright.sync_api import expect

class ContactPage:
    def __init__(self, page):
        self.page = page

    # Selectors
    def get_in_touch_heading(self):
        return self.page.get_by_role("heading", name="Get In Touch")
    
    def name_input(self):
        return self.page.locator("input[data-qa='name']")
    
    def name_input(self):
        return self.page.locator("input[data-qa='name']")
    
    def email_input(self):
        return self.page.locator("input[data-qa='email']")
    
    def subject_input(self):
        return self.page.locator("input[data-qa='subject']")
    
    def message_textarea(self):
        return self.page.locator("textarea[data-qa='message']")
    
    def submit_button(self):
        return self.page.locator("input[data-qa='submit-button']")
    
    def success_message(self):
        return self.page.locator(".status.alert.alert-success")
    
    # Actions
    def assert_contact_page_loaded(self):
        expect(self.get_in_touch_heading()).to_be_visible()

    def fill_contact_form(self, name, email, subject, message):
        self.name_input().fill(name)
        self.email_input().fill(email)
        self.subject_input().fill(subject)
        self.message_textarea().fill(message)

    def submit_form(self):
        def handle_dialog(dialog):
            dialog.accept()

        self.page.once("dialog", handle_dialog)
        self.submit_button().scroll_into_view_if_needed()
        self.submit_button().click(force=True)

    def assert_success_message_visible(self):
        expect(self.success_message()).to_have_text("Success! Your details have been submitted successfully.")