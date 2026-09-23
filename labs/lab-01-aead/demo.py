"""Reference workflow using synthetic data and an ephemeral key."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'src'))
from crypto_workshop.aead import generate_key, seal_record, open_record, EncryptedRecord
from cryptography.exceptions import InvalidTag


def main():
    key = generate_key()
    record = seal_record(key, b'invoice=7;amount=125;currency=USD', 'acme', 'invoice-7')
    assert open_record(key, record, 'acme', 'invoice-7') == b'invoice=7;amount=125;currency=USD'
    print('PASS: original record authenticates.')
    changed = EncryptedRecord(record.nonce, bytes([record.ciphertext[0] ^ 1]) + record.ciphertext[1:])
    for label, candidate, tenant, record_id in [
        ('modified ciphertext', changed, 'acme', 'invoice-7'),
        ('wrong tenant', record, 'other', 'invoice-7'),
        ('wrong record', record, 'acme', 'invoice-8'),
    ]:
        try:
            open_record(key, candidate, tenant, record_id)
        except InvalidTag:
            print(f'PASS: rejected {label}.')
        else:
            raise AssertionError(f'Unexpected acceptance: {label}')
    assert open_record(key, record, 'acme', 'invoice-7') == open_record(key, record, 'acme', 'invoice-7')
    print('OBSERVE: unchanged replay authenticates; freshness needs application state.')


if __name__ == '__main__':
    main()
