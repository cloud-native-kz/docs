# После отписки пользователя

## Описание функции

Backend приложения может просматривать ситуации отписки пользователя в реальном времени через этот webhook.

## Примечания

- Для включения этого webhook необходимо настроить URL webhook и включить соответствующий переключатель для этого webhook. Дополнительные сведения о методе конфигурации см. в разделе [Конфигурация Webhook](https://www.tencentcloud.com/document/product/647/74157).
- Во время этого webhook backend Chat инициирует HTTP POST запрос к backend приложения.
- После получения запроса webhook backend приложения должен проверить, является ли SDKAppID, содержащийся в URL запроса, SDKAppID приложения.
- Дополнительные соображения безопасности см. в разделе **Security Considerations** в [Обзор Webhook](https://www.tencentcloud.com/document/product/647/64412#security-considerations).

## Сценарии срабатывания Webhook

- Пользователь приложения отправляет запрос на отписку через клиент.
- Администратор приложения отправляет запрос на отписку через REST API.

## Время срабатывания Webhook

Срабатывает при успешной отписке.

## Описание вызова API

### Пример URL запроса

В следующем примере URL webhook, настроенный для приложения, — это `https://www.example.com`. **Пример:**

```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json&ClientIP=$ClientIP&OptPlatform=$OptPlatform
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса — HTTPS, метод запроса — POST. |
| www.example.com | URL webhook. |
| SdkAppid | SDKAppID, назначенный приложению при его создании в консоли Chat. |
| CallbackCommand | Фиксированное значение: Follow.CallbackAfterFollowDelete. |
| contenttype | Фиксированное значение: `json`. |
| ClientIP | IP-адрес клиента. Например, 127.0.0.1. |
| OptPlatform | Платформа клиента. Допустимые значения см. в описании `OptPlatform` в разделе **Webhook Protocols** в [Обзор Webhook](https://www.tencentcloud.com/document/product/647/64412#d8e83f91-15ef-46e9-b370-9ba6c93a6ada). |

### Пример запросов

```
{  "CallbackCommand": "Follow.CallbackAfterFollowDelete",  "From_Account": "UserID_001",  "To_Account": [    "UserID_002",    "UserID_003"  ],  "EventTime": 1702018343678}
```

### Поля запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда webhook. |
| From_Account | String | UserID пользователя, который инициировал операцию отписки. |
| To_Account | Array | Массив объектов пользователей, которые успешно отписались. |
| EventTime | Integer | Временная метка срабатывания события в миллисекундах. |

### Пример ответа

```
{    "ActionStatus": "OK",    "ErrorCode": 0,    "ErrorInfo": ""}
```

### Поля ответа

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Обязательно | Результат обработки запроса: OK: обработка успешна. FAIL: ошибка обработки. |
| ErrorCode | Integer | Обязательно | Код ошибки: 0: обработка успешна. Ненулевое значение: ошибка обработки. |
| ErrorInfo | String | Обязательно | Сообщение об ошибке. |

## Ссылки

[Обзор Webhook](https://www.tencentcloud.com/document/product/1047/34354)


---
*Источник: [https://trtc.io/document/74357](https://trtc.io/document/74357)*

---
*Источник (EN): [after-a-user-is-unfollowed.md](./after-a-user-is-unfollowed.md)*
