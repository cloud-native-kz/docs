# Обратный вызов при достижении 70% от создания комнат

## Описание функции

Бэкэнд приложения может просматривать количество созданных комнат в текущей комнате через этот обратный вызов.

## Меры предосторожности

- Для включения обратного вызова необходимо настроить URL обратного вызова и включить переключатель, соответствующий этому протоколу обратного вызова. Способ конфигурации см. в разделе [Third-Party Callback Configuration](https://www.tencentcloud.com/document/product/647/64420#).
- Направление обратного вызова — от бэкэнда Live к бэкэнду приложения через HTTP POST-запрос.
- После получения запроса обратного вызова бэкэнд приложения должен проверить, совпадает ли значение параметра SDKAppID в URL-адресе запроса с его собственным SDKAppID.

## Сценарии срабатывания обратного вызова

- Пользователи приложения создают комнату через клиент.
- Администраторы приложения создают комнату через REST API.

## Время срабатывания обратного вызова

Комната успешно создана.

## Описание API

### Образец URL-адреса запроса

В следующем примере URL-адрес обратного вызова, настроенный для приложения: `https://www.example.com`.

**Пример:**

```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json&ClientIP=$ClientIP&OptPlatform=$OptPlatform
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса — HTTPS, способ запроса — POST. |
| www.example.com | URL-адрес обратного вызова |
| SdkAppid | SDKAppID, назначенный в консоли IM при создании приложения |
| CallbackCommand | `Live.CallbackAfterCreateRoomReachingThreshold` |
| contenttype | Значение фиксируется как `json`. |
| ClientIP | IP-адрес клиента в формате `127.0.0.1`. |
| OptPlatform | Платформа клиента. Допустимые значения см. в описании параметра OptPlatform в Webhook Protocol в [Webhook Overview](https://www.tencentcloud.com/document/product/647/64412#). |

### Образец пакета запроса

```
{    "CallbackCommand": "Live.CallbackAfterCreateRoomReachingThreshold",    "Operator_Account": "brennanli",    "EventTime": 1739966441121,    "CurRoomCount": 400,    "MaxRoomCount": 500}
```

### Поля пакета запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда обратного вызова |
| Operator_Account | String | UserID оператора, инициирующего запрос createRoom |
| CurRoomCount | String | Текущее количество созданных комнат |
| MaxRoomCount | Array | Максимальное количество созданных комнат |
| EventTime | Integer | Временная метка срабатывания события в миллисекундах. |

### Образец пакета ответа

Пакет ответа возвращается после синхронизации данных бэкэндом приложения.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0 // Ignore the callback result}
```

### Поля пакета ответа

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Обязательно | Результат обработки запроса. OK: обработка успешна; FAIL: обработка не удалась. |
| ErrorInfo | String | Обязательно | Сообщение об ошибке |
| ErrorCode | Integer | Обязательно | Код ошибки. Введите 0 здесь, чтобы игнорировать результат обратного вызова. |

## Справочные материалы

- [Webhook Overview](https://www.tencentcloud.com/document/product/647/64412)


---
*Источник: [https://trtc.io/document/70485](https://trtc.io/document/70485)*

---
*Источник (EN): [creating-room-reaches-70-alert-callback.md](./creating-room-reaches-70-alert-callback.md)*
