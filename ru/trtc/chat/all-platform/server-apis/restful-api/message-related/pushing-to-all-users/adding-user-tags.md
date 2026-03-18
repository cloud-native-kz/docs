# Добавление тегов пользователей

## Обзор функции

Этот API используется администратором для добавления тегов пользователям.

> **Примечание:** Каждый запрос может добавлять теги максимум для 100 пользователей. В теле запроса можно добавить максимум 10 тегов для каждого пользователя. Для каждого пользователя можно установить максимум 100 тегов. Если пользователь имеет более 100 тегов, необходимо удалить старые теги перед добавлением новых. Максимальная длина одного тега составляет 50 байт.

## Описание вызова API

Отправка всем пользователям доступна только в Pro edition, Pro Plus edition и Enterprise edition. Чтобы использовать эту функцию, необходимо [приобрести Pro edition, Pro Plus edition или Enterprise edition](https://www.tencentcloud.com/document/product/1047/34577), перейти в [консоль](https://console.trtc.io/chat), выбрать **Feature Configuration** > **Login and Message** > **Push to all users** и включить функцию.

### Пример URL запроса

```
https://xxxxxx/v4/all_member_push/im_add_tag?usersig=xxx&identifier=admin&sdkappid=88888888&random=99999999&contenttype=json
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса HTTPS, метод запроса POST. |
| xxxxxx | Доменное имя, соответствующее стране/региону, где находится ваш SDKAppID. Китай: `console.tim.qq.com` Сингапур: `adminapisgp.im.qcloud.com` Сеул: `adminapikr.im.qcloud.com` Токио: `adminapijpn.im.qcloud.com` Франкфурт: `adminapiger.im.qcloud.com` Кремниевая долина: `adminapiusa.im.qcloud.com` Джакарта: `adminapiidn.im.qcloud.com` |
| v4/all_member_push/im_add_tag | API запроса |
| usersig | Подпись, созданная в учетной записи администратора приложения. Дополнительную информацию см. в разделе [Создание UserSig](https://intl.cloud.tencent.com/document/product/1047/34385). |
| identifier | Учетная запись администратора приложения. |
| sdkappid | `SDKAppID`, назначенный консолью Chat при создании приложения |
| random | Случайное 32-битное целое число без знака |
| contenttype | Значение всегда `json`. |

### Максимальная частота вызовов

100 раз/сек

### Пример запроса

```
{    "UserTags": [        {            "To_Account": "xiaojun012",            "Tags": ["a", "b"]        },        {            "To_Account": "xiaojun013",            "Tags": ["a", "b"]        }    ]}
```

### Поля запроса

| Поле | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| To_Account | String | Да | Учетная запись целевого пользователя |
| Tags | Array | Да | Набор тегов |

### Пример ответа

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode":0}
```

### Поля ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ActionStatus | String | Результат запроса. `OK`: успешно; `FAIL`: ошибка |
| ErrorCode | Integer | Код ошибки |
| ErrorInfo | String | Информация об ошибке |

## Коды ошибок

Если не возникает сетевая ошибка (например, ошибка 502), код возврата HTTP для этого API всегда равен 200. `ErrorCode` **и** `ErrorInfo` **в ответе представляют фактический код ошибки и информацию об ошибке.** Для общих кодов ошибок (60000–79999) см. [Коды ошибок](https://intl.cloud.tencent.com/document/product/1047/34348).
В следующей таблице описаны коды ошибок, специфичные для этого API:

| Код ошибки | Описание |
| --- | --- |
| 90001 | Ошибка при разборе формата JSON. Проверьте соответствие JSON запроса спецификациям JSON. |
| 90009 | Запрос требует прав администратора приложения. |
| 90018 | Количество запрашиваемых учетных записей превышает лимит. |
| 91000 | Внутренняя ошибка службы. Попробуйте еще раз. |

## Инструмент отладки API

Используйте [онлайн инструмент отладки RESTful API](https://tcc.tencentcs.com/im-api-tool/index.html#/v4/all_member_push/im_add_tag) для отладки этого API.

## Справочные материалы

- [API для отправки всем пользователям](https://intl.cloud.tencent.com/document/product/1047/37165)
- [Отправка всем пользователям](https://intl.cloud.tencent.com/document/product/1047/37166)
- [Установка имен атрибутов приложения](https://intl.cloud.tencent.com/document/product/1047/37167)
- [Получение имен атрибутов приложения](https://intl.cloud.tencent.com/document/product/1047/37168)
- [Установка атрибутов пользователя](https://intl.cloud.tencent.com/document/product/1047/37170)
- [Удаление атрибутов пользователя](https://intl.cloud.tencent.com/document/product/1047/37171)
- [Получение атрибутов пользователя](https://intl.cloud.tencent.com/document/product/1047/37169)
- [Получение тегов пользователя](https://intl.cloud.tencent.com/document/product/1047/37172)
- [Удаление тегов пользователя](https://intl.cloud.tencent.com/document/product/1047/37174)
- [Удаление всех тегов пользователя](https://intl.cloud.tencent.com/document/product/1047/37175)


---
*Источник: [https://trtc.io/document/37173](https://trtc.io/document/37173)*

---
*Источник (EN): [adding-user-tags.md](./adding-user-tags.md)*
