# После настройки расширения сообщения в личной переписке

## Обзор функции

Этот webhook позволяет вашему серверному приложению отслеживать операции расширения сообщений пользователя в личных чатах (C2C) в режиме реального времени.

## Примечания

- Для получения этого webhook необходимо настроить URL обратного вызова и включить соответствующий переключатель. Подробные инструкции по настройке см. в разделе [Обзор webhook](https://www.tencentcloud.com/document/product/1047/34354).
- Серверная часть Chat отправляет HTTPS POST запросы на ваш серверный адрес. После получения запроса webhook убедитесь, что параметр `SDKAppID` совпадает с SDKAppID вашего приложения. Дополнительные соображения безопасности см. в разделе [Обзор webhook: соображения безопасности](https://www.tencentcloud.com/document/product/1047/34354#security-considerations).

## Сценарии срабатывания webhook

Этот webhook срабатывает, когда расширения сообщений устанавливаются для личных чатов через:

- **Client SDK:** пользователи настраивают расширения сообщений через клиента.
- **REST API:** администраторы настраивают расширения сообщений с помощью [Установить расширение сообщения](https://www.tencentcloud.com/document/product/1047/51195).

## Время срабатывания webhook

Webhook срабатывает **после** успешной установки расширения сообщения C2C.

## Описание API

### Пример URL запроса

В следующем примере URL обратного вызова, настроенный для приложения: `https://www.example.com`.

**Пример:**

```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json&ClientIP=$ClientIP&OptPlatform=$OptPlatform
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| HTTPS | Протокол запроса — HTTPS, метод запроса — POST. |
| www.example.com | URL обратного вызова. |
| SDKAppID | SDKAppID, назначенный в консоли chat при создании приложения. |
| CallbackCommand | Фиксированное значение: `C2C.CallbackAfterC2CMsgExtension`. |
| contenttype | Тело запроса зафиксировано как `JSON`. |
| ClientIP | IP адрес клиента (например, `127.0.0.1`). |
| OptPlatform | Платформа клиента. Допустимые значения см. в описании параметра `OptPlatform` в разделе [Протокол webhook](https://www.tencentcloud.com/document/product/1047/34354#webhook-protocol). |

### Пример запроса

```
// Set Message Extension KV{  "CallbackCommand": "C2C.CallbackAfterC2CMsgExtension",  "From_Account":"user1",  "To_Account":"user2",  "MsgKey":"93847636_1287657_1764688415",  "OperateType":1,  "ExtensionList":[    {"Key":"k1","Value":"v1","Seq":1}, // Version number of a single KV    {"Key":"k2","Value":"v2","Seq":1},    {"Key":"k3","Value":"v3","Seq":1}  ],  "Seq":1,  // Represents the latest version number of the entire message  "EventTime":1764688540182}// Delete message extensions KV{  "CallbackCommand": "C2C.CallbackAfterC2CMsgExtension", // Callback command  "From_Account":"user1",  "To_Account":"user2",  "MsgKey":"93847636_1287657_1764688415",  "OperateType":2,  "ExtensionList":[    {"Key":"k1","Value":"","Seq":2},     {"Key":"k2","Value":"","Seq":2},    {"Key":"k3","Value":"","Seq":2}  ],  "Seq":2, // Represents the latest version number of the entire message  "EventTime":1764688641499}// Clear message extensions KV{  "CallbackCommand": "C2C.CallbackAfterC2CMsgExtension", // Callback command  "From_Account":"user1",  "To_Account":"user2",  "MsgKey":"93847636_1287657_1764688415",  "OperateType":3,  "ExtensionList":[],  "Seq":3, // Represents the latest version number of the entire message  "EventTime":1764688662721}
```

### Поля запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда обратного вызова. |
| From_Account | String | UserID отправителя сообщения. |
| To_Account | String | UserID получателя сообщения. |
| MsgKey | String | Уникальный идентификатор сообщения. |
| OperateType | Integer | 1: установить пары ключ-значение (KV) расширения сообщения. 2: удалить KV расширения сообщения. 3: очистить все KV расширения сообщения. |
| ExtensionList | Array | Пара ключ-значение расширения сообщения. |
| Seq | Integer | Номер версии. |
| EventTime | Integer | Временная метка срабатывания события в миллисекундах. |

### Пример ответа

```
{  "ActionStatus": "OK",  "ErrorInfo": "",  "ErrorCode": 0 // 0: callback successful; 1: callback error.}
```

### Поля ответа

| Поле | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Да | Результат обработки запроса: OK: успешно обработано. FAIL: обработка не удалась. |
| ErrorCode | Integer | Да | Код ошибки: 0: обратный вызов успешно обработан. 1: ошибка обработки обратного вызова. |
| ErrorInfo | String | Да | Сообщение об ошибке. |

## Ссылки

- [Обзор webhook](https://www.tencentcloud.com/document/product/1047/34354)
- REST API: [Установить расширение сообщения](https://www.tencentcloud.com/document/product/1047/51195)


---
*Источник: [https://trtc.io/document/76006](https://trtc.io/document/76006)*

---
*Источник (EN): [after-a-one-to-one-message-extension-is-configured.md](./after-a-one-to-one-message-extension-is-configured.md)*
