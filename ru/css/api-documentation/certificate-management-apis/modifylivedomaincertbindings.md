# ModifyLiveDomainCertBindings

## 1. Описание API

Доменное имя для запроса API: live.tencentcloudapi.com.

Этот API используется для привязки сертификата к нескольким доменам воспроизведения и обновления конфигурации HTTPS для этих доменов.
Если используется собственный сертификат, он будет автоматически загружен в SSL Certificate Service Tencent Cloud.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет множество возможностей, включая онлайн-вызовы, проверку подписи, генерацию кода SDK и быстрый поиск API. Это позволяет просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://intl.cloud.tencent.com/document/api/267/30763).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: ModifyLiveDomainCertBindings. |
| Version | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| DomainInfos.N | Да | Array of [LiveCertDomainInfo](https://intl.cloud.tencent.com/document/api/267/30767#LiveCertDomainInfo) | Домены воспроизведения для привязки и включение ли HTTPS для них. |
| CloudCertId | Нет | String | ID SSL-сертификата, назначенный Tencent Cloud. Подробнее см. https://intl.cloud.tencent.com/document/api/400/41665?from_cn_redirect=1 |
| CertificatePublicKey | Нет | String | Открытый ключ сертификата. Можно указать либо `CloudCertId`, либо открытый/закрытый ключ. Если указаны оба, параметры закрытого и открытого ключа будут проигнорированы. Если передать только открытый и закрытый ключи, соответствующий сертификат будет загружен в SSL Certificate Service Tencent Cloud, который создаст `CloudCertId` для сертификата. |
| CertificatePrivateKey | Нет | String | Закрытый ключ сертификата. Можно указать либо `CloudCertId`, либо открытый/закрытый ключ. Если указаны оба, параметры закрытого и открытого ключа будут проигнорированы. Если передать только открытый и закрытый ключи, соответствующий сертификат будет загружен в SSL Certificate Service Tencent Cloud, который создаст `CloudCertId` для сертификата. |
| CertificateAlias | Нет | String | Примечания для сертификата в SSL Certificate Service Tencent Cloud. Этот параметр будет проигнорирован, если указан `CloudCertId`. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| MismatchedDomainNames | Array of String | Домены, пропущенные из-за несоответствия сертификата. |
| Errors | Array of [BatchDomainOperateErrors](https://intl.cloud.tencent.com/document/api/267/30767#BatchDomainOperateErrors) | Домены, для которых API не смог выполнить привязку, включая те, что находятся в `MismatchedDomainNames`, и информацию об ошибках. Примечание: это поле может возвращать null, указывая, что значения не получены. |
| RequestId | String | Уникальный ID запроса, возвращаемый для каждого запроса. RequestId требуется для поиска проблемы. |

## 4. Пример

### Пример 1 Пример запроса

#### Пример входных данных

```
POST / HTTP/1.1
Host: live.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: ModifyLiveDomainCertBindings
<Common request parameters>

{
    "CloudCertId": "hZy2N9vF",
    "DomainInfos": [
        {
            "DomainName": "abc.tst.com.cn",
            "Status": 1
        }
    ]
}
```

#### Пример выходных данных

```
{
    "Response": {
        "RequestId": "cb91d382-e9be-4688-9008-d57088271b5f",
        "MismatchedDomainNames": [],
        "Errors": []
    }
}
```

## 5. Ресурсы разработчика

### SDK

TencentCloud API 3.0 интегрирует SDK для различных языков программирования, что упрощает вызовы API.

Tencent Cloud SDK 3.0 for Python
Tencent Cloud SDK 3.0 for Java
Tencent Cloud SDK 3.0 for PHP
Tencent Cloud SDK 3.0 for Go
Tencent Cloud SDK 3.0 for Node.js
Tencent Cloud SDK 3.0 for .NET
Tencent Cloud SDK 3.0 for C++

### Интерфейс командной строки

Tencent Cloud CLI 3.0

## 6. Коды ошибок

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://intl.cloud.tencent.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation | Операция не удалась. |
| FailedOperation.AuthError | У вас нет прав для выполнения этой операции. |
| FailedOperation.CannotBeDeletedIssued | Не удалось удалить сертификат, так как он был выдан. |
| FailedOperation.CannotBeDeletedWithinHour | Бесплатные сертификаты не могут быть удалены в течение одного часа после подачи заявки. |
| FailedOperation.CertificateExists | Сертификат уже существует. |
| FailedOperation.CertificateInvalid | Сертификат недействителен. |
| FailedOperation.CertificateMismatch | Сертификат и закрытый ключ не совпадают. |
| FailedOperation.CertificateNotFound | Сертификат не существует. |
| FailedOperation.ConfigCDNFailed | Ошибка конфигурации CDN. |
| FailedOperation.ExceedsFreeLimit | Превышено ограничение на количество бесплатных сертификатов. |
| FailedOperation.InvalidCertificateStatusCode | Неверное состояние сертификата. |
| FailedOperation.InvalidParam | Неверный параметр. |
| FailedOperation.NetworkError | Система CA занята. Повторите попытку позже. |
| FailedOperation.NoProjectPermission | У вас нет прав для работы с этим проектом. |
| FailedOperation.NoRealNameAuth | Вы не завершили проверку личности. |
| InternalError | Внутренняя ошибка. |
| InternalError.ConnectDbError | Ошибка подключения к базе данных. |
| InternalError.CrtDateInUsing | Сертификат используется. |
| InternalError.CrtDateNotFound | Сертификат не существует. |
| InternalError.CrtDateNotLegal | Сертификат недействителен. |
| InternalError.CrtDateOverdue | Сертификат истек. |
| InternalError.CrtDomainNotFound | Нет связанного доменного имени. |
| InternalError.CrtKeyNotMatch | Ключ сертификата не совпадает. |
| InternalError.DBError | Ошибка выполнения DB. |
| InternalError.NetworkError | Внутренняя ошибка сети. |
| InvalidParameter | Неверный параметр. |
| InvalidParameter.CloudCrtIdError | Неверный ID сертификата, размещенного в Tencent Cloud. |
| InvalidParameter.CrtDateInUsing | Сертификат используется. |
| InvalidParameter.CrtDateNotFound | Сертификат не существует. |
| InvalidParameter.CrtDateNotLegal | Сертификат недействителен. |
| InvalidParameter.CrtDateOverdue | Сертификат истек. |
| InvalidParameter.CrtDomainNotFound | Не удалось найти домен. |
| InvalidParameter.CrtKeyNotMatch | Ключ сертификата не совпадает. |
| InvalidParameter.CrtOrKeyNotExist | Содержимое сертификата или закрытый ключ не были предоставлены. |
| LimitExceeded.RateLimitExceeded | Достигнут лимит частоты запросов API. |
| ResourceNotFound.CrtDateNotFound | Сертификат не существует. |
| ResourceNotFound.CrtDomainNotFound | Сертификат не найден. |
| ResourceNotFound.DomainNotExist | Доменное имя не существует или не совпадает. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.StopService | Сервис был приостановлен из-за задолженности по счету. Пополните счет до положительного баланса, чтобы сначала активировать сервис. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/49644](https://www.tencentcloud.com/document/product/267/49644)*

---
*Источник (EN): [modifylivedomaincertbindings.md](./modifylivedomaincertbindings.md)*
