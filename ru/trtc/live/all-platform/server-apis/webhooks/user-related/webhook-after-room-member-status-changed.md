# Webhook при изменении статуса участника комнаты

## Обзор функции

Бэкенд приложения может отслеживать в реальном времени изменения статуса онлайн и офлайн пользователей в комнате через данный webhook.

## Примечания

- Для включения этого webhook необходимо настроить URL webhook и включить соответствующий протокол. Дополнительные сведения о методе конфигурации см. в документации [Конфигурация стороннего Webhook](https://www.tencentcloud.com/document/product/647/64412).
- Во время работы этого webhook бэкенд Live инициирует HTTP POST запрос к бэкенду приложения.
- После получения запроса webhook бэкенд приложения должен проверить, совпадает ли SDKAppID, содержащийся в URL запроса, с его собственным SDKAppID.
- Этот callback прерывается немедленно при растворении комнаты.

## Сценарии, которые могут запустить этот Webhook

- Пользователи вызывают интерфейсы SDK для входа в комнату или выхода из неё.
- Истечение времени ожидания heartbeat пользователя в комнате и восстановление heartbeat.

## Время срабатывания Webhook

После успешного создания комнаты.

## Описание API

### Пример URL запроса

В следующем примере URL webhook, настроенный в приложении, — это `https://www.example.com`.
**Пример:**

```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json&ClientIP=$ClientIP&OptPlatform=$OptPlatform
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса — HTTPS, метод запроса — POST. |
| www.example.com | URL webhook. |
| SdkAppid | SDKAppID, назначенный консолью Instant Messaging при создании приложения. |
| CallbackCommand | Зафиксировано как Live.CallbackMemberStateChanged. |
| contenttype | Фиксированное значение: JSON. |

### Пример пакетов запроса

```
{    "CallbackCommand":"Live.CallbackAfterMemberStateChanged",    "RoomId":"room_id",    "EventType":"Online", // Online or Offline    "EventCause":"Enter", // Four types: Enter (enter room), Leave (leave room), HeartbeatInterrupt, HeartbeatRecover    "MemberList":[        {            "Member_Account": "jared"        },        {            "Member_Account": "tommy"        }    ],    "EventTime":1703589922780}
```

### Поля пакета запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда webhook. |
| RoomId | String | ID комнаты. |
| EventType | String | Тип события: разделяется на два типа — онлайн и офлайн пользователя, Online, Offline. |
| EventCause | String | Причина события, разделяется на следующие четыре типа: Enter (вход в комнату), Leave (выход), HeartbeatInterrupt, HeartbeatRecover. |
| MemberList | Array | Список затронутых участников. |
| EventTime | Integer | Timestamp срабатывания события в миллисекундах. |

### Пример пакета ответа

Пакет ответа webhook отправляется после синхронизации данных бэкендом приложения.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0 // Ignore webhook result}
```

### Описание полей пакета ответа

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Обязательный | Результат процесса запроса: OK указывает на успех; FAIL указывает на ошибку. |
| ErrorCode | Integer | Обязательный | Код ошибки, здесь 0 означает игнорирование результата ответа. |
| ErrorInfo | String | Обязательный | Сообщение об ошибке. |

## Справка

- [Обзор Webhook](https://www.tencentcloud.com/document/product/647/64412)


---
*Источник: [https://trtc.io/document/64424](https://trtc.io/document/64424)*

---
*Источник (EN): [webhook-after-room-member-status-changed.md](./webhook-after-room-member-status-changed.md)*
