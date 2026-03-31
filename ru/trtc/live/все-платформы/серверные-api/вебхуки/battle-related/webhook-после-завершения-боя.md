# Webhook После Завершения Боя

## Описание Функции

Сервер приложения может использовать этот webhook для отслеживания завершения боя.

## Обязательные Сведения

- Для включения webhook требуется конфигурация.
- URL и включение переключателя, соответствующего этому протоколу webhook. Подробнее о методах конфигурации см. в документе [Third-Party Webhook Configuration](https://www.tencentcloud.com/document/product/647/64420#).
- Направление webhook заключается в том, что живой бэкэнд инициирует HTTP POST запрос на бэкэнд приложения.
- После получения запроса webhook сервер приложения должен проверить, совпадает ли параметр SDKAppID в URL запроса с его собственным SDKAppID.

## Сценарии, Которые Могут Вызвать Этот Webhook

- Боь завершается нормально по истечении времени.
- Во время боя все владельцы комнат выходят из боя.
- После создания боя он заканчивается сразу же, если все приглашённые владельцы комнат не согласны присоединиться к бою.

## Время Возникновения Webhook

После завершения боя.

## Описание API

### Пример URL Запроса:

В следующем примере webhook URL, настроенный для приложения, — это `https://www.example.com`.

**Пример:**

```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json&ClientIP=$ClientIP&OptPlatform=$OptPlatform
```

### Описание Параметров Запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса — HTTPS, метод запроса — POST |
| www.example.com | webhook URL |
| SdkAppid | SDKAppID, назначенный в консоли Chat при создании приложения |
| CallbackCommand | Зафиксировано как `Live.CallbackAfterEndBattle` |
| contenttype | Зафиксированное значение — `json` |
| ClientIP | IP клиента, формат: `127.0.0.1` |
| OptPlatform | Платформа клиента. Значение см. в [Introduction to Third-Party Webhook](https://www.tencentcloud.com/document/product/647/64412#) для значения параметра OptPlatform |

### Пример Пакета Запроса:

```
{    "CallbackCommand": "Live.CallbackAfterEndBattle",    "BattleId": "4siHsNsWN/T3aub9zKraqPfGQAimPhdFoe6VWhtz9lY=",    "Duration": 30000,    "CreateTime": 1739956115,    "StartTime": 1739956115,    "EndTime": 1739956145,    "OpType": 0, // 0 обозначает нормальное завершение по истечении времени; 1 обозначает завершение, вызванное выходом всех трансляторов после начала боя; 2 обозначает, что боь был создан, но завершился напрямую без начала, потому что никакие трансляторы не присоединились.    "FromRoomInfo": {  // Информация о вызывающем        "RoomId": "pk-3",        "Score": 0,        "Owner_Account": 144115245353757792    },    "ToRoomList": [ // Информация о вызываемой стороне        {            "RoomId": "pk-5",            "Score": 0,            "Owner_Account": 144115245442327522        }    ],    "EventTime": 1739956146119}
```

### Описание Полей Пакета Запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда callback |
| BattleId | String | ID боя |
| Duration | Integer | Длительность боя |
| CreateTime | Integer | Время создания боя |
| StartTime | Integer | Время начала боя |
| EndTime | Integer | Время завершения боя |
| OpType | Integer | 0 обозначает нормальное завершение по истечении времени; 1 обозначает завершение, вызванное выходом всех владельцев комнат после начала боя; 2 обозначает, что боь была создана, но завершилась напрямую без начала, потому что никакие владельцы комнат не присоединились. |
| FromRoomInfo | String | Информация о вызывающем боя |
| ToRoomList | Array | Информация о вызываемой стороне боя |
| RoomId | String | ID комнаты |
| Score | Integer | Счёт комнаты в бою |
| Owner_Account | String | Владелец комнаты в бою |
| EventTime | Integer | Временная метка уровня миллисекунд, вызванная событием |

### Пример Пакета Ответа

После синхронизации данных приложением в фоновом режиме оно отправляет пакет ответа webhook.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0 // Игнорировать результат webhook}
```

### Описание Полей Пакета Ответа

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Обязательное | Результат обработки запроса. OK означает успешную обработку, FAIL означает ошибку |
| ErrorInfo | String | Обязательное | Сообщение об ошибке |
| ErrorCode | Integer | Обязательное | Код ошибки |

## Ссылки

- [Introduction to Third-Party Webhook](https://www.tencentcloud.com/document/product/647/64412#)


---
*Источник: [https://trtc.io/document/68261](https://trtc.io/document/68261)*

---
*Источник (EN): [webhook-after-ending-battle.md](./webhook-after-ending-battle.md)*
