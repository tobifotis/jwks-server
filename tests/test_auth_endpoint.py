# tests/test_auth_endpoint.py

import json
from jwks_server.main import create_app


def test_auth_endpoint():
    app = create_app()
    client = app.test_client()

    # Test normal (unexpired) token
    response = client.post('/auth')
    assert response.status_code == 200

    data = json.loads(response.data)
    assert 'token' in data
