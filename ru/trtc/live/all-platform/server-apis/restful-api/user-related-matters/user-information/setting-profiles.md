# Установка профилей

## Обзор функции

Этот API используется для установки [стандартных полей профиля](https://intl.cloud.tencent.com/document/product/1047/33520) и [пользовательских полей профиля](https://intl.cloud.tencent.com/document/product/1047/33520).

## Описание вызова API

### Пример URL запроса

```
https://xxxxxx/v4/profile/portrait_set?sdkappid=88888888&identifier=admin&usersig=xxx&random=99999999&contenttype=json
```

### Параметры запроса

В следующей таблице описаны измененные параметры при вызове этого API. Для других параметров см. [Обзор RESTful API](https://intl.cloud.tencent.com/document/product/1047/34620).

| Параметр | Описание |
| --- | --- |
| xxxxxx | Доменное имя, соответствующее стране/региону, где находится ваш SDKAppID.Китай: `console.tim.qq.com`Сингапур: `adminapisgp.im.qcloud.com`Сеул: `adminapikr.im.qcloud.com`Токио: `adminapijpn.im.qcloud.com`Франкфурт: `adminapiger.im.qcloud.com`Кремниевая долина: `adminapiusa.im.qcloud.com`Джакарта: `adminapiidn.im.qcloud.com` |
| v4/profile/portrait_set | API запроса |
| sdkappid | SDKAppID, назначенный консолью Chat при создании приложения |
| identifier | Учетная запись администратора приложения. Для получения дополнительной информации см. раздел **Администратор приложения** в [Аутентификация входа](https://intl.cloud.tencent.com/document/product/1047/33517). |
| usersig | Подпись, созданная учетной записью администратора приложения. Подробнее см. [Создание UserSig](https://intl.cloud.tencent.com/document/product/1047/34385). |
| random | Случайное 32-битное целое число без знака в диапазоне от 0 до 4294967295. |
| contenttype | Формат запроса, который всегда должен быть `json`. |

### Максимальная частота вызовов

200 вызовов в секунду

### Пример запроса

```
{    "From_Account":"id",    "ProfileItem":    [        {            "Tag":"Tag_Profile_IM_Nick",            "Value":"MyNickName"        }    ]}
```

### Поля запроса

| Поле | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| From_Account | String | Да | UserID пользователя, чей профиль необходимо установить |
| ProfileItem | Array | Да | Массив объектов профиля целевого пользователя. Каждый объект в массиве содержит тег и значение. |
| Tag | String | Да | Поле профиля для установки. Поля профиля, которые можно установить, включают:[Стандартные поля профиля](https://intl.cloud.tencent.com/document/product/1047/33520)[Пользовательские поля профиля](https://intl.cloud.tencent.com/document/product/1047/33520) |
| Value | uint64_t/string/bytes | Да | Значение поля профиля для установки. Подробнее см. [Поля профиля](https://intl.cloud.tencent.com/document/product/1047/33520). |

### Пример ответа

```
{    "ActionStatus":"FAIL",    "ErrorCode":40001,    "ErrorInfo":"Err_Profile_Comm_Decode_Fail",    "ErrorDisplay":""}
```

### Поля ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ActionStatus | String | Результат запроса. `OK` означает, что запрос был успешным. `FAIL` означает, что запрос не удался. |
| ErrorCode | Integer | Код ошибки. `0`: Успешно; другие значения: Ошибка |
| ErrorInfo | String | Подробная информация об ошибке. |
| ErrorDisplay | String | Подробная информация, отображаемая на клиенте. |

## Коды ошибок

Возвращаемый HTTP-статус для этого API всегда 200, если не произойдет ошибка сети (например, ошибка 502). Конкретный код ошибки и подробности можно найти в полях ответа `ErrorCode` и `ErrorInfo` соответственно.
Для общих кодов ошибок (60000-79999) см. [Коды ошибок](https://intl.cloud.tencent.com/document/product/1047/34348).
В следующей таблице описаны коды ошибок, характерные для этого API:

| Код ошибки | Описание |
| --- | --- |
| 40001 | Неверный параметр запроса. Проверьте ваш запрос в соответствии с описанием ошибки. |
| 40003 | Запрашиваемая учетная запись не существует. |
| 40004 | Запрос требует разрешения администратора приложения. |
| 40006 | Внутренняя ошибка сервера. Повторите попытку позже. |
| 40008 | Нет разрешения на запись полей профиля. |
| 40009 | Тег поля профиля не существует. |
| 40601 | Значение поля профиля превышает ограничение длины в 500 байт. |
| 40605 | Неверное значение стандартного поля профиля. Подробнее см. [Стандартные поля профиля](https://intl.cloud.tencent.com/document/product/1047/33520). |
| 40610 | Неверный тип значения стандартного поля профиля. Подробнее см. [Стандартные поля профиля](https://intl.cloud.tencent.com/document/product/1047/33520). |

## Инструмент отладки API

Используйте [онлайн-инструмент отладки RESTful API](https://tcc.tencentcs.com/im-api-tool/index.html#/v4/profile/portrait_set) для отладки этого API.

## Ссылки

Получение профилей ([v4/profile/portrait_get](https://intl.cloud.tencent.com/document/product/1047/34917))


---
*Источник: [https://trtc.io/document/34916](https://trtc.io/document/34916)*

---
*Источник (EN): [setting-profiles.md](./setting-profiles.md)*
