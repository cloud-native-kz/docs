# Webhook после начала боя

## Описание функции

Сервер приложения может использовать этот webhook для мониторинга начала боя.

## Важные моменты

- Для включения webhook необходимо настроить URL webhook и включить переключатель, соответствующий этому протоколу webhook. Методы настройки см. в документе [Конфигурация webhook третьей стороны](https://www.tencentcloud.com/document/product/647/64420#).
- Направление webhook таково, что серверная часть боев инициирует HTTP Post запрос к серверной части приложения.
- После получения запроса webhook серверная часть приложения должна проверить, что параметр SDKAppID в URL запроса соответствует ее собственному SDKAppID.

## Сценарии, которые могут вызвать этот webhook

- После создания боя он может напрямую перейти в запущенное состояние без ожидания, когда .
- После создания боя, как только все получатели вызова обработают запрос боя, если хотя бы один владелец комнаты получателя согласится присоединиться к бою, бой официально начинается.

## Время возникновения webhook

После официального запуска боя.

## Описание API

### Пример URL запроса:

В следующем примере настроенный для приложения URL webhook имеет значение `https://www.example.com`.

**Пример:**

```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json&ClientIP=$ClientIP&OptPlatform=$OptPlatform
```

### Описание параметров запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса: HTTPS, метод запроса: POST |
| www.example.com | URL webhook |
| SdkAppid | SDKAppID, назначенный в консоли Chat при создании приложения |
| CallbackCommand | Зафиксирован как `Live.CallbackAfterStartBattle` |
| contenttype | Зафиксированное значение — `json` |
| ClientIP | IP клиента, формат: `127.0.0.1` |
| OptPlatform | Платформа клиента. Значения см. в [Введение в webhook третьей стороны](https://www.tencentcloud.com/document/product/647/64412#) для значения параметра OptPlatform |

### Пример пакета запроса

```
{    "CallbackCommand": "Live.CallbackAfterStartBattle",      "BattleId": "4siHsNsWN/T3aub9zKraqI4zZAyPRpXQhdtKv1q4HOs=", // battle id    "Duration": 60000, // battle duration    "CreateTime": 1739954005, // battle creation time, in seconds    "StartTime": 1739954005, // battle start time, in seconds    "FromRoomInfo": {  // Caller information in battle        "RoomId": "pk-3",        "Owner_Account": "brennan"    },    "ToRoomList": [ // Called party information in battle        {            "RoomId": "pk-5",            "Owner_Account": "tandy"        }    ],    "EventTime": 1739954005000, // Callback trigger time, in milliseconds}
```

### Описание полей пакета запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда webhook |
| BattleId | String | Идентификатор боя |
| Duration | Integer | Продолжительность боя |
| CreateTime | Integer | Время создания боя |
| StartTime | Integer | Время начала боя |
| FromRoomInfo | String | Информация об инициаторе в бою |
| ToRoomList | Array | Информация о получателе, участвующем в бою |
| RoomId | String | Идентификатор комнаты |
| Owner_Account | String | Идентификатор владельца комнаты |
| EventTime | Integer | Временная метка уровня миллисекунд, вызванная событием |

### Пример пакета ответа

После синхронизации данных в фоновом режиме приложение отправляет пакет ответа webhook.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0 // Ignore webhook result}
```

### Описание полей пакета ответа

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Обязательно | Результат обработки запроса. OK указывает на успех, FAIL указывает на отказ. |
| ErrorCode | Integer | Обязательно | Код ошибки. Укажите 0 здесь, чтобы игнорировать результат webhook. |
| ErrorInfo | String | Обязательно | Сообщение об ошибке. |

## Справочные материалы

- [Введение в webhook третьей стороны](https://www.tencentcloud.com/document/product/647/64412#)


---
*Источник: [https://trtc.io/document/68260](https://trtc.io/document/68260)*

---
*Источник (EN): [webhook-after-starting-battle.md](./webhook-after-starting-battle.md)*
