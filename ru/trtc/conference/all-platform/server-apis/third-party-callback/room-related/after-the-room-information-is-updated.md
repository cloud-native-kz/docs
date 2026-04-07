# После обновления информации комнаты

## Обзор функции

Бэкенд приложения может просматривать изменения информации о комнате в режиме реального времени через этот обратный вызов, включая запись изменений информации о комнате в реальном времени (например, ведение логов или синхронизация с другими системами).

## Примечания

- Чтобы включить обратный вызов, необходимо настроить URL обратного вызова и активировать переключатель, соответствующий этому протоколу обратного вызова. Методы конфигурации см. в документе [Конфигурация обратного вызова третьей стороны](https://www.tencentcloud.com/document/product/1047/34520).
- Направление обратного вызова идет от бэкенда комнаты к бэкенду приложения через HTTP POST запрос.
- После получения запроса обратного вызова бэкенд приложения должен проверить, совпадает ли SDKAppID, содержащийся в URL запроса, с его собственным SDKAppID.

## Сценарии

- Пользователи приложения обновляют информацию о комнате через клиент.
- Администраторы приложения обновляют информацию о комнате через RESTful API.

## Время срабатывания обратного вызова

После успешного обновления информации о комнате.

## Описание API

### Пример URL запроса

В следующем примере URL обратного вызова, настроенный в приложении, — это `https://www.example.com`.
**Пример:**

```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json&ClientIP=$ClientIP&OptPlatform=$OptPlatform
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса — HTTPS, метод запроса — POST |
| www.example.com | URL обратного вызова |
| SdkAppid | SDKAppID, назначенный консолью Chat при создании приложения |
| CallbackCommand | Фиксированное значение: Room.CallbackAfterUpdateRoomInfo |
| contenttype | Фиксированное значение: JSON |
| ClientIP | IP-адрес клиента, формат, например, 127.0.0.1 |
| OptPlatform | Платформа клиента. Значение см. в описании параметра OptPlatform в документе [Обзор Webhook: Протокол обратного вызова](https://www.tencentcloud.com/document/product/1047/34354#.E5.9B.9E.E8.B0.83.E5.8D.8F.E8.AE.AE). |

### Пример пакетов запроса

```
{    "CallbackCommand":"Room.CallbackAfterUpdateRoomInfo",    "Operator_Account":"bob",    "RoomInfo" : {        "RoomId":"rid-123",        "RoomName" : "rname-123",         "Owner_Account" : "jack",        "TakeSeatMode" : "FreeToTake",         "MaxMemberCount" : 300, // Maximum room capacity          "IsVideoDisabled" : false, // Whether to enable video for all, default false         "IsAudioDisabled" : false, // Whether to enable mute for all, default false        "IsMessageDisabled" : false, // Whether to disable sending text messages, default false        "IsScreenSharingDisabled" : false, // Whether to disable screen sharing, default false                                 "IsCloudRecordingDisabled" : "false", // Cloud recording is not disabled, default is false        "CustomInfo" : "123", // Room custom information    }    "EventTime":1670574414123// Millisecond level, event trigger timestamp}
```

### Описание полей пакета запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда обратного вызова |
| Operator_Account | String | UserID оператора, инициирующего запрос на создание группы |
| RoomId | String | ID комнаты |
| RoomName | String | Название комнаты |
| Owner_Account | String | ID ведущего |
| MaxMemberCount | Integer | Максимальное количество членов комнаты |
| IsVideoDisabled | Bool | Отключить видео для всех |
| IsAudioDisabled | Bool | Отключить аудио для всех |
| IsMessageDisabled | Bool | Запретить всем членам отправлять текстовые сообщения |
| IsScreenSharingDisabled | Bool | Отключить общий доступ к экрану |
| IsCloudRecordingDisabled | Bool | Отключить облачную запись |
| CustomInfo | String | Поля пользовательского определения |
| EventTime | Integer | Временная метка срабатывания события в миллисекундах |

### Пример пакетов ответов

Пакет ответа обратного вызова отправляется после того, как бэкенд приложения синхронизирует данные.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0 // Ignore callback result}
```

### Описание полей пакета ответа

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Обязательный | Результат процесса запроса. OK для успеха, FAIL для отказа. |
| ErrorCode | Integer | Обязательный | Код ошибки, 0 означает игнорировать результат ответа |
| ErrorInfo | String | Обязательный | Сообщение об ошибке |

## Справочные материалы

- [Обзор Webhook](https://www.tencentcloud.com/document/product/647/60722#)
- RESTful API: [Обновление информации о комнате](https://www.tencentcloud.com/document/product/647/60705#)


---
*Источник: [https://trtc.io/document/60731](https://trtc.io/document/60731)*

---
*Источник (EN): [after-the-room-information-is-updated.md](./after-the-room-information-is-updated.md)*
