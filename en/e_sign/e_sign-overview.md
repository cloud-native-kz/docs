# E-Contract — Electronic Contract Signing

E-Contract is the CNS Platform service for cross-border electronic contract signing between Kazakh and Chinese companies. It lets document flow systems, trading platforms, and any business application embed legally valid signing directly into their product — without needing to build relationships with certification authorities on their own.

---

## Who this service is for

E-Contract is designed for third-party integrators: companies building products in document management, cross-border trade, or financial services. If your platform facilitates transactions between Kazakhstan and China and you need contracts to be signed electronically with legal force in both countries, E-Contract handles exactly that.

An integrator connects to the CNS OpenAPI, pushes a contract through a single request, and receives a ready-to-use signing page URL. All interaction with the Chinese Certification Authority (CA) is handled transparently inside the platform.

---

## How the service works

CNS Platform is integrated with an accredited Chinese Certification Authority. Once connected, you do not need to build a direct relationship with the CA or navigate its API — CNS handles all interaction on your behalf: routing, authentication, status tracking, and recording the outcome.

---

## What the service handles

After a contract is pushed via API, the platform independently:

- forwards the contract to the Chinese CA through a secure proxy;
- notifies the intended signer by SMS and email;
- tracks signing status asynchronously, without polling pressure on your backend;
- stores the signed document and evidence — the file, hash, TSA timestamp, blockchain transaction ID;
- creates a billing event on your CNS account upon successful signing.

You receive a completion notification when the Kazakh side calls your `sign-complete` endpoint.

---

## Compliance

Signing physically takes place on infrastructure hosted in China. This is a requirement of Article 71, Paragraph 3 of the Cybersecurity Law of the People's Republic of China: operators of critical information infrastructure may not store personal data or important data outside of China.

On the CNS side, only the contract status, metadata, and an encrypted reference to the signed file are stored. Personal data of transaction participants does not pass through or get stored on CNS servers.

Traffic between CNS and the Chinese CA is routed through a secure Alibaba Cloud Singapore proxy. Measured latency is 60-156 ms — acceptable for an asynchronous signing flow.

---

## Getting started

To connect to E-Contract you will need:

1. An active CNS billing account.
2. An API key issued in the **API Keys** tab of the CNS Console.
3. Read [How it works](./e_sign-concepts.md) to understand the contract lifecycle and key concepts.
4. Go to the [API Reference](./e_sign-api.md) to start integrating.

---

> **Need help?** Open a ticket in the [Support](https://console.cloud-native.kz/support) section or email <cns-support@fcd.kz>.
