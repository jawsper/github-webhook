import hashlib
import hmac
import logging

from fastapi import Request

from .config import config

log = logging.getLogger(__name__)


async def validate_request(request: Request):
    signature = request.headers.get("x-hub-signature-256")
    return validate_signature(signature, await request.body())


def validate_signature(signature: str | None, body: bytes):
    if not signature:
        log.warn("signature missing")
        return False

    hash_function, hash = signature.split("=")
    if not (hash_function and hash):
        log.warn("missing hash function")
        return False
    if hash_function != "sha256":
        log.warn(f"unknown hash function {hash_function}")
        return False

    secret = config.github_secret.encode()

    expected_signature = hmac.new(
        secret, body, getattr(hashlib, hash_function)
    ).hexdigest()

    if hmac.compare_digest(hash, expected_signature):
        return True

    log.warn(f"signature validation failed {hash} != {expected_signature}")
    return False
