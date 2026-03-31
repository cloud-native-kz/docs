# Перед ответом на запрос дружбы

## Описание функции

Этот API используется бэкендом приложения для:

- Просмотра ответов на запросы дружбы в реальном времени.
- Блокировки вредоносных ответов на запросы дружбы.

## Примечания

- Для включения этого обратного вызова необходимо настроить URL обратного вызова и включить соответствующий протокол. Дополнительные сведения о методе конфигурации см. в разделе [Конфигурация обратного вызова](https://intl.cloud.tencent.com/document/product/1047/34520).
- При выполнении этого обратного вызова бэкенд Chat инициирует HTTP POST запрос на бэкенд приложения.
- После получения запроса обратного вызова бэкенд приложения должен проверить, является ли `SDKAppID`, содержащийся в URL запроса, `SDKAppID` приложения.
- Дополнительные рекомендации по безопасности см. в разделе **Рекомендации по безопасности** в статье [Обзор обратных вызовов третьих сторон](https://intl.cloud.tencent.com/document/product/1047/34354).

## Сценарии срабатывания обратного вызова

- Пользователь приложения инициирует ответ на принятие или отклонение запроса дружбы.

## Время срабатывания обратного вызова

Бэкенд Chat получает ответ от пользователя приложения на запрос дружбы.

> **Внимание:** Ответы, инициированные через вызовы RESTful API к запросам дружбы, не будут срабатывать обратный вызов.

## Описание вызова API

### Пример URL запроса

В следующем примере URL обратного вызова, настроенный в приложении, — это `https://www.example.com`.
**Пример:**

```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json&ClientIP=$ClientIP&OptPlatform=$OptPlatform
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса — HTTPS, метод запроса — POST. |
| www.example.com | URL обратного вызова |
| SdkAppid | `SDKAppID`, назначенный консолью Chat при создании приложения |
| CallbackCommand | Всегда `Sns.CallbackPrevFriendResponse` |
| contenttype | Всегда `json` |
| ClientIP | IP-адрес клиента, например 127.0.0.1 |
| OptPlatform | Платформа клиента. Допустимые значения см. в описании `OptPlatform` в разделе **Протоколы обратного вызова** статьи [Обзор обратных вызовов третьих сторон](https://intl.cloud.tencent.com/document/product/1047/34354). |

### Пример запроса

```
{  "CallbackCommand": "Sns.CallbackPrevFriendResponse",  "Requester_Account": "id",  "From_Account": "id",  "ResponseFriendItem": [    {      "To_Account": "id1",      "Remark": "remark1",      "TagName": "group1",      "ResponseAction": "Response_Action_AgreeAndAdd"    },    {      "To_Account": "id2",      "Remark": "remark2",      "TagName": "group2",      "ResponseAction": "Response_Action_Reject"    }  ],  "EventTime": 1631777645424}
```

### Поля запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда обратного вызова |
| Requester_Account | String | `UserID` пользователя, инициирующего запрос дружбы |
| From_Account | String | `UserID` пользователя, ответившего на запрос дружбы |
| ResponseFriendItem | Array | Параметр ответа на запрос дружбы |
| To_Account | String | `UserID` пользователя, отправившего запрос дружбы |
| Remark | String | Замечание для друга, установленное `From_Account` для `To_Account`. Дополнительные сведения см. в разделе **Стандартные поля друга** в статье [Управление контактами](https://intl.cloud.tencent.com/document/product/1047/33521). |
| TagName | String | Список друзей, установленный `From_Account` для `To_Account`. Дополнительные сведения см. в разделе **Стандартные поля друга** в статье [Управление контактами](https://intl.cloud.tencent.com/document/product/1047/33521). |
| ResponseAction | String | Способ ответа. Допустимые значения:`Response_Action_AgreeAndAdd`: принять запрос дружбы и добавить другую сторону в друзья.`Response_Action_Agree`: согласиться позволить другой стороне добавить вас в друзья.`Response_Action_Reject`: отклонить запрос дружбы. |
| EventTime | Integer | Временная метка в миллисекундах |

### Пример ответа

```
{  "ActionStatus": "OK",  "ErrorCode": 0,  "ErrorInfo": "",  "ResultItem": [    {      "To_Account": "id1",      "ResultCode": 0,      "ResultInfo": ""    },    {      "To_Account": "id2",      "ResultCode": 0,      "ResultInfo": ""    }  ]}
```

### Поля ответа

| Поле | Тип | Требуется | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Да | Результат запроса. `OK`: успешно; `FAIL`: ошибка |
| ErrorCode | Integer | Да | Код ошибки. Допустимые значения:`0`: обработка бэкендом приложения успешна.Другие значения: обработка бэкендом приложения не удалась. Бэкенд Chat по умолчанию игнорирует эту ошибку.При неудачной обработке установите код ошибки в диапазон [38000, 39000]. |
| ErrorInfo | String | Да | Информация об ошибке |
| ResultItem | Array | Да | Результат обработки от бэкенда приложения |
| To_Account | String | Да | `UserID` пользователя, инициирующего запрос дружбы |
| ResultCode | Integer | Да | Код результата. Допустимые значения:`0`: разрешить добавление в друзья.Другие значения: не разрешать добавление в друзья.Чтобы не разрешить добавление в друзья, установите код результата в диапазон [38000, 39000]. |
| ResultInfo | String | Да | Информация об ошибке |

## Ссылки

- [Обзор обратных вызовов третьих сторон](https://intl.cloud.tencent.com/document/product/1047/34354)
- [Добавление друзей](https://intl.cloud.tencent.com/document/product/1047/34902)


---
*Источник: [https://trtc.io/document/43467](https://trtc.io/document/43467)*

---
*Источник (EN): [before-a-friend-request-is-responded.md](./before-a-friend-request-is-responded.md)*
