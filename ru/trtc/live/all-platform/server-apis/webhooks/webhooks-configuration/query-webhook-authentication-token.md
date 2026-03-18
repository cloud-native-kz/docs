# Запрос маркера аутентификации вебхука

## Обзор функции

Администраторы приложения могут запрашивать маркер аутентификации вебхука через этот интерфейс. Для получения подробной информации об использовании маркера см. [Соображения безопасности](https://www.tencentcloud.com/document/product/647/64412#security-considerations).

## Описание вызова API

### Пример URL запроса

```
https://xxxxxx/v4/live_config/get_callback_token?sdkappid=88888888&identifier=admin&usersig=xxx&random=99999999&contenttype=json
```

### Параметры запроса

В таблице ниже приведены только параметры, измененные при вызове этого API, и их описание. Для получения дополнительной информации см. [Обзор RESTful API](https://www.tencentcloud.com/document/product/647/63398#).

| Параметр | Описание |
| --- | --- |
| xxxxxxx | Зарезервированный домен для страны/региона, где расположен SDKAppID: Китай: `console.tim.qq.com`Сингапур: `adminapisgp.im.qcloud.com`Америка: `adminapiusa.im.qcloud.com` |
| v4/livee_config/get_callback_token | API запроса |
| sdkappid | SDKAppID, назначенный консолью Chat при создании приложения |
| identifier | Должна быть учетная запись администратора приложения. Для получения дополнительной информации см. [Администратор приложения](https://www.tencentcloud.com/document/product/647/69882#app-admin) |
| usersig | Подпись, созданная учетной записью администратора приложения. Подробные инструкции см. в разделе [Генерация UserSig](https://www.tencentcloud.com/document/product/647/69883#) |
| random | Случайное 32-битное целое число без знака в диапазоне от 0 до 4294967295 |
| contenttype | Формат запроса — фиксированное значение `json` |

### Максимальная частота вызовов

200 запросов/сек.

### Пример пакетов запроса

**Базовая форма**

```
{}
```

### Поля пакета запроса

### Пример пакетов ответа

**Базовая форма**

```
{    "ErrorCode": 0,    "ErrorInfo": "",    "ActionStatus": "OK",    "RequestId": "Id-59876bec05e648efbd5bb9373bdecbc1-O-Seq-1424636",    "Response": {        "Token": "kdjsgjdskgjwejsdkkjgkjfklgjdfkjhnkdfhjgkglasdjkfjsekdhgjfsdhgsdjgkdjskgjfhjdfkjgsfdkjgeljsfkjsdkgdfkhgdfjgksdjfsdkjfksdgskhgssss",        "IsTokenEnable": true    }}
```

### Описание полей пакета ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ActionStatus | String | Результат процесса запроса: OK — успех; FAIL — ошибка |
| ErrorCode | Integer | Код ошибки. 0: успех; другие значения: ошибка |
| ErrorInfo | String | Сообщение об ошибке |
| RequestId | String | Уникальный ID запроса возвращается с каждым запросом и требуется предоставить этот RequestId при локализации проблем |
| Token | String | Маркер, используемый для аутентификации вебхука. Для использования маркера см. [Соображения безопасности](https://www.tencentcloud.com/document/product/647/64412#security-considerations) |
| IsTokenEnable | Bool | Включена ли аутентификация вебхука, true означает включено, false означает отключено |

## Коды ошибок

Если не возникает сетевая ошибка (например, ошибка 502), код состояния HTTP для этого интерфейса всегда будет 200. Фактические коды ошибок и сообщения передаются через ErrorCode и ErrorInfo в теле ответа.

Распространенные коды ошибок (60000–79999) см. в документации [Код ошибки](https://www.tencentcloud.com/document/product/647/60027#).

Частные коды ошибок для этого API приведены ниже:

| Код ошибки | Описание |
| --- | --- |
| 100001 | Внутренняя ошибка сервера, повторите попытку |
| 100002 | Недопустимый параметр. Проверьте запрос в соответствии с описанием ошибки. |
| 100302 | Конфигурация вебхука аутентификации не существует. Вы можете создать ее, установив интерфейс маркера аутентификации вебхука. |


---
*Источник: [https://trtc.io/document/69529](https://trtc.io/document/69529)*

---
*Источник (EN): [query-webhook-authentication-token.md](./query-webhook-authentication-token.md)*
