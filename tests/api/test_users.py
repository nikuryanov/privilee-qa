import requests

BASE_URL = "https://gorest.co.in/public/v2"

def test_get_users_status_code():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200

def test_get_users_returns_list():
    response = requests.get(f"{BASE_URL}/users")
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_users_required_fields():
    response = requests.get(f"{BASE_URL}/users")
    users = response.json()
    required_fields = {"id", "name", "email", "gender", "status"}
    for user in users:
        assert required_fields.issubset(user.keys())
