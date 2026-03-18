# DescribeCloudSliceTask

## 1. Описание API

Доменное имя для запроса API: trtc.intl.tencentcloudapi.com.

Этот API используется для запроса статуса задачи нарезки после её запуска, что действительно только во время выполнения задачи. Ошибка будет возвращена, если задача завершена.

Максимум 20 запросов могут быть инициированы в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписей, генерацию кода SDK и быстрый поиск API. Он позволяет просмотреть запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Для полного списка общих параметров см. [Общие параметры запроса](https://www.tencentcloud.com/document/api/647/34263).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: DescribeCloudSliceTask. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: 2019-07-22. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Дополнительную информацию см. в [списке регионов](https://www.tencentcloud.com/document/api/647/34263#region-list), поддерживаемых продуктом. Этот API поддерживает только: ap-singapore, eu-frankfurt. |
| SdkAppId | Да | Integer | SDKAppId TRTC, который совпадает с SDKAppId, соответствующим комнате записи. |
| TaskId | Да | String | Уникальный идентификатор задачи нарезки, который возвращается после запуска задачи. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TaskId | String | Уникальный идентификатор задачи нарезки, который возвращается после запуска задачи. |
| Status | String | Информация о статусе задачи облачной нарезки. Idle: указывает, что текущая задача неактивна; InProgress: указывает, что текущая задача выполняется; Exited: указывает, что текущая задача завершается. |
| RequestId | String | Уникальный идентификатор запроса, сгенерированный сервером, будет возвращён для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для локализации проблемы. |

## 4. Пример

### Пример 1. Запрос информации о задаче нарезки

#### Пример входных данных

```
POST / HTTP/1.1
Host: xxx.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeInstances
<Common request parameters>

{
    "SdkAppId": 20010806,
    "TaskId": "-nHwQ8NU7t7Ps1bc3MXN7wTw1-BZVg7bbhyXLoK-mumNM6KipeAYnB3iUGIpBL-ajrCF-pd2AQ.."
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "dc45d9cd-f615-43a5-943e-89f559cb3f7b",
        "Status": "InProgress",
        "TaskId": "-nHwQ8NU7t7Ps1bc3MXN7wTw1-BZVg7bbhyXLoK-mumNM6KipeAYnB3iUGIpBL-ajrCF-pd2AQ.."
    }
}
```

## 5. Ресурсы разработчика

### SDK

TencentCloud API 3.0 интегрирует SDK, которые поддерживают различные языки программирования, чтобы облегчить вам вызов API.

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

Ниже приведены только коды ошибок, относящиеся к логике бизнеса API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/647/34270#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| AuthFailure | Ошибка подписи CAM или ошибка аутентификации. |
| AuthFailure.UnRealNameAuthenticated | Проверка личности не завершена, поэтому эта операция не допускается. |
| AuthFailure.UnauthorizedOperation | Ошибка аутентификации CAM. |
| AuthFailure.UnsupportedOperation | Неподдерживаемая операция. |
| FailedOperation | Операция не выполнена. |
| FailedOperation.CSUnsupportMethod | Метод облачной нарезки не поддерживается. |
| InternalError.CSInternalError | Внутренняя ошибка сервиса облачной нарезки. |
| InvalidParameter.OutOfRange | Значение параметра выходит за допустимый диапазон. |
| InvalidParameter.SdkAppId | `SdkAppId` некорректен. |
| MissingParameter.RoomId | `RoomId` отсутствует. |
| MissingParameter.SdkAppId | `SdkAppId` отсутствует. |
| MissingParameter.TaskId | Параметр `TaskId` отсутствует. |
| MissingParameter.UserId | Отсутствует параметр `UserId`. |
| ResourceNotFound | Ресурс не найден. |


---
*Источник: [https://trtc.io/document/72329](https://trtc.io/document/72329)*

---
*Источник (EN): [describecloudslicetask.md](./describecloudslicetask.md)*
