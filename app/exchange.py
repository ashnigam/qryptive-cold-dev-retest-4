from cryptography.hazmat.primitives.asymmetric import ec, x25519


def ecdh_shared(peer_public):
    private_key = ec.generate_private_key(ec.SECP384R1())
    return private_key.exchange(ec.ECDH(), peer_public)


def x25519_shared(peer_public):
    private_key = x25519.X25519PrivateKey.generate()
    return private_key.exchange(peer_public)
