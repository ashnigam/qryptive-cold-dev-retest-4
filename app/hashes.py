import hashlib


def legacy_etag(data: bytes) -> str:
    return hashlib.md5(data).hexdigest()


def legacy_fingerprint(data: bytes) -> str:
    return hashlib.sha1(data).hexdigest()
