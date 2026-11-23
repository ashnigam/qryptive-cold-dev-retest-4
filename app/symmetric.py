import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def seal_small(data: bytes) -> bytes:
    key = AESGCM.generate_key(bit_length=128)
    return AESGCM(key).encrypt(os.urandom(12), data, None)


def seal_strong(data: bytes) -> bytes:
    key = AESGCM.generate_key(bit_length=256)
    return AESGCM(key).encrypt(os.urandom(12), data, None)
