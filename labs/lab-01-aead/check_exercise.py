"""Acceptance checks for the learner implementation; no solution imports."""
import unittest
from starter import decrypt_verified
from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


class LearnerChecks(unittest.TestCase):
    def setUp(self):
        self.key = AESGCM.generate_key(bit_length=256)
        self.nonce = bytes(range(12))  # Fresh key per test; one encryption.
        self.aad = b'workshop:invoice-7'
        self.body = AESGCM(self.key).encrypt(self.nonce, b'amount=125', self.aad)

    def test_valid_record(self):
        self.assertEqual(decrypt_verified(self.key, self.nonce, self.body, self.aad), b'amount=125')

    def test_reject_mutations(self):
        flip = lambda data: bytes([data[0] ^ 1]) + data[1:]
        for label, key, nonce, body, aad in [
            ('ciphertext', self.key, self.nonce, flip(self.body), self.aad),
            ('tag', self.key, self.nonce, self.body[:-1] + bytes([self.body[-1] ^ 1]), self.aad),
            ('nonce', self.key, flip(self.nonce), self.body, self.aad),
            ('key', flip(self.key), self.nonce, self.body, self.aad),
            ('aad', self.key, self.nonce, self.body, b'workshop:invoice-8'),
            ('truncated', self.key, self.nonce, self.body[:8], self.aad),
        ]:
            with self.subTest(label=label), self.assertRaises(InvalidTag):
                decrypt_verified(key, nonce, body, aad)

    def test_empty_plaintext(self):
        key = AESGCM.generate_key(bit_length=256)
        body = AESGCM(key).encrypt(self.nonce, b'', self.aad)
        self.assertEqual(decrypt_verified(key, self.nonce, body, self.aad), b'')

    def test_invalid_nonce_length(self):
        with self.assertRaises(ValueError):
            decrypt_verified(self.key, b'short', self.body, self.aad)


if __name__ == '__main__':
    unittest.main()
