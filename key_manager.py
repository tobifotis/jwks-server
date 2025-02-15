# key_manager.py

import datetime
import base64
import hashlib
import threading

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

KEY_VALIDITY_MINUTES = 5  # How long each key is valid

class Key:
    """
    Represents an RSA key pair with:
    - kid (key ID)
    - expiry (datetime)
    - private_key (rsa.RSAPrivateKey)
    - public_key (rsa.RSAPublicKey)
    """
    def __init__(self, kid, expiry, private_key):
        self.kid = kid
        self.expiry = expiry
        self.private_key = private_key
        self.public_key = private_key.public_key()

# A thread-safe list to store keys
lock = threading.Lock()
keys = []

def generate_rsa_key():
    """
    Generates a new RSA key pair, computes a unique kid, and sets expiry.
    """
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    # Convert public key to bytes (DER format) to create a stable kid
    pub_bytes = private_key.public_key().public_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Use a SHA-256 hash of the public key bytes as kid
    kid_raw = hashlib.sha256(pub_bytes).digest()
    kid = base64.urlsafe_b64encode(kid_raw).decode('utf-8').rstrip("=")

    expiry = datetime.datetime.utcnow() + datetime.timedelta(minutes=KEY_VALIDITY_MINUTES)
    new_key = Key(kid, expiry, private_key)

    with lock:
        keys.append(new_key)

    return new_key

def get_valid_key():
    """
    Returns an unexpired key if one exists, otherwise generates a new one.
    """
    now = datetime.datetime.utcnow()
    with lock:
        for k in keys:
            if now < k.expiry:
                return k
    # No valid key found, generate a new one
    return generate_rsa_key()

def get_expired_key():
    """
    Returns a newly generated key but forces it to be expired.
    """
    new_key = generate_rsa_key()
    new_key.expiry = datetime.datetime.utcnow() - datetime.timedelta(minutes=1)
    return new_key

def get_unexpired_keys():
    """
    Returns a list of all keys that have not expired.
    """
    now = datetime.datetime.utcnow()
    unexpired = []
    with lock:
        for k in keys:
            if now < k.expiry:
                unexpired.append(k)
    return unexpired
