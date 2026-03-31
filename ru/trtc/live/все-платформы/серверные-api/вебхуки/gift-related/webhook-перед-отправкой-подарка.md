# Webhook перед отправкой подарка

## Описание функции

Backend приложения может использовать callback для определения необходимости прохождения проверки отправки подарка в других сценариях.

## Меры предосторожности

- Включить callback. Настройте URL callback и включите переключатель, соответствующий этому callback. Способ настройки см. в разделе [Конфигурация Callback](https://www.tencentcloud.com/document/product/647/64420).
- Направление callback - от Live backend к App backend через HTTP POST запрос.
- После получения запроса callback, App backend должен проверить, что значение параметра SDKAppID в URL запроса совпадает с его собственным SDKAppID.

## Сценарии срабатывания Callback

- Пользователь приложения отправляет подарок через клиент

## Время срабатывания Callback

Перед отправкой подарка.

## Описание API

### Пример URL запроса

В следующем примере URL callback, настроенный для приложения, это `https://www.example.com`.

**Пример:**

```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json&ClientIP=$ClientIP&OptPlatform=$OptPlatform
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса - HTTPS, метод запроса - POST. |
| www.example.com | URL callback. |
| SdkAppid | SDKAppID, назначенный в консоли Chat при создании приложения. |
| CallbackCommand | Зафиксирован как Live.CallbackBeforeSendGift. |
| contenttype | Значение зафиксировано как json. |
| ClientIP | IP адрес клиента в формате 127.0.0.1. |
| OptPlatform | Платформа клиента. Допустимые значения см. в описании параметра OptPlatform в протоколе Webhook в разделе [Обзор Webhook](https://www.tencentcloud.com/document/product/647/64412). |

### Пример пакета запроса

```
{    "CallbackCommand": "Live.CallbackBeforeSendGift",    "Operator_Account": "brennanli",    "RoomId":"room_id",    "GiftWater": {        "From_Account": "from",        "To_Account": ["to1"],        "Time": 1703589922,        "GiftId": "gift1",        "Count": 1,        "Coins": 1000    }}
```

### Поля пакета запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | команда callback. |
| Operator_Account | String | UserID оператора, который инициировал запрос на баттл. |
| RoomId | String | ID комнаты. |
| From_Account | String | отправитель подарка. |
| To_Account | Array | получатель подарка. |
| Time | Integer | Временная метка. |
| GiftId | String | ID подарка. |
| Count | Integer | количество подарков. |
| Coins | Integer | стоимость подарка. |

### Пример пакета ответа

Пакет ответа callback отправляется после того, как App backend синхронизирует данные.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0}
```

Если приложение должно **заблокировать отправку подарка**, установите ErrorCode в пакете ответа на ненулевое значение. **Если live backend не получит пакет ответа в течение 2 секунд, отправка подарка также будет заблокирована по умолчанию.**

Если приложение требует **сценарий неблокирующей отправки подарка** (если пакет ответа не удается отправить или live backend не возвращает пакет ответа в течение 2 секунд, в этом случае будет разрешено), вы можете установить [конфигурацию неблокирующего callback перед отправкой подарка](https://www.tencentcloud.com/document/product/647/64413).

### Поля пакета ответа

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Обязательно | Результат обработки запроса. OK: обработка выполнена успешно; FAIL: обработка не выполнена. |
| ErrorCode | Integer | Обязательно | **0 означает согласие, 1 означает отклонение. Диапазон кодов ошибок, которые могут быть переданы: [102100,102200].** |
| ErrorInfo | String | Обязательно | Сообщение об ошибке. |

## Справочные материалы

- [Обзор Webhook](https://www.tencentcloud.com/document/product/647/64412)
- [Список команд callback](https://www.tencentcloud.com/document/product/647/64413)


---
*Источник: [https://trtc.io/document/72210](https://trtc.io/document/72210)*

---
*Источник (EN): [webhook-before-sending-gift.md](./webhook-before-sending-gift.md)*
