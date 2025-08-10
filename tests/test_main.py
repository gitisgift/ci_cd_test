from fastapi.testclient import TestClient
from root.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "welcome home"
