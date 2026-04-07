# Установка конфигурации веб-хуков

## Обзор функции

Администраторы могут создавать обратные вызовы через этот API.

## Описание API

> **Примечание:** Если API вызывается несколько раз, действует последний результат.

### Пример URL запроса

```
https://xxxxxx/v1/callback/set?sdkappid=88888888&identifier=administrator&usersig=xxx&random=99999999&contenttype=json
```

### Параметры запроса

В таблице ниже перечислены только параметры, изменяемые при вызове этого API, и их описание. Для получения дополнительной информации обратитесь к [Обзор REST API](https://www.tencentcloud.com/document/product/647/60138#).

| Параметр | Описание |
| --- | --- |
| xxxxxx | Зарезервированный домен для страны/региона, где находится SDKAppID: `callkit-intl.trtc.tencent-cloud.com` |
| v1/callback/set | API запроса |
| sdkappid | SDKAppID, назначенный консолью при создании приложения |
| identifier | Должна быть учетная запись администратора Chat App |
| usersig | Подпись, созданная учетной записью администратора приложения; для получения подробных инструкций обратитесь к [Генерирование UserSig](https://www.tencentcloud.com/document/product/647/39074#) |
| random | Введите случайное 32-битное целое число без знака в диапазоне от 0 до 4294967295 |
| contenttype | Формат запроса, фиксированное значение `json` |

### Максимальная частота вызовов

10 раз в секунду.

### Пример пакета запроса

```
{    "address":"http://www.example.com/callback",    "actions": [        "call_busy",         "normal_end",        "caller_start_call",        "invite_user",        "callee_reject_call"    ]}
```

### Описание поля запроса

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| address | String | Обязательно | Адрес обратного вызова, должен начинаться с http/https; рекомендуется использовать более безопасный https |
| actions | Array | Обязательно | Сценарии, требующие запуска обратного вызова; см. [Список команд обратного вызова](https://www.tencentcloud.com/document/product/647/60135#2147ef13-cf14-4134-9b18-5e3f5d4a026c) для получения списка |

### Пример пакета ответа

```
{    "errorCode": 0,    "errorMessage": "Success",    "requestId": "a1d8543a9b1daef5d0f0c21517a4bc0a",    "data": "http://www.example.com/callback"}
```

### Описание поля пакета ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| errorCode | Integer | Код ошибки; 0 указывает на успех |
| errorMessage | String | Сообщение об ошибке |
| requestId | String | Уникальный ID запроса |
| data | String | Успешная конфигурация адреса обратного вызова |

## Коды ошибок

| Код ошибки | Описание |
| --- | --- |
| 0 | Запрос успешен |
| 50001 | Текущее приложение должно приобрести пакет TUICallKit Group Call Version для использования |
| 70001 | Адрес обратного вызова должен начинаться с http или https |


---
*Источник: [https://trtc.io/document/60134](https://trtc.io/document/60134)*

---
*Источник (EN): [establishing-webhooks-configuration.md](./establishing-webhooks-configuration.md)*
