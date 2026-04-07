# Получение имен атрибутов приложения

## Обзор функции

Этот API используется администратором для получения имен атрибутов приложения. Перед вызовом этого API необходимо [установить имена атрибутов приложения](https://intl.cloud.tencent.com/document/product/1047/37167).

## Описание вызова API

Отправка всем пользователям доступна только в редакциях Pro, Pro Plus и Enterprise. Чтобы использовать эту функцию, необходимо [приобрести редакцию Pro, Pro Plus или Enterprise](https://www.tencentcloud.com/document/product/1047/34577), перейти в [консоль](https://console.trtc.io/chat), выбрать **Конфигурация функций** > **Вход и сообщения** > **Отправка всем пользователям** и включить функцию.

### Пример URL запроса

```
https://xxxxxx/v4/all_member_push/im_get_attr_name?usersig=xxx&identifier=admin&sdkappid=88888888&random=99999999&contenttype=json
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса — HTTPS, метод запроса — POST. |
| xxxxxx | Доменное имя, соответствующее стране/региону, в котором находится ваш SDKAppID.Китай: `console.tim.qq.com`Сингапур: `adminapisgp.im.qcloud.com`Сеул: `adminapikr.im.qcloud.com`Токио: `adminapijpn.im.qcloud.com`Франкфурт: `adminapiger.im.qcloud.com`Кремниевая долина: `adminapiusa.im.qcloud.com`Джакарта: `adminapiidn.im.qcloud.com` |
| v4/all_member_push/im_get_attr_name | API запроса |
| usersig | Подпись, созданная в учетной записи администратора приложения. Дополнительную информацию см. в разделе [Создание UserSig](https://intl.cloud.tencent.com/document/product/1047/34385). |
| identifier | Учетная запись администратора приложения. |
| sdkappid | `SDKAppID`, назначенный консолью Chat при создании приложения |
| random | Случайное 32-битное целое число без знака |
| contenttype | Значение всегда `json`. |

### Максимальная частота вызовов

100 раз/сек

### Пример запроса

```
{}
```

### Поля запроса

Нет.

### Пример ответа

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0,    "AttrNames": {        "0": "sex",        "1": "city",        "2": "Membership level"    }}
```

### Поля ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ActionStatus | String | Результат запроса. `OK`: успешно. `FAIL`: ошибка |
| ErrorCode | Integer | Код ошибки |
| ErrorInfo | String | Информация об ошибке |
| AttrNames | Object | Серия пар "ключ:значение". Каждая пара "ключ:значение" указывает имя соответствующего атрибута. Например, "0":"xxx" указывает, что имя атрибута 0 — это xxx. |

## Коды ошибок

Если не возникнет ошибка сети (например, ошибка 502), код возврата HTTP для этого API всегда равен 200. `ErrorCode`**и**`ErrorInfo`**в ответе представляют фактический код ошибки и информацию об ошибке.** Для публичных кодов ошибок (60000–79999) см. [Коды ошибок](https://intl.cloud.tencent.com/document/product/1047/34348).
В таблице ниже описаны коды ошибок, характерные для этого API:

| Код ошибки | Описание |
| --- | --- |
| 90001 | Ошибка парсинга формата JSON. Проверьте, соответствует ли JSON-запрос спецификациям JSON. |
| 90009 | Запрос требует разрешений администратора приложения. |
| 90018 | Количество запрошенных учетных записей превышает лимит. |
| 91000 | Ошибка внутреннего сервиса. Повторите попытку. |

## Инструмент отладки API

Используйте [инструмент онлайн-отладки RESTful API](https://tcc.tencentcs.com/im-api-tool/index.html#/v4/all_member_push/im_get_attr_name) для отладки этого API.

## Ссылки

- [API для отправки всем пользователям](https://intl.cloud.tencent.com/document/product/1047/37165)
- [Отправка всем пользователям](https://intl.cloud.tencent.com/document/product/1047/37166)
- [Установка имен атрибутов приложения](https://intl.cloud.tencent.com/document/product/1047/37167)
- [Установка атрибутов пользователя](https://intl.cloud.tencent.com/document/product/1047/37170)
- [Удаление атрибутов пользователя](https://intl.cloud.tencent.com/document/product/1047/37171)
- [Получение атрибутов пользователя](https://intl.cloud.tencent.com/document/product/1047/37169)
- [Добавление тегов пользователя](https://intl.cloud.tencent.com/document/product/1047/37173)
- [Получение тегов пользователя](https://intl.cloud.tencent.com/document/product/1047/37172)
- [Удаление тегов пользователя](https://intl.cloud.tencent.com/document/product/1047/37174)
- [Удаление всех тегов пользователя](https://intl.cloud.tencent.com/document/product/1047/37175)


---
*Источник: [https://trtc.io/document/37168](https://trtc.io/document/37168)*

---
*Источник (EN): [getting-application-attribute-names.md](./getting-application-attribute-names.md)*
