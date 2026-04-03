from turtle import heading

from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

def test_homepage_loads():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://automationexercise.com/")

        expect(page.get_by_role("heading", name="Full-Fledged practice website for Automation Engineers")).to_be_visible()
        
        browser.close()

def test_homepage_button():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # 1. Block Google Ad services globally
        page.route("**/*googleads*", lambda route: route.abort())
        page.route("**/*adsbygoogle*", lambda route: route.abort())

        page.goto("https://automationexercise.com/")
        
        """# 1. Define the 'Close' button inside the ad iframe
        ad_close_button = page.frame_locator('iframe[name="aswift_1"]').frame_locator('iframe[name="ad_iframe"]').get_by_role("button", name="Close")

        # 2. Register the handler before clicking your link
        page.add_locator_handler(ad_close_button, lambda: ad_close_button.click())

        # 3. Perform your original click
        page.locator("ul.nav.navbar-nav").get_by_role("link", name="Test Cases").click()"""

        page.locator("ul.nav.navbar-nav").get_by_role("link", name=" Test Cases").click()
        
        page.wait_for_url("**/test_cases")  

        heading = page.locator("h2.title >> text='Test Cases'")
        expect(heading).to_be_visible() 

        browser.close()