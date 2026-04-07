# После отправки группового сообщения

## Обзор функции

Это событие вебхука используется бэкэндом приложения для проверки сообщений пользователей в реальном времени. Бэкэнд приложения может быть уведомлен об успешной отправке сообщения и может синхронизировать данные по мере необходимости.

## Ограничения

- Для включения этого вебхука необходимо настроить URL обратного вызова и включить соответствующий переключатель для этого вебхука. Дополнительные сведения о методе конфигурации см. в разделе [Конфигурация вебхука](https://www.tencentcloud.com/document/product/647/74157).
- Во время этого события вебхука бэкэнд Chat инициирует HTTP POST запрос к бэкэнду приложения.
- После получения запроса вебхука бэкэнд приложения должен проверить, что `SDKAppID`, содержащийся в URL запроса, соответствует `SDKAppID` приложения.
- Дополнительные соображения безопасности см. в разделе **Security Considerations** (Соображения безопасности) в [Обзоре вебхука](https://www.tencentcloud.com/document/product/647/64412#security-considerations).

## Сценарии срабатывания вебхука

- Пользователь приложения отправляет групповое сообщение с клиента.
- Администратор приложения отправляет групповое сообщение через RESTful API.

## Время срабатывания вебхука

Вебхук срабатывает после успешной отправки группового сообщения.

## Описание вызова API

### Пример URL запроса

В следующем примере URL вебхука, настроенный в приложении, — это `https://www.example.com`.

**Пример:**

```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json&ClientIP=$ClientIP&OptPlatform=$OptPlatform
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса — HTTPS, метод запроса — POST. |
| www.example.com | URL вебхука |
| SdkAppid | `SDKAppID`, назначенный консолью Chat при создании приложения |
| CallbackCommand | Фиксированное значение: `Group.CallbackAfterSendMsg`. |
| contenttype | Фиксированное значение: `json`. |
| ClientIP | IP адрес клиента, например 127.0.0.1 |
| OptPlatform | Платформа клиента. Допустимые значения см. в описании `OptPlatform` в разделе **Callback Protocols** (Протоколы обратного вызова) в [Обзоре вебхука](https://www.tencentcloud.com/document/product/647/64412#d8e83f91-15ef-46e9-b370-9ba6c93a6ada). |

### Примеры запросов

```
{    "CallbackCommand": "Group.CallbackAfterSendMsg", // Webhook command    "GroupId": "@TGS#2J4SZEAEL", // Room ID    "Type": "Live", // Room type    "From_Account": "jared", // Sender    "Operator_Account":"admin", // Request initiator    "Random": 123456, // Random number    "MsgId": "144115233406643804-1727580296-4026038328", // Unique identifier of the message on the client    "MsgSeq": 123, // Sequence number of the message    "MsgTime": 1490686222, // Time of the message    "MsgBody": [ // Message body. For more information, see the `TIMMessage` message object.        {            "MsgType": "TIMTextElem", // Text            "MsgContent":{                "Text": "red packet"            }        }    ],    "CloudCustomData": "your cloud custom data",    "EventTime":"1670574414123"// Event trigger timestamp in milliseconds		}
```

### Поля запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда вебхука. |
| GroupId | String | ID группы, в которой генерируются групповые сообщения. |
| Type | String | Тип группы, в которой генерируются групповые сообщения. Фиксированное значение: `Live`. |
| From_Account | String | `UserID` отправителя сообщения. |
| Operator_Account | String | `UserID` инициатора запроса, по которому система может определить, инициирован ли запрос администратором. |
| Random | Integer | 32-битное случайное число в запросе. |
| MsgId | String | Уникальный идентификатор сообщения на клиенте. |
| MsgSeq | Integer | Номер последовательности сообщения, который уникально идентифицирует сообщение. Групповые сообщения сортируются по `MsgSeq`. Чем больше значение `MsgSeq`, тем ниже ранг сообщения. |
| MsgTime | Integer | Временная метка отправки сообщения, соответствующая времени бэкэнд-сервера. |
| MsgBody | Array | Тело сообщения. Содержание связано с запросом на отправку сообщения, подробно описано в разделах [Отправка обычного сообщения](https://www.tencentcloud.com/document/product/647/74353#f1db57c4-02dd-47ff-ae52-19e4e91d9c25) и [Отправка пользовательского сообщения](https://www.tencentcloud.com/document/product/647/74354#f1db57c4-02dd-47ff-ae52-19e4e91d9c25). |
| CloudCustomData | String | Пользовательские данные сообщения. Они сохраняются в облаке и будут отправлены получателю. Такие данные можно получить после удаления и переустановки приложения. Содержание связано с запросом на отправку сообщения, подробно описано в разделах [Отправка обычного сообщения](https://www.tencentcloud.com/document/product/647/74353#f1db57c4-02dd-47ff-ae52-19e4e91d9c25). |
| EventTime | Integer | Временная метка срабатывания события в миллисекундах. |

> **Примечание:** После отправки сообщения в группе используется возможность обратного вызова сообщений группы IM. В обратном вызове `MsgBody` и `CloudCustomData` являются результатом упаковки запроса на отправку сообщения. Подробности см. в разделах [Отправка обычного сообщения](https://www.tencentcloud.com/document/product/647/74353#f1db57c4-02dd-47ff-ae52-19e4e91d9c25) и [Отправка пользовательского сообщения](https://www.tencentcloud.com/document/product/647/74354#f1db57c4-02dd-47ff-ae52-19e4e91d9c25).

### Пример ответа

Ответ отправляется после синхронизации данных бэкэндом приложения.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0 //The value `0` indicates that the webhook result is ignored.}
```

### Поля ответа

| Поле | Тип | Обязательное | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Да | Результат запроса. `OK`: успешно; `FAIL`: ошибка. |
| ErrorCode | Integer | Да | Код ошибки. Значение `0` указывает на то, что результат вебхука игнорируется. |
| ErrorInfo | String | Да | Информация об ошибке. |

## Ссылки

- [Обзор вебхука](https://www.tencentcloud.com/document/product/647/64412)


---
*Источник: [https://trtc.io/document/74348](https://trtc.io/document/74348)*

---
*Источник (EN): [after-group-message-is-sent.md](./after-group-message-is-sent.md)*
