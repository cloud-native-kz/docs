# Вебхук после удаления метаданных комнаты

## Описание функции

Сервер приложения может использовать этот вебхук для отслеживания удаления метаданных комнаты.

## Важная информация

- Для включения вебхука необходимо настроить URL вебхука и включить переключатель, соответствующий этому протоколу вебхука. Методы конфигурации см. в документе [Third-Party Webhook Configuration](https://www.tencentcloud.com/document/product/647/64420#).
- Направление вебхука заключается в том, что сервер прямого эфира инициирует HTTP POST запрос на сервер приложения.
- После получения запроса вебхука сервер приложения должен проверить, совпадает ли параметр SDKAppID в URL запроса с его собственным SDKAppID.

## Сценарии, которые могут активировать этот вебхук

- Пользователи приложения удаляют метаданные через клиент.
- Администратор приложения удаляет метаданные через REST API.

## Время возникновения вебхука

После успешного удаления данных метаданных комнаты.

## Описание API

### Пример URL запроса:

В следующем примере URL вебхука, настроенный для приложения, — это `https://www.example.com`.

**Пример:**

```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json&ClientIP=$ClientIP&OptPlatform=$OptPlatform
```

### Описание параметров запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса — HTTPS, метод запроса — POST |
| www.example.com | URL вебхука |
| SdkAppid | SDKAppID, назначенный в консоли Chat при создании приложения |
| CallbackCommand | Фиксировано как `Live.CallbackAfterSetMetadata` |
| contenttype | Фиксированное значение `json` |
| ClientIP | IP адрес клиента, формат: `127.0.0.1` |
| OptPlatform | Платформа клиента. Значения параметра OptPlatform см. в разделе [Introduction to Third-Party Webhook](https://www.tencentcloud.com/document/product/647/64412#) |

### Пример пакета запроса:

```
{    "CallbackCommand": "Live.CallbackAfterDelMetadata",    "Operator_Account": "brennanli",    "RoomId": "live-room1111",    "Keys": [        "key1", "key2"    ],    "EventTime": 1739966441121}
```

### Описание полей пакета запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда вебхука |
| Operator_Account | String | UserID оператора, инициирующего запрос на удаление комнаты |
| RoomId | String | ID комнаты |
| Keys | Array | Соответствующий Key в данных метаданных |
| EventTime | Integer | Временная метка на уровне миллисекунд, вызванная событием |

### Пример пакета ответа

После синхронизации данных на фоне приложение отправляет пакет ответа вебхука.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0 // Ignore webhook result}
```

### Описание полей пакета ответа

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Обязательно | Результат обработки запроса. OK указывает на успех, FAIL указывает на ошибку. |
| ErrorInfo | String | Обязательно | Сообщение об ошибке. |
| ErrorCode | Integer | Обязательно | Код ошибки. |

## Ссылки

- [Introduction to Third-Party Webhook](https://www.tencentcloud.com/document/product/647/64412#)
- [Delete Room Metadata](https://www.tencentcloud.com/document/product/647/64376#)


---
*Источник: [https://trtc.io/document/68223](https://trtc.io/document/68223)*

---
*Источник (EN): [webhook-after-room-metadata-deleted.md](./webhook-after-room-metadata-deleted.md)*
