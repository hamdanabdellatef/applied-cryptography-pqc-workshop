"""Behavior and boundary tests for the teaching record API."""
from pathlib import Path
import sys
import unittest
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from crypto_workshop.aead import (build_aad, generate_key, seal_record, open_record,
                                  decrypt_verified, EncryptedRecord)
from cryptography.exceptions import InvalidTag


class RecordTests(unittest.TestCase):
    def setUp(self):
        self.key = generate_key()
        self.message = b'invoice=7;amount=125;currency=USD'
        self.record = seal_record(self.key, self.message, 'acme', 'invoice-7')

    def test_round_trip_and_sizes(self):
        self.assertEqual(len(self.key), 32)
        self.assertEqual(len(self.record.nonce), 12)
        self.assertEqual(len(self.record.ciphertext), len(self.message) + 16)
        self.assertEqual(open_record(self.key, self.record, 'acme', 'invoice-7'), self.message)

    def test_wrong_context_key_and_modified_bytes(self):
        flip = lambda b: bytes([b[0] ^ 1]) + b[1:]
        variants = [
            ('key', flip(self.key), self.record, 'acme', 'invoice-7'),
            ('tenant', self.key, self.record, 'other', 'invoice-7'),
            ('record', self.key, self.record, 'acme', 'invoice-8'),
            ('nonce', self.key, EncryptedRecord(flip(self.record.nonce), self.record.ciphertext), 'acme', 'invoice-7'),
            ('ciphertext', self.key, EncryptedRecord(self.record.nonce, flip(self.record.ciphertext)), 'acme', 'invoice-7'),
            ('tag', self.key, EncryptedRecord(self.record.nonce, self.record.ciphertext[:-1] + bytes([self.record.ciphertext[-1] ^ 1])), 'acme', 'invoice-7'),
            ('truncation', self.key, EncryptedRecord(self.record.nonce, self.record.ciphertext[:8]), 'acme', 'invoice-7'),
        ]
        for label, key, record, tenant, record_id in variants:
            with self.subTest(label=label), self.assertRaises(InvalidTag):
                open_record(key, record, tenant, record_id)

    def test_empty_unicode_and_binary(self):
        for plaintext in (b'', 'فاتورة'.encode('utf-8'), bytes(range(256))):
            with self.subTest(plaintext=plaintext):
                record = seal_record(self.key, plaintext, 'acme', 'invoice-7')
                self.assertEqual(open_record(self.key, record, 'acme', 'invoice-7'), plaintext)

    def test_aad_is_unambiguous_and_context_is_validated(self):
        self.assertNotEqual(build_aad('ab', 'c'), build_aad('a', 'bc'))
        for tenant, record_id in [('', 'r'), ('x' * 65, 'r'), ('a|b', 'r'), (None, 'r'), ('a', 'bad context')]:
            with self.subTest(tenant=tenant), self.assertRaises(ValueError):
                build_aad(tenant, record_id)

    def test_exact_aad_bytes_are_required(self):
        with self.assertRaises(InvalidTag):
            decrypt_verified(self.key, self.record.nonce, self.record.ciphertext,
                             build_aad('acme', 'invoice-7') + b' ')

    def test_invalid_nonce_and_plaintext_type(self):
        for nonce in (b'', bytes(8), bytes(13)):
            with self.assertRaises(ValueError):
                decrypt_verified(self.key, nonce, self.record.ciphertext, b'')
        with self.assertRaises(TypeError):
            seal_record(self.key, 'encode me', 'acme', 'invoice-7')

    def test_each_encryption_requests_a_new_nonce(self):
        with patch('crypto_workshop.aead.secrets.token_bytes', side_effect=[b'a' * 12, b'b' * 12]) as rng:
            first = seal_record(self.key, self.message, 'acme', 'invoice-7')
            second = seal_record(self.key, self.message, 'acme', 'invoice-7')
        self.assertEqual(rng.call_count, 2)
        self.assertNotEqual(first.nonce, second.nonce)
        self.assertNotEqual(first.ciphertext, second.ciphertext)
        self.assertEqual(open_record(self.key, second, 'acme', 'invoice-7'), self.message)

    def test_replay_is_not_prevented(self):
        for _ in range(2):
            self.assertEqual(open_record(self.key, self.record, 'acme', 'invoice-7'), self.message)


if __name__ == '__main__':
    unittest.main()
