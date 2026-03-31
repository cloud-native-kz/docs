# ModifyCloudRecording

## 1. Описание API

Доменное имя для запроса API: trtc.intl.tencentcloudapi.com.

Этот API используется для изменения задачи записи. Он работает только когда задача выполняется. Если задача уже завершена при вызове этого API, будет возвращена ошибка. Для каждого запроса необходимо указать все параметры, а не только те, которые требуется изменить.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуется использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызовы, проверку подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просмотреть запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в [Общих параметрах запроса](https://www.tencentcloud.com/document/api/647/34263).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение для этого API: ModifyCloudRecording. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение для этого API: 2019-07-22. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Дополнительную информацию см. в [списке регионов](https://www.tencentcloud.com/document/api/647/34263#region-list), поддерживаемых продуктом. Этот API поддерживает только: ap-beijing, ap-guangzhou, ap-mumbai, ap-shanghai, ap-singapore. |
| SdkAppId | Да | Integer | `SDKAppID` комнаты, потоки которой записываются. |
| TaskId | Да | String | Уникальный ID задачи записи, который возвращается после успешного начала записи. |
| MixLayoutParams | Нет | [MixLayoutParams](https://www.tencentcloud.com/document/api/647/36760#MixLayoutParams) | Новая раскладка смешивания потоков. |
| SubscribeStreamUserIds | Нет | [SubscribeStreamUserIds](https://www.tencentcloud.com/document/api/647/36760#SubscribeStreamUserIds) | Белый список/чёрный список для подписки на потоки. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TaskId | String | ID задачи, назначенный сервисом записи, который уникально идентифицирует процесс записи и становится недействительным после окончания задачи записи. |
| RequestId | String | Уникальный ID запроса, созданный сервером, будет возвращен для каждого запроса (если запрос не достигает сервер по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Примеры

### Пример 1. Изменение задачи облачной записи

Этот пример показывает, как подписаться на видео и аудиопотоки пользователей 123 и 456 и настроить раскладку для задачи записи с ID задачи xx приложения, `SDKAppID` которого равен `1234`.

#### Пример входных данных

```
POST / HTTP/1.1
Host: trtc.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: ModifyCloudRecording
<Common request parameters>

{
    "SubscribeStreamUserIds": {
        "SubscribeVideoUserIds": [
            "123",
            "456"
        ],
        "SubscribeAudioUserIds": [
            "123",
            "456"
        ]
    },
    "TaskId": "xx",
    "SdkAppId": 1234,
    "MixLayoutParams": {
        "MixLayoutMode": 4,
        "MixLayoutList": [
            {
                "Top": 100,
                "UserId": "123",
                "Height": 100,
                "Width": 100,
                "Left": 100
            },
            {
                "Top": 200,
                "UserId": "456",
                "Height": 100,
                "Width": 100,
                "Left": 200
            }
        ]
    }
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "TaskId": "5df46eb2-8e4b-490e-9c3c-dbd3b84faefc",
        "RequestId": "71993312-6ab8-4768-9124-118e0a20c45f"
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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/647/34270#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| AuthFailure | Ошибка подписи CAM/аутентификации. |
| AuthFailure.UnRealNameAuthenticated | Проверка личности не завершена, поэтому эта операция не разрешена. |
| AuthFailure.UnauthorizedOperation | Ошибка аутентификации CAM. |
| AuthFailure.UnsupportedOperation | Неподдерживаемая операция. |
| FailedOperation | Операция не выполнена. |
| FailedOperation.CRUnsupportMethod | Неподдерживаемый метод облачной записи. |
| InternalError.CRInternalError | Внутренняя ошибка облачной записи. |
| InvalidParameter.OutOfRange | Значение параметра выходит за допустимый диапазон. |
| MissingParameter.RoomId | `RoomId` отсутствует. |
| MissingParameter.SdkAppId | `SdkAppId` отсутствует. |
| MissingParameter.TaskId | Параметр `TaskId` отсутствует. |
| MissingParameter.UserId | Параметр `UserId` отсутствует. |
| ResourceNotFound | Ресурс не найден. |


---
*Источник: [https://trtc.io/document/46957](https://trtc.io/document/46957)*

---
*Источник (EN): [modifycloudrecording.md](./modifycloudrecording.md)*
