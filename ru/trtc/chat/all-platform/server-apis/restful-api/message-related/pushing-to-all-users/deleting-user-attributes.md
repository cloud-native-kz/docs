# Удаление атрибутов пользователя

## Обзор функции

Этот API используется администратором для удаления атрибутов пользователей. Каждый запрос может удалять атрибуты максимум для 100 пользователей. Перед использованием этого API обязательно [установите имена атрибутов приложения](https://intl.cloud.tencent.com/document/product/1047/37167).

## Описание вызова API

Отправка для всех пользователей доступна только в Pro, Pro Plus и Enterprise версиях. Чтобы использовать эту функцию, необходимо [приобрести Pro, Pro Plus или Enterprise версию](https://www.tencentcloud.com/document/product/1047/34577), перейти на [консоль](https://console.trtc.io/chat), выбрать **Конфигурация функций** > **Вход и сообщения** > **Отправка для всех пользователей** и включить функцию.

### Пример URL запроса

```
https://xxxxxx/v4/all_member_push/im_remove_attr?usersig=xxx&identifier=admin&sdkappid=88888888&random=99999999&contenttype=json
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса — HTTPS, метод запроса — POST. |
| xxxxxx | Доменное имя, соответствующее стране/региону, где находится ваш SDKAppID. Китай: `console.tim.qq.com` Сингапур: `adminapisgp.im.qcloud.com` Сеул: `adminapikr.im.qcloud.com` Франкфурт: `adminapiger.im.qcloud.com` Токио: `adminapijpn.im.qcloud.com` Кремниевая долина: `adminapiusa.im.qcloud.com` Джакарта: `adminapiidn.im.qcloud.com` |
| v4/all_member_push/im_remove_attr | API запроса |
| usersig | Подпись, созданная в учетной записи администратора приложения. Дополнительные сведения см. в [Генерирование UserSig](https://intl.cloud.tencent.com/document/product/1047/34385). |
| identifier | Учетная запись администратора приложения. |
| sdkappid | `SDKAppID`, назначенный консолью Chat при создании приложения |
| random | Случайное 32-битное целое число без знака |
| contenttype | Значение всегда `json`. |

### Максимальная частота вызовов

100 раз/секунду

### Пример запроса

```
{    "UserAttrs": [        {            "To_Account": "xiaojun013",            "Attrs": [                "sex",                "city"            ]        },        {            "To_Account": "xiaojun012",            "Attrs": [                "sex",                "city"            ]        }    ]}
```

### Поля запроса

| Поле | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| To_Account | String | Да | Учетная запись целевого пользователя |
| Attrs | Array | Да | Набор тегов. Обратите внимание, что здесь нужно указать только имена атрибутов. Дополнительные сведения о формате и значениях `Attrs` см. в [Установка имен атрибутов приложения](https://intl.cloud.tencent.com/document/product/1047/37167). |

### Пример ответа

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0}
```

### Поля ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ActionStatus | String | Результат запроса. `OK`: Успешно. `FAIL`: Ошибка |
| ErrorCode | Integer | Код ошибки |
| ErrorInfo | String | Информация об ошибке |

## Коды ошибок

Если не возникает ошибка сети (например, ошибка 502), HTTP код возврата для этого API всегда 200. `ErrorCode` **и** `ErrorInfo` **в ответе представляют фактический код ошибки и информацию об ошибке.** Общие коды ошибок (60000–79999) см. в [Коды ошибок](https://intl.cloud.tencent.com/document/product/1047/34348).
В следующей таблице описаны коды ошибок, специфичные для этого API:

| Код ошибки | Описание |
| --- | --- |
| 90001 | Ошибка при разборе формата JSON. Проверьте, соответствует ли JSON запрос спецификациям JSON. |
| 90009 | Запрос требует разрешений администратора приложения. |
| 90018 | Количество запрашиваемых учетных записей превышает лимит. |
| 90033 | Недопустимый атрибут. |
| 91000 | Внутренняя ошибка сервиса. Повторите попытку. |

## Инструмент отладки API

Используйте [инструмент онлайн-отладки RESTful API](https://tcc.tencentcs.com/im-api-tool/index.html#/v4/all_member_push/im_remove_attr) для отладки этого API.

## Ссылки

- [API отправки для всех пользователей](https://intl.cloud.tencent.com/document/product/1047/37165)
- [Отправка для всех пользователей](https://intl.cloud.tencent.com/document/product/1047/37166)
- [Установка имен атрибутов приложения](https://intl.cloud.tencent.com/document/product/1047/37167)
- [Получение имен атрибутов приложения](https://intl.cloud.tencent.com/document/product/1047/37168)
- [Установка атрибутов пользователя](https://intl.cloud.tencent.com/document/product/1047/37170)
- [Получение атрибутов пользователя](https://intl.cloud.tencent.com/document/product/1047/37169)
- [Добавление тегов пользователя](https://intl.cloud.tencent.com/document/product/1047/37173)
- [Получение тегов пользователя](https://intl.cloud.tencent.com/document/product/1047/37172)
- [Удаление тегов пользователя](https://intl.cloud.tencent.com/document/product/1047/37174)
- [Удаление всех тегов пользователя](https://intl.cloud.tencent.com/document/product/1047/37175)


---
*Источник: [https://trtc.io/document/37171](https://trtc.io/document/37171)*

---
*Источник (EN): [deleting-user-attributes.md](./deleting-user-attributes.md)*
