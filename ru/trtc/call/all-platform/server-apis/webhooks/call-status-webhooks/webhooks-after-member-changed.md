# Вебхуки после изменения статуса участника

## Описание функции

Бэкенд приложения может просматривать изменения статуса участников вызова в реальном времени через этот обратный вызов.

## Необходимая информация

- Для включения обратного вызова необходимо настроить URL обратного вызова через REST API и включить переключатель, соответствующий этому протоколу обратного вызова. О методе конфигурации см. в разделе [Параметры конфигурации обратного вызова](https://www.tencentcloud.com/document/product/647/68938#).
- Направление обратного вызова: бэкенд Call инициирует HTTP POST запрос к бэкенду App.
- После получения запроса обратного вызова бэкенд App должен проверить, соответствует ли значение параметра SDKAppID в URL запроса его собственному SDKAppID.

## Сценарии срабатывания обратного вызова

Этот обратный вызов срабатывает при изменении статуса участников вызова в результате операций, выполняемых пользователями App через клиент, таких как подключение, разъединение и т. д.

## Время срабатывания обратного вызова

После изменения статуса участника вызова.

## Описание API

### Пример URL запроса

В следующем примере URL обратного вызова, настроенный для App, — это `https://www.example.com`.

**Пример:**

```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json&ClientIP=$ClientIP&OptPlatform=$OptPlatform
```

### Параметры запроса

| Параметры | Описание |
| --- | --- |
| https | Протокол запроса — HTTPS, метод запроса — POST. |
| www.example.com | URL обратного вызова |
| SdkAppid | SDKAppID, назначенный в консоли Chat при создании приложения |
| CallbackCommand | Фиксированное значение `Call.CallbackAfterMemberChanged` |
| contenttype | Значение фиксировано как `json` |
| ClientIP | IP-адрес клиента в формате `127.0.0.1` |
| OptPlatform | Платформа клиента. Значения параметров см. в описании параметра OptPlatform в разделе [Обзор обратного вызова третьей стороны: Протокол обратного вызова](https://www.tencentcloud.com/zh/document/product/1047/34354#.E5.9B.9E.E8.B0.83.E5.8D.8F.E8.AE.AE) |

### Пример пакета запроса

```
{    "CallbackCommand":"Call.CallbackAfterMemberChanged",    "CallId":"055662e1-bc8a-469c-a334-1126c8c17d58",    "UserList":[        {            "User_Account":"user1",            "Status":"Calling"        },        {            "User_Account":"user2",            "Status":"Calling"        }    ],    "ChangedUserList":[        {            "User_Account":"user2",            "ActionType":"Answer"  // Answer: Ответил; Reject: Отклонил; NotAnswer: Не ответил; Hangup: Повесил трубку; Join: Присоединился; Offline: Офлайн (истечение сигнала); Invite: Пригласить; Cancel_Invite: Отменить приглашение;        }    ]    "EventTime":1740464128807}
```

### Поля пакета запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда обратного вызова |
| CallId | String | ID вызова |
| UserList | Array | Список участников вызова |
| User_Account | String | ID пользователя, который звонит |
| Status | String | Статус вызова: `Calling` : в вызове `Waiting` : ожидание подключения |
| ChangedUserList | Array | Список участников |
| ChangedUserList.User_Account | String | ID пользователя, статус которого изменился |
| ActionType | String | Операция изменения, вызывающая изменения`Accept`:  Ответил`Reject`:  Отклонил`NotAnswer`:  Не ответил`Hang Up`:  Повесил трубку`Join`:  Присоединился к вызову`Offline`:  Офлайн`Invited`:   Приглашен звонящим присоединиться к вызову`Canncel_Invite`:  Приглашение отменено звонящим |
| EventTime | Integer | Временная метка срабатывания события в миллисекундах |

### Пример пакета ответа

Пакет ответа возвращается после синхронизации данных бэкендом App.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0 // Игнорировать результат обратного вызова}
```

### Поля пакета ответа

| Поле | Тип | Требуется | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Требуется | Результат обработки запроса. OK: обработка успешна; FAIL: обработка не удалась. |
| ErrorInfo | String | Требуется | Сообщение об ошибке. |
| ErrorCode | Integer | Требуется | Код ошибки. Введите 0 здесь, чтобы игнорировать результат обратного вызова. |

## Справочные материалы

- [Обзор вебхуков](https://www.tencentcloud.com/document/product/647/68933#)
- REST API: [Получить статус вызова в реальном времени](https://www.tencentcloud.com/document/product/647/68932#)


---
*Источник: [https://trtc.io/document/69215](https://trtc.io/document/69215)*

---
*Источник (EN): [webhooks-after-member-changed.md](./webhooks-after-member-changed.md)*
