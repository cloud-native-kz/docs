# После отправки группового сообщения

## Обзор функции

Это событие webhook используется бэкэндом приложения для проверки групповых сообщений пользователей в реальном времени. Бэкэнд приложения может получать уведомления об успешной отправке группового сообщения и синхронизировать данные по мере необходимости.

## Ограничения

- Чтобы включить этот webhook, вы должны настроить URL-адрес обратного вызова и включить соответствующий переключатель для этого webhook. Дополнительные сведения о методе конфигурации см. в разделе [Конфигурация Webhook](https://intl.cloud.tencent.com/document/product/1047/34520).
- Во время этого события webhook бэкэнд Chat инициирует HTTP-запрос POST к бэкэнду приложения.
- После получения запроса webhook бэкэнд приложения должен проверить, что `SDKAppID`, содержащийся в URL-адресе запроса, является `SDKAppID` приложения.
- Для получения дополнительной информации о соображениях безопасности см. раздел **Соображения безопасности** в [Обзоре Webhook](https://intl.cloud.tencent.com/document/product/1047/34354).

## Сценарии срабатывания Webhook

- Пользователь приложения отправляет групповое сообщение с клиента.
- Администратор приложения отправляет групповое сообщение через RESTful API.

## Время срабатывания Webhook

Webhook срабатывает после успешной отправки группового сообщения.

## Описание вызова API

### Пример URL запроса

В следующем примере webhook URL, настроенный в приложении, — это `https://www.example.com`.
**Пример:**

```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json&ClientIP=$ClientIP&OptPlatform=$OptPlatform
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса — HTTPS, метод запроса — POST. |
| www.example.com | URL-адрес Webhook |
| SdkAppid | `SDKAppID`, назначенный консолью Chat при создании приложения |
| CallbackCommand | Фиксированное значение: `Group.CallbackAfterSendMsg`. |
| contenttype | Фиксированное значение: `json`. |
| ClientIP | IP-адрес клиента, например 127.0.0.1 |
| OptPlatform | Платформа клиента. Допустимые значения см. в описании `OptPlatform` в разделе **Протоколы обратного вызова** в [Обзоре Webhook](https://intl.cloud.tencent.com/document/product/1047/34354). |

### Примеры запросов

```
{    "CallbackCommand": "Group.CallbackAfterSendMsg", // Webhook command    "GroupId": "@TGS#2J4SZEAEL", // Group ID    "Type": "Public", // Group type    "From_Account": "jared", // Sender    "Operator_Account":"admin", // Request initiator    "Random": 123456, // Random number    "MsgId": "144115233406643804-1727580296-4026038328", // Unique identifier of the message on the client    "MsgSeq": 123, // Sequence number of the message    "MsgTime": 1490686222, // Time of the message    "OnlineOnlyFlag": 1, // The value is `1` if it is an online message and `0` (default) if itâs not. For audio-video groups, the value is `0`.    "MsgBody": [ // Message body. For more information, see the `TIMMessage` message object.        {            "MsgType": "TIMTextElem", // Text            "MsgContent":{                "Text": "red packet"            }        }    ],    "CloudCustomData": "your cloud custom data",    "EventTime":"1670574414123"// Event trigger timestamp in milliseconds		}
```

### Поля запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда Webhook. |
| GroupId | String | ID группы, которая генерирует групповые сообщения. |
| Type | String | Тип группы, которая генерирует групповые сообщения, например `Public`. Дополнительные сведения см. в разделе **Типы групп** в [Система групп](https://intl.cloud.tencent.com/document/product/1047/33529). |
| From_Account | String | `UserID` отправителя сообщения. |
| Operator_Account | String | `UserID` инициатора запроса, на основании которого система может определить, инициирован ли запрос администратором. |
| Random | Integer | 32-битное случайное число в запросе. |
| MsgId | String | Уникальный идентификатор сообщения на клиенте. |
| MsgSeq | Integer | Номер последовательности сообщения, который однозначно идентифицирует сообщение. Групповые сообщения сортируются по `MsgSeq`. Чем больше значение `MsgSeq`, тем ниже ранг сообщения. |
| MsgTime | Integer | Временная метка отправки сообщения, соответствующая времени бэкэнд-сервера. |
| OnlineOnlyFlag | Integer | Значение `1`, если это онлайн-сообщение, и `0` (по умолчанию), если это не так. Для аудиовидео-групп значение равно `0`. |
| MsgBody | Array | Тело сообщения. Дополнительные сведения см. в разделе [Форматы сообщений](https://intl.cloud.tencent.com/document/product/1047/33527). |
| CloudCustomData | String | Пользовательские данные сообщения. Они сохраняются в облаке и будут отправлены получателю. Такие данные можно получить после удаления и переустановки приложения. |
| TopicId | String | ID темы, которая указывает на отправку сообщения в теме и применяется только к сообществам с включенными темами. |
| EventTime | Integer | Временная метка срабатывания события в миллисекундах. |
| GroupAtInfo | Array | Информация об упоминании (@) в этом сообщении. GroupAtAllFlag = 1 указывает @all; GroupAtAllFlag = 0 указывает конкретные упомянутые члены. GroupAt_Account представляет конкретно упомянутых членов. В настоящее время одновременно можно упомянуть максимум 30 членов. |

### Пример ответа

Ответ отправляется после синхронизации данных бэкэндом приложения.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0 //The value `0` indicates that the webhook result is ignored.}
```

### Поля ответа

| Поле | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Да | Результат запроса. `OK`: успешно; `FAIL`: ошибка. |
| ErrorCode | Integer | Да | Код ошибки. Значение `0` указывает, что результат webhook игнорируется. |
| ErrorInfo | String | Да | Информация об ошибке. |

## Ссылки

- [Обзор Webhook](https://intl.cloud.tencent.com/document/product/1047/34354)
- RESTful API: [Отправка обычных сообщений в группу](https://intl.cloud.tencent.com/document/product/1047/34959)


---
*Источник: [https://trtc.io/document/34375](https://trtc.io/document/34375)*

---
*Источник (EN): [after-a-group-message-is-sent.md](./after-a-group-message-is-sent.md)*
