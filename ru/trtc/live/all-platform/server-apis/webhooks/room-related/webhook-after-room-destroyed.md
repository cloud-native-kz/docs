# Webhook после удаления комнаты

## Обзор функции

Бэкенд приложения может использовать этот webhook для мониторинга растворения комнаты в реальном времени, включая запись растворения комнаты в реальном времени (например, логирование или синхронизацию с другими системами).

## Примечания

- Чтобы включить этот webhook, необходимо настроить URL webhook и переключить соответствующий протокол. Подробнее о методе конфигурации см. документацию [Third party webhook configuration](https://www.tencentcloud.com/document/product/647/64420).
- Во время этого webhook бэкенд Live инициирует HTTP POST запрос к бэкенду приложения.
- После получения webhook запроса бэкенд приложения должен проверить, совпадает ли SDKAppID, содержащийся в URL запроса, с его собственным SDKAppID.

## Сценарии, которые могут вызвать этот webhook

- Пользователь приложения успешно растворил комнату с помощью клиента
- Администратор приложения успешно растворил комнату с помощью REST API

## Время срабатывания Webhook

После успешного удаления комнаты.

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
| https | Протокол запроса — HTTPS, метод запроса — POST |
| www.example.com | URL Webhook |
| SdkAppid | SDKAppID, назначенный консолью Chat при создании приложения |
| CallbackCommand | Зафиксирован как Live.CallbackAfterDestroyRoom |
| contenttype | Зафиксированное значение: JSON |
| ClientIP | IP клиента, например 127.0.0.1 |
| OptPlatform | Платформа клиента, справочное значение см. [Webhook Overview: Webhook Protocol](https://www.tencentcloud.com/document/product/647/64412#d8e83f91-15ef-46e9-b370-9ba6c93a6ada) для значения параметра OptPlatform |

### Пример пакетов запроса

```
{    "CallbackCommand":"Live.CallbackAfterDestroyRoom",    "Operator_Account":"admin",    "RoomId":"tandy-test-rest",    "EventType":"DestroyByUser", //"DestroyByUser", "DestroyBySystem" указывает на два вида: растворение, инициированное пользователем, и автоматическое растворение системой при пустой комнате    "EventTime":1703589922780,    "RoomInfo": {        "RoomName": "live name",        "RoomType": "Live",        "Owner_Account": 144115216631667826,        "IsSeatEnabled": true,        "TakeSeatMode": "FreeToTake",        "MaxMemberCount": 400,        "MaxSeatCount": 4,        "Category": [1, 2, 3],        "CustomInfo": "",        "IsMessageDisabled": false,        "CoverURL": "cover url",        "ActivityStatus": 0,        "IsPublicVisible": false,        "ViewCount": 0,        "BackgroundURL": "background url",        "IsUnlimitedRoomEnabled": true     },     "Statistic": {            "TotalViewers": 0,            "TotalGiftsSent": 0,            "TotalGiftCoins": 0,            "TotalUniqueGiftSenders": 0,            "TotalLikesReceived": 0     }}
```

### Поля пакета запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда Webhook |
| Operator_Account | String | UserID оператора, инициирующего запрос на удаление комнаты |
| RoomId | String | ID комнаты |
| EventType | String | Тип растворения: разделяется на растворение, инициированное пользователем (DestroyByUser) и автоматическое растворение системой (DestroyBySystem) |
| EventTime | Integer | Временная метка события срабатывания в миллисекундах |
| RoomName | String | Имя комнаты |
| RoomType | String | Тип комнаты: Meeting (Конференц-зал) |
| Owner_Account | String | ID хоста |
| IsSeatEnabled | Bool | Доступна ли поддержка микрофона |
| TakeSeatMode | String | Режим мест: None (Выключено), FreeToTake (Свободное присоединение к подиуму), ApplyToTake (Запрос на подключение микрофона) |
| MaxMemberCount | Integer | Максимальное количество участников комнаты |
| MaxSeatCount | Integer | Максимальное количество микрофонов |
| Category | Array | Идентификация типа комнаты, тип массива целых чисел |
| CustomInfo | String | Настраиваемые поля |
| IsMessageDisabled | Bool | Запретить всем участникам отправлять текстовые сообщения |
| CoverURL | String | URL обложки комнаты |
| ActivityStatus | Integer | Статус активности прямой комнаты: определяемый пользователем тег |
| IsPublicVisible | Bool | Комната открытая или нет |
| ViewCount | Integer | Общее количество входов пользователя в комнату |
| BackgroundURL | String | URL фона комнаты |
| IsUnlimitedRoomEnabled | Bool | Включить ли микширование комнаты для поддержки сценариев высокого уровня параллелизма. Значение по умолчанию — false. Если true, это соответствует [TUILiveKit](https://www.tencentcloud.com/document/product/647/60034) на стороне SDK |
| TotalViewers | Integer | Общее количество входов в комнату, подсчитывается N раз для повторного входа одного пользователя |
| TotalGiftsSent | Integer | Общее количество подарков |
| TotalGiftCoins | Integer | Общая стоимость подарков |
| TotalUniqueGiftSenders | Integer | Общее количество отправителей подарков |
| TotalLikesReceived | Integer | Общее количество лайков |

### Пример пакета ответа

Пакет ответа webhook отправляется после синхронизации данных бэкендом приложения.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0 // Игнорировать результат webhook}
```

### Описание поля пакета ответа

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Обязательное | Результат процесса запроса: OK указывает на успех; FAIL указывает на неудачу |
| ErrorCode | Integer | Обязательное | Код ошибки, здесь 0 означает игнорировать результат ответа |
| ErrorInfo | String | Обязательное | Сообщение об ошибке |

## Справочник

- [Webhook Overview](https://www.tencentcloud.com/document/product/647/64412)
- REST API:[Dissolve Room](https://www.tencentcloud.com/document/product/647/63406)


---
*Источник: [https://trtc.io/document/64423](https://trtc.io/document/64423)*

---
*Источник (EN): [webhook-after-room-destroyed.md](./webhook-after-room-destroyed.md)*
