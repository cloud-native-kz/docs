# Getting Started with Cloud Native Solutions

Cloud Native Solutions is a managed cloud platform for businesses and teams. This guide walks you through the entire onboarding process: from receiving your invitation to logging into the console and getting started.

---

## Table of Contents

1. [How Access Works](#1-how-access-works)
2. [Registration](#2-registration)
3. [Logging In](#3-logging-in)
4. [First Login to the Console](#4-first-login-to-the-console)
5. [Glossary](#5-glossary)

---

→ To explore the console interface, see [Console Overview](./console-overview.md).
→ Recommended actions after your first login are described in [First Steps After Login](./first-steps.md).

---

## 1. How Access Works

Cloud Native Solutions uses **invitation-based registration**. There is no open self-service sign-up.

This is intentional: the platform is designed for businesses and teams that need a managed, secure cloud environment. Access is currently available through limited testing and demo access for partners. Public self-service registration is planned for the future.

Each new account is tied to an **Organization** — a workspace that groups your team, projects, services, and billing. Before you can start, our team reviews your request and sends you a personal invitation.

**How to get access:**

1. Contact the Cloud Native Solutions team or your account manager to request access.
2. You will receive an invitation email at the address you provided.
3. Follow the link in the email to complete your registration.

![img.png](../../ru/getting-started/img.png)

> **Note:** Invitation links are single-use and expire after a limited period. If your link has expired, contact support to request a new one.

---

## 2. Registration

When you follow the invitation link, you will be taken to the account creation page at `console.cloud-native.kz`.

![img_2.png](../../ru/getting-started/img_2.png)

**Steps:**

1. Confirm or decline the invitation.
2. After confirming, you will be taken to a form where you need to set a password.
3. Create a **new password** for your account.
4. Confirm the password.
5. Click **Complete Registration**.

After successful registration you will be automatically redirected to the console.

---

## 3. Logging In

To log in to the console, go to:

```
https://console.cloud-native.kz
```

You will be redirected to the authentication page at `auth.cloud-native.kz`.

![img_3.png](../../ru/getting-started/img_3.png)

**Steps:**

1. Enter your **email address** in the username field.
2. Enter your **password**.
3. Press **Enter**.

After successful authentication you will be redirected to the console.

> **Forgot your password?** Email [cns-support@fcd.kz](mailto:cns-support@fcd.kz) — the support team will help you regain access.

---

## 4. First Login to the Console

After logging in you will land on the **Dashboard** — the main screen of the console.

At this point you are inside your **Organization**. The organization is created automatically when you register. To switch between organizations or view the current one, use the **dropdown menu in the top-right corner** of the screen.

<!-- screenshot: console dashboard (in development) -->

Before using paid services, you need to **create a Billing Account** (see [Creating a Billing Account](../billing/setup.md)).

---

## 5. Glossary

| Term | Definition |
|---|---|
| **Organization** | The top-level entity that groups all team members, projects, services, and billing. Each account belongs to one or more Organizations. |
| **Project** | A logical grouping of cloud resources within an Organization. Used to separate environments (e.g., production, staging) or teams. |
| **Owner** | An organization role with full administrative privileges. At least one Owner must exist in an organization. |
| **Administrator** | An organization role that can manage billing, invite members, and configure projects. |
| **Member** | An organization role with access to resources as configured by the Administrator. |
| **Billing Account** | The financial profile attached to your Organization. Contains payer details, payment method, and transaction history. |
| **Payment Method** | The method used to charge for platform usage. Available options: bank card and bank transfer (coming soon). |
| **Individual** | A billing account type for private users. |
| **Legal Entity** | A billing account type for companies (LLP, JSC, etc.). Required for issuing official invoices, acts of work, and access to corporate platform terms. |
| **Personal Access Token** | A credential used for programmatic API access. Used instead of a username and password for API calls. |
| **CDN** | Content Delivery Network — a distributed network of servers that delivers content to users from the nearest geographic node. |
| **HCI** | Hyper-Converged Infrastructure — a unified compute, storage, and networking system. Used in Sangfor. |
| **Invitation-based Registration** | An access model where new users can only register after receiving a personal invitation link. |

---

> **Need help?** Open a ticket in the [Support](https://console.cloud-native.kz/support) section.
