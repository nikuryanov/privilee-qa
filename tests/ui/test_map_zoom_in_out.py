from playwright.sync_api import sync_playwright

MAP_URL = "https://staging-website.privilee.ae/map"

def test_map_zoom_in_out():
    """Simulate zoom in/out via mouse wheel (Functionality / Interaction)."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(MAP_URL, wait_until="domcontentloaded")
        page.wait_for_timeout(5000)

        canvas = page.locator("canvas")
        box = canvas.bounding_box()
        center_x = box["x"] + box["width"] / 2
        center_y = box["y"] + box["height"] / 2

        page.mouse.move(center_x, center_y)

        # Zoom in
        page.mouse.wheel(delta_x=0, delta_y=-100)
        page.wait_for_timeout(1000)

        # Zoom out
        page.mouse.wheel(delta_x=0, delta_y=100)
        page.wait_for_timeout(1000)

        screenshot_bytes = canvas.screenshot()
        assert len(screenshot_bytes) > 0, "Canvas not rendered after zooming"
