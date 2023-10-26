from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    res = client.get("/")
    assert res.status_code == 200
    assert res.json() == {"message" : "Welcome to the Wikipedia API"}

def test_read_phrase():
    res = client.get("/phrase/Barack Obama")
    assert res.status_code == 200
    assert "result" in res.json()

def test_read_wiki():
    res = client.get("/wiki/kratos")
    assert res.status_code == 200

def test_read_search():
    res = client.get("/search/kratos")
    assert res.status_code == 200
    assert "Kratos (God of War)" in res.json()['result']