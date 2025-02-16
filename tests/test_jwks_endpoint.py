import json
from jwks_server.main import create_app  # Corrected import


def test_jwks_endpoint():
    app = create_app()
    client = app.test_client()

    response = client.get('/.well-known/jwks.json')  # Corrected endpoint
    assert response.status_code == 200

    data = json.loads(response.data)
    assert 'keys' in data
    assert len(data['keys']) >= 1  # Should have at least 1 unexpired key
