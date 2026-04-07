# ModifyCloudSliceTask

## 1. Описание API

Доменное имя для запроса API: trtc.intl.tencentcloudapi.com.

Этот API используется для обновления задачи нарезки после её запуска. Его можно использовать для обновления списка разрешённых или запрещённых адресов для указанного потока подписки.

Максимум 20 запросов к этому API могут быть инициированы в секунду.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет набор возможностей, включая онлайн-вызовы, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет просмотреть запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса предоставляет только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/647/34263).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение для этого API: ModifyCloudSliceTask. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение для этого API: 2019-07-22. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Дополнительную информацию см. в [списке поддерживаемых регионов](https://www.tencentcloud.com/document/api/647/34263#region-list). Этот API поддерживает только: ap-singapore, eu-frankfurt. |
| SdkAppId | Да | Integer | SDKAppId TRTC, совпадающий с SDKAppId, соответствующим комнате TRTC. |
| TaskId | Да | String | Уникальный идентификатор задачи нарезки, возвращаемый после запуска задачи. |
| SubscribeStreamUserIds | Нет | [SubscribeStreamUserIds](https://www.tencentcloud.com/document/api/647/36760#SubscribeStreamUserIds) | Задаёт список разрешённых или запрещённых адресов для потока подписки. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TaskId | String | Уникальный идентификатор задачи нарезки, возвращаемый после запуска задачи. |
| RequestId | String | Уникальный идентификатор запроса, генерируемый сервером, будет возвращён для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId необходим для устранения проблем. |

## 4. Пример

### Пример 1: Изменение задачи облачной нарезки

#### Пример входных данных

```
POST / HTTP/1.1
Host: trtc.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: ModifyCloudSliceTask
<Common request parameters>

{
    "SdkAppId": 20010806,
    "TaskId": "-nHwQ8NU7t7Ps1bc3MXN7wTw1-BZVg7bbhyXLoK-mumNM6KipeAYnB3iUGIpBL-ajrCF-pd2AQ..",
    "SubscribeStreamUserIds": {
        "SubscribeAudioUserIds": [
            "555"
        ]
    }
}
```

#### Пример выходных данных

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

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, чтобы облегчить вам вызов API.

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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/647/34270#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| AuthFailure | Ошибка подписи CAM/аутентификации. |
| AuthFailure.UnRealNameAuthenticated | Проверка личности не завершена, поэтому эта операция не разрешена. |
| AuthFailure.UnauthorizedOperation | Ошибка аутентификации CAM. |
| AuthFailure.UnsupportedOperation | Неподдерживаемая операция. |
| FailedOperation | Операция не выполнена. |
| FailedOperation.CSUnsupportMethod | Метод облачной нарезки не поддерживается. |
| InternalError.CSInternalError | Внутренняя ошибка сервиса облачной нарезки. |
| InvalidParameter.OutOfRange | Значение параметра выходит за допустимый диапазон. |
| MissingParameter.RoomId | `RoomId` отсутствует. |
| MissingParameter.SdkAppId | `SdkAppId` отсутствует. |
| MissingParameter.TaskId | Параметр `TaskId` отсутствует. |
| MissingParameter.UserId | Параметр `UserId` отсутствует. |
| ResourceNotFound | Ресурс не найден. |


---
*Источник: [https://trtc.io/document/72328](https://trtc.io/document/72328)*

---
*Источник (EN): [modifycloudslicetask.md](./modifycloudslicetask.md)*
