# Запрос количества непрочитанных личных сообщений

## Обзор функции

Этот API используется для запроса количества непрочитанных сообщений в личной беседе или всех личных беседах.

## Описание вызова API

### Пример URL запроса

```
https://xxxxxx/v4/openim/get_c2c_unread_msg_num?sdkappid=88888888&identifier=admin&usersig=xxx&random=99999999&contenttype=json
```

### Параметры запроса

В следующей таблице описаны изменённые параметры при вызове этого API. Для других параметров см. [Обзор RESTful API](https://intl.cloud.tencent.com/document/product/1047/34620).

| Параметр | Описание |
| --- | --- |
| xxxxxx | Доменное имя, соответствующее стране/региону, где находится ваш SDKAppID.Китай: `console.tim.qq.com`Сингапур: `adminapisgp.im.qcloud.com`Сеул: `adminapikr.im.qcloud.com`Токио: `adminapijpn.im.qcloud.com`Франкфурт: `adminapiger.im.qcloud.com`Кремниевая долина: `adminapiusa.im.qcloud.com`Джакарта: `adminapiidn.im.qcloud.com` |
| v4/openim/get_c2c_unread_msg_num | API запроса |
| sdkappid | SDKAppID, назначенный консолью Chat при создании приложения |
| identifier | Учётная запись администратора приложения. Дополнительные сведения см. в разделе **App Admin** в [Аутентификация входа](https://intl.cloud.tencent.com/document/product/1047/33517). |
| usersig | Подпись, созданная учётной записью администратора приложения. Подробные сведения см. в [Генерирование UserSig](https://intl.cloud.tencent.com/document/product/1047/34385). |
| random | Случайное 32-битное беззнаковое целое число в диапазоне от 0 до 4294967295. |
| contenttype | Формат запроса, всегда должен быть `json`. |

### Максимальная частота вызовов

200 вызовов в секунду

### Запрос общего количества непрочитанных личных сообщений учётной записи

#### Пример запроса

В этом примере показано, как администратор запрашивает общее количество непрочитанных личных сообщений пользователя `dramon1`. Требуется только `To_Account`.

```
{    "To_Account":"dramon1"}
```

#### Пример ответа

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0,    "AllC2CUnreadMsgNum": 12}
```

### Запрос количества непрочитанных сообщений в нескольких личных беседах одновременно

#### Пример запроса

В этом примере показано, как администратор запрашивает количество непрочитанных сообщений в беседах пользователя `dramon1` с `dramon2` и `teacher`.

```
{    "To_Account":"dramon1",    "Peer_Account":[        "dramon2",        "teacher"    ]}
```

#### Пример ответа

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0,    "C2CUnreadMsgNumList": [        {            "Peer_Account": "dramon2",            "C2CUnreadMsgNum": 12        },        {            "Peer_Account": "teacher",            "C2CUnreadMsgNum": 12        }    ]}
```

### Поля запроса

| Поле | Тип | Обязательное | Описание |
| --- | --- | --- | --- |
| To_Account | String | Да | `UserID` пользователя для запроса |
| Peer_Account | Array | Нет | `UserID` другой стороны в беседе для запросаЭто поле требуется для запроса конкретной личной беседы.Массив может содержать до 10 значений `UserID`. |

### Поля ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ActionStatus | String | Результат запроса. `OK`: Успешно; `FAIL`: Ошибка |
| ErrorCode | Integer | Код ошибки. `0`: Успешно; другие значения: Ошибка |
| ErrorInfo | String | Информация об ошибке |
| AllC2CUnreadMsgNum | Integer | Общее количество непрочитанных сообщений во всех беседах |
| C2CUnreadMsgNumList.Peer_Account | String | `UserID` другой стороны в личной беседе |
| C2CUnreadMsgNumList.C2CUnreadMsgNum | Integer | Количество непрочитанных сообщений в личной беседе |
| ErrorList.Peer_Account | String | Целевая учётная запись, для которой запрос не удался |
| ErrorList.ErrorCode | Integer | Код ошибки. `70107` указывает, что учётная запись не существует. |

## Коды ошибок

Код состояния HTTP, возвращённый этим API, всегда равен 200, если не происходит ошибка сети (например, ошибка 502). Конкретные коды ошибок и сведения можно найти в полях ответа `ErrorCode` и `ErrorInfo` соответственно.
Для общих кодов ошибок (60000–79999) см. [Коды ошибок](https://intl.cloud.tencent.com/document/product/1047/34348).
В следующей таблице описаны коды ошибок, характерные для этого API:

| Код ошибки | Описание |
| --- | --- |
| 90001 | Ошибка при разборе JSON запроса. Убедитесь, что формат верен. |
| 90003 | Поле `To_Account` отсутствует в JSON запросе, или учётная запись, указанная в `To_Account`, не существует. |
| 90008 | Поле `From_Account` отсутствует в JSON запросе, или учётная запись, указанная в `From_Account`, не существует. |

## Ссылки

- [Отправка личных сообщений одному пользователю](https://intl.cloud.tencent.com/document/product/1047/34919) (v4/openim/sendmsg)
- [Отправка личных сообщений нескольким пользователям](https://intl.cloud.tencent.com/document/product/1047/34920) (v4/openim/batchsendmsg)
- Запрос личных сообщений ([v4/openim/admin_getroammsg](https://intl.cloud.tencent.com/document/product/1047/35478))
- [Отзыв личных сообщений](https://intl.cloud.tencent.com/document/product/1047/35015) (v4/openim/admin_msgwithdraw)


---
*Источник: [https://trtc.io/document/41046](https://trtc.io/document/41046)*

---
*Источник (EN): [querying-unread-one-to-one-message-count.md](./querying-unread-one-to-one-message-count.md)*
