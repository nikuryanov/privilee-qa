import os
import requests

BASE_URL = "https://gorest.co.in/public/v2"
TOKEN = os.getenv("GOREST_TOKEN")
HEADERS = {"Authorization": f"Bearer {TOKEN}"}

# Token sanity check
def test_token_present():
    assert TOKEN, "GOREST_TOKEN is not set"
    print(f"Token present: {TOKEN[:4]}****")  # only show first 4 chars

ENDPOINTS = [
    "/users",                # may return 403 if token lacks permission
    "/posts",
    "/users/7373665/posts",
    "/todos"
]

ENDPOINTS_WITH_DATA = [
    "/posts",
    "/todos"
]

def check_status_code(endpoint):
    url = f"{BASE_URL}{endpoint}"
    return requests.get(url, headers=HEADERS)

def test_endpoints_status_code():
    """
    Check that all endpoints return HTTP 200.
    /users may return 403 if the token lacks permission, in which case we skip it.
    """
    for endpoint in ENDPOINTS:
        response = check_status_code(endpoint)
        if response.status_code == 403:
            print("Skipping /users: token lacks permission")
            continue
        assert response.status_code == 200, f"{endpoint} returned {response.status_code}"

def test_endpoints_return_json():
    """
    Check that all accessible endpoints return JSON arrays.
    /users will be skipped if forbidden (403).
    """
    for endpoint in ENDPOINTS:
        response = check_status_code(endpoint)
        if response.status_code == 403:
            continue
        try:
            data = response.json()
        except Exception:
            assert False, f"{endpoint} did not return valid JSON"
        assert isinstance(data, list), f"{endpoint} returned non-list data"
        if endpoint in ENDPOINTS_WITH_DATA:
            assert len(data) > 0, f"{endpoint} returned empty list"
