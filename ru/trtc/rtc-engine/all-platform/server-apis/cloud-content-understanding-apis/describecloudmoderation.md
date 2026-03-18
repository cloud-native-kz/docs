# DescribeCloudModeration

## 1. Описание API

Доменное имя для запроса API: trtc.intl.tencentcloudapi.com.

Этот API используется для запроса статуса задачи модерации и информации о списке блокировки и списке разрешений подписки после запуска задачи. Действителен только при выполнении задачи. Если задача завершена, будет возвращена ошибка.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет набор возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/647/34263).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение для этого API: DescribeCloudModeration. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение для этого API: 2019-07-22. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Дополнительные сведения см. в [списке поддерживаемых регионов](https://www.tencentcloud.com/document/api/647/34263#region-list). Этот API поддерживает только: ap-singapore. |
| SdkAppId | Да | Integer | SDKAppId TRTC, который совпадает с SDKAppId, соответствующим комнате записи. |
| TaskId | Да | String | Уникальный идентификатор задачи облачной модерации, возвращаемый после запуска задачи. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TaskId | String | Уникальный идентификатор задачи модерации, возвращаемый после запуска задачи. |
| Status | String | Информация о статусе задачи облачной модерации. Idle: указывает на то, что текущая задача неактивна; InProgress: указывает на то, что текущая задача выполняется; Exited: указывает на то, что текущая задача завершается. |
| SubscribeStreamUserIds | [SubscribeModerationUserIds](https://www.tencentcloud.com/document/api/647/36760#SubscribeModerationUserIds) | Список блокировки и список разрешений подписки. |
| RequestId | String | Уникальный идентификатор запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, RequestId не будет получен). RequestId требуется для поиска проблемы. |

## 4. Пример

### Пример 1. Запрос информации о задачах облачной модерации

#### Пример входных данных

```
POST / HTTP/1.1
Host: xxx.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeCloudModeration
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
        "TaskId": "-npVoIhU7nVF+0aF9cAU08H4y253LKPbBX+UIoK-4pycoZWQndibGOPu9klhRT7bEDv5XoewCQE.",
        "Status": "InProgress",
        "RequestId": "uis_mock",
        "SubscribeStreamUserIds": {
            "SubscribeAudioUserIds": [],
            "UnSubscribeAudioUserIds": [],
            "SubscribeVideoUserIds": [],
            "UnSubscribeVideoUserIds": []
        }
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, для упрощения вызова API.

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

Ниже приведены только коды ошибок, связанные с логикой API. Информацию о других кодах ошибок см. в разделе [Общие коды ошибок](https://www.tencentcloud.com/document/api/647/34270#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| AuthFailure | Ошибка подписи CAM/аутентификации. |
| AuthFailure.UnRealNameAuthenticated | Проверка личности не завершена, поэтому эта операция не разрешена. |
| AuthFailure.UnauthorizedOperation | Ошибка аутентификации CAM. |
| AuthFailure.UnsupportedOperation | Неподдерживаемая операция. |
| FailedOperation | Операция не выполнена. |
| FailedOperation.CSUnsupportMethod | Метод облачного нарезания не поддерживается. |
| InternalError.CSInternalError | Возникла внутренняя ошибка сервиса облачного нарезания. |
| InvalidParameter.OutOfRange | Значение параметра выходит за пределы допустимого диапазона. |
| InvalidParameter.SdkAppId | `SdkAppId` неверен. |
| MissingParameter.RoomId | Отсутствует `RoomId`. |
| MissingParameter.SdkAppId | Отсутствует `SdkAppId`. |
| MissingParameter.TaskId | Отсутствует параметр `TaskId`. |
| MissingParameter.UserId | Отсутствует параметр `UserId`. |
| ResourceNotFound | Ресурс не найден. |


---
*Источник: [https://trtc.io/document/72646](https://trtc.io/document/72646)*

---
*Источник (EN): [describecloudmoderation.md](./describecloudmoderation.md)*
