# DisableSchedule

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для отключения схемы.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет различные возможности, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически генерируемые примеры.

## 2. Входные параметры

Следующий список параметров запроса предоставляет только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в [Общих параметрах запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Требуется | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: DisableSchedule. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| ScheduleId | Да | Integer | ID схемы. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, сгенерированный сервером, будет возвращен для каждого запроса (если запрос не дойдет до сервера по другим причинам, запрос не получит RequestId). RequestId требуется для решения проблемы. |

## 4. Пример

### Пример1 Отключение схемы

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DisableSchedule
<Общие параметры запроса>

{
    "ScheduleId": 0
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, чтобы упростить вызов API.

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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation | Операция не выполнена. |
| FailedOperation.BucketNotifyAlreadyExist | Операция не выполнена: уведомление уже установлено для бакета. |
| FailedOperation.CosStatusInavlid | Операция не выполнена: служба COS приостановлена. |
| FailedOperation.GetSourceNotify | Операция не выполнена: ошибка при получении исходного уведомления. |
| FailedOperation.InvalidMpsUser | Операция не выполнена: неавторизованный пользователь MPS. |
| FailedOperation.InvalidUser | Операция не выполнена: недействительный пользователь. |
| FailedOperation.SetSourceNotify | Операция не выполнена: ошибка при установке исходного уведомления. |
| InternalError | Внутренняя ошибка. |
| InternalError.AccessDBError | Ошибка данных. |
| InvalidParameter | Ошибка параметра. |
| ResourceNotFound.CosBucketNameInvalid | Ресурс не существует: недействительное имя бакета COS. |
| ResourceNotFound.CosBucketNotExist | Ресурс не существует: бакет COS не существует. |
| ResourceNotFound.TemplateNotExist | Ресурс не существует: шаблон не существует. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/54032](https://www.tencentcloud.com/document/product/1041/54032)*

---
*Источник (EN): [disableschedule.md](./disableschedule.md)*
