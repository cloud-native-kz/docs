# Обратные вызовы тревожных сигналов перегрузки API

#### Обзор функции

Когда частота запросов API превышает 80% от порога, серверная часть приложения уведомляется о информации тревожного сигнала частоты вызовов через обратный вызов.

#### Примечания

- Для включения обратного вызова необходимо настроить URL обратного вызова. Подробные методы настройки см. в [Конфигурация Webhook](https://intl.cloud.tencent.com/document/product/1047/34520).
- После настройки URL обратного вызова тревожный обратный вызов по умолчанию срабатывает, если частота запросов превышает порог тревожного сигнала.
- Во время этого обратного вызова серверная часть Chat инициирует HTTP POST запрос к серверной части приложения.
- После получения запроса обратного вызова серверная часть приложения должна проверить, соответствует ли SDKAppID, содержащийся в URL запроса, его собственному SDKAppID.
- По другим вопросам безопасности см. [Обзор Webhook - Вопросы безопасности](https://intl.cloud.tencent.com/document/product/1047/34354).

### Описание API

#### Пример URL запроса

В следующем примере URL обратного вызова, настроенный в приложении, — это `https://www.example.com`
Пример:

```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&OptPlatform=$OptPlatform&contenttype=json
```

#### Параметры запроса

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса — HTTPS, метод запроса — POST. |
| www.example.com | URL обратного вызова |
| SdkAppid | SDKAppID, выделенный консолью Chat при создании приложения |
| CallbackCommand | Зафиксирован как Alert.RequestOverLimit |
| contenttype | Зафиксированное значение: JSON |
| OptPlatform | Платформа клиента. Значения см. в [Обзор Webhook - Протокол Webhook](https://intl.cloud.tencent.com/document/product/1047/34354) для определения параметра OptPlatform. |

#### Пример пакета запроса

```
{
    "CallbackCommand": "Alert.RequestOverLimit",
    "ServiceName": "openim",
    "Command": "batchsendmsg",
    "Request": 510,
    "Limit": 200
}
```

#### Поля пакета запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Зафиксирован как Alert.RequestOverLimit |
| ServiceName | String | Внутреннее имя сервиса API. Разные ServiceName соответствуют разным типам сервисов. |
| Command | String | Командное слово API, используется вместе с ServiceName для определения конкретных бизнес-функций. |
| Request | Integer | Частота QPS запроса API |
| Limit | Integer | Порог QPS запроса API |

#### Пример пакета ответа

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0}
```

#### Поля пакета ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ActionStatus | String | Результат обработки запроса: OK указывает на успешную обработку. FAIL указывает на ошибку обработки. |
| ErrorCode | Integer | Код ошибки |
| ErrorInfo | String | Описание ошибки |

## Ссылки

- [Обзор Webhook](https://intl.cloud.tencent.com/document/product/1047/34354)
- [RESTful APIs](https://intl.cloud.tencent.com/document/product/1047/34621)


---
*Источник: [https://trtc.io/document/60256](https://trtc.io/document/60256)*

---
*Источник (EN): [api-overclocking-alarm-callbacks.md](./api-overclocking-alarm-callbacks.md)*
