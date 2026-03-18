# DescribeLiveCerts

## 1. Описание API

Доменное имя для запроса API: live.tencentcloudapi.com.

Этот API используется для получения списка информации о сертификатах.

Максимум 500 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет набор возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

В следующем списке параметров запроса указаны только параметры запроса API и некоторые распространённые параметры. Полный список общих параметров см. в [Общих параметрах запроса](https://intl.cloud.tencent.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: DescribeLiveCerts. |
| Version | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Этот параметр не требуется для этого API. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| CertInfoSet | Array of [CertInfo](https://intl.cloud.tencent.com/document/api/267/30767#CertInfo) | Список информации о сертификатах. |
| RequestId | String | Уникальный ID запроса, возвращается для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Примеры

### Пример 1 Пример запроса

#### Пример входных данных

```
https://live.tencentcloudapi.com/?Action=DescribeLiveCerts
&<Common request parameters>
```

#### Пример выходных данных

```
{
    "Response": {
        "CertInfoSet": [
            {
                "CertId": 1000,
                "CertName": "testName",
                "Description": "testDesc",
                "CreateTime": "2018-11-30T15:50:12Z",
                "HttpsCrt": "xxx",
                "CertType": 0,
                "CertExpireTime": "2018-12-30T15:50:12Z",
                "DomainList": [
                    "5000.livepush.play.com"
                ]
            }
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

## 5. Ресурсы разработчика

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, что облегчает вызов API.

Tencent Cloud SDK 3.0 для Python
Tencent Cloud SDK 3.0 для Java
Tencent Cloud SDK 3.0 для PHP
Tencent Cloud SDK 3.0 для Go
Tencent Cloud SDK 3.0 для Node.js
Tencent Cloud SDK 3.0 для .NET
Tencent Cloud SDK 3.0 для C++

### Командная строка

Tencent Cloud CLI 3.0

## 6. Коды ошибок

Ниже перечислены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://intl.cloud.tencent.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvokeVideoApiFail | Произошло исключение при работе с API VOD. |
| InternalError | Внутренняя ошибка. |
| InvalidParameter | Неверный параметр. |
| InvalidParameterValue | Неверное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.CrtDomainNotFound | Сертификат не найден. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Служба приостановлена. |
| ResourceNotFound.StopService | Служба была приостановлена из-за задолженности по счёту. Пожалуйста, пополните счёт до положительного баланса, чтобы активировать службу. |
| ResourceNotFound.UserDisableService | Вы отключили службу. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30778](https://www.tencentcloud.com/document/product/267/30778)*

---
*Источник (EN): [describelivecerts.md](./describelivecerts.md)*
