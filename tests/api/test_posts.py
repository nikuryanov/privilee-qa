import requests

BASE_URL = "https://gorest.co.in/public/v2"

def test_get_posts_status_code():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200

def test_get_posts_returns_list():
    response = requests.get(f"{BASE_URL}/posts")
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_posts_required_fields():
    response = requests.get(f"{BASE_URL}/posts")
    posts = response.json()
    required_fields = {"id", "user_id", "title", "body"}
    for post in posts:
        assert required_fields.issubset(post.keys())
