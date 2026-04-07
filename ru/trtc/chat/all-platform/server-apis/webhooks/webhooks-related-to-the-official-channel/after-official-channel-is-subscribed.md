# После подписки на официальный канал

## Обзор функции

После подписки на официальный канал бэкэнд приложения может использовать этот вебхук для просмотра сообщений подписки в реальном времени, включая: уведомление бэкэнду приложения при подписке члена на официальный канал, позволяя приложению выполнить необходимую синхронизацию данных.

## Примечания

- Для включения вебхука необходимо настроить URL вебхука и включить соответствующий протокол. Дополнительную информацию о методе конфигурации см. в [Конфигурация вебхука](https://www.tencentcloud.com/document/product/1047/34520).
- Во время этого вебхука бэкэнд Chat инициирует HTTP POST запрос к бэкэнду приложения.
- После получения запроса вебхука бэкэнд приложения должен проверить, является ли SDKAppID, содержащийся в URL запроса, `SDKAppID` приложения.
- По дополнительным вопросам безопасности обратитесь к документу [Обзор вебхука: рассмотрения безопасности](https://www.tencentcloud.com/document/product/1047/34354).

## Сценарии запуска вебхука

- Пользователи приложения подписываются на официальный канал через клиент.
- Администратор приложения добавляет подписчиков через REST API.

## Время запуска вебхука

После успешной подписки пользователя на официальный канал.

## Описание вызова API

### Пример URL запроса

В последующем примере URL вебхука, настроенный в приложении, это `https://www.example.com`.
**Пример:**

```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json&ClientIP=$ClientIP&OptPlatform=$OptPlatform
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса — HTTPS, метод запроса — POST. |
| www.example.com | URL вебхука. |
| SdkAppid | SDKAppID, назначенный консолью Chat при создании приложения. |
| CallbackCommand | Установить значение: OfficialAccount.CallbackAfterAddSubscriber. |
| contenttype | Фиксированное значение: JSON. |
| ClientIP | IP-адрес клиента, например: 127.0.0.1. |
| OptPlatform | Платформа клиента, для значений обратитесь к [Обзор вебхука: протокол вебхука](https://www.tencentcloud.com/document/product/1047/34354) для определения параметра OptPlatform. |

### Пример запроса

```
 {    "CallbackCommand": "OfficialAccount.CallbackAfterAddSubscriber",    "Official_Account": "@TOA#_test_for_penn",    "Operator_Account": "107867",    "SubscribeAccountList": [        {            "Subscriber_Account": "jared"        },        {            "Subscriber_Account": "leckie"        }    ],    "EventTime": 1670574414123// Event trigger timestamp in milliseconds		}
```

### Поля запроса

| Объект | Тип | Функция |
| --- | --- | --- |
| CallbackCommand | String | Команда вебхука. |
| Official_Account | String | Идентификатор пользователя официального канала подписки. |
| Operator_Account | String | Идентификатор пользователя оператора, инициировавшего запрос. |
| SubscribeAccountList | Array | Список добавленных подписчиков. |
| EventTime | Integer | Временная метка запуска события в миллисекундах. |

### Пример ответа

После синхронизации данных бэкэнд приложения отправляет пакет ответа вебхука.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0 // Ignore response results}
```

### Поля ответа

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Обязательное | Результат обработки запроса: OK: указывает на успешную обработку; FAIL: указывает на сбой |
| ErrorCode | Integer | Обязательное | Код ошибки, 0 означает, что результаты ответа могут быть проигнорированы. |
| ErrorInfo | String | Обязательное | Сообщение об ошибке. |

## Ссылки

- [Обзор вебхука](https://www.tencentcloud.com/document/product/1047/34354)
- REST API: [Добавление подписчиков](https://www.tencentcloud.com/document/product/1047/60760#)


---
*Источник: [https://trtc.io/document/60800](https://trtc.io/document/60800)*

---
*Источник (EN): [after-official-channel-is-subscribed.md](./after-official-channel-is-subscribed.md)*
