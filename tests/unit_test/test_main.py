from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Hello World"


def test_fibonacci_1():
    response = client.get("/fibonacci/1")
    assert response.status_code == 200
    assert response.text == "1"


def test_fibonacci_2():
    response = client.get("/fibonacci/2")
    assert response.status_code == 200
    assert response.text == "1"


def test_fibonacci_3():
    response = client.get("/fibonacci/6")
    assert response.status_code == 200
    assert response.text == "8"


def test_parenthesis_1():
    response = client.post("/parenthesis", json={"sequence": "(())"})
    assert response.status_code == 200
    assert response.json()["is_valid"]


def test_parenthesis_2():
    response = client.post("/parenthesis", json={"sequence": "([()])"})
    assert response.status_code == 200
    assert response.json()["is_valid"]


def test_parenthesis_3():
    response = client.post("/parenthesis", json={"sequence": "({[()]})"})
    assert response.status_code == 200
    assert response.json()["is_valid"]



def test_parenthesis_4():
    response = client.post("/parenthesis", json={"sequence": "({[(]})"})
    assert response.status_code == 200
    assert not response.json()["is_valid"]
