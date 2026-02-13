import os
import requests

BASE_URL = "https://gorest.co.in/public/v2"
TOKEN = os.getenv("GOREST_TOKEN")  # must be set in environment or GitHub secret
HEADERS = {"Authorization": f"Bearer {TOKEN}"}

ENDPOINTS = [
    "/users",
    "/posts",
    "/users/7373665/posts",
    "/todos"
]

def check_status_code(endpoint):
    """Helper to GET endpoint and return response"""
    url = f"{BASE_URL}{endpoint}"
    response = requests.get(url, headers=HEADERS)
    return response

def test_endpoints_status_code():
    """Check all endpoints return 200"""
    for endpoint in ENDPOINTS:
        response = check_status_code(endpoint)
        assert response.status_code == 200, f"{endpoint} returned {response.status_code}"

def test_endpoints_return_list():
    """Check all endpoints return a list"""
    for endpoint in ENDPOINTS:
        response = check_status_code(endpoint)
        try:
            data = response.json()
        except ValueError:
            assert False, f"{endpoint} did not return JSON"
        assert isinstance(data, list), f"{endpoint} did not return a list"

def test_posts_required_fields():
    """Check posts endpoint returns required fields"""
    response = check_status_code("/posts")
    posts = response.json()
    required_fields = {"id", "user_id", "title", "body"}
    for post in posts:
        assert required_fields.issubset(post.keys()), f"Post {post.get('id')} missing required fields"

def test_user_posts_required_fields():
    """Check specific user posts endpoint returns required fields"""
    response = check_status_code("/users/7373665/posts")
    posts = response.json()
    required_fields = {"id", "user_id", "title", "body"}
    for post in posts:
        assert required_fields.issubset(post.keys()), f"User post {post.get('id')} missing required fields"

def test_todos_required_fields():
    """Check todos endpoint returns required fields"""
    response = check_status_code("/todos")
    todos = response.json()
    required_fields = {"id", "user_id", "title", "due_on", "status"}
    for todo in todos:
        assert required_fields.issubset(todo.keys()), f"Todo {todo.get('id')} missing required fields"
