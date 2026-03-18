# Callback оповещения о превышении порога суточного прироста группы

## Обзор функции

Серверная часть приложения может получать предупреждения о превышении лимита суточного прироста группы через этот callback.

## Примечания

- Для включения этого callback необходимо настроить URL. Этот callback и callback после изменения профиля группы используют один и тот же переключатель. Подробные инструкции см. в разделе [Конфигурация Webhook](https://trtc.io/document/34520).
- Во время этого callback серверная часть Chat инициирует HTTP POST запрос к серверной части приложения.
- После получения запроса callback серверная часть приложения должна проверить, что `SDKAppID`, содержащийся в URL запроса, совпадает с `SDKAppID` приложения.
- Дополнительные соображения безопасности см. в разделе **Security Considerations** в [Обзор сторонних callback](https://trtc.io/document/34354).
- Перед использованием необходимо [включить функцию топиков в консоли](https://intl.cloud.tencent.com/document/product/1047/34419).

## Сценарии срабатывания Callback

- Пользователь приложения создает группу через клиент, и суточный прирост группы (количество созданных групп минус количество растворенных групп) превышает 70% лимита.
- Администратор приложения создает группу через REST API, и суточный прирост группы (количество созданных групп минус количество растворенных групп) превышает 70% лимита.

## Время срабатывания Callback

После создания группы.

## Описание вызова API

### Пример URL запроса

В следующем примере callback URL, настроенный в приложении, это `https://www.example.com`.
**Пример:**

```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json&ClientIP=$ClientIP&OptPlatform=$OptPlatform
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса — HTTPS, метод запроса — POST. |
| www.example.com | URL callback |
| SdkAppid | `SDKAppID`, назначенный консолью Chat при создании приложения |
| CallbackCommand | Фиксированное значение: `Group.CallbackOnDailyGroupQuotaAlarm`. |
| contenttype | Фиксированное значение: `JSON`. |
| ClientIP | IP-адрес клиента, например 127.0.0.1 |
| OptPlatform | Платформа клиента. Допустимые значения см. в описании `OptPlatform` в разделе **Callback Protocols** в [Обзор сторонних callback](https://intl.cloud.tencent.com/document/product/1047/34354). |

### Пример запроса

```
{    "CallbackCommand": "Group.CallbackOnDailyGroupQuotaAlarm", // Callback command    "QuotaUsed" : 7321, // daily newly created groups    "Quota": 10000,     // daily newly created groups limit    "EventTime":"1670574414123"// timestamp        }
```

### Поля запроса

| Параметр | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда callback |
| QuotaUsed | Integer | Суточное количество вновь созданных групп |
| Quota | Integer | Лимит суточного количества вновь созданных групп |
| EventTime | Integer | Временная метка |

### Пример ответа

Серверная часть приложения записывает оповещение и отправляет пакет ответа callback.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0}
```

### Поля ответа

| Объект | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Да | Результат запроса. Допустимые значения: `OK` (успех); `FAIL`: (ошибка). |
| ErrorCode | Integer | Да | Код ошибки. Рекомендуется установить значение `0`. |
| ErrorInfo | String | Да | Информация об ошибке |

## Ссылки

- [Обзор сторонних callback](https://intl.cloud.tencent.com/document/product/1047/34354)


---
*Источник: [https://trtc.io/document/57455](https://trtc.io/document/57455)*

---
*Источник (EN): [group-creation-daily-net-increase-threshold-alarm-callback.md](./group-creation-daily-net-increase-threshold-alarm-callback.md)*
