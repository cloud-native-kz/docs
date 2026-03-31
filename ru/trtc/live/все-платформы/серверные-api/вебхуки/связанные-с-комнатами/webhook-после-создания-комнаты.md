# Webhook после создания комнаты

## Обзор функции

Бэкэнд приложения может использовать этот webhook для просмотра информации в реальном времени о создании комнат пользователями, включая уведомления об успешном создании комнаты, что позволяет синхронизировать данные и выполнять другие операции.

## Примечания

- Для включения webhook необходимо настроить URL webhook и активировать переключатель, соответствующий данному протоколу webhook. Методы конфигурации см. в документе [Конфигурация webhook третьей стороны](https://www.tencentcloud.com/document/product/647/64420#).
- Во время webhook бэкэнд Live инициирует HTTP POST запрос к бэкэнду приложения.
- После получения запроса webhook бэкэнд приложения должен проверить, соответствует ли SDKAppID, содержащийся в URL запроса, собственному SDKAppID приложения.

## Сценарии, которые могут вызвать этот webhook

- Пользователи приложения успешно создают комнату через клиент
- Администраторы приложения успешно создают комнату через REST API

## Время запуска Webhook

После успешного создания комнаты.

## Описание API

### Пример URL запроса

В следующем примере URL webhook, настроенный в приложении — `https://www.example.com`.
**Пример:**

```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json&ClientIP=$ClientIP&OptPlatform=$OptPlatform
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса — HTTPS, метод запроса — POST |
| www.example.com | URL webhook |
| SdkAppid | SDKAppID, выданный консолью Instant Messaging при создании приложения |
| CallbackCommand | Фиксированное значение: Live.CallbackAfterCreateRoom |
| contenttype | Фиксированное значение: JSON |
| ClientIP | IP адрес клиента, например 127.0.0.1 |
| OptPlatform | Платформа клиента. Значения параметра OptPlatform см. в [Обзор Webhook: Протокол Webhook](https://www.tencentcloud.com/document/product/647/64412#d8e83f91-15ef-46e9-b370-9ba6c93a6ada) |

### Пример пакета запроса

```
{    "CallbackCommand":"Live.CallbackAfterCreateRoom",    "Operator_Account":"admin",    "RoomInfo":{        "RoomId":"tandy-test-rest",        "RoomName":"tandy-test-rest",        "RoomType":"Live",        "Owner_Account":"user3",        "MaxMemberCount":300,        "IsMessageDisabled":true,        "CustomInfo":"custom123",        "IsSeatEnabled":true,        "TakeSeatMode":"ApplyToTake",        "MaxSeatCount":16,        "CreateTime":1703589922,        "IsPublicVisible":true,        "CoverURL":"cover url",        "Category":[1,2]    }}
```

### Поля пакета запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда webhook |
| Operator_Account | String | UserID оператора, инициирующего запрос на создание комнаты |
| RoomId | String | ID комнаты |
| RoomName | String | Название комнаты |
| RoomType | String | Тип комнаты: Meeting (Переговорная комната) |
| Owner_Account | String | ID хозяина |
| MaxMemberCount | Integer | Максимальное количество участников комнаты |
| IsMessageDisabled | Bool | Запретить всем участникам отправлять текстовые сообщения |
| CustomInfo | String | Поля пользовательского определения |
| IsSeatEnabled | Bool | Доступна ли поддержка микрофона? |
| MaxSeatCount | Integer | Максимальное количество микрофонов |
| TakeSeatMode | String | Режим микрофона: None (Выключено), FreeToTake (Свободно присоединяться к подиуму), ApplyToTake (Применить для присоединения к микрофону) |
| CreateTime | Integer | Запланированное время начала встречи |
| IsPublicVisible | Bool | Является ли комната общедоступной |
| CoverURL | String | URL обложки комнаты |
| Category | Array | Идентификация типа комнаты, тип целочисленного массива |
| EventTime | Integer | Временная метка запуска события в миллисекундах |

### Пример пакета ответа

Пакет ответа webhook отправляется после синхронизации данных бэкэндом приложения.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0 // Ignore webhook result}
```

### Описание полей пакета ответа

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Обязательное | Результат процесса запроса: OK указывает на успех; FAIL указывает на ошибку |
| ErrorCode | Integer | Обязательное | Код ошибки, здесь 0 означает игнорировать результат ответа |
| ErrorInfo | String | Обязательное | Сообщение об ошибке |

## Ссылки

- [Обзор Webhook](https://www.tencentcloud.com/document/product/647/64412#)
- REST API: [Создание комнаты](https://www.tencentcloud.com/document/product/647/63401#)


---
*Источник: [https://trtc.io/document/64422](https://trtc.io/document/64422)*

---
*Источник (EN): [webhook-after-room-creation.md](./webhook-after-room-creation.md)*
