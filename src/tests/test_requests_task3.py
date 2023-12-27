from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
task_id = 1
non_existent_id = 50000

# Сожалею, что так мало тестов =(

class TestRequests:
    def test_get_request(self):
        resp = client.get("/tasks")
        assert resp.status_code == 200

    def test_get_first_item_request(self):
        resp = client.get(f"/tasks/{task_id}")
        assert resp.status_code == 200

    def test_wrong_item_request(self):
        resp = client.get(f"/tasks/{non_existent_id}")
        assert resp.status_code == 404
