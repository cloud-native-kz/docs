# Webhook после установки метаданных комнаты

## Описание функции

Сервер приложения может использовать этот webhook для мониторинга параметров метаданных комнаты в реальном времени.

## Важные сведения

- Для включения webhook необходимо настроить URL webhook и включить переключатель, соответствующий этому протоколу webhook. Методы конфигурации см. в документе [Конфигурация стороннего Webhook](https://www.tencentcloud.com/document/product/647/64420#).
- Направление webhook таково, что сервер трансляции инициирует HTTP POST запрос к серверу приложения.
- После получения запроса webhook сервер приложения должен проверить, является ли параметр SDKAppID в URL запроса его собственным SDKAppID.

## Сценарии, которые могут вызвать этот webhook

- Пользователи приложения устанавливают метаданные через клиент.
- Администратор приложения устанавливает метаданные через REST API.

## Время возникновения webhook

После успешной установки метаданных комнаты.

## Описание API

### Пример URL запроса:

В следующем примере URL webhook, настроенный для приложения, — это `https://www.example.com`.

**Пример:**

```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json&ClientIP=$ClientIP&OptPlatform=$OptPlatform
```

### Описание параметров запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса — HTTPS, метод запроса — POST |
| www.example.com | URL webhook |
| SdkAppid | SDKAppID, назначенный в консоли Chat при создании приложения |
| CallbackCommand | Фиксированное значение `Live.CallbackAfterSetMetadata` |
| contenttype | Фиксированное значение `json` |
| ClientIP | IP адрес клиента, формат: `127.0.0.1` |
| OptPlatform | Платформа клиента. Для значения см. [Введение в стороннее Webhook](https://www.tencentcloud.com/document/product/647/64412#) для значения параметра OptPlatform |

### Пример пакета запроса

```
{    "CallbackCommand": "Live.CallbackAfterSetMetadata",    "Operator_Account": "brennanli",    "RoomId": "live-room1111",    "Metadata": [        {            "Key": "key1",            "Value": "value1"        },        {            "Key": "key2",            "Value": "value2"        }    ],    "EventTime": 1739965885831}
```

### Описание полей пакета запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда webhook. |
| Operator_Account | String | UserID оператора, инициирующего запрос на уничтожение комнаты |
| RoomId | String | ID комнаты |
| Metadata | Array | Данные метаданных |
| EventTime | Integer | Временная метка события в миллисекундах |
| Key | String | Ключ метаданных |
| Value | String | Значение метаданных |

### Пример пакета ответа

После синхронизации данных в фоновом режиме приложение отправляет пакет ответа webhook.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0 // Игнорировать результат webhook}
```

### Описание полей пакета ответа

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Обязательно | Результат обработки запроса. OK указывает на успешную обработку, FAIL указывает на ошибку. |
| ErrorInfo | String | Обязательно | Сообщение об ошибке. |
| ErrorCode | Integer | Обязательно | Код ошибки, 0 означает ОК. |

## Справка

- [Введение в стороннее Webhook](https://www.tencentcloud.com/document/product/647/64412#)
- [Установка метаданных комнаты](https://www.tencentcloud.com/document/product/647/64375#)


---
*Источник: [https://trtc.io/document/68222](https://trtc.io/document/68222)*

---
*Источник (EN): [webhook-after-room-metadata-set.md](./webhook-after-room-metadata-set.md)*
