# Инвалидация состояний входа в аккаунт

## Описание функции

Этот API используется для инвалидации состояния входа (например, UserSig) аккаунта приложения.

Например, когда разработчик обнаруживает вредоносный аккаунт, разработчик может вызвать этот API для инвалидации состояния входа пользователя. Когда пользователь пытается войти в Chat, используя оригинальное состояние UserSig, вход не удается.

> **Примечание:** Когда администратор использует этот API для инвалидации статуса входа пользователя, все предыдущие значения UserSig для этого пользователя истекают. Сведения о поведении на клиентской стороне см. в документации [login](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a73fc0e14c5f2f5fc06a80081479fb416). После инвалидации состояния входа пользователя с помощью этого API пользователь может войти в Chat, используя недавно созданное состояние UserSig. Этот API может инвалидировать только один аккаунт за раз.

## Описание вызова

### Пример URL запроса

```
https://xxxxxx/v4/im_open_login_svc/kick?sdkappid=88888888&identifier=admin&usersig=xxx&random=99999999&contenttype=json
```

### Параметры запроса

В следующей таблице описаны только параметры, которые изменяются при вызове этого API. Для получения дополнительной информации о других параметрах см. [Обзор RESTful API](https://intl.cloud.tencent.com/document/product/1047/34620).

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса — HTTPS, метод запроса — POST. |
| xxxxxx | Страна/регион, в котором находится ваш SDKAppID. Китай: `console.tim.qq.com` Сингапур: `adminapisgp.im.qcloud.com` Сеул: `adminapikr.im.qcloud.com` Токио: `adminapijpn.im.qcloud.com` Франкфурт: `adminapiger.im.qcloud.com` Кремниевая долина: `adminapiusa.im.qcloud.com` Джакарта: `adminapiidn.im.qcloud.com` |
| v4/im_open_login_svc/kick | API запроса. |
| sdkappid | SDKAppID, назначенный консолью Chat при создании приложения. |
| identifier | Значение этого параметра должно быть аккаунтом администратора приложения. Дополнительные сведения см. в разделе [App Admin](https://intl.cloud.tencent.com/document/product/1047/33517#app-.E7.AE.A1.E7.90.86.E5.91.98). |
| usersig | Подпись, созданная аккаунтом администратора приложения. Подробности операции см. в разделе [Generating UserSig](https://intl.cloud.tencent.com/document/product/1047/34385). |
| random | Случайное 32-битное целое число без знака в диапазоне от 0 до 4294967295. |
| contenttype | Формат запроса. Значение всегда `json`. |

### Максимальная частота вызовов

200 раз/сек

### Пример пакета запроса

```
{   "UserID":"test"}
```

### Поля пакета запроса

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| UserID | String | Обязательное | Имя пользователя |

### Пример пакета ответа

```
{   "ActionStatus":"OK",   "ErrorInfo":"",   "ErrorCode":0}
```

### Поля пакета ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ActionStatus | String | Результат обработки запроса. OK: успешно. FAIL: не удалось. |
| ErrorCode | Integer | Код ошибки. 0: успешно. Другие значения: не удалось. |
| ErrorInfo | String | Информация об ошибке. |

## Коды ошибок

Если не возникает сетевая ошибка (например, ошибка 502), код возврата HTTP для этого API всегда равен 200. ErrorCode и ErrorInfo в пакете ответа представляют фактический код ошибки и информацию об ошибке.
Для общих кодов ошибок (60000–79999) см. [Коды ошибок](https://intl.cloud.tencent.com/document/product/1047/34348).
В следующей таблице описаны коды ошибок, специфичные для этого API.

| Код ошибки | Описание |
| --- | --- |
| 70107 | Запрошенный аккаунт пользователя не существует. |
| 70169 | Произошел внутренний тайм-аут сервера. Попробуйте позже. |
| 70402 | Параметры недействительны. Проверьте, указаны ли обязательные поля и соответствуют ли указанные поля требованиям протокола. |
| 70403 | Запрос требует прав администратора приложения. |
| 70500 | Произошла внутренняя ошибка сервера. Попробуйте позже. |

## Инструмент отладки

Используйте [инструмент онлайн-отладки RESTful API](https://tcc.tencentcs.com/im-api-tool/#/v4/openim/admin_msgwithdraw?locale=en-US) для отладки этого API.

## Ссылки

- Импорт аккаунта ([v4/im_open_login_svc/account_import](https://intl.cloud.tencent.com/document/product/1047/34953))
- Импорт нескольких аккаунтов ([v4/im_open_login_svc/multiaccount_import](https://intl.cloud.tencent.com/document/product/1047/34954))
- Удаление аккаунтов ([v4/im_open_login_svc/account_delete](https://intl.cloud.tencent.com/document/product/1047/34955))
- Запрос аккаунтов ([v4/im_open_login_svc/account_check](https://intl.cloud.tencent.com/document/product/1047/34956))
- Запрос онлайн-статуса аккаунта ([v4/openim/query_online_status](https://intl.cloud.tencent.com/document/product/1047/35477))


---
*Источник: [https://trtc.io/document/34957](https://trtc.io/document/34957)*

---
*Источник (EN): [invalidating-account-login-states.md](./invalidating-account-login-states.md)*
