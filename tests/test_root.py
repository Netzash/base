from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    try:
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"Hello": "World"}
    except NameError as er:
        print(er)
