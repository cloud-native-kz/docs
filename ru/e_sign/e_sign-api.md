# API-справочник

## Базовый URL

```
https://ec-api.cloud-native.kz/openapi/v1
```

---

## Аутентификация

Аутентификация выполняется на уровне организации с помощью HMAC-ключа, выданного во вкладке **API Keys** консоли CNS. Каждый запрос обязан содержать четыре заголовка:

| Заголовок | Описание |
| --- | --- |
| `X-App-Id` | Публичный идентификатор ключа. Начинается с `cns_ec_…` |
| `X-Timestamp` | Текущее время Unix в секундах. Отклонение более 5 минут — отказ. |
| `X-Nonce` | Уникальная случайная строка (не менее 16 символов). Повторы блокируются на 10 минут. |
| `X-Signature` | Доказательство владения секретом. |

Подпись (`X-Signature`) вычисляется по канонической строке:

```
METHOD\nPATH\nCANONICAL_QUERY\nX-App-Id\nX-Timestamp\nX-Nonce\nsha256(body-hex)
```

> **Текущий режим (MVP):** Можно передавать секрет напрямую в `X-Signature` — шлюз проверяет его через Argon2. В фазе 2 будет включена полная схема HMAC-SHA256; ключи, выданные сейчас, продолжат работать.

---

## Эндпоинты

| Метод | Путь | Описание |
| --- | --- | --- |
| `POST` | `/contracts` | Отправить договор на подпись. Идемпотентен по `(org, foreignContractNo)`. |
| `GET` | `/contracts/{requestId}` | Получить статус договора. Параметр `?fresh=true` — принудительный опрос УЦ. |
| `POST` | `/contracts/{requestId}/revoke` | Отозвать договор до завершения подписания. |
| `POST` | `/contracts/{requestId}/sign-complete` | Зафиксировать подписание. Единственный путь к статусу `SIGNED`; запускает биллинг. |

---

## POST /contracts

Отправить новый договор на подпись. Повторный запрос с тем же телом возвращает `200` с `idempotent: true`. Изменение тела при том же `foreignContractNo` возвращает ошибку `40901`.

### Запрос

```bash
curl -X POST "https://ec-api.cloud-native.kz/openapi/v1/contracts" \
  -H "X-App-Id: cns_ec_XXXXXXXXXXXXXXXX" \
  -H "X-Timestamp: $(date +%s)" \
  -H "X-Nonce: $(uuidgen)" \
  -H "X-Signature: <ваш секрет>" \
  -H "Content-Type: application/json" \
  -d '{
    "foreignContractNo": "ORDER-2026-0517",
    "contractTitle": "Договор о трансграничных поставках",
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

### Поля запроса

**Верхний уровень**

| Поле | Тип | Обяз. | Описание |
| --- | --- | --- | --- |
| `foreignContractNo` | string | Да | Номер договора на стороне казахстанского партнёра. Ключ идемпотентности. |
| `contractTitle` | string | Да | Название договора для отображения. |
| `contractFileUrl` | string | Да | URL файла договора. CNS хранит только ссылку. |
| `fileName` | string | Нет | Имя файла для отображения. |
| `fileSha256` | string | Нет | SHA-256 хеш файла для проверки целостности. |
| `foreignSignUrl` | string | Да | URL страницы подписания казахстанского УЦ. |
| `domesticParty` | object | Да | Данные китайской стороны (см. ниже). |
| `foreignParty` | object | Да | Данные казахстанской стороны (см. ниже). |
| `currency` | string | Нет | Код валюты, например `USD`. |
| `amount` | number | Нет | Сумма договора. |
| `expireTime` | string | Нет | Срок действия в ISO-8601 UTC. |
| `notifyMobiles` | string[] | Нет | Номера для SMS. Хотя бы одно из `notifyMobiles`/`notifyEmails` обязательно. |
| `notifyEmails` | string[] | Нет | Email для уведомлений. Хотя бы одно из `notifyMobiles`/`notifyEmails` обязательно. |

**`domesticParty` — китайская сторона**

| Поле | Тип | Обяз. | Описание |
| --- | --- | --- | --- |
| `enterpriseName` | string | Да | Название компании. |
| `uniformCode` | string | Да | Единый социальный кредитный код (USCC), 18 символов. |
| `legalName` | string | Нет | ФИО законного представителя. |
| `contactName` | string | Нет | ФИО контактного лица - подписанта. |
| `contactMobile` | string | Нет | Телефон контактного лица. |
| `contactEmail` | string | Нет | Email контактного лица. |

**`foreignParty` — казахстанская сторона**

| Поле | Тип | Обяз. | Описание |
| --- | --- | --- | --- |
| `name` | string | Да | Название организации. |
| `country` | string | Нет | Код страны, например `KZ`. |
| `registerNo` | string | Нет | БИН, 12 цифр. |

### Ответ

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

| Поле | Описание |
| --- | --- |
| `requestId` | Уникальный ID договора в CNS. Используйте во всех последующих запросах. |
| `foreignSignUrl` | Ссылка на страницу подписания УЦ. |
| `status` | Сразу после создания — `PENDING`. |
| `idempotent` | `true`, если договор уже существовал и возвращён без изменений. |

---

## GET /contracts/{requestId}

Получить текущий статус договора. По умолчанию — локально кэшированное состояние. Параметр `?fresh=true` принудительно синхронизирует с УЦ; используйте редко — запросы лимитированы.

### Запрос

```bash
curl "https://ec-api.cloud-native.kz/openapi/v1/contracts/8c1f7e3a-4d6b-4b1f-9a3a-9f0c2e1b1d77?fresh=true" \
  -H "X-App-Id: cns_ec_XXXXXXXXXXXXXXXX" \
  -H "X-Timestamp: $(date +%s)" \
  -H "X-Nonce: $(uuidgen)" \
  -H "X-Signature: <ваш секрет>"
