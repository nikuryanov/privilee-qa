import os
import requests

BASE_URL = "https://gorest.co.in/public/v2"
TOKEN = os.getenv("GOREST_TOKEN")
HEADERS = {"Authorization": f"Bearer {TOKEN}"}

# List of endpoints to test
ENDPOINTS = [
    "/users",
    "/posts",
    "/users/7373665/posts",
    "/todos"
]

# Endpoints that are expected to have at least 1 item
ENDPOINTS_WITH_DATA = [
    "/users",
    "/posts",
    "/todos"
]

def check_status_code(endpoint):
    """Helper to GET an endpoint with auth headers"""
    url = f"{BASE_URL}{endpoint}"
    response = requests.get(url, headers=HEADERS)
    return response

def test_token_is_valid():
    """Check the token works with /users"""
    response = check_status_code("/users")
    assert response.status_code == 200, f"Token invalid, got {response.status_code}"

def test_endpoints_status_code():
    """Check all endpoints return 200"""
    for endpoint in ENDPOINTS:
        response = check_status_code(endpoint)
        assert response.status_code == 200, f"{endpoint} returned {response.status_code}"

def test_endpoints_return_json():
    """Check all endpoints return JSON list"""
    for endpoint in ENDPOINTS:
        response = check_status_code(endpoint)
        try:
            data = response.json()
        except Exception:
            assert False, f"{endpoint} did not return valid JSON"
        assert isinstance(data, list), f"{endpoint} returned non-list data"

        # Only assert length > 0 for endpoints expected to have data
        if endpoint in ENDPOINTS_WITH_DATA:
            assert len(data) > 0, f"{endpoint} returned empty list"

def test_endpoints_required_fields():
    """Check required fields exist in each item"""
    REQUIRED_FIELDS = {
        "/users": {"id", "name", "email", "gender", "status"},
        "/posts": {"id", "user_id", "title", "body"},
        "/users/7373665/posts": {"id", "user_id", "title", "body"},
        "/todos": {"id", "user_id", "title", "due_on", "status"}
    }

    for endpoint in ENDPOINTS:
        response = check_status_code(endpoint)
        try:
            items = response.json()
        except Exception:
            assert False, f"{endpoint} did not return valid JSON"

        # Skip if empty list
        if not items:
            continue

        required_fields = REQUIRED_FIELDS.get(endpoint, set())
        for item in items:
            assert required_fields.issubset(item.keys()), f"{endpoint} missing fields in item {item}"
