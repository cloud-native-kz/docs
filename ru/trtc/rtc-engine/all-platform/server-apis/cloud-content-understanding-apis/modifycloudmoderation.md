# ModifyCloudModeration

## 1. Описание API

Доменное имя для запроса API: trtc.intl.tencentcloudapi.com.

Этот API используется для обновления списка блокировок и списка разрешений после успешного запуска задачи облачной модерации.

Для этого API можно инициировать максимум 20 запросов в секунду.

Мы рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет набор возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просмотреть запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/647/34263).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение для этого API: ModifyCloudModeration. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение для этого API: 2019-07-22. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Дополнительную информацию см. в [списке регионов](https://www.tencentcloud.com/document/api/647/34263#region-list), поддерживаемых продуктом. Этот API поддерживает только: ap-singapore. |
| SdkAppId | Да | Integer | SDKAppId сервиса TRTC, который совпадает с SDKAppId, соответствующим комнате TRTC. |
| TaskId | Да | String | Уникальный идентификатор задачи модерации, возвращаемый после запуска задачи. |
| SubscribeStreamUserIds | Нет | [SubscribeStreamUserIds](https://www.tencentcloud.com/document/api/647/36760#SubscribeStreamUserIds) | Указывает список разрешений или список блокировок для потока подписки. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TaskId | String | Уникальный идентификатор задачи модерации, возвращаемый после запуска задачи. |
| RequestId | String | Уникальный идентификатор запроса, генерируемый сервером и возвращаемый для каждого запроса (если запрос не достигнет сервера по другим причинам, RequestId не будет получен). RequestId требуется для локализации проблемы. |

## 4. Пример

### Пример 1. Изменение задач облачной модерации

#### Пример входного значения

```
POST / HTTP/1.1
Host: trtc.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: ModifyCloudModeration
<Common request parameters>

{
    "SdkAppId": 20010806,
    "TaskId": "-nHwQ8NU7t7Ps1bc3MXN7wTw1-BZVg7bbhyXLoK-mumNM6KipeAYnB3iUGIpBL-ajrCF-pd2AQ..",
    "SubscribeStreamUserIds": {
        "SubscribeAudioUserIds": [
            "user1"
        ]
    }
}
```

#### Пример выходного значения

```json
{
    "Response": {
        "RequestId": "b4d09681-4413-4f21-972d-bba98422aa30",
        "TaskId": "-nHwQ8NU7t7Ps1bc3MXN7wTw1-BZVg7bbhyXLoK-mumNM6KipeAYnB3iUGIpBL-ajrCF-pd2AQ.."
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

Ниже приводятся только коды ошибок, связанные с бизнес-логикой API. Для получения других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/647/34270#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| AuthFailure | Ошибка подписи/аутентификации CAM. |
| AuthFailure.UnRealNameAuthenticated | Проверка личности не завершена, поэтому эта операция не разрешена. |
| AuthFailure.UnauthorizedOperation | Ошибка аутентификации CAM. |
| AuthFailure.UnsupportedOperation | Неподдерживаемая операция. |
| FailedOperation | Операция не удалась. |
| FailedOperation.CSUnsupportMethod | Метод облачной нарезки не поддерживается. |
| InternalError.CSInternalError | Внутренняя ошибка сервиса облачной нарезки. |
| InvalidParameter.OutOfRange | Значение параметра выходит за допустимый диапазон. |
| MissingParameter.RoomId | Отсутствует `RoomId`. |
| MissingParameter.SdkAppId | Отсутствует `SdkAppId`. |
| MissingParameter.TaskId | Отсутствует параметр `TaskId`. |
| MissingParameter.UserId | Отсутствует параметр `UserId`. |
| ResourceNotFound | Ресурс не существует. |


---
*Источник: [https://trtc.io/document/72645](https://trtc.io/document/72645)*

---
*Источник (EN): [modifycloudmoderation.md](./modifycloudmoderation.md)*
