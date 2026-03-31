# DescribeWebRecord

## 1. Описание API

Домен для запроса API: trtc.intl.tencentcloudapi.com.

Запрашивает статус задачи веб-страницы записи

Для этого API можно инициировать максимум 20 запросов в секунду.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет просмотреть запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Для полного списка общих параметров см. [Общие параметры запроса](https://www.tencentcloud.com/document/api/647/34263).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: DescribeWebRecord. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: 2019-07-22. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Для получения дополнительной информации см. [список поддерживаемых регионов](https://www.tencentcloud.com/document/api/647/34263#region-list) продукта. Этот API поддерживает только: ap-singapore. |
| TaskId | Нет | String | Идентификатор задачи, возвращаемый при запуске веб-страницы записи |
| SdkAppId | Нет | Integer | SdkAppId, передаваемый при инициировании веб-страницы записи |
| RecordId | Нет | String | RecordId, передаваемый при инициировании записи. При передаче этого значения необходимо передать SdkAppId |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Status | Integer | 1: Запись в процессе |
| TaskId | String | Возвращается при запросе с использованием RecordId |
| RecordId | String | Возвращается при запросе с использованием TaskId |
| RequestId | String | Уникальный идентификатор запроса, сгенерированный сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId необходим для выявления проблемы. |

## 4. Примеры

### Пример1 Запрашивает статус задачи веб-страницы записи

#### Пример входных данных

```
POST / HTTP/1.1
Host: trtc.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeWebRecord
<Common request parameters>

{
    "TaskId": "HMLm5HWNuUAXSb0gTEOx0z1x+nLMZNjXrY3keyUSvu7uu8mF9O656uNtbUtvaWLkpMY134jTN2Ix4vuqgOJ68nQ8tho3ri"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "Status": 1,
        "RequestId": "record_class_1"
    }
}
```

## 5. Ресурсы разработчика

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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/647/34270#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.TaskNotExist | Задача не существует. |
| InvalidParameter.TaskId | Ошибка параметра TaskId. |


---
*Источник: [https://trtc.io/document/72067](https://trtc.io/document/72067)*

---
*Источник (EN): [describewebrecord.md](./describewebrecord.md)*
