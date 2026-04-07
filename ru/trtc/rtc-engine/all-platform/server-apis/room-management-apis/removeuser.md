# RemoveUser

## 1. Описание API

Имя домена для запроса API: trtc.intl.tencentcloudapi.com.

Этот API используется для удаления пользователя из комнаты. Применяется в сценариях, когда якорь, владелец комнаты или администратор хочет исключить пользователя. Поддерживает все платформы. Для Android, iOS, Windows и macOS требуется обновление TRTC SDK до версии v6.6 или выше.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуется использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Позволяет просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/647/34263).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение для этого API: RemoveUser. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение для этого API: 2019-07-22. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Дополнительную информацию см. в [списке регионов](https://www.tencentcloud.com/document/api/647/34263#region-list), поддерживаемых продуктом. Этот API поддерживает только: ap-beijing, ap-guangzhou, ap-singapore. |
| SdkAppId | Да | Integer | `SDKAppId` TRTC. |
| RoomId | Да | Integer | Номер комнаты. |
| UserIds.N | Да | Array of String | Список до 10 пользователей, которые будут удалены. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный идентификатор запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1. Удаление пользователей из комнаты

Этот пример показывает, как удалить пользователей `test1` и `test2` из комнаты `1234`.

#### Пример входных данных

```
https://trtc.intl.tencentcloudapi.com/?Action=RemoveUser
&SdkAppId=1400000001
&RoomId=1234
&UserIds.0=test1
&UserIds.1=test2
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, что облегчает вызов API.

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

Ниже перечислены только коды ошибок, относящиеся к бизнес-логике API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/647/34270#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.RoomNotExist | Комната не существует. |
| InternalError | Внутренняя ошибка. |
| InternalError.GetRoomCacheIpError | Ошибка при запросе информации о комнате. |
| InternalError.GetRoomFromCacheError | Ошибка при получении информации о комнате. |
| InvalidParameter.RoomId | `RoomId` некорректен. |
| InvalidParameter.SdkAppId | `SdkAppId` некорректен. |
| InvalidParameter.UserIds | `UserIds` некорректен. |
| InvalidParameterValue.RoomId | Неверное значение RoomId. |
| MissingParameter.RoomId | `RoomId` отсутствует. |
| MissingParameter.SdkAppId | `SdkAppId` отсутствует. |
| MissingParameter.UserIds | `UserIds` отсутствует. |
| UnauthorizedOperation.SdkAppId | Нет разрешения на манипулирование `SdkAppId`. |


---
*Источник: [https://trtc.io/document/34268](https://trtc.io/document/34268)*

---
*Источник (EN): [removeuser.md](./removeuser.md)*
