# main.py

from flask import Flask
from .jwks_endpoint import jwks_bp
from .auth_endpoint import auth_bp
from .key_manager import get_valid_key

def create_app():
    app = Flask(__name__)
    # Generate at least one valid key so /jwks won't be empty
    get_valid_key()

    # Register the endpoints
    app.register_blueprint(jwks_bp)
    app.register_blueprint(auth_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=8080, debug=True)
