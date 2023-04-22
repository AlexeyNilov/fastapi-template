import os
import sys
sys.path.insert(0, os.path.abspath('..'))
import app.backend as backend
from fastapi.testclient import TestClient


def test_health():
    client = TestClient(backend.app)
    response = client.get('/health')
    data = response.json()
    assert response.status_code == 200
    assert data['message'] == ['I am fine']
    assert data['workers_count'] == 2
