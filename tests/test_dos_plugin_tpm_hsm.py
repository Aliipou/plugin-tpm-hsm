import pytest

from dos_plugin_tpm_hsm import HardwareSigner, Pkcs11Signer


def test_signer_matches_protocol_shape():
    s = Pkcs11Signer("pkcs11:token=demo;object=kernel")
    assert isinstance(s, HardwareSigner) and s.key_uri.startswith("pkcs11:")


def test_is_honest_stub():
    with pytest.raises(NotImplementedError):
        Pkcs11Signer("pkcs11:x").sign(b"x")
