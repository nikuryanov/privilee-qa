from playwright.sync_api import sync_playwright

MAP_URL = "https://staging-website.privilee.ae/map"

def test_click_map_center():
    """Simulate a click at the center of the map canvas (Functionality)."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(MAP_URL, wait_until="networkidle")
        page.wait_for_timeout(5000)

        canvas = page.locator("canvas")
        box = canvas.bounding_box()
        center_x = box["x"] + box["width"] / 2
        center_y = box["y"] + box["height"] / 2

        page.mouse.click(center_x, center_y)
        page.screenshot(path="map_center_click.png")
