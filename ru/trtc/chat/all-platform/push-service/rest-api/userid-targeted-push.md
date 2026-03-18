# Целевая push-рассылка по UserID

Обзор функции

- Push на указанный список учетных записей получателей, который должен содержать от [1, 500] учетных записей.
- Поддерживает Online Channel, Manufacturer Channel (APNS, Huawei, Honor, OPPO, vivo, Xiaomi, Meizu, Google).
- По умолчанию не увеличивает счетчик непрочитанных сообщений.

> **Примечание:** Этот интерфейс поддерживает как Online Push, так и Offline Push. Online Push поддерживается только в версии SDK ≥ 8.2.6325.

## Описание вызова API

### Пример URL запроса

```
https://xxxxxx/v4/timpush/batch?usersig=xxx&identifier=admin&sdkappid=88888888&random=99999999&contenttype=json
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса: HTTPS Метод запроса: POST |
| xxxxxx | Выделенный домен, соответствующий стране/региону вашего SDKAppID. Китай: `console.tim.qq.com` Сингапур: `adminapisgp.im.qcloud.com` Сеул: `adminapikr.im.qcloud.com` Франкфурт: `adminapiger.im.qcloud.com` Кремниевая долина: `adminapiusa.im.qcloud.com` Джакарта: `adminapiidn.im.qcloud.com` |
| v4/timpush/batch | API запроса |
| usersig | Подпись, созданная учетной записью администратора приложения. Дополнительные сведения см. в разделе [Создание UserSig](https://www.tencentcloud.com/document/product/1047/34385) |
| identifier | Должна быть учетная запись администратора приложения. Для получения дополнительных сведений см. раздел [Администраторы приложения](https://www.tencentcloud.com/document/product/1047/33517) |
| sdkappid | SdkAppid, выданный консолью Chat при создании приложения |
| random | Случайное 32-битное целое число без знака, находящееся в диапазоне от 0 до 4294967295 |
| contenttype | Фиксированное значение: `json` |

### Ограничение частоты вызовов

По умолчанию бесплатная версия поддерживает 10 раз/с, стандартная версия 30 раз/с и продвинутая версия 40 раз/с.

### Пример пакетов запроса

```
{  "From_Account": "administrator",  "To_Account": ["user1","user2"], // Array size range between [1,500]  "MsgRandom": 3674128,  "OfflinePushInfo": {      "PushFlag": 0,  // 0 means offline push enabled, 1 means offline push disabled      "Title": "Offline Push Title",      "Desc": "Offline Push Content"  }}
```

> **Примечание:** Этот интерфейс поддерживает как Online Push, так и Offline Push. Online Push поддерживается только в версии SDK ≥ 8.2.6325.

### Поля пакета запроса

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| From_Account | String | Обязательное | Учетная запись отправителя, поддерживает UserID или RegistrationID. |
| To_Account | Array | Обязательное | Список целевых учетных записей пользователя, поддерживает UserID или RegistrationID. |
| MsgRandom | Integer | Обязательное | 32-битное целое число без знака, диапазон значений от 0 до 4294967295. Бэкенд использует дедупликацию сообщений в течение одной секунды. **Пожалуйста, убедитесь, что это случайное число**. |
| OfflinePushInfo | Object | Обязательное | Конфигурация уведомления об автономной push-рассылке, пожалуйста, обратитесь к [Описанию OfflinePushInfo](https://www.tencentcloud.com/document/product/1047/77715) |
| DataId | String | Опциональное | Пользовательский идентификатор бизнеса клиента. Это поле будет передано бэкенду приложения при обратном вызове. Поле ограничено максимум 64 байтами. |

### Пример пакетов ответа

Все успешно:

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0,    "TaskId": "batch_667015d4_537529d8_2000005e80aa873_d03ac87_56f5e750"}
```

Все ошибочно:

```
{    "ActionStatus": "FAIL",    "ErrorInfo": "Invalid format of MsgRandom", // MsgRandom is invalid or not set    "ErrorCode": 90001,    "TaskId": ""}
```

Частично успешно:

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0,    "TaskId": "batch_667015d4_537529d8_2000005e80aa873_d03ac87_56f5e750",    "ErrorList": [        {            "ErrorCode": 70107, // account does not exist            "To_Account": "user"        }    ]}
```

### Описание полей пакета ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ActionStatus | String | Результат обработки запроса: OK: означает успешную обработку. FAIL: обработка не удалась. |
| ErrorCode | Integer | Код ошибки. |
| ErrorInfo | String | Сообщение об ошибке. |
| TaskId | String | ID задачи push-рассылки. |
| ErrorList | Object Array | Список учетных записей с неудачной отправкой. Если все отправлены успешно, ErrorList пусто. |

Описание полей JSON-объекта в массиве ErrorList

| Поле | Тип | Описание |
| --- | --- | --- |
| To_Account | String | Целевая учетная запись пользователя: UserID или RegistrationID. |
| ErrorCode | Integer | Код ошибки. |
| ErrorInfo | String | Описание ошибки, может быть пусто. |

## Коды ошибок

Если не произойдет сетевая ошибка (например, ошибка 502), код состояния HTTP для этого интерфейса всегда будет 200. **Реальные коды ошибок и сообщения указаны в теле ответа через ErrorCode и ErrorInfo**. Для общих кодов ошибок (60000–79999) см. документ [Код ошибки](https://intl.cloud.tencent.com/document/product/1047/34348).

Приватные коды ошибок для этого API следующие:

| Код ошибки | Описание |
| --- | --- |
| 90001 | Ошибка при разборе формата JSON. Пожалуйста, убедитесь, что пакет запроса соответствует спецификации JSON. |
| 90009 | Запрос требует разрешения администратора приложения. |
| 90045 | All-user/Tags/Single Push не включен. |
| 90057 | Предоставленный DataId превышает максимально допустимую длину в 64 байта. |
| 91000 | Внутренняя ошибка службы, пожалуйста, попробуйте позже. |

## Инструмент отладки API

Используйте инструмент [RESTful API Online Test](https://tcc.tencentcs.com/im-api-tool/index.html#/v4/timpush/batch) для отладки этого интерфейса.

## Ссылки

- [All-user/Tag Push](https://www.tencentcloud.com/document/product/1047/60561)
- [Single push with userID](https://www.tencentcloud.com/document/product/1047/67553)
- [Obtaining Application Attribute Names](https://www.tencentcloud.com/document/product/1047/60562)
- [Setting Application Attribute Names](https://www.tencentcloud.com/document/product/1047/60563)
- [Getting User Attributes](https://www.tencentcloud.com/document/product/1047/60564)
- [Setting User Attributes](https://www.tencentcloud.com/document/product/1047/60565)
- [Deleting User Attributes](https://www.tencentcloud.com/document/product/1047/60566)
- [Getting User Tags](https://www.tencentcloud.com/document/product/1047/60567)
- [Adding User Tags](https://www.tencentcloud.com/document/product/1047/60568)
- [Deleting User Tags](https://www.tencentcloud.com/document/product/1047/60569)
- [Clearing User Tags](https://www.tencentcloud.com/document/product/1047/60570)
- [Recall Push](https://www.tencentcloud.com/document/product/1047/60571)


---
*Источник: [https://trtc.io/document/67553](https://trtc.io/document/67553)*

---
*Источник (EN): [userid-targeted-push.md](./userid-targeted-push.md)*
