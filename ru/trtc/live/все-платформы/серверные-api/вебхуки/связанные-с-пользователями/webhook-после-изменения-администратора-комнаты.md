# Webhook после изменения администратора комнаты

## Описание функции

App-бэкенд может просматривать информацию об изменении администратора комнаты через этот callback.

## Примечание

- Чтобы включить этот callback, необходимо настроить URL callback и включить переключатель, соответствующий этому callback. Способ настройки см. в разделе [Конфигурация Webhook](https://www.tencentcloud.com/document/product/647/64418).
- Направление callback — от Live-бэкенда к App-бэкенду через HTTP POST-запрос.
- После получения запроса callback, App-бэкенд должен проверить, соответствует ли значение параметра SDKAppID в URL запроса его собственному SDKAppID.

## Сценарии запуска callback

- Пользователь App успешно изменил администратора через клиент.
- Администратор App успешно изменил администратора через REST API.

## Время запуска callback

После успешного изменения администратора в комнате.

## Описание API

### Пример URL запроса

В следующем примере URL callback, настроенный для App, это `https://www.example.com`.

**Пример:**

```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса — HTTPS, метод запроса — POST. |
| www.example.com | URL callback |
| SdkAppid | SDKAppID, назначенный в консоли Chat при создании приложения |
| CallbackCommand | Фиксированное значение: Live.CallbackAfterModifyAdmin |
| contenttype | Фиксированное значение: JSON. |

### Пример пакета запроса

```
{    "CallbackCommand":"Live.CallbackAfterModifyAdmin",    "RoomId":"room_id",    "EventTime":1703589922780,    "Operator_Account":"admin",    "Admin_Account": ["user1", "user2"],    "opType": "add"}
```

### Поля пакета запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда callback |
| RoomId | String | ID комнаты |
| Admin_Account | Array | Список измененных администраторов |
| opType | String | Тип операции: add — добавить администратора, delete — удалить администратора |
| Operator_Account | String | Оператор |
| EventTime | Integer | Временная метка запуска события в миллисекундах. |

### Пример пакета ответа

Пакет ответа возвращается после синхронизации данных App-бэкенда.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0 // Ignore the callback result}
```

### Поля пакета ответа

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Обязательный | Результат обработки запроса. OK: обработка успешна; FAIL: обработка не удалась. |
| ErrorCode | Integer | Обязательный | Код ошибки. Введите здесь 0, чтобы игнорировать результат callback. |
| ErrorInfo | String | Обязательный | Сообщение об ошибке |

## Справочные материалы

- [Обзор Webhook](https://www.tencentcloud.com/document/product/647/64412)


---
*Источник: [https://trtc.io/document/72554](https://trtc.io/document/72554)*

---
*Источник (EN): [webhook-after-room-admin-change.md](./webhook-after-room-admin-change.md)*
