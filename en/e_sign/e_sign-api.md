# API Reference

## Base URL

```
https://ec-api.cloud-native.kz/openapi/v1
```

---

## Authentication

Authentication is per-organization using an HMAC key issued in the **API Keys** tab of the CNS Console. Every request must include four headers:

| Header | Description |
| --- | --- |
| `X-App-Id` | Public key identifier. Prefixed with `cns_ec_…` |
| `X-Timestamp` | Current Unix time in seconds. Drift greater than 5 minutes is rejected. |
| `X-Nonce` | Unique random string (at least 16 characters). Replays are blocked for 10 minutes. |
| `X-Signature` | Proof of secret possession. |

The signature (`X-Signature`) is computed over the canonical string:

```
METHOD\nPATH\nCANONICAL_QUERY\nX-App-Id\nX-Timestamp\nX-Nonce\nsha256(body-hex)
```

> **Current mode (MVP):** You may pass your plaintext secret directly in `X-Signature` — the gateway verifies it via Argon2. Phase 2 will switch to full HMAC-SHA256; keys issued now will continue to work.

---

## Endpoints

| Method | Path | Description |
| --- | --- | --- |
| `POST` | `/contracts` | Push a contract for signing. Idempotent on `(org, foreignContractNo)`. |
| `GET` | `/contracts/{requestId}` | Fetch contract status. `?fresh=true` forces a sync poll against the CA. |
| `POST` | `/contracts/{requestId}/revoke` | Revoke a contract before signing completes. |
| `POST` | `/contracts/{requestId}/sign-complete` | Record signing completion. The only path to `SIGNED`; triggers billing. |

---

## POST /contracts

Push a new contract for signing. Repeating the same request body returns `200` with `idempotent: true`. Changing the body for an existing `foreignContractNo` returns error `40901`.

### Request

```bash
curl -X POST "https://ec-api.cloud-native.kz/openapi/v1/contracts" \
  -H "X-App-Id: cns_ec_XXXXXXXXXXXXXXXX" \
  -H "X-Timestamp: $(date +%s)" \
  -H "X-Nonce: $(uuidgen)" \
  -H "X-Signature: <your secret>" \
  -H "Content-Type: application/json" \
  -d '{
    "foreignContractNo": "ORDER-2026-0517",
    "contractTitle": "Cross-border procurement agreement",
    "contractFileUrl": "https://files.example.com/contracts/order-2026-0517.pdf",
    "fileName": "order-2026-0517.pdf",
    "fileSha256": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
    "foreignSignUrl": "https://your-app.example.com/contracts/callback",
    "domesticParty": {
      "enterpriseName": "Shanghai Trading Co., Ltd",
      "uniformCode": "91310000MA1234567X",
      "legalName": "Wang Xiao",
      "contactName": "Li Mei",
      "contactMobile": "+8613800000000",
      "contactEmail": "limei@shanghai-trading.example.com"
    },
    "foreignParty": {
      "name": "Kazakh Logistics LLP",
      "country": "KZ",
      "registerNo": "180440017542"
    },
    "currency": "USD",
    "amount": 12500.00,
    "expireTime": "2026-06-30T23:59:59Z",
    "notifyMobiles": ["+77001234567"],
    "notifyEmails": ["aigerim@kazakh-logistics.example.com"]
  }'
```

### Request fields

**Top-level**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `foreignContractNo` | string | Yes | Contract number on the Kazakh side. Idempotency key. |
| `contractTitle` | string | Yes | Contract title for display. |
| `contractFileUrl` | string | Yes | Contract file URL. CNS stores a reference only. |
| `fileName` | string | No | File name for display. |
| `fileSha256` | string | No | SHA-256 file hash for integrity verification. |
| `foreignSignUrl` | string | Yes | Kazakh CA signing page URL. |
| `domesticParty` | object | Yes | Chinese-side organization data (see below). |
| `foreignParty` | object | Yes | Kazakh-side organization data (see below). |
| `currency` | string | No | Currency code, e.g. `USD`. |
| `amount` | number | No | Contract amount. |
| `expireTime` | string | No | Expiration timestamp in ISO-8601 UTC. |
| `notifyMobiles` | string[] | No | SMS notification numbers. At least one of `notifyMobiles`/`notifyEmails` required. |
| `notifyEmails` | string[] | No | Email notification addresses. At least one of `notifyMobiles`/`notifyEmails` required. |

