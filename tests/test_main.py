from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_api_info():
    response = client.get("/api/info")
    assert response.status_code == 200

    data = response.json()

    assert data["project"] == "AWS DevOps Cloud-Native"
    assert data["version"] == "1.0.0"
    assert "Docker" in data["technologies"]


def test_invalid_endpoint():
    response = client.get("/nonexistent")
    assert response.status_code == 404