# JWKS Server

This is a simple implementation of a JWKS (JSON Web Key Set) server that provides public keys for verifying JWTs (JSON Web Tokens).

## Requirements

- Python 3.x
- Flask
- PyJWT
- Cryptography

## Setup

1. Clone the repository:
```bash
git clone https://github.com/tobifotis/jwks-server.git
```

2. Navigate into the project directory:
```bash
cd jwks-server
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the server:
```bash
python -m jwks_server.main
```

## Endpoints
- /auth - Generates and returns a JWT
- /.well-known/jwks.json - Returns the JWKS with public keys


