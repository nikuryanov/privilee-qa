from playwright.sync_api import sync_playwright
import time
from PIL import Image
import io

MAP_URL = "https://staging-website.privilee.ae/map"

def test_map_tiles_loaded():
    """Check the map canvas has non-empty pixels (Performance / Data Accuracy)."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(MAP_URL, wait_until="domcontentloaded")

        canvas = page.locator("canvas")

        start_time = time.time()
        non_empty = False
        timeout = 10  # seconds
        while time.time() - start_time < timeout:
            screenshot_bytes = canvas.screenshot()
            img = Image.open(io.BytesIO(screenshot_bytes))
            pixels = list(img.getdata())
            if img.mode in ("RGB", "RGBA"):
                non_empty = any(pixel[:3] != (255, 255, 255) for pixel in pixels)
            else:
                non_empty = any(pixel != 0 for pixel in pixels)
            if non_empty:
                break
            page.wait_for_timeout(500)

        assert non_empty, f"Canvas appears empty after {timeout}s (performance issue?)"

        browser.close()
