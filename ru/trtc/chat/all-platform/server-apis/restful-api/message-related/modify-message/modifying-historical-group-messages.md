# Изменение исторических сообщений группы

## Описание вызова API

- Этот API используется администратором для изменения исторических сообщений группового чата.
- Вы можете изменять поля `MsgBody` и `CloudCustomData` отдельно или одновременно для сообщения, перезаписывая значения полей в историческом сообщении значениями, указанными в запросах.
- Этот API нельзя использовать для изменения исторических сообщений аудио-видео групп.

> **Примечание**: сообщения, изменённые этим API, не могут быть восстановлены.

### Пример URL запроса

```
https://xxxxxx/v4/openim/modify_group_msg?sdkappid=88888888&identifier=admin&usersig=xxx&random=99999999&contenttype=json
```

### Параметры запроса

В следующей таблице описаны только изменённые параметры при вызове этого API. Для других параметров см. [Обзор RESTful API](https://intl.cloud.tencent.com/document/product/1047/34620).

| Параметр | Описание |
| --- | --- |
| xxxxxx | Доменное имя, соответствующее стране/региону, где расположен ваш SDKAppID. Китай: `console.tim.qq.com` Сингапур: `adminapisgp.im.qcloud.com` Сеул: `adminapikr.im.qcloud.com` Токио: `adminapijpn.im.qcloud.com` Франкфурт: `adminapiger.im.qcloud.com` Кремниевая долина: `adminapiusa.im.qcloud.com` Джакарта: `adminapiidn.im.qcloud.com` |
| v4/openim/modify_group_msg | API запроса |
| sdkappid | SDKAppID, назначенный консолью Chat при создании приложения |
| identifier | Учётная запись администратора приложения. Для получения дополнительной информации см. раздел **App Admin** в [Login Authentication](https://intl.cloud.tencent.com/document/product/1047/33517). |
| usersig | Подпись, созданная учётной записью администратора приложения. Подробности см. в [Generating UserSig](https://intl.cloud.tencent.com/document/product/1047/34385). |
| random | Случайное 32-битное целое число без знака в диапазоне от 0 до 4294967295. |
| contenttype | Формат запроса, который всегда должен быть `json`. |

### Максимальная частота вызовов

200 вызовов в секунду

### Пример запроса

#### Изменение только информации `MsgBody` объекта сообщения

```
{    "GroupId": "@TGS#1HYEP2SHC",    "MsgSeq": 23,    "MsgBody": [        {            "MsgType": "TIMTextElem",            "MsgContent": {                "Text": "hello"            }        }    ]}
```

#### Изменение только информации `CloudCustomData` объекта сообщения

```
{    "GroupId": "@TGS#1HYEP2SHC",    "MsgSeq": 23,    "CloudCustomData": "your cloud custom data"}
```

#### Изменение информации `MsgBody` и `CloudCustomData` объекта сообщения одновременно

```
{    "GroupId": "@TGS#1HYEP2SHC",    "MsgSeq": 23,    "MsgBody": [        {            "MsgType": "TIMTextElem",            "MsgContent": {                "Text": "hello"            }        }    ],    "CloudCustomData": "your cloud custom data"}
```

### Поля запроса

| Поле | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| GroupId | String | Да | ID группы, чьи исторические сообщения будут изменены |
| MsgSeq | Integer | Да | Порядковый номер изменяемого сообщения |
| MsgBody | Array | Нет | Тело сообщения. Подробности формата см. в [Message Formats](https://intl.cloud.tencent.com/document/product/1047/33527). (Примечание: сообщение может содержать несколько элементов сообщения, в этом случае `MsgBody` является массивом.) |
| CloudCustomData | String | Нет | Пользовательские данные сообщения. Сохраняются в облаке и будут отправлены получателю. Такие данные можно получить после удаления и переустановки приложения. |
| TopicId | String | Нет | ID темы, для которой изменяются исторические сообщения. Это поле применяется только к группам сообществ с поддержкой тем. |

#### Пример ответа

```
{    "ActionStatus": "OK",    "ErrorCode": 0,    "ErrorInfo": "succeed"}
```

### Поля ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ActionStatus | String | Результат запроса. `OK`: успешно; `FAIL`: ошибка |
| ErrorCode | Integer | Код ошибки. `0`: успешно; другие значения: ошибка |
| ErrorInfo | String | Информация об ошибке |

## Коды ошибок

Код состояния HTTP, возвращаемый этим API, всегда равен 200, если не происходит ошибка сети (например, ошибка 502). Конкретный код ошибки и детали можно найти в полях ответа `ErrorCode` и `ErrorInfo` соответственно.
Для общих кодов ошибок (60000–79999) см. [Error Codes](https://intl.cloud.tencent.com/document/product/1047/34348).
В следующей таблице описаны коды ошибок, специфичные для этого API:

| Код ошибки | Описание |
| --- | --- |
| 20001 | Неверный запрос. |
| 20002 | `UserSig` или `A2` истёк. |
| 20004 | Ошибка сети. Повторите попытку. |
| 20005 | Внутренняя ошибка сервера. Повторите попытку. |
| 90001 | Ошибка синтаксического анализа JSON запроса. Убедитесь в корректности формата. |
| 90002 | `MsgBody` в JSON запросе не соответствует требованиям формата сообщения или `MsgBody` не является массивом. Для получения дополнительной информации см. раздел **Message Element TIMMsgElement** в [Message Formats](https://intl.cloud.tencent.com/document/product/1047/33527#.E6.B6.88.E6.81.AF.E5.85.83.E7.B4.A0-timmsgelement). |
| 90003 | JSON запрос не содержит поле `To_Account` или поле `To_Account` не является строкой. |
| 90007 | Поле `MsgBody` в JSON запросе не является массивом. Измените его на массив. |
| 90009 | Запрос требует прав администратора приложения. |
| 90010 | JSON запрос не соответствует требованиям формата сообщения. Для получения дополнительной информации см. раздел **Message Element TIMMsgElement** в [Message Formats](https://intl.cloud.tencent.com/document/product/1047/33527#.E6.B6.88.E6.81.AF.E5.85.83.E7.B4.A0-timmsgelement). |
| 91000 | Внутренняя ошибка сервиса. Повторите попытку. |
| 90992 | Внутренняя ошибка сервиса. Повторите попытку. Если этот код ошибки возвращается для всех запросов и webhook включен, убедитесь, что сервер приложения нормально возвращает результаты в Chat backend. |

## Инструмент отладки API

Используйте [инструмент онлайн-отладки RESTful API](https://tcc.tencentcs.com/im-api-tool/index.html#/v4/openim/modify_group_msg) для отладки этого API.

## Ссылки

Отправка обычных сообщений в группе ([v4/group_open_http_svc/send_group_msg](https://intl.cloud.tencent.com/document/product/1047/34959))
Получение исторических сообщений ([group_open_http_svc/group_msg_get_simple](https://intl.cloud.tencent.com/document/product/1047/34971))


---
*Источник: [https://trtc.io/document/47948](https://trtc.io/document/47948)*

---
*Источник (EN): [modifying-historical-group-messages.md](./modifying-historical-group-messages.md)*
