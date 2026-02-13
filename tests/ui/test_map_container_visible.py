from playwright.sync_api import sync_playwright

MAP_URL = "https://staging-website.privilee.ae/map"

def test_map_container_visible():
    """Check the Mapbox canvas container exists and is visible (UI)."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(MAP_URL, wait_until="networkidle")
        page.wait_for_timeout(5000)

        canvas = page.locator("canvas")
        assert canvas.count() > 0, "No canvas element found"
        box = canvas.bounding_box()
        assert box["width"] > 0 and box["height"] > 0, "Canvas has no size"
