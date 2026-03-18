# Отзыв личных сообщений

## Обзор функции

- Этот API позволяет администраторам отзывать личные сообщения.
- Этот API может отзывать все личные сообщения, включая отправленные клиентами или через API [v4/openim/sendmsg](https://intl.cloud.tencent.com/document/product/1047/34919) и [v4/openim/batchsendmsg](https://intl.cloud.tencent.com/document/product/1047/34920) RESTful.
- Для отзыва личных сообщений, отправленных клиентами, можно включить callback API [C2C.CallbackBeforeSendMsg](https://intl.cloud.tencent.com/document/product/1047/34364) или [C2C.CallbackAfterSendMsg](https://intl.cloud.tencent.com/document/product/1047/34365). Запишите `MsgKey` каждого личного сообщения через callback API и введите его в поле `MsgKey` этого API для отзыва сообщения. Вы также можете использовать API [v4/openim/admin_getroammsg](https://intl.cloud.tencent.com/document/product/1047/35478) для запроса `MsgKey` отзываемого личного сообщения и введите его в поле `MsgKey` этого API для отзыва сообщения.
- Поле `MsgKey` в ответах на вызовы API [v4/openim/sendmsg](https://intl.cloud.tencent.com/document/product/1047/34919) и [v4/openim/batchsendmsg](https://intl.cloud.tencent.com/document/product/1047/34920) требуется для отзыва личных сообщений, отправленных через эти два API.
- После того как личное сообщение отозвано этим API, оно удаляется из автономного хранилища, облачного хранилища истории и локального кэша клиентов отправителя и получателя.
- Этот API может отзывать личные сообщения, отправленные в любое время. Ограничений по времени нет.

> **Примечание** Обратите внимание, что личные сообщения, отозванные этим API, невозможно восстановить.

## Описание вызова API

### Пример URL запроса

```
https://xxxxxx/v4/openim/admin_msgwithdraw?sdkappid=88888888&identifier=admin&usersig=xxx&random=99999999&contenttype=json
```

### Параметры запроса

В следующей таблице описаны измененные параметры при вызове этого API. Для других параметров см. [Обзор RESTful API](https://intl.cloud.tencent.com/document/product/1047/34620).

| Параметр | Описание |
| --- | --- |
| xxxxxx | Доменное имя, соответствующее стране/региону, где находится ваш SDKAppID.Китай: `console.tim.qq.com`Сингапур: `adminapisgp.im.qcloud.com`Сеул: `adminapikr.im.qcloud.com`Токио: `adminapijpn.im.qcloud.com`Франкфурт: `adminapiger.im.qcloud.com`Кремниевая долина: `adminapiusa.im.qcloud.com`Джакарта: `adminapiidn.im.qcloud.com` |
| v4/openim/admin_msgwithdraw | API запроса. |
| sdkappid | SDKAppID, назначенный консолью Chat при создании приложения |
| identifier | Учетная запись администратора приложения. Для получения дополнительной информации см. раздел **Администратор приложения** в [Аутентификация входа](https://intl.cloud.tencent.com/document/product/1047/33517). |
| usersig | Подпись, созданная учетной записью администратора приложения. Подробности см. в [Генерация UserSig](https://intl.cloud.tencent.com/document/product/1047/34385). |
| random | Случайное 32-битное целое число без знака в диапазоне от 0 до 4294967295. |
| contenttype | Формат запроса, который всегда должен быть `json`. |

### Максимальная частота вызовов

200 вызовов в секунду

### Пример запроса

```
{    "From_Account": "vinson",    "To_Account": "dramon",    "MsgKey": "31906_833502_1572869830"}
```

### Поля запроса

| Поле | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| From_Account | String | Да | UserID отправителя сообщения. |
| To_Account | String | Да | `UserID` получателя |
| MsgKey | String | Да | Уникальный идентификатор отзываемого сообщения, который можно найти в ответах на вызовы API [v4/openim/sendmsg](https://intl.cloud.tencent.com/document/product/1047/34919) и [v4/openim/batchsendmsg](https://intl.cloud.tencent.com/document/product/1047/34920). |

### Пример ответа

- Ответ при успешном запросе

```
{  "ActionStatus": "OK",   "ErrorInfo": "",   "ErrorCode": 0}
```

- Ответ при неудачном запросе

```
{  "ActionStatus": "FAIL",   "ErrorInfo": "Fail to Parse json data of body, Please check it",   "ErrorCode": 90001}
```

### Поля ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ActionStatus | String | Результат запроса. `OK`: Успешно. `FAIL`: Ошибка |
| ErrorCode | Integer | Код ошибки. `0`: Успешно. Другие значения: Ошибка |
| ErrorInfo | String | Информация об ошибке |

## Коды ошибок

Возвращаемый HTTP код состояния для этого API всегда 200, если не возникает ошибка сети (например, ошибка 502). Конкретный код ошибки и детали можно найти в полях ответа `ErrorCode` и `ErrorInfo` соответственно.
Для общих кодов ошибок (60000–79999) см. [Коды ошибок](https://intl.cloud.tencent.com/document/product/1047/34348).
В следующей таблице описаны коды ошибок, относящиеся к этому API:

| Код ошибки | Описание |
| --- | --- |
| 20022 | Отзываемое сообщение не существует. Проверьте. |
| 20023 | Сообщение уже отозвано. |
| 90001 | Ошибка при разборе JSON запроса. Убедитесь, что формат правильный. |
| 90003 | Поле `To_Account` отсутствует в пакете JSON запроса или указанная учетная запись не существует. |
| 90008 | Поле `From_Account` отсутствует в пакете JSON запроса или указанная учетная запись не существует. |
| 90009 | Запрос требует прав администратора приложения. |
| 90054 | Недействительный `MsgKey`. |
| 91000 | Ошибка внутреннего сервиса. Повторите попытку. |

## Инструмент отладки API

Используйте [инструмент онлайн-отладки RESTful API](https://tcc.tencentcs.com/im-api-tool/index.html#/v4/openim/admin_msgwithdraw) для отладки этого API.

## Справочный материал

- [Отправка личных сообщений одному пользователю](https://intl.cloud.tencent.com/document/product/1047/34919) (v4/openim/sendmsg)
- [Отправка личных сообщений нескольким пользователям](https://intl.cloud.tencent.com/document/product/1047/34920) (v4/openim/batchsendmsg)
- Запрос личных сообщений ([v4/openim/admin_getroammsg](https://intl.cloud.tencent.com/document/product/1047/35478))


---
*Источник: [https://trtc.io/document/35015](https://trtc.io/document/35015)*

---
*Источник (EN): [recalling-one-to-one-messages.md](./recalling-one-to-one-messages.md)*
