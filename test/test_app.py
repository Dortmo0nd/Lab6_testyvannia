import pytest
from src.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Перевірка, чи фронтенд сторінка завантажується успішно."""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"MyProject" in rv.data

def test_api_data(client):
    """Перевірка роботи бекенд API."""
    rv = client.get('/api/data')
    assert rv.status_code == 200
    assert rv.json == {"status": "success", "message": "Привіт від бекенду на Python!"}