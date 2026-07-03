"""Hardware-backed signing seam (TPM / HSM / PKCS#11 / secure enclave).

INTERFACE ONLY. The Decision OS honesty limit is 'an attacker who compromises the
kernel process can read the key'. This plugin's job is to remove that limit by
keeping the private key in hardware. Implementations wrap PKCS#11 / TPM2 / a cloud
KMS. Not implemented here — it requires real hardware and integration tests.
"""

from __future__ import annotations

from typing import Protocol, runtime_checkable


@runtime_checkable
class HardwareSigner(Protocol):
    """A signer whose private key never leaves the hardware boundary."""

    key_uri: str          # e.g. 'pkcs11:token=...;object=kernel' or 'tpm2:...'
    algorithm: str

    def sign(self, message: bytes) -> bytes: ...
    def public_key(self) -> bytes: ...


class Pkcs11Signer:
    """PKCS#11 (HSM) backed signer — INTERFACE ONLY (wire python-pkcs11 here)."""

    algorithm = "ed25519"

    def __init__(self, key_uri: str) -> None:
        self.key_uri = key_uri

    def sign(self, message: bytes) -> bytes:  # pragma: no cover
        raise NotImplementedError("Wire a PKCS#11 provider (e.g. python-pkcs11) here.")

    def public_key(self) -> bytes:  # pragma: no cover
        raise NotImplementedError
