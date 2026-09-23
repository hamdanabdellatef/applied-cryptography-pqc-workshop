"""Small-message AES-GCM teaching helpers, not a storage/network protocol.

Random nonces suit the small number of records in this lab. Production systems
need an explicit per-key usage budget and nonce strategy.
"""
from dataclasses import dataclass
import json
import re
import secrets
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

NONCE_BYTES = 12
TAG_BYTES = 16


def build_aad(tenant_id: str, record_id: str) -> bytes:
    """Encode expected context from an authorized request, not an untrusted blob.

    This restricted teaching schema is not a general canonical-JSON protocol.
    """
    for value in (tenant_id, record_id):
        if not isinstance(value, str) or not re.fullmatch(r'[A-Za-z0-9_-]{1,64}', value):
            raise ValueError('Context identifiers must be 1-64 ASCII letters, digits, _ or -.')
    context = {'purpose': 'workshop-invoice', 'version': 1,
               'tenant': tenant_id, 'record': record_id}
    return json.dumps(context, sort_keys=True, separators=(',', ':')).encode('ascii')


@dataclass(frozen=True)
class EncryptedRecord:
    """Public nonce plus encrypted bytes with the full tag appended."""
    nonce: bytes
    ciphertext: bytes


def generate_key() -> bytes:
    """Generate a fresh 256-bit key; never print or store it with ciphertext."""
    return AESGCM.generate_key(bit_length=256)


def seal_record(key: bytes, plaintext: bytes, tenant_id: str, record_id: str) -> EncryptedRecord:
    """Encrypt a small record with a new random 96-bit nonce for this lab."""
    if not isinstance(plaintext, bytes):
        raise TypeError('Encode plaintext to bytes before encrypting.')
    aad = build_aad(tenant_id, record_id)
    nonce = secrets.token_bytes(NONCE_BYTES)
    return EncryptedRecord(nonce, AESGCM(key).encrypt(nonce, plaintext, aad))


def decrypt_verified(key: bytes, nonce: bytes, ciphertext: bytes, expected_aad: bytes) -> bytes:
    """Return authenticated plaintext; propagate InvalidTag on mismatch.

    InvalidTag does not identify the wrong input. Do not suppress it,
    return substitute plaintext, or retry without authentication.
    """
    if len(nonce) != NONCE_BYTES:
        raise ValueError('This lab format requires a 12-byte nonce.')
    return AESGCM(key).decrypt(nonce, ciphertext, expected_aad)


def open_record(key: bytes, record: EncryptedRecord, tenant_id: str, record_id: str) -> bytes:
    """Open in the expected context. Does not enforce authorization or freshness."""
    return decrypt_verified(key, record.nonce, record.ciphertext,
                            build_aad(tenant_id, record_id))
