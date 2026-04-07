# Webhook для исключений при отправке групповых сообщений

## Обзор функции

Этот callback позволяет отслеживать исключения на бэкенде приложения при отправке групповых сообщений, включая:

- Отправленное сообщение содержит неправильный параметр (например, ID группы не существует).
- Частота отправки сообщений превышает лимит.
- Отправленное сообщение признано несоответствующим после фильтрации контента.
- Отправитель заблокирован.

## Примечания

- Для включения этого callback необходимо настроить URL callback и включить соответствующий переключатель для этого callback. Для получения дополнительной информации о методе конфигурации см. [Конфигурация callback](https://intl.cloud.tencent.com/document/product/1047/34520).
- Во время этого callback бэкенд Chat инициирует HTTP POST запрос к бэкенду приложения.
- После получения запроса callback бэкенд приложения должен проверить, является ли `SDKAppID`, содержащийся в URL запроса, `SDKAppID` приложения.
- Дополнительные соображения безопасности см. в разделе **Security Considerations** в [Обзор сторонних callback](https://intl.cloud.tencent.com/document/product/1047/34354).

## Сценарии срабатывания callback

- Пользователь приложения отправляет групповое сообщение с клиента.
- Администратор приложения отправляет групповое сообщение через вызов RESTful API.

## Время срабатывания callback

Будет срабатывать после того, как бэкенд Chat не удастся доставить групповое сообщение членам группы.

## Описание вызова API

### Пример URL запроса

В следующем примере URL callback, настроенный в приложении, — `https://www.example.com`.
**Пример:**

```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json&ClientIP=$ClientIP&OptPlatform=$OptPlatform
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса — HTTPS, метод запроса — POST. |
| www.example.com | URL callback |
| SdkAppid | `SDKAppID`, назначенный консолью Chat при создании приложения |
| CallbackCommand | Фиксированное значение: `Group.CallbackSendMsgException`. |
| contenttype | Фиксированное значение: `JSON`. |
| OptPlatform | Платформа клиента. Допустимые значения см. в описании `OptPlatform` в разделе **Callback Protocols** [Обзор сторонних callback](https://intl.cloud.tencent.com/document/product/1047/34354). |

### Пример запроса

```
{    "CallbackCommand": "Group.CallbackSendMsgException", // Команда callback    "GroupId": "@TGS#2J4SZEAEL", // ID группы    "Type": "Public", // Тип группы    "From_Account": "jared", // Отправитель    "Operator_Account":"admin", // Инициатор запроса    "Random": 123456, // Случайное число    "OnlineOnlyFlag": 1, // Значение `1`, если это онлайн сообщение, и `0` (по умолчанию), если это не так. Для аудиовидео групп значение `0`.    "MsgBody": [ // Тело сообщения. Дополнительную информацию см. в объекте сообщения `TIMMessage`.        {            "MsgType": "TIMTextElem", // Текст            "MsgContent":{                "Text": "red packet"            }        }    ],    "CloudCustomData": "your cloud custom data",    "ErrorCode": 10023, // Код ошибки исключения сообщения    "ErrorInfo": "msg count exceeds limit,please retry later", // Детали исключения сообщения    "EventTime":"1670574414123"// Временная метка срабатывания события в миллисекундах}
```

### Поля запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда callback |
| GroupId | String | ID группы, которая генерирует групповые сообщения |
| Type | String | Тип группы, которая генерирует групповые сообщения, например `Public`. Подробности см. в разделе **Group Types** [Система групп](https://intl.cloud.tencent.com/document/product/1047/33529). |
| From_Account | String | `UserID` отправителя сообщения |
| Operator_Account | String | UserID инициатора запроса, по которому система может определить, инициирован ли запрос администратором. |
| Random | Integer | 32-битное случайное число в запросе |
| OnlineOnlyFlag | Integer | Значение `1`, если это онлайн сообщение, и `0` (по умолчанию), если это не так. Для аудиовидео групп значение `0`. |
| MsgBody | Array | Тело сообщения. Дополнительную информацию см. в [Форматы сообщений](https://intl.cloud.tencent.com/document/product/1047/33527). |
| CloudCustomData | String | Пользовательские данные сообщения. Они сохраняются в облаке и будут отправлены другой стороне. Такие данные можно получить после удаления и переустановки приложения. |
| ErrorCode | Interger | Код ошибки исключения сообщения. Дополнительную информацию см. в [Коды ошибок](https://intl.cloud.tencent.com/document/product/1047/34348). |
| ErrorInfo | String | Детали исключения сообщения |
| EventTime | Integer | Временная метка срабатывания события в миллисекундах |

### Пример ответа

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0}
```

### Поля ответа

| Поле | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Да | Результат запроса. Фиксированное значение: `OK`. |
| ErrorCode | Integer | Да | Код ошибки. Фиксированное значение: `0`. |
| ErrorInfo | String | Да | Сообщение об ошибке. Фиксированное значение: пустая строка. |

## Ссылки

- [Обзор сторонних callback](https://intl.cloud.tencent.com/document/product/1047/34354)
- RESTful API: [Отправка обычных сообщений в группе](https://intl.cloud.tencent.com/document/product/1047/34959)


---
*Источник: [https://trtc.io/document/49462](https://trtc.io/document/49462)*

---
*Источник (EN): [webhook-for-exceptions-when-group-messages-are-sent.md](./webhook-for-exceptions-when-group-messages-are-sent.md)*
