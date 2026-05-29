import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    """Health endpoint should return 200"""
    response = client.get("/health")
    assert response.status_code == 200

def test_register_user(client):
    """Register endpoint should return 201"""
    response = client.post("/register", json={
        "username": "testuser",
        "password": "testpass123"
    })
    assert response.status_code == 201

def test_register_weak_password(client):
    """Short password should be rejected"""
    response = client.post("/register", json={
        "username": "testuser2",
        "password": "123"
    })
    assert response.status_code == 400

def test_register_missing_fields(client):
    """Missing fields should return 400"""
    response = client.post("/register", json={})
    assert response.status_code == 400

def test_login_invalid_user(client):
    """Login with non-existent user should return 401"""
    response = client.post("/login", json={
        "username": "nobody",
        "password": "wrongpass"
    })
    assert response.status_code == 401

def test_protected_without_token(client):
    """Protected endpoint without token should return 401"""
    response = client.get("/protected")
    assert response.status_code == 401

def test_full_auth_flow(client):
    """Register then login should return JWT token"""
    # Register
    client.post("/register", json={
        "username": "flowuser",
        "password": "securepass123"
    })
    # Login
    response = client.post("/login", json={
        "username": "flowuser",
        "password": "securepass123"
    })
    assert response.status_code == 200
    data = response.get_json()
    assert "access_token" in data
