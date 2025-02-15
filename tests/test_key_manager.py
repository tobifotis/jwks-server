import pytest
from datetime import datetime
from jwks_server.key_manager import generate_rsa_key, get_valid_key, get_expired_key, get_unexpired_keys  # Corrected import

def test_generate_rsa_key():
    key = generate_rsa_key()
    assert key.private_key is not None
    assert key.public_key is not None
    assert key.kid is not None
    assert key.expiry > datetime.utcnow()

def test_get_valid_key():
    key = get_valid_key()
    assert key.expiry > datetime.utcnow()

def test_get_expired_key():
    key = get_expired_key()
    assert key.expiry < datetime.utcnow()

def test_get_unexpired_keys():
    valid_key = get_valid_key()
    unexpired = get_unexpired_keys()
    assert valid_key in unexpired
