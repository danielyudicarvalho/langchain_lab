import os
from fastapi.testclient import TestClient
from langchain.api import app
from dotenv import load_dotenv

load_dotenv()

client = TestClient(app)

def test_upload_file():
    file_path = "test_file.txt"
    with open(file_path, "w") as f:
        f.write("test content")

    response = client.post("/upload/", files={"file": open(file_path, "rb")})
    assert response.status_code == 200
    assert response.json() == {"filename": "test_file.txt"}

    os.remove(file_path)

def test_create_agent():
    response = client.post("/create_agent/", json={"document": "test_document"})
    assert response.status_code == 200
    assert response.json() == {"agent_id": "test_document"}

def test_chat():
    response = client.post("/chat/", json={"agent_id": "test_document", "user_message": "test message"})
    assert response.status_code == 200
    assert response.json() == {"message": "test message"}

def test_summarize():
    file_path = "test_file.txt"
    with open(file_path, "w") as f:
        f.write("test content")

    response = client.post("/summarize/", files={"file": open(file_path, "rb")})
    assert response.status_code == 200
    assert response.json() == {"filename": "test_file.txt.summary"}

    os.remove(file_path)

def test_extract():
    response = client.post("/extract/", json={"text": "test text"})
    assert response.status_code == 200
    assert response.json() == {"properties": ["test text"]}

def test_create_schema():
    response = client.post("/create_schema/", json={"name": "test_property", "type": "string"})
    assert response.status_code == 200
    assert response.json() == {"message": "Schema updated"}

def test_get_schema():
    response = client.get("/schema/")
    assert response.status_code == 200
    assert response.json() == {"properties": {"test_property": {"type": "string"}}, "required": ["test_property"]}

def test_get_chats():
    response = client.get("/chats/")
    assert response.status_code == 200
    assert response.json() == {"test_document": "test_document"}

def test_get_retrievers():
    response = client.get("/retrievers/")
    assert response.status_code == 200
    assert response.json() == ["test_document"]