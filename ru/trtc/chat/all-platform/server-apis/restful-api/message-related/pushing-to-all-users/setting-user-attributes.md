# Установка атрибутов пользователя

## Обзор функции

Этот API используется администратором для установки атрибутов пользователей. Каждый запрос может установить атрибуты для максимум 100 пользователей. Перед использованием этого API убедитесь, что вы [установили имена атрибутов приложения](https://intl.cloud.tencent.com/document/product/1047/37167).

## Описание вызова API

Отправка всем пользователям доступна только для выпусков Pro edition, Pro Plus edition и Enterprise edition. Для использования необходимо [приобрести выпуск Pro edition, Pro Plus edition или Enterprise edition](https://www.tencentcloud.com/document/product/1047/34577), перейти в [консоль](https://console.trtc.io/chat), выбрать **Feature Configuration** > **Login and Message** > **Push to all users** и включить функцию.

### Пример URL запроса

```
https://xxxxxx/v4/all_member_push/im_set_attr?usersig=xxx&identifier=admin&sdkappid=88888888&random=99999999&contenttype=json
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса — HTTPS, метод запроса — POST. |
| xxxxxx | Доменное имя, соответствующее стране/региону, где расположен ваш SDKAppID. Китай: `console.tim.qq.com` Сингапур: `adminapisgp.im.qcloud.com` Сеул: `adminapikr.im.qcloud.com` Токио: `adminapijpn.im.qcloud.com` Франкфурт: `adminapiger.im.qcloud.com` Кремниевая долина: `adminapiusa.im.qcloud.com` Джакарта: `adminapiidn.im.qcloud.com` |
| v4/all_member_push/im_set_attr | API запроса |
| usersig | Подпись, созданная в учетной записи администратора приложения. Дополнительные сведения см. в разделе [Генерирование UserSig](https://intl.cloud.tencent.com/document/product/1047/34385). |
| identifier | Учетная запись администратора приложения. |
| sdkappid | `SDKAppID`, назначенный консолью Chat при создании приложения |
| random | Случайное 32-битное беззнаковое целое число |
| contenttype | Значение всегда равно `json`. |

### Максимальная частота вызовов

100 раз/секунду

### Пример запроса

```
{    "UserAttrs":    [        {            "To_Account": "xiaojun012",            "Attrs": {                "sex": "attr1",                "city": "attr2"            }        },        {            "To_Account": "xiaojun013",            "Attrs": {                "city": "attr3",                "sex": "attr4"            }        }    ]}
```

### Поля запроса

| Поле | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| To_Account | String | Да | Учетная запись целевого пользователя |
| Attrs | Object | Да | Набор атрибутов. Каждый атрибут представляет собой пару ключ-значение, где ключ — имя атрибута, а значение — соответствующее значение атрибута пользователя. Значение атрибута пользователя не может превышать 50 байт. |

### Пример ответа

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0}
```

### Поля ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ActionStatus | String | Результат запроса. `OK`: успешно. `FAIL`: ошибка |
| ErrorCode | Integer | Код ошибки |
| ErrorInfo | String | Информация об ошибке |

## Коды ошибок

Если не происходит сетевая ошибка (например, ошибка 502), HTTP-код возврата для этого API всегда равен 200. **`ErrorCode` и `ErrorInfo` в ответе представляют фактический код ошибки и информацию об ошибке.** Для общих кодов ошибок (60000–79999) см. раздел [Коды ошибок](https://intl.cloud.tencent.com/document/product/1047/34348).
В следующей таблице описаны коды ошибок, специфичные для этого API:

| Код ошибки | Описание |
| --- | --- |
| 90001 | Ошибка при разборе формата JSON. Проверьте, соответствует ли запрос JSON спецификациям JSON. |
| 90009 | Запрос требует разрешения администратора приложения. |
| 90018 | Количество запрошенных учетных записей превышает лимит. |
| 90033 | Недействительный атрибут. |
| 91000 | Внутренняя ошибка сервиса. Повторите попытку. |

## Инструмент отладки API

Используйте [инструмент онлайн-отладки RESTful API](https://tcc.tencentcs.com/im-api-tool/index.html#/v4/all_member_push/im_set_attr) для отладки этого API.

## Справочная информация

- [API для отправки всем пользователям](https://intl.cloud.tencent.com/document/product/1047/37165)
- [Отправка всем пользователям](https://intl.cloud.tencent.com/document/product/1047/37166)
- [Установка имен атрибутов приложения](https://intl.cloud.tencent.com/document/product/1047/37167)
- [Получение имен атрибутов приложения](https://intl.cloud.tencent.com/document/product/1047/37168)
- [Удаление атрибутов пользователя](https://intl.cloud.tencent.com/document/product/1047/37171)
- [Получение атрибутов пользователя](https://intl.cloud.tencent.com/document/product/1047/37169)
- [Добавление тегов пользователя](https://intl.cloud.tencent.com/document/product/1047/37173)
- [Получение тегов пользователя](https://intl.cloud.tencent.com/document/product/1047/37172)
- [Удаление тегов пользователя](https://intl.cloud.tencent.com/document/product/1047/37174)
- [Удаление всех тегов пользователя](https://intl.cloud.tencent.com/document/product/1047/37175)


---
*Источник: [https://trtc.io/document/37170](https://trtc.io/document/37170)*

---
*Источник (EN): [setting-user-attributes.md](./setting-user-attributes.md)*
