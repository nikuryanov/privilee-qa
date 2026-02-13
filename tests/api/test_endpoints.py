import os
import requests

# --- Config ---
BASE_URL = "https://gorest.co.in/public/v2"
TOKEN = os.getenv("GOREST_TOKEN")
HEADERS = {"Authorization": f"Bearer {TOKEN}"}

# --- Sanity check for token ---
def test_token_present():
    assert TOKEN, "GOREST_TOKEN is not set"
    print(f"Token present: {TOKEN[:4]}****")  # only show first 4 chars

# --- Endpoints to test ---
ENDPOINTS = [
    "/users",
    "/posts",
    "/users/7373665/posts",
    "/todos"
]

# Endpoints expected to always have at least one item
ENDPOINTS_WITH_DATA = [
    "/posts",
    "/todos"
]

# --- Helper ---
def check_status_code(endpoint):
    url = f"{BASE_URL}{endpoint}"
    return requests.get(url, headers=HEADERS)

# --- Tests ---
def test_endpoints_status_code():
    """
    Ensure all endpoints return HTTP 200.
    """
    for endpoint in ENDPOINTS:
        response = check_status_code(endpoint)
        assert response.status_code == 200, f"{endpoint} returned {response.status_code}"

def test_endpoints_return_json():
    """
    Ensure all endpoints return valid JSON arrays.
    Check that endpoints expected to have data are not empty.
    """
    for endpoint in ENDPOINTS:
        response = check_status_code(endpoint)
        try:
            data = response.json()
        except Exception:
            assert False, f"{endpoint} did not return valid JSON"
        
        assert isinstance(data, list), f"{endpoint} returned non-list data"
        
        if endpoint in ENDPOINTS_WITH_DATA:
            assert len(data) > 0, f"{endpoint} returned empty list"
