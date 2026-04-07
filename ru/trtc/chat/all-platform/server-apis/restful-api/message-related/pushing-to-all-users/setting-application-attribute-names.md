# Установка имен атрибутов приложения

## Обзор функции

Вы можете установить максимум 10 пользовательских атрибутов пользователя для каждого приложения. Этот API используется для установки имени каждого атрибута. После установки имен атрибутов они могут использоваться для push-уведомлений по атрибутам пользователя и других целей.

## Описание вызова API

Отправка всем пользователям доступна только для Pro edition, Pro Plus edition и Enterprise edition. Для использования необходимо [приобрести Pro edition, Pro Plus edition или Enterprise edition](https://www.tencentcloud.com/document/product/1047/34577), перейти на [консоль](https://console.trtc.io/chat), выбрать **Конфигурация функций** > **Вход и сообщения** > **Отправка всем пользователям** и включить функцию.

### Пример URL запроса

```
https://xxxxxx/v4/all_member_push/im_set_attr_name?usersig=xxx&identifier=admin&sdkappid=88888888&random=99999999&contenttype=json
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса — HTTPS, метод запроса — POST. |
| xxxxxx | Доменное имя, соответствующее стране/региону, где находится ваш SDKAppID. Китай: `console.tim.qq.com` Сингапур: `adminapisgp.im.qcloud.com` Сеул: `adminapikr.im.qcloud.com` Токио: `adminapijpn.im.qcloud.com` Франкфурт: `adminapiger.im.qcloud.com` Кремниевая долина: `adminapiusa.im.qcloud.com` Джакарта: `adminapiidn.im.qcloud.com` |
| v4/all_member_push/im_set_attr_name | API запроса |
| usersig | Подпись, созданная в учетной записи администратора приложения. Для получения дополнительной информации см. [Генерирование UserSig](https://intl.cloud.tencent.com/document/product/1047/34385). |
| identifier | Учетная запись администратора приложения. |
| sdkappid | `SDKAppID`, назначенный консолью Chat при создании приложения |
| random | Случайное 32-битное беззнаковое целое число |
| contenttype | Значение всегда `json`. |

### Максимальная частота вызовов

100 раз/сек

### Пример запроса

Установите атрибут `0` приложения в `sex`, атрибут `1` в `city` и атрибут `2` в `country`.

```
{    "AttrNames": {        "0": "sex",        "1": "city",        "2": "country"    }}
```

### Поля запроса

| Поле | Тип | Обязательный параметр | Описание |
| --- | --- | --- | --- |
| Цифровой ключ | String | Да | Номер атрибута (от 0 до 9). |
| Имя атрибута | String | Да | Имя атрибута не может превышать лимит длины 50 байт. Приложение может иметь максимум 10 push-атрибутов (нумерованных от 0 до 9), и пользователи могут настраивать значение каждого атрибута. |

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

Если не возникает ошибка сети (например, ошибка 502), HTTP-код возврата для этого API всегда равен 200. `ErrorCode` **и** `ErrorInfo` **в ответе представляют фактический код ошибки и информацию об ошибке.** Для общих кодов ошибок (60000–79999) см. [Коды ошибок](https://intl.cloud.tencent.com/document/product/1047/34348).
В следующей таблице описаны коды ошибок, специфичные для этого API:

| Код ошибки | Описание |
| --- | --- |
| 90001 | Ошибка при анализе формата JSON. Проверьте, соответствует ли JSON запрос спецификациям JSON. |
| 90009 | Запрос требует разрешений администратора приложения. |
| 91000 | Ошибка внутреннего сервиса. Повторите попытку. |

## Инструмент отладки API

Используйте [онлайн инструмент отладки RESTful API](https://tcc.tencentcs.com/im-api-tool/index.html#/v4/all_member_push/im_set_attr_name) для отладки этого API.

## Ссылки

- [API для отправки всем пользователям](https://intl.cloud.tencent.com/document/product/1047/37165)
- [Отправка всем пользователям](https://intl.cloud.tencent.com/document/product/1047/37166)
- [Получение имен атрибутов приложения](https://intl.cloud.tencent.com/document/product/1047/37168)
- [Установка атрибутов пользователя](https://intl.cloud.tencent.com/document/product/1047/37170)
- [Удаление атрибутов пользователя](https://intl.cloud.tencent.com/document/product/1047/37171)
- [Получение атрибутов пользователя](https://intl.cloud.tencent.com/document/product/1047/37169)
- [Добавление тегов пользователя](https://intl.cloud.tencent.com/document/product/1047/37173)
- [Получение тегов пользователя](https://intl.cloud.tencent.com/document/product/1047/37172)
- [Удаление тегов пользователя](https://intl.cloud.tencent.com/document/product/1047/37174)
- [Удаление всех тегов пользователя](https://intl.cloud.tencent.com/document/product/1047/37175)


---
*Источник: [https://trtc.io/document/37167](https://trtc.io/document/37167)*

---
*Источник (EN): [setting-application-attribute-names.md](./setting-application-attribute-names.md)*
