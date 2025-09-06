from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # headless = no visible window
        page = browser.new_page()

        # Go to the Calendly page (replace with your actual URL)
       # page.goto("https://calendly.com/cgc/coaching/2025-09-20T20:45:00-04:00?embed_domain=classical.guitarcorneracademy.com&embed_type=Inline&month=2025-09&name=Catherina&email=catherina%40microsaurus.com&date=2025-09-20")

        page.goto("https://calendly.com/cat-microsaurus/30min/2025-09-26T09:30:00+02:00?month=2025-09&date=2025-09-26&name=Catherina&email=catherina%40microsaurus.com")


        # Wait until the button is available, then click
        page.wait_for_selector("button[type='submit'] >> text=Schedule Event", timeout=30000)
        page.click("button[type='submit'] >> text=Schedule Event")

        # Optional: wait for confirmation (adjust text as needed)
        page.wait_for_selector("text=Confirmed", timeout=10000)

        browser.close()

if __name__ == "__main__":
    run()


