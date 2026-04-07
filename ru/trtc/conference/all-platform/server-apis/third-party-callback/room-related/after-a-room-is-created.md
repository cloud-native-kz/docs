# После создания комнаты

## Описание функции

Бэкэнд приложения может в реальном времени просматривать информацию о комнате, созданной пользователем, через этот callback, включая уведомления об успешном создании комнаты в бэкэнде приложения, что позволяет выполнять такие действия, как синхронизация данных.

## Примечания

- Для включения callback необходимо настроить URL callback и активировать переключатель, соответствующий этому протоколу callback. Методы конфигурации см. в документе [Конфигурация callback-ов третьей стороны](https://www.tencentcloud.com/document/product/1047/34520).
- Направление callback идёт от бэкэнда комнаты к бэкэнду приложения через HTTP POST запрос.
- После получения callback запроса бэкэнд приложения должен проверить, соответствует ли SDKAppID, содержащийся в URL запроса, его собственному SDKAppID.

## Сценарии

- Пользователи приложения успешно создают комнату через клиент.
- Администраторы приложения успешно создают комнату через RESTful API.

## Время срабатывания callback

После успешного создания комнаты.

## Описание API

### Пример URL запроса

В следующем примере URL callback, настроенный в приложении, это `https://www.example.com`.
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
| CallbackCommand | Фиксированное значение Room.CallbackAfterCreateRoom |
| contenttype | Фиксированное значение `JSON` |
| ClientIP | IP адрес клиента, формат, например 127.0.0.1 |
| OptPlatform | Платформа клиента. Для значения см. описание параметра OptPlatform в [Обзор Webhook: Протокол callback](https://www.tencentcloud.com/document/product/1047/34354#.E5.9B.9E.E8.B0.83.E5.8D.8F.E8.AE.AE). |

### Пример пакета запроса

```
{    "CallbackCommand":"Room.CallbackAfterCreateRoom",    "Operator_Account":"admin",    "RoomInfo":{        "RoomId":"tandy-test-rest",        "RoomName":"tandy-test-rest",        "RoomType":"Meeting",        "Owner_Account":"user3",        "MaxMemberCount":300,        "MaxSeatCount":16,        "IsVideoDisabled":true,        "IsAudioDisabled":true,        "IsMessageDisabled":true,        "IsScreenSharingDisabled":true,        "IsCloudRecordingDisabled":true,        "CustomInfo":"custom123",        "ScheduleStartTime":1703589922,        "ScheduleEndTime":1703593522,        "RoomStatus":"Running",        "IsSeatEnabled":true,        "TakeSeatMode":"ApplyToTake",        "CreateTime":1703589922    },    "ScheduleInviteeList_Account":["user2", "user3", "user3"],    "EventTime":1703589922780}
```

### Описание полей пакета запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда callback |
| Operator_Account | String | UserID оператора, инициирующего запрос на создание группы |
| RoomId | String | ID комнаты |
| RoomName | String | Имя комнаты |
| RoomType | String | Тип комнаты: conference (конференц-зал) |
| Owner_Account | String | ID ведущего |
| MaxMemberCount | Integer | Максимальное количество участников комнаты |
| ScheduleStartTime | Integer | Запланированное время начала встречи |
| ScheduleStartTime | Integer | Запланированное время окончания встречи |
| IsVideoDisabled | Bool | Отключить видео для всех |
| IsAudioDisabled | Bool | Отключить аудио для всех |
| IsMessageDisabled | Bool | Запретить всем участникам отправлять текстовые сообщения |
| IsScreenSharingDisabled | Bool | Запретить совместное использование экрана |
| IsCloudRecordingDisabled | Bool | Запретить облачное сохранение |
| CustomInfo | String | Пользовательские поля определения |
| RoomStatus | String | Статус комнаты: None, NotStarted, Running |
| IsSeatEnabled | Bool | Поддерживается ли функция позиций (мест). |
| MaxSeatCount | Integer | Максимальное количество мест |
| TakeSeatMode | String | Режим мест: None (выключено), FreeToTake (открытый микрофон), ApplyToTake (микрофон по запросу) |
| CreateTime | Integer | Запланированное время начала встречи |
| EventTime | Integer | Временная метка срабатывания события в миллисекундах |

### Пример пакета ответа

Пакет ответа callback отправляется после синхронизации данных бэкэндом приложения.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0 // Игнорировать результат callback}
```

### Описание полей пакета ответа

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Обязательное | Результат обработки запроса. OK для успеха, FAIL для ошибки. |
| ErrorCode | Integer | Обязательное | Код ошибки, 0 означает игнорирование результата ответа |
| ErrorInfo | String | Обязательное | Сообщение об ошибке |

## Справочные материалы

- [Обзор Webhook](https://www.tencentcloud.com/document/product/647/60722#)
- RESTful API: [Создать комнату](https://www.tencentcloud.com/document/product/647/60707#)


---
*Источник: [https://trtc.io/document/60733](https://trtc.io/document/60733)*

---
*Источник (EN): [after-a-room-is-created.md](./after-a-room-is-created.md)*
