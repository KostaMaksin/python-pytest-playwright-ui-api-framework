from pages.home_page import HomePage
from pages.contact_page import ContactPage

def test_user_can_submit_contact_form(page):
    home_page = HomePage(page)
    contact_page = ContactPage(page)

    home_page.block_google_ad_services()
    home_page.open()
    home_page.click_contact_us()

    contact_page.assert_contact_page_loaded()
    contact_page.fill_contact_form(
        name="Test User",
        email="test@example.com",
        subject="Test Subject",
        message="This is a test message."
    )
    contact_page.submit_form()
    contact_page.assert_success_message_visible()

