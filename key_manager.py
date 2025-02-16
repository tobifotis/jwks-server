import datetime
import uuid
from cryptography.hazmat.primitives.asymmetric import rsa

# Global variable to store the valid key instance
_valid_key = None


class Key:
    def __init__(self, private_key, expiry, kid):
        self.private_key = private_key
        self.expiry = expiry
        self.kid = kid
        self.public_key = private_key.public_key()


# Add the generate_rsa_key function
def generate_rsa_key():
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    expiry = (
            datetime.datetime.utcnow()
            + datetime.timedelta(days=1)
    )  # Valid for 1 day
    return Key(key, expiry, str(uuid.uuid4()))


def get_valid_key():
    global _valid_key
    if _valid_key is None:
        key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        expiry = (
                datetime.datetime.utcnow()
                + datetime.timedelta(days=1)
        )  # Valid for 1 day
        # Generate a unique key ID using uuid
        _valid_key = Key(key, expiry, str(uuid.uuid4()))
    return _valid_key


def get_expired_key():
    # Generate a new key that is already expired
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    expiry = (
            datetime.datetime.utcnow()
            - datetime.timedelta(days=1)
    )  # Expired 1 day ago
    return Key(key, expiry, str(uuid.uuid4()))


def get_unexpired_keys():
    # Return the valid key if it hasn't expired;
    # otherwise, return an empty list.
    key = get_valid_key()
    if key.expiry > datetime.datetime.utcnow():
        return [key]
    return []
