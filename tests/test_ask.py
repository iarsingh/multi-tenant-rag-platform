from fastapi.testclient import TestClient
from tenrag.main import app

client = TestClient(app)


def test_answers_and_refuses():
    hit = client.post("/ask", json={"question": 'Where does the north tenant store invoices?'}).json()
    assert hit["answered"] is True
    assert hit["citation"] == "north"
    miss = client.post("/ask", json={"question": 'music charts'}).json()
    assert miss["answered"] is False


def test_empty_is_refused():
    assert client.post("/ask", json={"question": " "}).status_code == 422
