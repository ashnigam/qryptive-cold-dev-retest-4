from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, ec, padding


def sign_invoice(payload: bytes) -> bytes:
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    return key.sign(payload, padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                                          salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())


def sign_event(payload: bytes) -> bytes:
    key = ec.generate_private_key(ec.SECP256R1())
    return key.sign(payload, ec.ECDSA(hashes.SHA256()))
