# auth_endpoint.py

import datetime
import jwt
from flask import Blueprint, request, jsonify

from .key_manager import get_valid_key, get_expired_key

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/auth', methods=['POST'])
def auth_handler():
    """
    Issues a JWT. If ?expired=true, it uses an expired key.
    """
    expired_flag = request.args.get('expired', 'false').lower() == 'true'

    if expired_flag:
        key = get_expired_key()
    else:
        key = get_valid_key()

    now = datetime.datetime.utcnow()
    claims = {
        "sub": "fake-user",  # No real auth check here
        "iat": now,
        "nbf": now,
        # Align the JWT expiry with the key expiry
        "exp": int(key.expiry.timestamp())
    }

    # Include the kid in the header so verifiers know which public key to use
    token = jwt.encode(
        payload=claims,
        key=key.private_key,
        algorithm="RS256",
        headers={"kid": key.kid}
    )

    return jsonify({"token": token})