**`domesticParty` — Chinese side**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `enterpriseName` | string | Yes | Company name. |
| `uniformCode` | string | Yes | Unified Social Credit Code (USCC), 18 characters. |
| `legalName` | string | No | Legal representative full name. |
| `contactName` | string | No | Intended signer contact name. |
| `contactMobile` | string | No | Intended signer mobile number. |
| `contactEmail` | string | No | Intended signer email. |

**`foreignParty` — Kazakh side**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | Organization name. |
| `country` | string | No | Country code, e.g. `KZ`. |
| `registerNo` | string | No | Business Identification Number (BIN), 12 digits. |

### Response

```http
HTTP/1.1 201 Created
Content-Type: application/json

{
  "requestId": "8c1f7e3a-4d6b-4b1f-9a3a-9f0c2e1b1d77",
  "foreignContractNo": "ORDER-2026-0517",
  "foreignSignUrl": "https://animall-signature.jgsysj.com/sign/8c1f7e3a...",
  "status": "PENDING",
  "idempotent": false
}
```

| Field | Description |
| --- | --- |
| `requestId` | Unique contract ID within CNS. Use in all subsequent requests. |
| `foreignSignUrl` | Active CA signing page URL. |
| `status` | Immediately after creation — `PENDING`. |
| `idempotent` | `true` if the contract already existed and was returned unchanged. |

---

## GET /contracts/{requestId}

Fetch the current contract status. Returns the locally cached state by default. Pass `?fresh=true` to force a sync poll against the CA — rate-limited, use sparingly.

### Request

```bash
curl "https://ec-api.cloud-native.kz/openapi/v1/contracts/8c1f7e3a-4d6b-4b1f-9a3a-9f0c2e1b1d77?fresh=true" \
  -H "X-App-Id: cns_ec_XXXXXXXXXXXXXXXX" \
  -H "X-Timestamp: $(date +%s)" \
  -H "X-Nonce: $(uuidgen)" \
  -H "X-Signature: <your secret>"
```

### Response

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "requestId": "8c1f7e3a-4d6b-4b1f-9a3a-9f0c2e1b1d77",
  "foreignContractNo": "ORDER-2026-0517",
  "status": "SENT",
  "canSign": true,
  "blockReason": null,
  "foreignSignUrl": "https://animall-signature.jgsysj.com/sign/8c1f7e3a...",
  "signedFileUrl": null,
  "signedAt": null,
  "createdAt": "2026-05-17T09:42:11Z",
  "updatedAt": "2026-05-17T09:43:02Z"
}
```

| Field | Description |
| --- | --- |
| `canSign` | `true` if signing is still possible. |
| `blockReason` | Reason signing is blocked, if `canSign` is `false`. |
| `signedFileUrl` | Populated after transition to `SIGNED`. |
| `signedAt` | Signing timestamp ISO-8601. Populated after `SIGNED`. |

---

## POST /contracts/{requestId}/revoke

Cancel a contract that has not yet been signed. After transitioning to `SIGNED`, revoke is rejected.

### Request

```bash
curl -X POST "https://ec-api.cloud-native.kz/openapi/v1/contracts/8c1f7e3a-4d6b-4b1f-9a3a-9f0c2e1b1d77/revoke" \
  -H "X-App-Id: cns_ec_XXXXXXXXXXXXXXXX" \
  -H "X-Timestamp: $(date +%s)" \
  -H "X-Nonce: $(uuidgen)" \
  -H "X-Signature: <your secret>" \
  -H "Content-Type: application/json" \
  -d '{
    "reason": "Customer cancelled the order before signing."
  }'
