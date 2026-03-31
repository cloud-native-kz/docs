# После входа в комнату

## Обзор функции

Backend приложения может просматривать сообщения о присоединении участников комнаты в реальном времени через этот callback, включая: уведомление backend приложения о присоединении участника к группе, позволяя приложению выполнить необходимую синхронизацию данных.

## Примечания

- Для включения callback необходимо настроить URL callback и активировать переключатель, соответствующий этому протоколу callback. Методы настройки см. в документе [Конфигурация callback третьих сторон](https://www.tencentcloud.com/document/product/1047/34520).
- Направление callback идёт от backend комнаты к backend приложения через HTTP POST запрос.
- После получения запроса callback, backend приложения должен проверить, совпадает ли SDKAppID, содержащийся в URL запроса, с его собственным SDKAppID.

## Сценарии

- Пользователи приложения активно присоединяются к комнате через клиент.

## Время срабатывания callback

После успешного присоединения пользователей к комнате.

## Описание API

### Пример URL запроса

В следующем примере URL callback, настроенный в приложении, — это `https://www.example.com`.
**Пример:**

```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json&ClientIP=$ClientIP&OptPlatform=$OptPlatform
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса — HTTPS, метод запроса — POST |
| www.example.com | URL callback |
| SdkAppid | SDKAppID, назначенный консолью Chat при создании приложения |
| CallbackCommand | Установленное значение: Room.CallbackAfterMemberEnter |
| contenttype | Фиксированное значение: JSON |
| ClientIP | IP-адрес клиента, формат, например 127.0.0.1 |
| OptPlatform | Платформа клиента. Для значения см. описание параметра OptPlatform в [Обзор Webhook: Протокол callback](https://www.tencentcloud.com/document/product/1047/34354#.E5.9B.9E.E8.B0.83.E5.8D.8F.E8.AE.AE). |

### Пример пакета запроса

```
{    "CallbackCommand":"Room.CallbackAfterMemberEnter",    "Operator_Account":"user1",    "RoomId":"rid-123",    "MemberCount":20,    "Type":"Enter", // Метод присоединения к комнате: Enter (присоединение самостоятельно)    "MemberList_Account":["user1"],    "EventTime":1670574414123// Уровень миллисекунд, временная метка срабатывания события}
```

### Описание полей пакета запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда callback |
| Operator_Account | String | UserID инициатора запроса |
| RoomId | String | ID комнаты |
| MemberCount | Integer | Вместимость комнаты |
| Type | String | Метод присоединения к комнате: Enter (присоединение самостоятельно) |
| MemberList_Account | Array | Список участников комнаты |
| EventTime | Integer | Временная метка срабатывания события в миллисекундах |

### Пример пакета ответа

Пакет ответа callback отправляется после синхронизации данных backend приложением.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0 // Игнорировать результат callback}
```

### Описание полей пакета ответа

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Обязательное | Результат процесса запроса. OK для успеха, FAIL для ошибки. |
| ErrorCode | Integer | Обязательное | Код ошибки, 0 означает игнорировать результат ответа |
| ErrorInfo | String | Обязательное | Сообщение об ошибке |

## Справочная информация

- [Обзор Webhook](https://www.tencentcloud.com/document/product/647/60722#)


---
*Источник: [https://trtc.io/document/60735](https://trtc.io/document/60735)*

---
*Источник (EN): [after-a-room-is-entered.md](./after-a-room-is-entered.md)*
