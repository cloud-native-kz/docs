# DescribeSchedules

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для запроса схемы.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Требуется | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: DescribeSchedules. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| ScheduleIds.N | Нет | Array of Integer | Идентификаторы запрашиваемых схем. Ограничение длины массива: 100. |
| TriggerType | Нет | String | Тип триггера. Допустимые значения: `CosFileUpload`: схема срабатывает при загрузке файла в Tencent Cloud Object Storage (COS).`AwsS3FileUpload`: схема срабатывает при загрузке файла в AWS S3. Если не указан этот параметр или оставлен пустым, будут возвращены все схемы независимо от типа триггера. |
| Status | Нет | String | Статус схемы. Допустимые значения: `Enabled``Disabled` Если не указан этот параметр, будут возвращены все схемы независимо от статуса. |
| Offset | Нет | Integer | Смещение для постраничной разбивки. Значение по умолчанию: 0. |
| Limit | Нет | Integer | Максимальное количество возвращаемых записей. Значение по умолчанию: 10. Максимальное значение: 100. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TotalCount | Integer | Общее количество записей, соответствующих условиям. |
| ScheduleInfoSet | Array of [SchedulesInfo](https://www.tencentcloud.com/document/api/1041/33690#SchedulesInfo) | Информация о схемах. |
| RequestId | String | Уникальный идентификатор запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для выявления проблемы. |

## 4. Пример

### Пример1 Запрос схемы

Этот пример показывает, как запросить схему с идентификатором `0`.

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeSchedules
<Common request parameters>

{
    "ScheduleIds": [
        0
    ]
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "TotalCount": 0,
        "ScheduleInfoSet": [],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, что упрощает вызов API.

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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.GenerateResource | Ошибка при создании ресурса. |
| FailedOperation.InvalidMpsUser | Ошибка операции: несанкционированный пользователь MPS. |
| FailedOperation.InvalidUser | Ошибка операции: недействительный пользователь. |
| InternalError | Внутренняя ошибка. |
| InternalError.AccessDBError | Ошибка данных. |
| InvalidParameter | Ошибка параметра. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/54033](https://www.tencentcloud.com/document/product/1041/54033)*

---
*Источник (EN): [describeschedules.md](./describeschedules.md)*
