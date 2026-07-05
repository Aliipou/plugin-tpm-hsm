# plugin-tpm-hsm

Hardware-backed signing seam (TPM / HSM / PKCS#11 / secure enclave) for the
Decision OS / AuthGate stack.

> Part of the Decision OS — governed by the Legitimacy ⊥ Authority pipeline
> (FDK legitimacy → AuthGate authority). Plugins are advisory only and hold
> **no authority**; the kernel remains the single authority.

**Status: interface-only (Protocol + honest stub).**

## What it does

Defines the `HardwareSigner` seam: keep the kernel's signing key inside a hardware
boundary (TPM2, an HSM via PKCS#11, or a cloud KMS) so it never lives in process
memory. This removes the stack's stated honesty limit — "an attacker who
compromises the kernel process can read the key." A `Pkcs11Signer` skeleton carries
the `key_uri` shape; the real provider must be wired in.

## Authority

This plugin holds **no authority**. It only signs bytes the kernel asks it to sign;
it makes no authorization decisions.

## Install

```bash
pip install "decision-os-min @ git+https://github.com/Aliipou/decision-os-min.git"
pip install -e . --no-deps
pytest -q          # AUTHGATE_BACKEND=python
```

## Usage

```python
from dos_plugin_tpm_hsm import Pkcs11Signer, HardwareSigner
s = Pkcs11Signer("pkcs11:token=demo;object=kernel")
isinstance(s, HardwareSigner)   # True
# s.sign(msg) raises NotImplementedError until a PKCS#11 provider is wired in.
```

## Status and limitations

- **Interface only.** `sign()` / `public_key()` raise `NotImplementedError`. A real
  backend must wrap `python-pkcs11` / a TPM2 stack / a cloud KMS and be validated
  against real hardware — not implemented here.
