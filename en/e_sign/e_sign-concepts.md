# How it works

## The signing flow

When you push a contract through the API, CNS accepts it and handles all interaction with the Chinese Certification Authority on your behalf. You don't need to think about how the CA connection works — you simply receive a status and a signing URL.

Once the contract is accepted, the CA prepares the signing flow and returns an active `foreignSignUrl`. The signer follows that link and signs the document on the CA's side. When signing is complete, you notify CNS via `/sign-complete` — and the contract is marked as signed.

---

## Contract statuses

Every contract moves through a set of states. Understanding these states is important for handling them correctly on your side.

```
DRAFT → PENDING → SENT → SIGNED
                       → REVOKED
                  ERROR
```

| Status | What it means |
| --- | --- |
| `DRAFT` | Contract accepted by CNS, being forwarded to the CA. |
| `PENDING` | The CA is processing the contract. |
| `SENT` | Ready for signing. The `foreignSignUrl` link is now active. |
| `SIGNED` | Contract is signed. Usage is charged. |
| `REVOKED` | Contract was cancelled before signing. Final state. |
| `ERROR` | The CA rejected the contract. See the `blockReason` field. |

The transition to `SIGNED` only happens when you explicitly call `/sign-complete`. The status does not change on its own — there is no need to continuously poll the API.

---

## Contract parties

This is an important detail that often causes integration errors.

The fields `domesticParty` and `foreignParty` are named from the perspective of the Chinese CA — meaning "domestic" refers to China, and "foreign" refers to Kazakhstan:

- `domesticParty` — the **Chinese** organization. Provide the USCC code (18 characters), e.g. `91310000MA1234567X`.
- `foreignParty` — the **Kazakh** organization. Provide the BIN (12 digits).

Swapping the parties will cause the CA to return error `40002`. You will need to correct the request and send it again with a new `foreignContractNo`.

---

## Idempotency

If you send the same request twice — for example, due to a network error — CNS will not create a duplicate. A repeated request with the same `foreignContractNo` and the same body will return the existing contract with `idempotent: true`.

If the request body changes while the `foreignContractNo` stays the same, the API returns error `40901`. This prevents accidentally overwriting an already-registered contract.

---

## Where data is stored

CNS does not store personal data of the parties involved. Only the contract status, metadata, and a reference to the signed file are stored on the CNS side. The signing process itself — including identity verification of the signer — takes place entirely on the CA's infrastructure in China.

This is a requirement of Chinese law (Cybersecurity Law of the PRC, Article 71, Paragraph 3), which CNS complies with at the architectural level.

---

## Pricing

Each successfully signed contract is charged as a single operation. The charge occurs when the contract transitions to `SIGNED`. Contracts that were revoked or ended in an error are not charged.

---

> **Need help?** Open a ticket in the [Support](https://console.cloud-native.kz/support) section or email <cns-support@fcd.kz>.
