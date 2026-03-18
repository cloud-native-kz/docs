# После отписки от официального канала

## Обзор функции

Серверная часть приложения может использовать этот webhook для просмотра в реальном времени активности пользователей, отписывающихся от официального канала, включая: регистрацию отписок пользователей в реальном времени (например, логирование или синхронизацию с другими системами).

## Примечания

- Для включения webhook необходимо настроить URL webhook и включить соответствующий протокол. Дополнительные сведения о методе конфигурации см. в разделе [Конфигурация webhook](https://www.tencentcloud.com/document/product/1047/34520).
- При использовании этого webhook серверная часть Chat инициирует HTTP POST запрос к серверной части приложения.
- После получения запроса webhook серверная часть приложения должна проверить, содержится ли SDKAppID в URL запроса, это `SDKAppID` приложения.
- По вопросам безопасности обратитесь к документу [Обзор webhook: Рекомендации по безопасности](https://www.tencentcloud.com/document/product/1047/34354).

## Сценарии срабатывания webhook

- Пользователи приложения отписываются от официального канала через клиент.
- Администраторы приложения удаляют подписчиков через REST API.

## Время срабатывания webhook

После того, как пользователь успешно отписался от официального канала.

## Описание вызова API

### Пример URL запроса

В следующем примере URL webhook, настроенный в приложении, имеет значение `https://www.example.com`.
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
| CallbackCommand | Фиксированное значение: OfficialAccount.CallbackAfterDeleteSubscriber. |
| contenttype | Фиксированное значение: JSON. |
| ClientIP | IP-адрес клиента, например: 127.0.0.1. |
| OptPlatform | Платформа клиента. Значения см. в разделе [Обзор webhook: Протокол webhook](https://www.tencentcloud.com/document/product/1047/34354) для описания параметра OptPlatform. |

### Пример запроса

```
{    "CallbackCommand": "OfficialAccount.CallbackAfterDeleteSubscriber", // Webhook команда    "Official_Account" : "@TOA#_test_OA_for_penn",    "Operator_Account": "leckie", // Оператор    "SubscribeAccountList": [        {            "Subscriber_Account": "jared"        },        {            "Subscriber_Account": "leckie"        }    ],    "EventTime": 1670574414123// Временная метка срабатывания события в миллисекундах		}
```

### Поля запроса

| Объект | Характеристики | Функция |
| --- | --- | --- |
| CallbackCommand | String | Webhook команда. |
| Official_Account | String | ID пользователя официального аккаунта, который отписался. |
| Operator_Account | String | UserID оператора, инициировавшего запрос. |
| SubscribeAccountList | Array | Список пользователей, которые отписались. |
| EventTime | Integer | Временная метка срабатывания события в миллисекундах. |

### Пример ответа

Ответ возвращается после синхронизации данных серверной частью приложения.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0 // Игнорировать результаты ответа}
```

### Поля ответа

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Обязательное | Результат обработанного запроса: OK: Указывает на успешную обработку. FAIL: Указывает на ошибку. |
| ErrorCode | Integer | Обязательное | Код ошибки, 0 означает, что результаты ответа можно игнорировать. |
| ErrorInfo | String | Обязательное | Сообщение об ошибке. |

## Ссылки

- [Обзор webhook](https://www.tencentcloud.com/document/product/1047/34354)
- REST API: [Удалить подписчика](https://www.tencentcloud.com/document/product/1047/60761#)


---
*Источник: [https://trtc.io/document/60802](https://trtc.io/document/60802)*

---
*Источник (EN): [after-official-channel-is-unsubscribed.md](./after-official-channel-is-unsubscribed.md)*
