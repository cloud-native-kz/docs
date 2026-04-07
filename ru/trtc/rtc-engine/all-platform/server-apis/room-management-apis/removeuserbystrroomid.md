# RemoveUserByStrRoomId

## 1. Описание API

Доменное имя для запроса API: trtc.intl.tencentcloudapi.com.

Этот API используется для удаления пользователя из комнаты. Позволяет ведущему, владельцу комнаты или администратору исключить пользователя и работает на всех платформах. Для Android, iOS, Windows и macOS необходимо обновить TRTC SDK до версии 6.6 или выше.

Максимально 20 запросов можно инициировать в секунду для этого API.

Рекомендуем вам использовать API Explorer

Попробовать

API Explorer предоставляет множество возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

В следующем списке параметров запроса указаны только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/647/34263).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: RemoveUserByStrRoomId. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: 2019-07-22. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Дополнительную информацию см. в разделе [список регионов](https://www.tencentcloud.com/document/api/647/34263#region-list), поддерживаемых продуктом. Этот API поддерживает только: ap-beijing, ap-guangzhou, ap-singapore. |
| SdkAppId | Да | Integer | `SDKAppId` TRTC |
| RoomId | Да | String | ID комнаты |
| UserIds.N | Да | Array of String | Список до 10 пользователей, которых необходимо удалить |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, RequestId не будет получен). RequestId требуется для локализации проблемы. |

## 4. Примеры

### Пример 1. Удаление пользователей из комнаты

Этот пример показывает, как удалить пользователей `test1` и `test2` из комнаты `abcd`.

#### Пример входных данных

```
https://trtc.intl.tencentcloudapi.com/?Action=RemoveUserByStrRoomId
&SdkAppId=1400000001
&RoomId=abcd
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

Ниже приведены только коды ошибок, относящиеся к бизнес-логике API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/647/34270#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.RoomNotExist | Комната не существует. |
| InternalError | Внутренняя ошибка. |
| InternalError.GetRoomCacheIpError | Ошибка при запросе информации о комнате. |
| InvalidParameter.RoomId | `RoomId` некорректен. |
| InvalidParameter.SdkAppId | `SdkAppId` некорректен. |
| InvalidParameter.UserIds | `UserIds` некорректен. |
| InvalidParameterValue.RoomId | Недействительный RoomId. |
| MissingParameter.RoomId | `RoomId` отсутствует. |
| MissingParameter.SdkAppId | `SdkAppId` отсутствует. |
| MissingParameter.UserIds | `UserIds` отсутствует. |
| UnauthorizedOperation.SdkAppId | Нет разрешения на манипулирование `SdkAppId`. |


---
*Источник: [https://trtc.io/document/39630](https://trtc.io/document/39630)*

---
*Источник (EN): [removeuserbystrroomid.md](./removeuserbystrroomid.md)*