```

### Response

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "requestId": "8c1f7e3a-4d6b-4b1f-9a3a-9f0c2e1b1d77",
  "foreignContractNo": "ORDER-2026-0517",
  "status": "REVOKED",
  "canSign": false,
  "blockReason": "revoked",
  "foreignSignUrl": "https://animall-signature.jgsysj.com/sign/8c1f7e3a...",
  "signedFileUrl": null,
  "signedAt": null,
  "createdAt": "2026-05-17T09:42:11Z",
  "updatedAt": "2026-05-17T10:02:55Z"
}
```

---

## POST /contracts/{requestId}/sign-complete

Record that the contract has been signed on the Kazakh partner's side. This is the only call that moves a contract to `SIGNED` and triggers billing. All fields are optional — in practice, send at least `signedFileUrl` and `signerName`.

### Request

```bash
curl -X POST "https://ec-api.cloud-native.kz/openapi/v1/contracts/8c1f7e3a-4d6b-4b1f-9a3a-9f0c2e1b1d77/sign-complete" \
  -H "X-App-Id: cns_ec_XXXXXXXXXXXXXXXX" \
  -H "X-Timestamp: $(date +%s)" \
  -H "X-Nonce: $(uuidgen)" \
  -H "X-Signature: <your secret>" \
  -H "Content-Type: application/json" \
  -d '{
    "signerName": "Aigerim Nurlanovna",
    "signerIdcard": "880101300123",
    "signedFileUrl": "https://files.example.com/contracts/order-2026-0517.signed.pdf",
    "evidenceHash": "d2c39b1f8c5f0e3a1b7d6e2c8f4a9b1d5e7c3f9a2b6e8d0c1f3a5b7e9c2d4f6a",
    "tsaSerial": "TSA-2026-9F0C2E1B",
    "chainTxId": "0xab12cd34ef56..."
  }'
```

### Request fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `signerName` | string | No | Signer's full name. |
| `signerIdcard` | string | No | Signer's identity document number. |
| `signedFileUrl` | string | No | URL of the signed contract file. |
| `evidenceHash` | string | No | Evidence hash for integrity verification. |
| `tsaSerial` | string | No | TSA timestamp serial number. |
| `chainTxId` | string | No | Blockchain transaction identifier. |

### Response

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "requestId": "8c1f7e3a-4d6b-4b1f-9a3a-9f0c2e1b1d77",
  "foreignContractNo": "ORDER-2026-0517",
  "status": "SIGNED",
  "canSign": false,
  "blockReason": null,
  "foreignSignUrl": "https://animall-signature.jgsysj.com/sign/8c1f7e3a...",
  "signedFileUrl": "https://files.example.com/contracts/order-2026-0517.signed.pdf",
  "signedAt": "2026-05-17T11:18:40Z",
  "createdAt": "2026-05-17T09:42:11Z",
  "updatedAt": "2026-05-17T11:18:42Z"
}
```

---

## Error Codes

| Code | HTTP | Meaning |
| --- | --- | --- |
| `40101` | 401 | HMAC signature missing or invalid; API key revoked. |
| `40103` | 401 | Timestamp drift exceeds 5 minutes, or nonce was already used. |
| `40301` | 403 | Organization has no active billing account. |
| `40901` | 409 | `foreignContractNo` already used with a different request body. |
| `50200` | 502 | Upstream CA returned an error. |
| `50400` | 504 | Upstream CA did not respond in time. |

---

## Recommended Integration Flow

1. Call `POST /contracts` — pass the contract data and `foreignSignUrl`.
2. Wait for the `SENT` status (poll `GET /contracts/{requestId}`, use `?fresh=true` sparingly).
3. Direct the signer to the active `foreignSignUrl`.
4. If the contract must be cancelled — call `POST .../revoke` before signing completes.
5. After signing on the Kazakh side — call `POST .../sign-complete` with the evidence payload.
6. Reconcile records using the `requestId` + `foreignContractNo` pair.

---

> **Need help?** Open a ticket in the [Support](https://console.cloud-native.kz/support) section or email <cns-support@fcd.kz>.
