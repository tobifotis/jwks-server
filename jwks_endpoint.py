# jwks_endpoint.py

import base64
from flask import Blueprint, jsonify
from .key_manager import get_unexpired_keys

jwks_bp = Blueprint('jwks', __name__)

@jwks_bp.route('/jwks', methods=['GET'])
def jwks_handler():
    """
    Returns public keys in JWKS format (only unexpired keys).
    """
    keys = get_unexpired_keys()
    jwks_keys = []

    for key in keys:
        # Extract the RSA modulus (n) and exponent (e)
        public_numbers = key.public_key.public_numbers()

        n_bytes = public_numbers.n.to_bytes((public_numbers.n.bit_length() + 7) // 8, 'big')
        e_bytes = public_numbers.e.to_bytes((public_numbers.e.bit_length() + 7) // 8, 'big')

        jwk = {
            "kty": "RSA",
            "use": "sig",
            "alg": "RS256",
            "kid": key.kid,
            "n": base64.urlsafe_b64encode(n_bytes).decode('utf-8').rstrip("="),
            "e": base64.urlsafe_b64encode(e_bytes).decode('utf-8').rstrip("="),
        }
        jwks_keys.append(jwk)

    return jsonify({"keys": jwks_keys})
