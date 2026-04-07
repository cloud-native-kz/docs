# Callback при напоминании чатбота в группе

## Описание функции

После включения "callback события чатбота" в консоли бэкенд приложения будет получать callback сообщения напоминания, когда пользователь напоминает чатбота в группе.

## Важная информация

- Чтобы включить этот callback, необходимо настроить URL callback и включить переключатель, соответствующий этому callback. Способ настройки см. в разделе [Конфигурация Webhook](https://www.tencentcloud.com/document/product/1047/34520).
- Направление callback заключается в том, что бэкенд Chat отправляет HTTP POST запросы на бэкенд приложения.
- После получения запроса callback бэкенд приложения должен проверить, соответствует ли значение параметра SDKAppID в URL запроса его собственному SDKAppID.
- По другим вопросам безопасности см. раздел Considerations in Security в [Обзор Webhook](https://www.tencentcloud.com/document/product/1047/34354#security-considerations).

## Сценарии срабатывания Callback

Пользователь напоминает чатбота в группе. (Callback не срабатывает, если напоминаются все члены группы.)

## Время срабатывания Callback

Callback срабатывает после того, как пользователь напоминает чатбота в группе.

## Описание API

### Пример URL запроса

В следующем примере URL callback, настроенный для приложения, это `https://www.example.com`.

**Пример:**

```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json&ClientIP=$ClientIP&OptPlatform=$OptPlatform
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса — HTTPS, метод запроса — POST. |
| www.example.com | URL callback. |
| SdkAppid | SDKAppID, назначенный приложению при его создании в консоли Chat. |
| CallbackCommand | Значение фиксировано как Bot.OnGroupMessage. |
| contenttype | Значение фиксировано как json. |
| ClientIP | IP адрес клиента. Например, 127.0.0.1. |
| OptPlatform | Платформа клиента. Допустимые значения см. в описании параметра OptPlatform в Webhook Protocol в разделе [Обзор Webhook](https://www.tencentcloud.com/document/product/1047/34354#webhook-protocol). |

### Пример пакета запроса

```
{    "CallbackCommand": "Bot.OnGroupMessage", // Callback команда.    "GroupId": "@TGS#2J4SZEAEL", // ID группы.    "Type": "Public", // Тип группы.    "From_Account": "jared", // Отправитель.    "Operator_Account":"admin", // Инициатор запроса.    "Random": 123456, // Случайное число.    "MsgSeq": 123, // Порядковый номер сообщения.    "MsgTime": 1490686222, // Временная метка отправки сообщения.    "OnlineOnlyFlag": 1, // Онлайн сообщение. 1: да; 0: нет. Для групп прямой трансляции этот атрибут игнорируется и используется значение по умолчанию 0.    "MsgBody": [ // Тело сообщения. См. объект сообщения TIMMessage.        {            "MsgType": "TIMTextElem", // Текст.            "MsgContent": {                "Text": "@@RBT#001 hello"            }        }    ],    "AtRobots_Account": [ "@RBT#001" ], // Список напомянутых чатботов. Пользователи могут напомнить более одного чатбота, если в группе существует несколько чатботов.    "CloudCustomData": "your cloud custom data",    "EventTime": 1670574414123// Временная метка срабатывания события в миллисекундах.        }
```

### Поля пакета запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Callback команда. |
| GroupId | String | ID группы с групповым сообщением. |
| Type | String | Тип группы с групповым сообщением. Например, Public. Подробнее см. в разделе Group Types в [Система групп](https://www.tencentcloud.com/document/product/1047/33529#differences-in-basic-group-capabilities). |
| From_Account | String | User ID отправителя сообщения. |
| Operator_Account | String | User ID инициатора запроса, который можно использовать для определения, был ли запрос инициирован администратором. |
| Random | Integer | 32-битное случайное число в запросе сообщения. |
| MsgSeq | Integer | Порядковый номер сообщения, который однозначно идентифицирует сообщение. Групповые сообщения отсортированы по MsgSeq. Сообщение отправлено более недавно, если его значение MsgSeq больше. |
| MsgTime | Integer | Временная метка отправки сообщения, соответствующая времени бэкенд-сервера. |
| OnlineOnlyFlag | Integer | Онлайн сообщение. 1: да; 0: нет. Для групп прямой трансляции этот атрибут игнорируется и используется значение по умолчанию 0. |
| MsgBody | Array | Тело сообщения. Подробнее см. в разделе [Форматы сообщений](https://www.tencentcloud.com/document/product/1047/33527). |
| AtRobots_Account | Array | Список напомянутых чатботов. Пользователи могут напомнить более одного чатбота, если в группе существует несколько чатботов. |
| CloudCustomData | String | Пользовательские данные сообщения. (Они сохраняются в облаке и будут отправлены получателю. Их можно получить даже после удаления и переустановки Chat.) |
| TopicId | String | ID темы. Если используется этот параметр, сообщения связаны с темой. Этот параметр применяется только к групповым чатам сообщества, поддерживающим темы. |
| EventTime | Integer | Временная метка срабатывания события в миллисекундах. |

### Пример пакета ответа

Пакет ответа возвращается после синхронизации данных бэкенд приложением.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0 // Результат callback игнорируется.}
```

### Поля пакета ответа

| Поле | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Да | Результат обработки запроса. OK: обработка успешна; FAIL: обработка не удалась. |
| ErrorCode | Integer | Да | Код ошибки. Значение 0 указывает, что результат callback игнорируется. |
| ErrorInfo | String | Да | Сообщение об ошибке. |

## Справочные материалы

- [Обзор Webhook](https://www.tencentcloud.com/document/product/1047/34354)
- REST API: [Отправка обычных сообщений в группе](https://www.tencentcloud.com/document/product/1047/34959)


---
*Источник: [https://trtc.io/document/68953](https://trtc.io/document/68953)*

---
*Источник (EN): [callback-after-reminding-a-chatbot-in-a-group.md](./callback-after-reminding-a-chatbot-in-a-group.md)*
