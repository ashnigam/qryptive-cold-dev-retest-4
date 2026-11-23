import ssl
from cryptography.hazmat.primitives.asymmetric import dh, ed25519


def server_context() -> ssl.SSLContext:
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.load_cert_chain("certs/server.crt", "certs/server.key")
    return ctx


def dh_shared(peer_public):
    params = dh.generate_parameters(generator=2, key_size=2048)
    key = params.generate_private_key()
    return key.exchange(peer_public)


def sign_release(data: bytes) -> bytes:
    signer = ed25519.Ed25519PrivateKey.generate()
    return signer.sign(data)
