from Crypto.Cipher import DES, ARC4, Blowfish


def des_encrypt(key: bytes, data: bytes) -> bytes:
    return DES.new(key, DES.MODE_ECB).encrypt(data)


def rc4_encrypt(key: bytes, data: bytes) -> bytes:
    return ARC4.new(key).encrypt(data)


def blowfish_encrypt(key: bytes, data: bytes) -> bytes:
    return Blowfish.new(key, Blowfish.MODE_ECB).encrypt(data)
