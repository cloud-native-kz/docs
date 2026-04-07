# Webhook После изменения списка позиций микрофона

## Обзор функции

Бэкенд приложения может просматривать сообщения об изменениях списка позиций микрофона в реальном времени через этот webhook.

## Примечания

- Для включения webhook необходимо настроить URL webhook и активировать переключатель, соответствующий этому протоколу webhook. Методы конфигурации см. в документе [Конфигурация вебхуков третьих сторон](https://www.tencentcloud.com/document/product/647/64412#).
- Во время этого webhook бэкенд Live инициирует HTTP POST запрос к бэкенду приложения.
- После получения запроса webhook бэкенд приложения должен проверить, совпадает ли SDKAppID, содержащийся в URL запроса, с его собственным SDKAppID.

## Сценарии, которые могут запустить этот Webhook

- Пользователь приложения отключает/включает микрофон.
- Операция блокировки позиции микрофона.

## Время срабатывания Webhook

После изменения информации о позиции микрофона.

## Описание API

### Пример URL запроса

В следующем примере URL webhook, настроенный в приложении: `https://www.example.com`.
**Пример:**

```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json&ClientIP=$ClientIP&OptPlatform=$OptPlatform
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса - HTTPS, метод запроса - POST |
| www.example.com | URL Webhook |
| SdkAppid | SDKAppID, назначенный консолью Chat при создании приложения |
| CallbackCommand | Фиксировано как Mic.CallbackAfterSeatInfoChanged |
| contenttype | Фиксированное значение: JSON |
| ClientIP | IP-адрес клиента, например 127.0.0.1 |
| OptPlatform | Платформа клиента, см. [Обзор Webhook: Протокол Webhook](https://www.tencentcloud.com/document/product/647/64412#) для значения параметров OptPlatform |

### Пример пакетов запроса

```
{    "CallbackCommand":"Mic.CallbackAfterSeatInfoChanged",    "RoomId":"rid-123",    "SeatList":[        {            // Номер позиции микрофона            "Index": 1,                 // Если текущая позиция микрофона занята, будет возвращен ID соответствующего пользователя. В противном случае это поле не будет установлено            "Member_Account": 144115233775727695,              // false: Доступ микрофона разрешен true: Доступ микрофона запрещен             "IsTakenDisabled": false,             // false: Передача видеопотока разрешена true: Передача видеопотока запрещена              "IsVideoDisabled": false,              // false: Разрешить передачу аудиопотока true: Запретить передачу аудиопотока             "IsAudioDisabled": false         }    ]    "EventTime":1670574414123// Уровень миллисекунд, временная метка срабатывания события}
```

### Поля пакета запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда webhook |
| RoomId | String | ID комнаты |
| SeatList | Array | Список позиций микрофона |
| Index | Integer | Номер позиции микрофона |
| Member_Account | String | ID пользователя на позиции микрофона. Если недоступно, это поле не будет установлено |
| IsTakenDisabled | Bool | Блокировка позиции микрофона |
| IsVideoDisabled | Bool | Запретить видеопоток микрофона |
| IsAudioDisabled | Bool | Запретить аудиопоток микрофона |

### Пример пакета ответа

Пакет ответа webhook отправляется после того, как бэкенд приложения синхронизирует данные.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0 // Игнорировать результат webhook}
```

### Описание полей пакета ответа

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Обязательное | Результат процесса запроса: OK указывает на успех; FAIL указывает на ошибку |
| ErrorCode | Integer | Обязательное | Код ошибки, здесь 0 означает игнорировать результат ответа |
| ErrorInfo | String | Обязательное | Сообщение об ошибке |

## Справка

- [Обзор Webhook](https://www.tencentcloud.com/document/product/647/64412#)


---
*Источник: [https://trtc.io/document/64425](https://trtc.io/document/64425)*

---
*Источник (EN): [webhook-after-seat-list-changed.md](./webhook-after-seat-list-changed.md)*
