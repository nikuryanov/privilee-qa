from playwright.sync_api import sync_playwright

MAP_URL = "https://staging-website.privilee.ae/map"

def test_map_responsive():
    """Check the map canvas resizes correctly for different viewports."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(MAP_URL, wait_until="networkidle")
        page.wait_for_timeout(5000)

        canvas = page.locator("canvas")
        # Desktop
        page.set_viewport_size({"width": 1920, "height": 1080})
        desktop_box = canvas.bounding_box()
        # Mobile
        page.set_viewport_size({"width": 375, "height": 667})
        page.wait_for_timeout(1000)
        mobile_box = canvas.bounding_box()

        assert desktop_box != mobile_box, "Canvas size did not change with viewport"
