# Отметить сообщения персональной переписки как прочитанные

## Обзор функции

Этот API используется для отметки сообщений персональной беседы как прочитанные. Групповые уведомления о прочтении с максимальным размером группы 200 участников.

## Описание вызова API

### Пример URL запроса

```
https://xxxxxx/v4/openim/admin_set_msg_read?sdkappid=88888888&identifier=admin&usersig=xxx&random=99999999&contenttype=json
```

### Параметры запроса

В следующей таблице описаны измененные параметры при вызове этого API. Для других параметров см. [Обзор RESTful API](https://intl.cloud.tencent.com/document/product/1047/34620).

| Параметр | Описание |
| --- | --- |
| xxxxxx | Доменное имя, соответствующее стране/региону, где находится ваш SDKAppID.Китай: `console.tim.qq.com`Сингапур: `adminapisgp.im.qcloud.com`Сеул: `adminapikr.im.qcloud.com`Токио: `adminapijpn.im.qcloud.com`Франкфурт: `adminapiger.im.qcloud.com`Кремниевая долина: `adminapiusa.im.qcloud.com`Джакарта: `adminapiidn.im.qcloud.com` |
| v4/openim/admin_set_msg_read | API запроса |
| sdkappid | SDKAppID, назначенный консолью Chat при создании приложения |
| identifier | Учетная запись администратора приложения. Для получения дополнительной информации см. раздел **App Admin** в [Проверка подлинности входа](https://intl.cloud.tencent.com/document/product/1047/33517). |
| usersig | Подпись, сгенерированная учетной записью администратора приложения. Для получения дополнительной информации см. [Генерирование UserSig](https://intl.cloud.tencent.com/document/product/1047/34385). |
| random | Случайное 32-битное целое число без знака в диапазоне от 0 до 4294967295. |
| contenttype | Формат запроса, который должен быть всегда `json`. |

### Максимальная частота вызовов

200 вызовов в секунду

### Пример запроса

Администратор указывает, что dramon1 отмечает все сообщения своей персональной беседы с dramon2 как прочитанные.

```
{    "Report_Account":"dramon1",    "Peer_Account":"dramon2"}
```

### Поля запроса

| Поле | Тип | Обязательное | Описание |
| --- | --- | --- | --- |
| Report_Account | String | Да | `UserId` учетной записи, для которой нужно отметить сообщения как прочитанные |
| Peer_Account | String | Да | `UserId` другой учетной записи в персональной беседе |
| MsgReadTime | String | Нет | Временная метка (в секундах). Все сообщения до указанной временной метки отмечаются как прочитанные. Если значение не указано, используется текущая временная метка. |

### Пример ответа

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0}
```

### Поля ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ActionStatus | String | Результат запроса. `OK`: Успешно. `FAIL`: Ошибка |
| ErrorCode | Integer | Код ошибки. `0`: Успешно. Другие значения: Ошибка |
| ErrorInfo | String | Информация об ошибке |

## Коды ошибок

HTTP код состояния, возвращаемый этим API, всегда равен 200, если не возникает ошибка сети (например, ошибка 502). Конкретный код ошибки и детали можно найти в полях ответа `ErrorCode` и `ErrorInfo` соответственно.
Для публичных кодов ошибок (60000–79999) см. [Коды ошибок](https://intl.cloud.tencent.com/document/product/1047/34348).
В следующей таблице описаны коды ошибок, характерные для этого API:

| Код ошибки | Описание |
| --- | --- |
| 90001 | Ошибка при парсировании JSON запроса. Убедитесь, что формат корректен. |
| 90003 | Поле `To_Account` отсутствует в JSON запросе, или учетная запись, указанная в `To_Account`, не существует. |
| 90008 | Поле `From_Account` отсутствует в JSON запросе, или учетная запись, указанная в `From_Account`, не существует. |

## Инструмент отладки API

Используйте [инструмент онлайн-отладки RESTful API](https://tcc.tencentcs.com/im-api-tool/index.html#/v4/openim/admin_set_msg_read) для отладки этого API.

## Справочные материалы

- [Отправка персональных сообщений одному пользователю](https://intl.cloud.tencent.com/document/product/1047/34919) (v4/openim/sendmsg)
- [Отправка персональных сообщений нескольким пользователям](https://intl.cloud.tencent.com/document/product/1047/34920) (v4/openim/batchsendmsg)
- Запрос персональных сообщений ([v4/openim/admin_getroammsg](https://intl.cloud.tencent.com/document/product/1047/35478))
- [Отзыв персональных сообщений](https://intl.cloud.tencent.com/document/product/1047/35015) (v4/openim/admin_msgwithdraw)


---
*Источник: [https://trtc.io/document/38996](https://trtc.io/document/38996)*

---
*Источник (EN): [marking-one-to-one-messages-as-read.md](./marking-one-to-one-messages-as-read.md)*
