# Webhook После создания боя

## Описание функции

Сервер приложения может использовать этот webhook для просмотра информации о боях, создаваемых пользователями в режиме реального времени.

## Важная информация

- Чтобы включить webhook, необходимо настроить URL webhook и включить переключатель, соответствующий этому протоколу webhook. Метод конфигурации см. в документации [Third-Party Webhook Configuration](https://www.tencentcloud.com/document/product/647/64420#).
- Направление webhook заключается в том, что сервер прямых трансляций инициирует POST-запрос HTTP на сервер приложения.
- После получения запроса webhook сервер приложения должен проверить, является ли параметр SDKAppID в URL-адресе запроса его собственным SDKAppID.

## Сценарии, которые могут вызвать этот webhook

- Пользователь приложения успешно создает бой через клиент.
- Администратор приложения успешно создает бой через REST API.

## Время возникновения webhook

После успешного создания боя.

## Описание API

### Пример URL запроса:

В следующем примере webhook URL, настроенный для приложения, — это `https://www.example.com`.

**Пример:**

```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json&ClientIP=$ClientIP&OptPlatform=$OptPlatform
```

### Описание параметров запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса — HTTPS, метод запроса — POST. |
| www.example.com | URL webhook |
| SdkAppid | SDKAppID, назначенный в консоли Chat при создании приложения |
| CallbackCommand | Фиксировано как `Live.CallbackAfterCreateBattle` |
| contenttype | Фиксированное значение — `json` |
| ClientIP | IP-адрес клиента, формат: `127.0.0.1` |
| OptPlatform | Платформа клиента. Значение см. в документации [Introduction to Third-Party Webhook](https://www.tencentcloud.com/document/product/647/64412#) для смысла параметра OptPlatform. |

### Пример пакета запроса

```
{    "CallbackCommand": "Live.CallbackAfterCreateBattle",    "Operator_Account": "brennanli",    "BattleId": "4siHsNsWN/T3aub9zKraqPbSEGRX2z6gs3LDFi+d/3M=",  //battle id    "FromRoomId": "pk-3", // Room ID of the caller initiating the battle    "ToRoomIdList": [ // Room ID list of the callee participating in the battle        "pk-5"    ],    "Timeout": 30000, // If NeedResponse is true, the maximum waiting duration for the callee to process; if the callee does not process, it indicates giving up participating in the battle    "Duration": 60000, // Duration after the battle starts, in milliseconds    "NeedResponse": false, // If false, start the battle directly; if true, wait for the callees to process before starting the battle    "ExtensionInfo": "extension pk",    "EventTime":1739954005000}
```

### Описание полей пакета запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда webhook. |
| Operator_Account | String | Пользователь, инициирующий запрос боя |
| BattleId | String | Идентификатор боя |
| FromRoomId | String | Идентификатор комнаты инициатора боя |
| ToRoomIdList | Array | Список комнат участников боя |
| Timeout | Integer | Максимальная длительность ожидания после создания боя для обработки вызываемыми сторонами, единица: мс. |
| Duration | Integer | Длительность боя |
| NeedResponse | Bool | После создания боя требуется ли согласие владельца комнаты вызываемой стороны для присоединения? |
| ExtensionInfo | String | Расширенная информация боя |
| EventTime | Integer | Временная метка на уровне миллисекунд, вызванная событием |

### Пример пакета ответа

После синхронизации данных приложением в фоновом режиме он отправляет пакет ответа webhook.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0 // Ignore webhook result}
```

### Описание полей пакета ответа

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Обязательный | Результат обработки запроса: OK — успех; FAIL — ошибка |
| ErrorCode | Integer | Обязательный | Код ошибки, здесь 0 означает игнорирование результата ответа |
| ErrorInfo | String | Обязательный | Сообщение об ошибке |

## Ссылки

- [Introduction to Third-Party Webhook](https://www.tencentcloud.com/document/product/647/64412#)


---
*Источник: [https://trtc.io/document/68259](https://trtc.io/document/68259)*

---
*Источник (EN): [webhook-after-creating-battle.md](./webhook-after-creating-battle.md)*
