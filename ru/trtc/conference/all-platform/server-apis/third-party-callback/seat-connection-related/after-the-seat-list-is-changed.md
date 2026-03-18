# После изменения списка мест

## Обзор функции

Бэкенд приложения может просматривать сообщения об изменении списка позиций в реальном времени через этот callback.

## Примечания

- Для включения callback необходимо настроить URL callback и активировать переключатель, соответствующий этому протоколу callback. Методы конфигурации см. в документе [Third-party Callback Configuration](https://www.tencentcloud.com/document/product/1047/34520).
- Направление callback — от бэкенда комнаты к бэкенду приложения через HTTP POST запрос.
- После получения запроса callback бэкенд приложения должен проверить, совпадает ли SDKAppID, содержащийся в URL запроса, с его собственным SDKAppID.

## Сценарии

- Добавить пользователя приложения на место/Удалить пользователя с места.
- Заблокировать позицию места.

## Время срабатывания Callback

После изменения информации о позиции места.

## Описание API

### Пример URL запроса

В следующем примере URL callback, настроенный в приложении, — `https://www.example.com`.
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
| CallbackCommand | Фиксированное значение: Mic.CallbackAfterSeatInfoChanged |
| contenttype | Фиксированное значение: JSON |
| ClientIP | IP клиента, например 127.0.0.1 |
| OptPlatform | Платформа клиента. Значение см. в описании параметра OptPlatform в разделе [Webhook Overview: Callback Protocol](https://www.tencentcloud.com/document/product/1047/34354#.E5.9B.9E.E8.B0.83.E5.8D.8F.E8.AE.AE). |

### Пример пакета запроса

```
{    "CallbackCommand":"Mic.CallbackAfterSeatInfoChanged",    "Operator_Account":"user1",    "RoomId":"rid-123",    "SeatList":[        {            // Seat Number            "Index": 1,                 // If the seat is currently occupied, return the user's ID            "Member_Account": 144115233775727695,              // false: Mic access allowed true: Mic access prohibited             "IsTakenDisabled": false,             // false: Pushing video stream allowed true: Pushing video stream prohibited              "IsVideoDisabled": false,              // false: Allow audio stream push true: Prohibit audio stream push             "IsAudioDisabled": false         }    ]    "EventTime":1670574414123// Millisecond level, event trigger timestamp}
```

### Описание полей пакета запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда callback |
| Operator_Account | String | UserID запрашивающего |
| RoomId | String | ID комнаты |
| SeatList | Array | Список мест |
| Index | Integer | Номер места |
| Member_Account | String | ID пользователя на позиции места, пусто указывает на отсутствие пользователя на месте |
| IsTakenDisabled | Bool | Заблокировать позицию места |
| IsVideoDisabled | Bool | Отключить видеопоток микрофона |
| IsAudioDisabled | Bool | Отключить аудиопоток микрофона |

### Пример пакета ответа

Пакет ответа callback отправляется после синхронизации данных бэкендом приложения.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0 // Ignore callback result}
```

### Описание полей пакета ответа

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Обязательно | Результат обработки запроса. OK для успеха, FAIL для неудачи. |
| ErrorCode | Integer | Обязательно | Код ошибки, 0 означает игнорировать результат ответа |
| ErrorInfo | String | Обязательно | Сообщение об ошибке |

## Справочная информация

- [Webhook Overview](https://www.tencentcloud.com/document/product/647/60722#)


---
*Источник: [https://trtc.io/document/60736](https://trtc.io/document/60736)*

---
*Источник (EN): [after-the-seat-list-is-changed.md](./after-the-seat-list-is-changed.md)*
