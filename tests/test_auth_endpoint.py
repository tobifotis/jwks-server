import json
from jwks_server.main import create_app  # Corrected import

def test_auth_endpoint():
    app = create_app()
    client = app.test_client()

    response = client.post('/auth')
    assert response.status_code == 200

    data = json.loads(response.data)
    assert 'token' in data
