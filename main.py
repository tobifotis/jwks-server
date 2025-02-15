from flask import Flask
from jwks_server.auth_endpoint import auth_bp  # Corrected import
from jwks_server.jwks_endpoint import jwks_bp  # Corrected import

def create_app():
    app = Flask(__name__)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(jwks_bp, url_prefix='/.well-known')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='127.0.0.1', port=8080)
