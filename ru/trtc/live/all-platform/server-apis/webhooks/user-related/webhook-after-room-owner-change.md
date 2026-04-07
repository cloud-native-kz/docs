# Webhook после изменения владельца комнаты

## Описание функции

Backend приложения может просматривать информацию об изменении владельца комнаты посредством исследования.

## Примечание

- Для включения этого callback требуется настроить URL callback и включить переключатель, соответствующий этому callback. Метод конфигурации см. в разделе [Конфигурация Webhook](https://www.tencentcloud.com/document/product/647/64418).
- Направление callback идет из Live backend в App backend через HTTP POST запрос.
- После получения запроса callback, backend приложения должен проверить, является ли значение параметра SDKAppID в URL запроса его собственным SDKAppID.

## Сценарии срабатывания Callback

- Пользователь приложения успешно изменил владельца комнаты через клиент.
- Администратор приложения успешно изменил владельца комнаты через REST API.

## Время срабатывания Callback

Владелец комнаты был успешно изменен.

## Описание API

### Пример URL запроса

В следующем примере URL callback, настроенный для приложения, — `https://www.example.com`.

**Пример:**

```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса — HTTPS, метод запроса — POST. |
| www.example.com | URL callback. |
| SdkAppid | SDKAppID, назначенный в консоли Chat при создании приложения |
| CallbackCommand | Зафиксирован как Live.CallbackAfterChangeOwner |
| contenttype | Значение зафиксировано как JSON. |

### Пример пакета запроса

```
{    "CallbackCommand":"Live.CallbackAfterChangeOwner",    "RoomId":"room_id",    "EventTime":1703589922780,    "Operator_Account":"admin",    "CurrentOwner_Account": "user2",    "OriginalOwner_Account": "user1"}
```

### Поля пакета запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда callback. |
| RoomId | String | ID комнаты |
| CurrentOwner_Account | String | новый владелец |
| OriginalOwner_Account | String | исходный владелец |
| Operator_Account | String | Оператор |
| EventTime | Interger | Временная метка срабатывания события в миллисекундах. |

### Пример пакета ответа

Пакет ответа возвращается после синхронизации данных backend приложением.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0 // Ignore the callback result}
```

### Поля пакета ответа

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Обязательно | Результат обработки запроса. OK: успешная обработка; FAIL: ошибка обработки. |
| ErrorCode | Integer | Обязательно | Код ошибки. Укажите здесь 0, чтобы игнорировать результат callback. |
| ErrorInfo | String | Обязательно | Сообщение об ошибке |

## Справочные материалы

- [Обзор Webhook](https://www.tencentcloud.com/document/product/647/64412)


---
*Источник: [https://trtc.io/document/72553](https://trtc.io/document/72553)*

---
*Источник (EN): [webhook-after-room-owner-change.md](./webhook-after-room-owner-change.md)*
