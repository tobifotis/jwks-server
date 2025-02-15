import datetime
import jwt
from flask import Blueprint, request, jsonify
from .key_manager import get_valid_key, get_expired_key

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('', methods=['POST'])  # Endpoint: /auth
def auth_handler():
    """
    Issues a JWT. If ?expired=true, it uses an expired key.
    """
    expired_flag = request.args.get('expired', 'false').lower() == 'true'
    key = get_expired_key() if expired_flag else get_valid_key()

    now = datetime.datetime.utcnow()
    claims = {
        "sub": "fake-user",
        "iat": now,
        "nbf": now,
        "exp": int(key.expiry.timestamp())
    }

    token = jwt.encode(
        payload=claims,
        key=key.private_key,
        algorithm="RS256",
        headers={"kid": key.kid}  # JWT header includes the key ID
    )

    return jsonify({"token": token})
