# Удаление атрибутов пользователя

## Обзор функции

Администратор удаляет атрибуты пользователей. Обратите внимание, что вы можете удалять атрибуты только для до 100 пользователей одновременно. Перед использованием, пожалуйста, [установите имена атрибутов приложения](https://www.tencentcloud.com/document/product/1047/60563).

### Пример URL запроса

```
https://xxxxxx/v4/timpush/remove_attr?usersig=xxx&identifier=admin&sdkappid=88888888&random=99999999&contenttype=json
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса: HTTPSМетод запроса: POST |
| xxxxxx | Выделенный домен, соответствующий стране/региону вашего SDKAppID.Китай: `console.tim.qq.com`Сингапур: `adminapisgp.im.qcloud.com`Сеул: `adminapikr.im.qcloud.com`Франкфурт: `adminapiger.im.qcloud.com`Кремниевая долина: `adminapiusa.im.qcloud.com`Джакарта: `adminapiidn.im.qcloud.com` |
| v4/timpush/remove_attr | API запроса |
| usersig | Подпись, созданная учетной записью администратора приложения. Подробнее см. [Генерирование UserSig](https://www.tencentcloud.com/document/product/1047/34385) |
| identifier | Должна быть учетная запись администратора приложения. Подробнее см. [Администраторы приложений](https://www.tencentcloud.com/document/product/1047/33517) |
| sdkappid | SdkAppid, назначенный консолью Instant Messaging при создании приложения |
| random | Случайное 32-битное беззнаковое целое число в диапазоне от 0 до 4294967295 |
| contenttype | Фиксированное значение: `json` |

### Лимит частоты вызовов

100 раз в секунду.

### Примеры пакетов запроса

```
{    "UserAttrs": [        {            "To_Account": "Mary",            "Attrs": [                "sex",                "city"            ]        },        {            "To_Account": "xiaoming",            "Attrs": [                "sex",                "city"            ]        }    ]}
```

### Описание полей пакета запроса

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| UserAttrs | Array | Обязательно | Массив атрибутов пользователя. Один атрибут пользователя состоит из To_Account и Attrs |
| To_Account | String | Обязательно | Целевая учетная запись пользователя, поддерживает UserID или RegistrationID. |
| Attrs | Array | Обязательно | Набор имен атрибутов, обратите внимание, что здесь требуются только имена атрибутов, не пары ключ-значение |

### Примеры пакетов ответа

Полностью успешно:

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0}
```

Частично успешно:

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0,    "ErrorList": [        {            "ErrorCode": 70107,            "To_Account": "Mary"        }    ]}
```

### Описание полей пакета ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ActionStatus | String | Результат обработки запроса: OK: обработка успешна. FAIL: обработка не удалась. |
| ErrorCode | Integer | Коды ошибок |
| ErrorInfo | String | Сообщение об ошибке. |
| ErrorList | Object Array | Установка атрибутов может быть частично успешной для некоторых пользователей и частично неудачной для других. Список сообщений об ошибках для неудачных учетных записей. |

Описание полей JSON объекта в массиве ErrorList

| Поле | Тип | Описание |
| --- | --- | --- |
| To_Account | String | Целевая учетная запись пользователя: UserID или RegistrationID. |
| ErrorCode | Integer | Код ошибки. |
| ErrorInfo | String | Описание ошибки, может быть пусто. |

## Коды ошибок

Если не возникнет ошибка сети (например, ошибка 502), код состояния HTTP для этого интерфейса всегда будет 200. **Реальные коды ошибок и сообщения указаны в теле ответа через ErrorCode и ErrorInfo**. Для общих кодов ошибок (60000–79999) см. документ [Код ошибки](https://intl.cloud.tencent.com/document/product/1047/34348).

Закрытые коды ошибок для этого API следующие:

| Код ошибки | Описание |
| --- | --- |
| 90001 | Ошибка анализа формата JSON, проверьте, соответствует ли пакет запроса спецификации JSON |
| 90009 | Запрос требует прав администратора приложения |
| 90018 | Количество запрошенных учетных записей превышает лимит |
| 90033 | Недействительный атрибут |
| 91000 | Внутренняя ошибка сервера, попробуйте снова |

## Инструмент отладки API

Используйте инструмент [RESTful API Online Test](https://tcc.tencentcs.com/im-api-tool/index.html#/v4/timpush/remove_attr) для отладки этого интерфейса.

## Ссылки

- [Push для всех пользователей/по тегам](https://www.tencentcloud.com/document/product/1047/60561)
- [Одиночный push с userID](https://www.tencentcloud.com/document/product/1047/67553)
- [Получение имен атрибутов приложения](https://www.tencentcloud.com/document/product/1047/60562)
- [Установка имен атрибутов приложения](https://www.tencentcloud.com/document/product/1047/60563)
- [Получение атрибутов пользователя](https://www.tencentcloud.com/document/product/1047/60564)
- [Установка атрибутов пользователя](https://www.tencentcloud.com/document/product/1047/60565)
- [Удаление атрибутов пользователя](https://www.tencentcloud.com/document/product/1047/60566)
- [Получение тегов пользователя](https://www.tencentcloud.com/document/product/1047/60567)
- [Добавление тегов пользователя](https://www.tencentcloud.com/document/product/1047/60568)
- [Удаление тегов пользователя](https://www.tencentcloud.com/document/product/1047/60569)
- [Очистка тегов пользователя](https://www.tencentcloud.com/document/product/1047/60570)
- [Отзыв push](https://www.tencentcloud.com/document/product/1047/60571)


---
*Источник: [https://trtc.io/document/60566](https://trtc.io/document/60566)*

---
*Источник (EN): [deleting-user-attributes.md](./deleting-user-attributes.md)*
