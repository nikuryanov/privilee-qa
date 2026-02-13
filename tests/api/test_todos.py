import requests

BASE_URL = "https://gorest.co.in/public/v2"

def test_get_todos_status_code():
    response = requests.get(f"{BASE_URL}/todos")
    assert response.status_code == 200

def test_get_todos_returns_list():
    response = requests.get(f"{BASE_URL}/todos")
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_todos_required_fields():
    response = requests.get(f"{BASE_URL}/todos")
    todos = response.json()
    required_fields = {"id", "user_id", "title", "due_on", "status"}
    for todo in todos:
        assert required_fields.issubset(todo.keys())
