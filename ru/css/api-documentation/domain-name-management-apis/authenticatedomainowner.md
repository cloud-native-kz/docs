# AuthenticateDomainOwner

## 1. Описание API

Доменное имя для запроса API: live.tencentcloudapi.com.

Этот API используется для проверки принадлежности домена.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем вам использовать API Explorer

Попробуйте

API Explorer предоставляет набор возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просмотреть запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Приведенный ниже список параметров запроса включает только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://intl.cloud.tencent.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: AuthenticateDomainOwner. |
| Version | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| DomainName | Да | String | Доменное имя для проверки. |
| VerifyType | Да | String | Тип проверки. Допустимые значения: dnsCheck: Немедленно проверить, был ли успешно добавлен записи DNS проверки. Если да, записать этот результат проверки. fileCheck: Немедленно проверить, был ли успешно загружен файл проверки HTML. Если да, записать этот результат проверки. dbCheck: Проверить, был ли домен уже успешно проверен. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Content | String | Проверенное содержимое. Если `VerifyType` имеет значение `dnsCheck`, это запись TXT, которую следует добавить для проверки. Если `VerifyType` имеет значение `fileCheck`, это файл, который следует загрузить для проверки. |
| Status | Integer | Статус проверки. Если значение этого параметра больше или равно 0, домен был проверен. Если значение этого параметра меньше 0, домен не был проверен. |
| MainDomain | String | Основной домен проверенного домена. Проверка не требуется, если другой домен в рамках того же основного домена был успешно проверен. |
| RequestId | String | Уникальный идентификатор запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1 Пример запроса

#### Пример входных данных

```
POST / HTTP/1.1
Host: live.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: AuthenticateDomainOwner
<Common request parameters>

{
    "VerifyType": "dnsCheck",
    "DomainName": "akxynt.cn"
}
```

#### Пример выходных данных

```
{
    "Response": {
        "Content": "cssauth_da06159efa92c365182ba5d453a7b65b",
        "MainDomain": "akxynt.cn",
        "RequestId": "20a9d1c1-7b2a-48b5-9a78-c0bccab3dfb6",
        "Status": 0
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, чтобы упростить для вас вызов API.

Tencent Cloud SDK 3.0 для Python
Tencent Cloud SDK 3.0 для Java
Tencent Cloud SDK 3.0 для PHP
Tencent Cloud SDK 3.0 для Go
Tencent Cloud SDK 3.0 для Node.js
Tencent Cloud SDK 3.0 для .NET
Tencent Cloud SDK 3.0 для C++

### Интерфейс командной строки

Tencent Cloud CLI 3.0

## 6. Коды ошибок

Приведенный ниже список содержит только коды ошибок, связанные с бизнес-логикой API. Информацию о других кодах ошибок см. в разделе [Общие коды ошибок](https://intl.cloud.tencent.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation | Операция не удалась. |
| InvalidParameter | Недействительный параметр. |
| InvalidParameter.DomainFormatError | Неверный формат доменного имени. Пожалуйста, введите допустимый. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/50612](https://www.tencentcloud.com/document/product/267/50612)*

---
*Источник (EN): [authenticatedomainowner.md](./authenticatedomainowner.md)*
