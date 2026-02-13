import requests
import time

BASE_URL = "https://gorest.co.in/public/v2"

def get_posts_with_retry(retries=3, delay=1):
    """Try to get posts with optional retries if blocked (403)."""
    for attempt in range(retries):
        response = requests.get(f"{BASE_URL}/posts")
        if response.status_code == 200:
            return response
        print(f"Attempt {attempt+1} failed with {response.status_code}, retrying in {delay}s...")
        time.sleep(delay)
    # Return last response anyway
    return response

def test_get_posts_status_code():
    response = get_posts_with_retry()
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

def test_get_posts_returns_list():
    response = get_posts_with_retry()
    data = response.json()
    assert isinstance(data, list), f"Expected list, got {type(data)}"
    assert len(data) > 0, "Expected at least 1 post"

def test_get_posts_required_fields():
    response = get_posts_with_retry()
    posts = response.json()
    required_fields = {"id", "user_id", "title", "body"}
    for post in posts:
        assert required_fields.issubset(post.keys()), f"Missing fields in post {post.get('id')}"
