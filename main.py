# main.py
from flask import Flask
from .auth_endpoint import auth_bp
from .jwks_endpoint import jwks_bp

app = Flask(__name__)

# Register endpoints:
# - /auth for issuing JWTs
# - /.well-known/jwks.json for serving the JWKS
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(jwks_bp, url_prefix='/.well-known')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)
