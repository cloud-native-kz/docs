# Обратный вызов после отправки сообщения в официальный канал

## Обзор функции

Бэкенд приложения может использовать этот webhook для проверки сообщений трансляции официального канала в реальном времени, включая уведомления об успешной отправке бэкендом приложения сообщения в официальный канал, что позволяет приложению выполнять необходимую синхронизацию данных.

## Примечания

- Для включения webhook необходимо настроить URL-адрес Webhook и включить соответствующий переключатель для этого webhook. Дополнительную информацию о методе конфигурации см. в разделе [Конфигурация Webhook](https://www.tencentcloud.com/document/product/1047/34520).
- Во время этого события webhook бэкенд Chat инициирует HTTP POST-запрос к бэкенду приложения.
- После получения запроса webhook бэкенд приложения должен проверить, является ли SDKAppID, содержащийся в URL-адресе запроса, значением `SDKAppID` приложения.
- Дополнительные рекомендации по безопасности см. в документе [Обзор Webhook: Рекомендации по безопасности](https://www.tencentcloud.com/document/product/1047/34354).

## Сценарии срабатывания Webhook

- Пользователь приложения отправляет сообщение официального аккаунта через клиент.
- Администратор приложения отправляет сообщение официального аккаунта через RESTful API.

## Время срабатывания Webhook

Webhook срабатывает после доставки бэкендом Chat сообщения официального канала подписчикам.

## Описание вызова API

### Пример URL-адреса запроса

В последующем примере URL-адрес webhook, настроенный в приложении, — это `https://www.example.com`.
**Пример:**

```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json&ClientIP=$ClientIP&OptPlatform=$OptPlatform
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса — HTTPS, метод запроса — POST. |
| www.example.com | URL-адрес Webhook. |
| SdkAppid | SDKAppID, назначенный консолью Chat при создании приложения. |
| CallbackCommand | Установить значение OfficialAccount.CallbackAfterSendMsg. |
| contenttype | Фиксированное значение: JSON. |
| ClientIP | IP-адрес клиента, например: 127.0.0.1. |
| OptPlatform | Платформа клиента, значения см. в [Обзор Webhook: Протокол Webhook](https://www.tencentcloud.com/document/product/1047/34354) для получения значения параметра OptPlatform. |

### Пример запроса

```
{    "CallbackCommand": "OfficialAccount.CallbackAfterSendMsg", // Команда webhook    "Official_Account": "@TOA#_2J4SZEAEL", // ID официального аккаунта    "MsgKey": "71_1_1698741698", // Уникальный идентификатор сообщения, может использоваться для отзыва сообщений официального аккаунта через REST API    "MsgTime": 1490686222, // Время отправки сообщения    "OnlineOnlyFlag": 1, // Значение `1`, если это онлайн-сообщение, и `0`, если нет    "MsgBody": [ // Тело сообщения, см. объект TIMMessage        {            "MsgType": "TIMTextElem", // Текст            "MsgContent": {                "Text": "red packet"            }        }    ],    "CloudCustomData": "your cloud custom data",    "EventTime": 1670574414123 // Уровень миллисекунд, временная метка срабатывания события		}
```

### Поля запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда webhook. |
| Official_Account | String | ID пользователя официального аккаунта. |
| MsgKey | String | Уникальный идентификатор этого сообщения, который может использоваться для [отзыва сообщений официального аккаунта](https://www.tencentcloud.com/document/product/1047/60811). |
| MsgTime | Integer | Временная метка сообщения, соответствующая серверному времени. |
| OnlineOnlyFlag | Integer | Онлайн-сообщение, `1`, если истинно, иначе `0`. |
| MsgBody | Array | Тело сообщения, см. [Описание формата сообщения](https://www.tencentcloud.com/document/product/1047/33527) для получения подробной информации. |
| CloudCustomData | String | Пользовательские данные сообщения (хранятся в облаке, будут отправлены адресату и могут быть получены даже после удаления и переустановки приложения). |
| EventTime | Integer | Временная метка срабатывания события в миллисекундах. |

### Пример ответа

После синхронизации данных бэкенд приложения отправляет пакет ответа webhook.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0 // Игнорировать результат webhook}
```

### Поля ответа

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Обязательное | Результат обработки запроса:OK: Указывает на успешную обработкуFAIL: Указывает на ошибку |
| ErrorCode | Integer | Обязательное | Код ошибки, значение 0 здесь означает игнорировать ответ. |
| ErrorInfo | String | Обязательное | Сообщение об ошибке. |

## Ссылки

- [Обзор Webhook](https://www.tencentcloud.com/document/product/1047/34354)
- RESTful API: [Отправка сообщений в официальный аккаунт](https://www.tencentcloud.com/document/product/1047/60810)


---
*Источник: [https://trtc.io/document/60804](https://trtc.io/document/60804)*

---
*Источник (EN): [callback-after-sending-an-official-channel-message.md](./callback-after-sending-an-official-channel-message.md)*
