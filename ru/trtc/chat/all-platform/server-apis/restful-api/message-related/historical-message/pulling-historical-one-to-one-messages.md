# Получение исторических персональных сообщений

## Обзор функции

- Этот API используется администратором приложения для запроса истории сообщений персональной беседы с точки зрения одной из сторон беседы в указанном временном диапазоне.
- Персональная беседа для запроса указывается параметрами `Operator_Account` и `Peer_Account` в запросе, а запрос выполняется с точки зрения стороны, указанной в `Operator_Account`. Результат запроса содержит сообщения, отправленные обеими сторонами. Отправитель и получатель каждого сообщения указаны в полях `From_Account` и `To_Account` соответственно.
- В большинстве случаев результат запроса одинаков, независимо от того, выполняется ли запрос с точки зрения любой из сторон персональной беседы. Однако есть четыре случая, когда результаты отличаются (некоторые сообщения в беседе могут быть запрошены одной стороной, но не другой):
- Одна из сторон беседы очистила историю сообщений, вызвав терминальный API [clearC2CHistoryMessage()](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a29aa6e75c2238c35cc609bef0e5a46ce).
- Одна из сторон беседы удалила беседу, вызвав терминальный API [deleteConversation()](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMConversationManager.html#a7a6e38c5a7431646bd4c0c4c66279077), веб/uni-app API [deleteConversation](https://web.sdk.qcloud.com/im/doc/en/SDK.html#deleteConversation) или [серверный API удаления беседы](https://intl.cloud.tencent.com/document/product/1047/43088) с установкой `ClearRamble` на `1`.
- Одна из сторон беседы удалила некоторые сообщения в беседе, вызвав терминальный API [deleteMessages()](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#adb346fede13d493e415f6574df911e9a) или веб/uni-app API [deleteMessage](https://web.sdk.qcloud.com/im/doc/en/SDK.html#deleteMessage).
- Для сообщений, отправленных через [API отправки персональных сообщений одному пользователю](https://intl.cloud.tencent.com/document/product/1047/34919) или [API отправки персональных сообщений нескольким пользователям](https://intl.cloud.tencent.com/document/product/1047/34920), параметр `SyncOtherMachine` установлен на `2`, что означает, что указанные сообщения не синхронизируются с историей сообщений другой стороны беседы.
- Результат запроса содержит отозванные сообщения, обозначенные полем `MsgFlagBits`.
- Поле `IsPeerRead` в результате запроса указывает, отправляет ли получатель квитанцию о прочтении сообщения. Значение поля равно `1` только когда получатель вызывает API [sendMessageReadReceipts (Android / iOS и Mac / Windows)](https://intl.cloud.tencent.com/document/product/1047/48022) или [sendMessageReadReceipt (Web)](https://intl.cloud.tencent.com/document/product/1047/48021).
- Если вы хотите отозвать сообщение, вы можете сначала вызвать этот API для запроса `MsgKey` сообщения, а затем вызвать [RESTful API отзыва персональных сообщений](https://intl.cloud.tencent.com/document/product/1047/35015) для отзыва сообщения.
- Временной диапазон записей сообщений, которые можно запросить, зависит от периода хранения сообщений ротамера, который по умолчанию составляет семь дней. Вы можете изменить период ротамера сообщений через консоль Chat. Продление периода хранения сообщений является платной услугой. Для получения дополнительной информации см. [Хранение сообщений](https://intl.cloud.tencent.com/document/product/1047/33524).
- Если общий размер сообщений в запрошенном временном диапазоне превышает верхний предел размера ответа (в настоящее время 13 КБ), требуется продолжить получение. Вы можете проверить, были ли получены все запрошенные сообщения, проверив поле `Complete` в ответе.

## Описание вызова API

### Пример URL запроса

```
https://xxxxxx/v4/openim/admin_getroammsg?sdkappid=88888888&identifier=admin&usersig=xxx&random=99999999&contenttype=json
```

### Параметры запроса

В следующей таблице описаны измененные параметры при вызове этого API. Для других параметров см. [Обзор RESTful API](https://intl.cloud.tencent.com/document/product/1047/34620).

| Параметр | Описание |
| --- | --- |
| xxxxxx | Доменное имя, соответствующее стране/региону, где находится ваш SDKAppID.Китай: `console.tim.qq.com`Сингапур: `adminapisgp.im.qcloud.com`Сеул: `adminapikr.im.qcloud.com`Токио: `adminapijpn.im.qcloud.com`Франкфурт: `adminapiger.im.qcloud.com`Кремниевая долина: `adminapiusa.im.qcloud.com`Джакарта: `adminapiidn.im.qcloud.com` |
| v4/openim/admin_getroammsg | API запроса |
| sdkappid | SDKAppID, назначенный консолью Chat при создании приложения |
| identifier | Учетная запись администратора приложения. Для получения дополнительной информации см. раздел **Администратор приложения** в [Аутентификации входа](https://intl.cloud.tencent.com/document/product/1047/33517). |
| usersig | Подпись, созданная учетной записью администратора приложения. Для получения подробной информации см. [Создание UserSig](https://intl.cloud.tencent.com/document/product/1047/34385). |
| random | Случайное 32-битное беззнаковое целое число в диапазоне от 0 до 4294967295. |
| contenttype | Формат запроса, который всегда должен быть `json`. |

### Максимальная частота вызовов

200 вызовов в секунду

### Примеры запросов и ответов

Например, `user1` и `user2` имели беседу, и вы хотите запросить историю беседы с 2020-03-20 10:00:00 по 2020-03-20 11:00:00 с точки зрения user2.

#### Пример запроса

```
{    "Operator_Account":"user2",    "Peer_Account":"user1",    "MaxCnt":100,    "MinTime":1584669600,    "MaxTime":1584673200}
```

#### Пример ответа

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0,    "Complete": 0,    "MsgCnt": 12, //12 сообщений было возвращено при получении.    "LastMsgTime": 1584669680,    "LastMsgKey": "549396494_2578554_1584669680",    "MsgList": [        {            "From_Account": "user1",            "To_Account": "user2",            "MsgSeq": 549396494,            "MsgRandom": 2578554,            "MsgTimeStamp": 1584669680,            "MsgFlagBits": 0,            "IsPeerRead": 0,            "MsgKey": "549396494_2578554_1584669680",            "MsgBody": [                {                    "MsgType": "TIMTextElem",                    "MsgContent": {                        "Text": "msg 1"                    }                }            ],            "CloudCustomData": "your cloud custom data"        },        {            "From_Account": "user2",            "To_Account": "user1",            "MsgSeq": 1054803289,            "MsgRandom": 7201,            "MsgTimeStamp": 1584669689,            "MsgFlagBits": 0,            "IsPeerRead": 0,            "MsgKey": "1054803289_7201_1584669689",            "MsgBody": [                {                    "MsgType": "TIMTextElem",                    "MsgContent": {                        "Text": "msg 2"                    }                }            ],            "CloudCustomData": "your cloud custom data"        },        { ... } // Оставшиеся десять сообщений не перечислены для краткости.    ]}
```

В ответе `"Complete": 0` означает, что не все сообщения, созданные в течение временного диапазона, были получены. Следовательно, требуется продолжить получение.
**При продолжении запроса получения значение `MaxTime` должно быть изменено на значение `LastMsgTime` в ответе, и **`LastMsgKey`** из ответа должен быть введен**, как показано ниже:

##### Пример запроса на продолжение получения

```
{    "Operator_Account":"user2",    "Peer_Account":"user1",    "MaxCnt":100,    "MinTime":1584669600,    "MaxTime":1584669680,    "LastMsgKey": "549396494_2578554_1584669680"}
```

#### Пример ответа

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0,    "Complete": 1,    "MsgCnt": 5, // Пять сообщений было возвращено при получении.    "LastMsgTime": 1584669601,    "LastMsgKey": "1456_23287_1584669601",    "MsgList": [        {            "From_Account": "user1",            "To_Account": "user2",            "MsgSeq": 1456,            "MsgRandom": 23287,            "MsgTimeStamp": 1584669601,            "MsgFlagBits": 0,            "IsPeerRead": 1,            "MsgKey": "1456_23287_1584669601",            "MsgBody": [                {                    "MsgType": "TIMTextElem",                    "MsgContent": {                        "Text": "msg 13"                    }                }            ],            "CloudCustomData": "your cloud custom data"        },        {            "From_Account": "user2",            "To_Account": "user1",            "MsgSeq": 9806,            "MsgRandom": 14,            "MsgTimeStamp": 1584669602,            "MsgFlagBits": 0,            "IsPeerRead": 1,            "MsgKey": "9806_14_1584669602",            "MsgBody": [                {                    "MsgType": "TIMTextElem",                    "MsgContent": {                        "Text": "msg 14"                    }                }            ],            "CloudCustomData": "your cloud custom data"        },        { ... } // Оставшиеся три сообщения не перечислены для краткости.    ]}
```

#### Поля запроса

| Поле | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| Operator_Account | String | Да | UserID одной из сторон беседы, для которой запрашиваются сообщения. Результат может быть разным, если вы запросите сообщения для другой стороны той же беседы. Для получения дополнительной информации см. раздел описания API. |
| Peer_Account | String | Да | `UserID` другой стороны в беседе |
| MaxCnt | Integer | Да | Количество сообщений для запроса |
| MinTime | Integer | Да | Минимальное значение временного диапазона для запроса сообщений в секундах |
| MaxTime | Integer | Да | Максимальное значение временного диапазона для запроса сообщений в секундах |
| LastMsgKey | String | Нет | `MsgKey` последнего полученного сообщения. Это поле требуется для продолжения получения. Для получения дополнительной информации см. предыдущий [пример](#example). |

### Пример ответа

- Ответ на успешный запрос

```
{  "ActionStatus": "OK",  "ErrorInfo": "",  "ErrorCode": 0,  "Complete": 1,  "MsgCnt": 1,  "LastMsgTime": 1584669680,  "LastMsgKey": "549396494_2578554_1584669680",  "MsgList": [      {          "From_Account": "user1",          "To_Account": "user2",          "MsgSeq": 549396494,          "MsgRandom": 2578554,          "MsgTimeStamp": 1584669680,          "MsgFlagBits": 0,          "IsPeerRead": 0,          "MsgKey": "549396494_2578554_1584669680",          "MsgBody": [              {                  "MsgType": "TIMTextElem",                  "MsgContent": {                      "Text": "1"                  }              }          ],          "CloudCustomData": "your cloud custom data"      }  ]}
```

- Ответ на неудачный запрос

```
{  "ActionStatus": "FAIL",   "ErrorInfo": "Fail to Parse json data of body, Please check it",   "ErrorCode": 90001}
```

### Поля ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ActionStatus | String | Результат запроса. `OK`: успешно; `FAIL`: ошибка |
| ErrorCode | Integer | Код ошибки. `0`: успешно; другие значения: ошибка |
| ErrorInfo | String | Информация об ошибке |
| Complete | Integer | Были ли получены все сообщения. `0`: нет, требуется продолжить получение; `1`: да |
| MsgCnt | Integer | Количество полученных сообщений на этот раз |
| LastMsgTime | Integer | Время последнего полученного сообщения на этот раз |
| LastMsgKey | String | Идентификатор последнего полученного сообщения на этот раз |
| MsgList | Array | Список возвращенных сообщений |
| MsgFlagBits | Integer | Атрибут сообщения. `0`: обычное сообщение; `8`: отозванное сообщение |
| IsPeerRead | Integer | Отправил ли получатель квитанцию о прочтении этого сообщения. Допустимые значения: `0` для нет и `1` для да. Для получения подробной информации см. описание функции этого API. |
| MsgBody | Array | Тело сообщения. Для получения подробной информации о форматах см. [Форматы сообщений](https://intl.cloud.tencent.com/document/product/1047/33527). (Примечание: сообщение может содержать несколько элементов сообщения, в этом случае `MsgBody` является массивом.) |
| CloudCustomData | String | Пользовательские данные сообщения. Они сохраняются в облаке и отправляются на другой конец. Такие данные могут быть получены после удаления и переустановки приложения. |
| MsgKey | String | Идентификатор сообщения. Вы можете использовать это поле при вызове [RESTful API отзыва персональных сообщений](https://intl.cloud.tencent.com/document/product/1047/35015). |

## Коды ошибок

HTTP код состояния для этого API всегда равен 200, если не происходит ошибка сети (например, ошибка 502). Конкретный код ошибки и детали можно найти в полях ответа `ErrorCode` и `ErrorInfo` соответственно.
Для публичных кодов ошибок (от 60000 до 79999) см. [Коды ошибок](https://intl.cloud.tencent.com/document/product/1047/34348).
В следующей таблице описаны коды ошибок, специфичные для этого API:

| Код ошибки | Описание |
| --- | --- |
| 90001 | Ошибка парсинга JSON запроса. Убедитесь, что формат верен. |
| 90003 | Поле `To_Account` отсутствует в JSON запросе или это не строка. |
| 90008 | Поле `From_Account` отсутствует в JSON запросе или указанная им учетная запись не существует. |
| 90009 | Запрос требует прав администратора приложения. |
| 91000 | Внутренняя ошибка сервиса. Повторите попытку. |

## Инструмент отладки API

Используйте [онлайн инструмент отладки RESTful API](https://tcc.tencentcs.com/im-api-tool/index.html#/v4/openim/admin_getroammsg) для отладки этого API.

## Ссылки

- [Отправка персональных сообщений одному пользователю](https://intl.cloud.tencent.com/document/product/1047/34919) (v4/openim/sendmsg)
- [Отправка персональных сообщений нескольким пользователям](https://intl.cloud.tencent.com/document/product/1047/34920) (v4/openim/batchsendmsg)
- [Отзыв персональных сообщений](https://intl.cloud.tencent.com/document/product/1047/35015) (v4/openim/admin_msgwithdraw)


---
*Источник: [https://trtc.io/document/35478](https://trtc.io/document/35478)*

---
*Источник (EN): [pulling-historical-one-to-one-messages.md](./pulling-historical-one-to-one-messages.md)*
