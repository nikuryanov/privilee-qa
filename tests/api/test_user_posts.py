import requests

BASE_URL = "https://gorest.co.in/public/v2"
USER_ID = 7373665

def test_get_user_posts_status_code():
    response = requests.get(f"{BASE_URL}/users/{USER_ID}/posts")
    assert response.status_code == 200

def test_get_user_posts_returns_list():
    response = requests.get(f"{BASE_URL}/users/{USER_ID}/posts")
    data = response.json()
    assert isinstance(data, list)

def test_get_user_posts_required_fields():
    response = requests.get(f"{BASE_URL}/users/{USER_ID}/posts")
    posts = response.json()
    required_fields = {"id", "user_id", "title", "body"}
    for post in posts:
        assert required_fields.issubset(post.keys())
