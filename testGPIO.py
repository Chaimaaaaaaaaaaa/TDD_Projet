import os
import pytest
from simple_flask_app.app import app

@pytest.fixture
def client():
    app.init_db("/tmp/test.db")
    yield app.test_client()
    os.remove("/tmp/test.db")

def test_home_page(client):
    """Test the home page returns the correct HTML and status code."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Current Number: 0' in response.data
