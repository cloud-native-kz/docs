# SetUserBlockedByStrRoomId

## 1. Описание API

Доменное имя для запроса API: trtc.intl.tencentcloudapi.com.

Этот API позволяет ведущему, владельцу комнаты или администратору отключать/включать звук у пользователя. Может использоваться на платформах Android, iOS, Windows, macOS, веб и WeChat Mini Program. Используйте этот API, когда ID комнаты является строкой.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет множество возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет просматривать запрос, ответ и автоматически генерируемые примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/647/34263).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: SetUserBlockedByStrRoomId. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: 2019-07-22. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Дополнительные сведения см. в [списке поддерживаемых регионов](https://www.tencentcloud.com/document/api/647/34263#region-list) продукта. Этот API поддерживает только: ap-beijing, ap-guangzhou, ap-singapore. |
| SdkAppId | Да | Integer | ID приложения. |
| StrRoomId | Да | String | ID комнаты (строка). |
| UserId | Да | String | ID пользователя. |
| IsMute | Да | Integer | Управляет состоянием активации аудио и видео. 0: Включить аудио и видео, 1: Отключить аудио и видео, 2: Отключить только аудио, 3: Отключить только видео. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, RequestId не будет получен). RequestId необходим для определения проблемы. |

## 4. Примеры

### Пример 1. Отключение аудио и видео пользователя (ID комнаты типа string)

#### Пример входных данных

```
https://trtc.intl.tencentcloudapi.com/?Action=SetUserBlockedByStrRoomId
&SdkAppId=1400188366
&StrRoomId="10006"
&UserId="29376"
&IsMute=1
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "44e494f6-8010-4bb2-9a9d-ba5fd191353a"
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

Ниже приведены только коды ошибок, связанные с деловой логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/647/34270#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.RoomNotExist | Комната не существует. |
| FailedOperation.SdkAppIdNotExist | ID приложения не существует. |
| FailedOperation.UserNotExist | Пользователь не находится в комнате. |
| InternalError | Внутренняя ошибка. |
| InvalidParameter | Ошибка параметра. |
| InvalidParameter.RoomId | `RoomId` некорректен. |
| InvalidParameter.SdkAppId | `SdkAppId` некорректен. |
| InvalidParameter.UserId | Некорректный `UserId`. |
| MissingParameter | Отсутствует параметр. |
| MissingParameter.AppId | Отсутствует `AppId`. |
| MissingParameter.RoomId | Отсутствует `RoomId`. |
| MissingParameter.SdkAppId | Отсутствует `SdkAppId`. |
| MissingParameter.UserId | Отсутствует параметр `UserId`. |
| UnauthorizedOperation.SdkAppId | Нет прав на манипулирование `SdkAppId`. |


---
*Источник: [https://trtc.io/document/51288](https://trtc.io/document/51288)*

---
*Источник (EN): [setuserblockedbystrroomid.md](./setuserblockedbystrroomid.md)*
