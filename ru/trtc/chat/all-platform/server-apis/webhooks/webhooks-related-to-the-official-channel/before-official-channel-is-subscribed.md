# До официальной подписки на канал

## Обзор функции

Это событие webhook позволяет серверной части приложения проверять запросы пользователей на подписку на официальный канал в реальном времени, включая возможность для серверной части перехватывать такие запросы.

## Примечания

- Чтобы включить webhook, необходимо настроить URL webhook и включить соответствующий протокол. Дополнительные сведения о методе конфигурации см. в разделе [Конфигурация webhook](https://www.tencentcloud.com/document/product/1047/34520).
- Во время этого webhook серверная часть Chat инициирует HTTP POST запрос к серверной части приложения.
- После получения запроса webhook серверная часть приложения должна проверить, соответствует ли SDKAppID, содержащийся в URL запроса, `SDKAppID` приложения.
- Для дополнительной информации о безопасности см. документ [Обзор webhook: Соображения безопасности](https://www.tencentcloud.com/document/product/1047/34354).

## Сценарии срабатывания webhook

- Пользователи приложения подписываются на официальный канал через клиент.
- Администратор приложения добавляет подписчиков через REST API.

## Время срабатывания webhook

До того, как пользователь подпишется на официальный канал.

## Описание вызова API

### Пример URL запроса

В приведенном ниже примере URL webhook, настроенный в приложении, — `https://www.example.com`.
**Пример:**

```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json&ClientIP=$ClientIP&OptPlatform=$OptPlatform
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса — HTTPS, метод запроса — POST. |
| www.example.com | URL webhook. |
| SdkAppid | SDKAppID, назначенный консолью Chat при создании приложения. |
| CallbackCommand | Зафиксировано: OfficialAccount.CallbackBeforeAddSubscriber. |
| contenttype | Фиксированное значение: JSON. |
| ClientIP | IP-адрес клиента, например: 127.0.0.1. |
| OptPlatform | Платформа клиента, для значений см. [Обзор webhook: Протокол webhook](https://www.tencentcloud.com/document/product/1047/34354) для объяснения параметра OptPlatform. |

### Пример запроса

```
 {    "CallbackCommand": "OfficialAccount.CallbackBeforeAddSubscriber",    "Official_Account": "@TOA#_test_for_penn",    "Operator_Account": "107867",    "SubscribeAccountList": [        {            "Subscriber_Account": "jared"        },        {            "Subscriber_Account": "leckie"        }    ],    "EventTime": 1670574414123// Millisecond level, event trigger timestamp		}
```

### Поля запроса

| Объект | Особенность | Функция |
| --- | --- | --- |
| CallbackCommand | String | Команда webhook. |
| Official_Account | String | ID пользователя официального канала подписки. |
| Operator_Account | String | UserID оператора, инициировавшего запрос. |
| SubscribeAccountList | Array | Список добавленных подписчиков. |
| EventTime | Integer | Временная метка события в миллисекундах. |

### Пример ответа

#### Разрешить всем пользователям подписаться на официальный канал

Серверная часть приложения согласна позволить всем пользователям во всех запросах подписаться на официальный канал.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0 }
```

#### Блокировать определенных пользователей от подписки на официальный канал

Серверная часть приложения отклоняет некоторых пользователей в запросе от подписки на официальный канал и возвращает эти идентификаторы в RefusedMembers_Account.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0,    "RefusedSubscribers_Account": [ // List of users who were denied subscription        "jared"    ]}
```

### Поля ответа

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Обязательный | Результат обработанного запроса:OK: указывает на успешную обработкуFAIL: указывает на ошибку |
| ErrorCode | Integer | Обязательный | Код ошибки, 0 разрешает продолжить добавление запросов (включая разрешение добавления некоторых пользователей); 1 отклоняет запрос. |
| ErrorInfo | String | Обязательный | Сообщение об ошибке. |
| RefusedSubscribers_Account | Array | Опциональный | Набор ID пользователей, которым отказано в добавлении. |

## Ссылки

- [Обзор webhook](https://www.tencentcloud.com/document/product/1047/34354)
- REST API:[Добавление подписчиков](https://www.tencentcloud.com/document/product/1047/60760#)


---
*Источник: [https://trtc.io/document/60799](https://trtc.io/document/60799)*

---
*Источник (EN): [before-official-channel-is-subscribed.md](./before-official-channel-is-subscribed.md)*
