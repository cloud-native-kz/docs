# Callback After Read Receipt

## Обзор функции

App Backend может использовать этот callback для просмотра статуса расписок о прочтении групповых сообщений в реальном времени и, соответственно, выполнения операций, таких как синхронизация данных.

## Примечания

- Чтобы включить callback, необходимо настроить URL callback и включить соответствующий переключатель протокола. Для получения подробных методов конфигурации см. документ [Конфигурация сторонних callbacks](https://www.tencentcloud.com/document/product/1047/34520).
- Во время этого callback Chat backend инициирует HTTP POST запрос к app backend.
- После получения запроса callback, app backend должен проверить, совпадает ли SDKAppID, содержащийся в URL запроса, с его собственным SDKAppID.
- По другим вопросам безопасности обратитесь к документу [Обзор Webhook - Рассмотрение безопасности](https://www.tencentcloud.com/document/product/1047/34354#.E5.AE.89.E5.85.A8.E8.80.83.E8.99.91).

## Сценарии, которые могут вызвать этот callback

- App пользователь отправляет сообщение о прочтении через клиент.
- App пользователь подтверждает расписки о прочтении групповых сообщений через клиент.
- App администратор отправляет сообщение о прочтении через RESTful APIs.

## Время срабатывания Callback

Отправка сообщения о прочтении или подтверждение сообщения как прочитанного.

## Описание API

### Пример URL запроса

В последующем примере URL callback, настроенный в приложении: `https://www.example.com`.
**Пример:**

```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json&ClientIP=$ClientIP&OptPlatform=$OptPlatform
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса — HTTPS, метод запроса — POST |
| www.example.com | URL callback |
| SdkAppid | SDKAppID, выделенный консолью Instant Messaging во время создания приложения |
| CallbackCommand | Зафиксировано как Group.CallbackAfterReadReceipt |
| contenttype | Фиксированное значение: JSON |
| ClientIP | IP клиента, например 127.0.0.1 |
| OptPlatform | Платформа клиента, см. значение OptPlatform в [Обзор Webhook: Протокол callback](https://www.tencentcloud.com/document/product/1047/34354#.E5.9B.9E.E8.B0.83.E5.8D.8F.E8.AE.AE) |

### Пример пакетов запроса

```
{    "CallbackCommand": "Group.CallbackAfterReadReceipt",    // Callback после расписки о прочтении    "GroupId": "@TGS#2TTV7VSII", // ID группы    "Type": "Public", // Тип группы    "GroupMsgReceiptList": [   // Информация о расписке о прочтении      {          "MsgSeq": 1,                 "ReadNum": 1,      // Количество прочитаних группового сообщения          "UnreadNum": 6     // Количество непрочитанных группового сообщения          "ReadReceiptMembers":[              {                  "Member_Account":"user0"              }          ]      },      {          "MsgSeq": 2,          "ReadNum": 1,          "UnreadNum": 6,          "ReadReceiptMembers":[              {                  "Member_Account":"user0"              }          ]      }    ],    "EventTime":"1670574414123"// Временная метка срабатывания события в миллисекундах}
```

### Поля пакета запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда callback |
| GroupId | String | ID рабочей группы |
| Type | String | Тип группы (Community в настоящее время не поддерживается) [Введение типа группы](https://www.tencentcloud.com/document/product/1047/33529#GroupType), например Public |
| GroupMsgReceiptList | Array | Информация о расписке о прочтении |
| MsgSeq | Integer | Seq сообщения |
| ReadNum | Integer | Количество членов, прочитавших сообщение |
| UnreadNum | Integer | Количество членов, не прочитавших сообщение |
| ReadReceiptMembers | Array | Список членов, прочитавших сообщение, Member_Account — это UserID членов, которые прочитали |
| EventTime | Integer | Временная метка срабатывания события в миллисекундах |

### Пример пакета ответа

После синхронизации данных app backend отправляет пакет ответа callback.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0 // Игнорировать результат callback}
```

### Описание полей пакета ответа

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Обязательное | Результат обработки запроса: OK: указывает на успешную обработкуFAIL: указывает на ошибку |
| ErrorCode | Integer | Обязательное | Код ошибки, введение 0 здесь означает игнорирование результата ответа |
| ErrorInfo | String | Обязательное | Сообщение об ошибке |

## Справочные материалы

- [Обзор сторонних callbacks](https://www.tencentcloud.com/document/product/1047/34354)
- RESTful API: [Отправка обычных сообщений в группе](https://www.tencentcloud.com/document/product/1047/34959)


---
*Источник: [https://trtc.io/document/60395](https://trtc.io/document/60395)*

---
*Источник (EN): [callback-after-read-receipt.md](./callback-after-read-receipt.md)*
