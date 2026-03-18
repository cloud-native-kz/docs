# Callback After Recalling Group Messages

## Overview

Это событие webhook используется серверной частью приложения для проверки отзыва групповых сообщений в реальном времени.

## Notes

- Чтобы включить этот webhook, необходимо настроить URL webhook и переключить соответствующий протокол. Дополнительные сведения о методе конфигурации см. в разделе [Webhook Configuration](https://intl.cloud.tencent.com/document/product/1047/34520).
- Во время этого события webhook серверная часть Chat инициирует HTTP POST запрос на серверную часть приложения.
- После получения запроса webhook серверная часть приложения должна проверить, является ли `SDKAppID`, содержащийся в URL запроса, `SDKAppID` приложения.
- Для получения дополнительной информации о соображениях безопасности см. раздел **Security Considerations** в [Webhook Overview](https://intl.cloud.tencent.com/document/product/1047/34354).

## Webhook Triggering Scenarios

- Пользователь приложения отзывает групповое сообщение на клиенте.
- Администратор приложения отзывает групповое сообщение с помощью вызова RESTful API.

## Webhook Triggering Timing

После успешного отзыва группового сообщения

## API Calling Description

### Sample request URL

В следующем примере URL webhook, настроенный в приложении, это `https://www.example.com`.
**Example:**

```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json&ClientIP=$ClientIP&OptPlatform=$OptPlatform
```

### Request parameters

| Parameter | Description |
| --- | --- |
| https | Протокол запроса — HTTPS, метод запроса — POST. |
| www.example.com | URL webhook. |
| SdkAppid | `SDKAppID`, назначенный консолью Chat при создании приложения. |
| CallbackCommand | Фиксированное значение: `Group.CallbackAfterRecallMsg`. |
| contenttype | Фиксированное значение: `json`. |
| ClientIP | IP-адрес клиента, например 127.0.0.1. |
| OptPlatform | Платформа клиента. Допустимые значения см. в описании `OptPlatform` в разделе **Webhook Protocols** статьи [Webhook Overview](https://intl.cloud.tencent.com/document/product/1047/34354). |

### Sample request

```
{    "CallbackCommand":"Group.CallbackAfterRecallMsg", // Webhook command    "Operator_Account":"admin", // Operator    "Type": "Community", // Group type    "GroupId":"1213456", // Group ID    "MsgSeqList":[ // `MsgSeq` list of recalled messages                   {          "MsgSeq":130,          "MsgId":"144115213033478435-1739361321-2512805311"        }    ],    "TopicId":"@TGS#_@TGS#cQVLVHIM62CJ@TOPIC#_TestTopic",// Topic ID, which applies only to topic-enabled communities    "EventTime":"1670574414123"// Event trigger timestamp in milliseconds		}
```

### Request fields

| Object | Type | Description |
| --- | --- | --- |
| CallbackCommand | String | Команда webhook. |
| Operator_Account | String | `UserID` оператора, который отзывает групповое сообщение. |
| Type | String | Тип группы, которая генерирует групповые сообщения, например `Public`. Дополнительные сведения см. в разделе **Group Types** статьи [Group System](https://intl.cloud.tencent.com/document/product/1047/33529). |
| GroupId | String | ID группы. |
| MsgSeqList | Array | Список отозванных сообщений, содержащий поля `MsgId` и `MsgSeq`, представляющие уникальный идентификатор сообщения клиента и MsgSeq отозванного сообщения соответственно. |
| TopicId | String | ID темы, который указывает на отзыв сообщения в теме и применяется только к сообществам с включенными темами. |
| EventTime | Integer | Временная метка срабатывания события в миллисекундах. |

### Sample response

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0 //The value `0` indicates that the webhook result is ignored.}
```

### Response fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| ActionStatus | String | Yes | Результат запроса. `OK`: успешно; `FAIL`: ошибка. |
| ErrorCode | Integer | Yes | Код ошибки. Значение `0` указывает на то, что результат webhook игнорируется. |
| ErrorInfo | String | Yes | Информация об ошибке. |

## References

- [Webhook Overview](https://intl.cloud.tencent.com/document/product/1047/34354)
- Restful API: [Recalling Group Messages](https://intl.cloud.tencent.com/document/product/1047/34965)


---
*Source: [https://trtc.io/document/46979](https://trtc.io/document/46979)*

---
*Источник (EN): [callback-after-recalling-group-messages.md](./callback-after-recalling-group-messages.md)*
