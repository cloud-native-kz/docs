# После настройки расширения группового сообщения

## Обзор функции

Этот webhook позволяет вашему бэкенду приложения отслеживать операции расширения сообщений пользователей в групповых чатах в реальном времени.

## Примечания

- Чтобы получить этот webhook, вы должны настроить URL обратного вызова и включить соответствующий переключатель. Подробные инструкции по настройке см. в разделе [Обзор Webhook](https://www.tencentcloud.com/document/product/1047/34354).
- Бэкенд Chat отправляет HTTPS POST запросы на ваш бэкенд приложения. После получения запроса webhook убедитесь, что параметр `SDKAppID` совпадает с SDKAppID вашего приложения. Дополнительные рекомендации по безопасности см. в разделе [Обзор Webhook: Соображения безопасности](https://www.tencentcloud.com/document/product/1047/34354#security-considerations).

## Сценарии запуска Webhook

Этот webhook запускается при установке расширений сообщений для групповых чатов следующими способами:

- **Client SDK:** пользователи настраивают расширения сообщений через клиент.
- **REST API:** администраторы настраивают расширения сообщений с помощью [Set Group Message Extension](https://www.tencentcloud.com/document/product/1047/52170).

## Время запуска Webhook

Webhook срабатывает **после** успешной установки расширения группового сообщения.

## Описание API

### Пример URL запроса

В следующем примере URL обратного вызова, настроенный для приложения, это `https://www.example.com`.

**Пример:**

```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json&ClientIP=$ClientIP&OptPlatform=$OptPlatform
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса — HTTPS, метод запроса — POST. |
| www.example.com | URL обратного вызова. |
| SDKAppID | SDKAppID, назначенный в консоли чата при создании приложения. |
| CallbackCommand | Фиксировано: `Group.CallbackAfterGroupMsgExtension`. |
| contenttype | Тело запроса фиксировано как `JSON`. |
| ClientIP | IP-адрес клиента (например, `127.0.0.1`). |
| OptPlatform | Платформа клиента. Допустимые значения см. в описании параметра OptPlatform в [Протокол Webhook](https://www.tencentcloud.com/document/product/1047/34354#webhook-protocol). |

### Пример запроса

```
// Set Message Extension KV{  "CallbackCommand": "Group.CallbackAfterGroupMsgExtension",  "GroupId":"test",  "MsgSeq":10,  "OperateType":1,  "ExtensionList":[    {"Key":"key2","Value":"value2","Seq":56},  // Version number of a single KV    {"Key":"key3","Value":"12122","Seq":56}  ],  "Seq":56, // Represents the latest version number of the entire message  "EventTime":1764688294360}// Delete Message Extension KV{  "CallbackCommand": "Group.CallbackAfterGroupMsgExtension",  "GroupId":"test",  "MsgSeq":10,  "OperateType":2,  "ExtensionList":[    {"Key":"key2","Value":"","Seq":57},    {"Key":"key3","Value":"","Seq":57}  ],  "Seq":57, // Represents the latest version number of the entire message  "EventTime":1764688312045}// Clear Message Extension KV{  "CallbackCommand": "Group.CallbackAfterGroupMsgExtension",  "GroupId":"test",  "MsgSeq":10,  "OperateType":3,  "ExtensionList":[],  "Seq":58, // Represents the latest version number of the entire message  "EventTime":1764688329047}
```

### Поля запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда обратного вызова. |
| GroupId | String | ID группы. |
| MsgSeq | Integer | Seq группового сообщения. |
| OperateType | Integer | 1: установка пар ключ-значение (KV) расширения сообщения. 2: удаление KV расширения сообщения. 3: очистка всех KV расширения сообщения. |
| ExtensionList | Array | Массив пар ключ-значение расширения сообщения. |
| Seq | Integer | Номер версии. |
| EventTime | Integer | Временная метка триггера события в миллисекундах. |

### Пример ответа

```
{  "ActionStatus": "OK",  "ErrorInfo": "",  "ErrorCode": 0 // 0: callback successful; 1: callback error.}
```

### Поля ответа

| Поле | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Да | Результат обработки запроса: OK: успешно обработан. FAIL: обработка не удалась. |
| ErrorCode | Integer | Да | Код ошибки: 0: callback успешно обработан. 1: ошибка обработки callback. |
| ErrorInfo | String | Да | Сообщение об ошибке. |

## Ссылки

- [Обзор Webhook](https://www.tencentcloud.com/document/product/1047/34354)
- REST API: [Set Group Message Extension](https://www.tencentcloud.com/document/product/1047/52170)


---
*Источник: [https://trtc.io/document/76007](https://trtc.io/document/76007)*

---
*Источник (EN): [after-a-group-message-extension-is-configured.md](./after-a-group-message-extension-is-configured.md)*
