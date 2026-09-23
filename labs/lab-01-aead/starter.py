"""Lab 1 exercise. Implement decrypt_verified, then run check_exercise.py."""
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def decrypt_verified(key: bytes, nonce: bytes, ciphertext: bytes, expected_aad: bytes) -> bytes:
    """Require a 12-byte nonce, return authenticated plaintext, propagate InvalidTag.

    Raise ValueError for a nonce of the wrong length. Authenticated empty
    plaintext must return b''. Do not catch authentication failures here.
    """
    raise NotImplementedError('Implement the authenticated-decryption exercise.')


if __name__ == "__main__":
    print('Edit decrypt_verified, then run python labs/lab-01-aead/check_exercise.py')
