from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_and_list_task():
    res = client.post("/tasks", json={"title": "Написать тесты"})
    assert res.status_code == 201
    task_id = res.json()["id"]

    res = client.get("/tasks")
    assert res.status_code == 200
    assert any(t["id"] == task_id for t in res.json())


def test_mark_done_not_found():
    res = client.patch("/tasks/99999/done")
    assert res.status_code == 404
