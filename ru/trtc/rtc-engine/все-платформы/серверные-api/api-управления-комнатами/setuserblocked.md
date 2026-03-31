# SetUserBlocked

## 1. Описание API

Доменное имя для запроса API: trtc.intl.tencentcloudapi.com.

Этот API используется для отключения или включения аудио и видео пользователя. Может использоваться ведущим, владельцем комнаты или администратором для блокировки или разблокировки пользователя. Поддерживает платформы Android, iOS, Windows, macOS, веб и WeChat Mini Program. Используйте этот API, если ID комнаты является числом.

Максимум 20 запросов можно инициировать в секунду для этого API.

Мы рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет широкий спектр возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Для полного списка общих параметров см. [Общие параметры запроса](https://www.tencentcloud.com/document/api/647/34263).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: SetUserBlocked. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: 2019-07-22. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Дополнительную информацию см. в [списке регионов](https://www.tencentcloud.com/document/api/647/34263#region-list), поддерживаемых продуктом. Этот API поддерживает только: ap-beijing, ap-guangzhou, ap-singapore. |
| SdkAppId | Да | Integer | ID приложения. |
| RoomId | Да | Integer | ID комнаты (число). |
| UserId | Да | String | ID пользователя. |
| IsMute | Да | Integer | Управляет состоянием активации аудио и видео. 0: включить аудио и видео, 1: отключить аудио и видео, 2: отключить только аудио, 3: отключить только видео. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, сгенерированный сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Пример

### Example1 Отключение аудио и видео пользователя

#### Пример входных данных

```
https://trtc.intl.tencentcloudapi.com/?Action=SetUserBlocked
&SdkAppId=1400188366
&RoomId=10006
&UserId=29376
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

TencentCloud API 3.0 интегрирует SDK-и, поддерживающие различные языки программирования, чтобы облегчить вам вызов API-й.

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
| FailedOperation.RoomNotExist | Комната не существует. |
| FailedOperation.SdkAppIdNotExist | ID приложения не существует. |
| FailedOperation.UserNotExist | Пользователь не находится в комнате. |
| InternalError | Внутренняя ошибка. |
| InternalError.UserNotExist | Пользователь не находится в комнате. |
| InvalidParameter | Ошибка параметра. |
| InvalidParameter.RoomId | `RoomId` некорректен. |
| InvalidParameter.SdkAppId | `SdkAppId` некорректен. |
| InvalidParameter.UserId | Недействительный `UserId`. |
| InvalidParameterValue.RoomId | Недействительный RoomId. |
| MissingParameter.RoomId | `RoomId` отсутствует. |
| MissingParameter.SdkAppId | `SdkAppId` отсутствует. |
| UnauthorizedOperation.SdkAppId | Нет прав на манипуляцию `SdkAppId`. |


---
*Источник: [https://trtc.io/document/51289](https://trtc.io/document/51289)*

---
*Источник (EN): [setuserblocked.md](./setuserblocked.md)*