```

### Ответ

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

| Поле | Описание |
| --- | --- |
| `canSign` | `true`, если подписание ещё возможно. |
| `blockReason` | Причина блокировки, если `canSign: false`. |
| `signedFileUrl` | Заполняется после перехода в `SIGNED`. |
| `signedAt` | Временна́я метка подписания ISO-8601. Заполняется после `SIGNED`. |

---

## POST /contracts/{requestId}/revoke

Отозвать договор, который ещё не подписан. После перехода в `SIGNED` отзыв невозможен.

### Запрос

```bash
curl -X POST "https://ec-api.cloud-native.kz/openapi/v1/contracts/8c1f7e3a-4d6b-4b1f-9a3a-9f0c2e1b1d77/revoke" \
  -H "X-App-Id: cns_ec_XXXXXXXXXXXXXXXX" \
  -H "X-Timestamp: $(date +%s)" \
  -H "X-Nonce: $(uuidgen)" \
  -H "X-Signature: <ваш секрет>" \
  -H "Content-Type: application/json" \
  -d '{
    "reason": "Клиент отменил заказ до подписания."
  }'
```

### Ответ

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

Зафиксировать, что договор подписан на стороне казахстанского партнёра. Это единственный вызов, который переводит договор в `SIGNED` и запускает биллинг. Все поля необязательны; рекомендуется передавать как минимум `signedFileUrl` и `signerName`.

### Запрос

```bash
curl -X POST "https://ec-api.cloud-native.kz/openapi/v1/contracts/8c1f7e3a-4d6b-4b1f-9a3a-9f0c2e1b1d77/sign-complete" \
  -H "X-App-Id: cns_ec_XXXXXXXXXXXXXXXX" \
  -H "X-Timestamp: $(date +%s)" \
  -H "X-Nonce: $(uuidgen)" \
  -H "X-Signature: <ваш секрет>" \
  -H "Content-Type: application/json" \
  -d '{
    "signerName": "Айгерим Нурланова",
    "signerIdcard": "880101300123",
    "signedFileUrl": "https://files.example.com/contracts/order-2026-0517.signed.pdf",
    "evidenceHash": "d2c39b1f8c5f0e3a1b7d6e2c8f4a9b1d5e7c3f9a2b6e8d0c1f3a5b7e9c2d4f6a",
    "tsaSerial": "TSA-2026-9F0C2E1B",
    "chainTxId": "0xab12cd34ef56..."
  }'
```

### Поля запроса

| Поле | Тип | Обяз. | Описание |
| --- | --- | --- | --- |
| `signerName` | string | Нет | ФИО подписанта. |
| `signerIdcard` | string | Нет | Номер удостоверения личности подписанта. |
| `signedFileUrl` | string | Нет | URL подписанного файла. |
| `evidenceHash` | string | Нет | Хеш доказательной базы. |
| `tsaSerial` | string | Нет | Серийный номер метки времени TSA. |
| `chainTxId` | string | Нет | Идентификатор транзакции в блокчейне. |

### Ответ

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

## Коды ошибок

| Код | HTTP | Значение |
| --- | --- | --- |
| `40101` | 401 | Подпись HMAC отсутствует или недействительна; API-ключ отозван. |
| `40103` | 401 | Отклонение временной метки превышает 5 минут, или nonce уже был использован. |
| `40301` | 403 | У организации нет активного биллингового аккаунта. |
| `40901` | 409 | `foreignContractNo` уже используется с другим телом запроса. |
| `50200` | 502 | УЦ вернул ошибку. |
| `50400` | 504 | УЦ не ответил в срок. |

---

## Рекомендуемая схема интеграции

1. Вызовите `POST /contracts` — передайте данные договора и `foreignSignUrl`.
2. Дождитесь перехода в `SENT` (опрашивайте `GET /contracts/{requestId}`, не злоупотребляя `?fresh=true`).
3. Направьте подписанта по активной ссылке `foreignSignUrl`.
4. Если договор нужно отменить — вызовите `POST .../revoke` до подписания.
5. После подписания казахстанской стороной — вызовите `POST .../sign-complete` с доказательной базой.
6. Сверку записей ведите по паре `requestId` + `foreignContractNo`.

---

> **Нужна помощь?** Создайте тикет в разделе [Поддержка](https://console.cloud-native.kz/support) или напишите на <cns-support@fcd.kz>.
