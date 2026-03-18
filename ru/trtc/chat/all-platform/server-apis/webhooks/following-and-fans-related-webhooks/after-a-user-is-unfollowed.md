# После отписания пользователя

## Описание функции

Бэкенд приложения может просматривать ситуации отписания пользователей в реальном времени через этот вебхук.

## Примечания

- Для активации этого вебхука необходимо настроить URL вебхука и включить соответствующий переключатель для этого вебхука. Дополнительную информацию о методе настройки см. в разделе [Конфигурация вебхука](https://www.tencentcloud.com/document/product/1047/34520).
- Во время этого вебхука бэкенд Chat инициирует HTTP POST запрос к бэкенду приложения.
- После получения запроса вебхука бэкенд приложения должен проверить, совпадает ли SDKAppID, содержащийся в URL запроса, с SDKAppID приложения.
- Дополнительные сведения о безопасности см. в разделе **Security Considerations** (Рассмотрение вопросов безопасности) в документе [Обзор вебхуков](https://www.tencentcloud.com/document/product/1047/34354).

## Сценарии активации вебхука

- Пользователь приложения отправляет запрос на отписку через клиент.
- Администратор приложения отправляет запрос на отписку через REST API.

## Время активации вебхука

Активируется при успешной отписке.

## Описание вызова API

### Примеры URL запроса

В следующем примере URL вебхука, настроенный для приложения, — `https://www.example.com`. **Пример:**

```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json&ClientIP=$ClientIP&OptPlatform=$OptPlatform
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса — HTTPS, метод запроса — POST. |
| www.example.com | URL вебхука. |
| SdkAppid | SDKAppID, назначенный приложению при его создании в консоли Chat. |
| CallbackCommand | Фиксировано: Follow.CallbackAfterFollowDelete. |
| contenttype | Фиксированное значение: `json`. |
| ClientIP | IP-адрес клиента. Например, 127.0.0.1. |
| OptPlatform | Платформа клиента. Допустимые значения см. в описании `OptPlatform` в разделе **Webhook Protocols** (Протоколы вебхука) в документе [Обзор вебхуков](https://www.tencentcloud.com/document/product/1047/34354#webhook-protocol). |

### Примеры запросов

```
{  "CallbackCommand": "Follow.CallbackAfterFollowDelete",  "From_Account": "UserID_001",  "To_Account": [    "UserID_002",    "UserID_003"  ],  "EventTime": 1702018343678}
```

### Поля запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда вебхука. |
| From_Account | String | UserID пользователя, инициировавшего операцию отписки. |
| To_Account | Array | Массив объектов пользователей, которые успешно отписались. |
| EventTime | Integer | Временная метка активации события в миллисекундах. |

### Примеры ответов

```
{    "ActionStatus": "OK",    "ErrorCode": 0,    "ErrorInfo": ""}
```

### Поля ответа

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Обязательно | Результат обработки запроса: OK: обработка успешна. FAIL: обработка не успешна. |
| ErrorCode | Integer | Обязательно | Код ошибки: 0: обработка успешна. Ненулевое значение: обработка не успешна. |
| ErrorInfo | String | Обязательно | Сообщение об ошибке. |

## Ссылки

[Обзор вебхуков](https://www.tencentcloud.com/document/product/1047/34354)


---
*Источник: [https://trtc.io/document/70356](https://trtc.io/document/70356)*

---
*Источник (EN): [after-a-user-is-unfollowed.md](./after-a-user-is-unfollowed.md)*
