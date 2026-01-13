import os
from playwright.sync_api import sync_playwright

def verify_landing_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Get the absolute path to the HTML file
        file_path = os.path.abspath("AMAZON1/INDEX.HTML")
        page.goto(f"file://{file_path}")

        # Wait for the hero animation to complete (approx 1s)
        page.wait_for_timeout(1000)

        # Hover over the first box to see the effect
        page.locator(".box").first.hover()
        page.wait_for_timeout(500) # Wait for transition

        # Take a screenshot
        page.screenshot(path="/home/jules/verification/landing_page_hover.png")

        browser.close()

if __name__ == "__main__":
    verify_landing_page()
