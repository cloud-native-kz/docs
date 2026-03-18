# Удаление всех тегов пользователя

## Обзор функции

Администратор удаляет все теги для пользователя. Обратите внимание, что вы можете удалить все теги максимум для 100 пользователей одновременно.

### Пример URL запроса

```
https://xxxxxx/v4/timpush/clear_all_tags?usersig=xxx&identifier=admin&sdkappid=88888888&random=99999999&contenttype=json
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса: HTTPSМетод запроса: POST |
| xxxxxx | Выделенный домен, соответствующий стране/региону вашего SDKAppID.Китай: `console.tim.qq.com`Сингапур: `adminapisgp.im.qcloud.com`Сеул: `adminapikr.im.qcloud.com`Токио: `adminapijpn.im.qcloud.com`Франкфурт: `adminapiger.im.qcloud.com`Кремниевая долина: `adminapiusa.im.qcloud.com`Джакарта: `adminapiidn.im.qcloud.com` |
| v4/timpush/clear_all_tags | API запроса. |
| usersig | Подпись, созданная учетной записью администратора приложения. Подробнее см. [Генерация UserSig](https://www.tencentcloud.com/document/product/1047/34385). |
| identifier | Должна быть учетная запись администратора приложения. Подробнее см. [Администраторы приложения](https://www.tencentcloud.com/document/product/1047/33517#app-admin). |
| sdkappid | SdkAppid, назначенный консолью обмена сообщениями при создании приложения. |
| random | Случайное 32-битное беззнаковое целое число в диапазоне от 0 до 4294967295. |
| contenttype | Фиксированное значение: `json` |

### Ограничение частоты вызовов

100 раз в секунду.

### Пример пакета запроса

```
{    "To_Account": [        "xiaoming",        "xiaohong"    ]}
```

### Поля пакета запроса

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| To_Account | Array | Обязательно | Целевая учетная запись пользователя. |

### Примеры пакетов ответов

Все успешно:

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0}
```

Частично успешно:

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0,    "ErrorList": [        {            "ErrorCode": 70107,            "To_Account": "xiaohong"        }    ]}
```

### Описание полей пакета ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ActionStatus | String | Результат обработки запроса:OK: указывает на успешную обработку.FAIL: указывает на ошибку. |
| ErrorCode | Integer | Код ошибки. |
| ErrorInfo | String | Сообщение об ошибке. |
| ErrorList | Object Array | Установка атрибутов. Некоторые пользователи могут быть успешно обработаны, а другие — нет. Список сообщений об ошибках для неудачных учетных записей. |

Описание полей JSON объекта в массиве ErrorList

| Поле | Тип | Описание |
| --- | --- | --- |
| To_Account | String | Целевая учетная запись пользователя. |
| ErrorCode | Integer | Код ошибки. |
| ErrorInfo | String | Описание ошибки, может быть пустым. |

## Коды ошибок

Если не возникает ошибка сети (например, ошибка 502), код возврата HTTP этого интерфейса всегда равен 200. **Фактический код ошибки и сообщение об ошибке указаны в полях ErrorCode и ErrorInfo в полезной нагрузке ответа.** Для общих кодов ошибок (60000–79999) см. документацию [Коды ошибок](https://www.tencentcloud.com/document/product/1047/34348).
Приватные коды ошибок для этого API приведены ниже:

| Код ошибки | Описание |
| --- | --- |
| 90001 | Не удалось разобрать формат JSON. Убедитесь, что пакет запроса соответствует спецификации JSON. |
| 90009 | Запрос требует прав администратора приложения. |
| 90018 | Количество запрашиваемых учетных записей превышает лимит. |
| 91000 | Ошибка внутреннего сервиса, пожалуйста, попробуйте снова. |

## Инструмент отладки API

Используйте [онлайн-инструмент отладки RESTful API](https://tcc.tencentcs.com/im-api-tool/index.html#/v4/timpush/clear_all_tags) для отладки этого API.

## Справка

- [Push для всех пользователей/тегов](https://www.tencentcloud.com/document/product/1047/67814)
- [Установка имени атрибута приложения](https://www.tencentcloud.com/document/product/1047/67816)
- [Получение имени атрибута приложения](https://www.tencentcloud.com/document/product/1047/67815)
- [Установка атрибутов пользователя](https://www.tencentcloud.com/document/product/1047/67818)
- [Удаление атрибутов пользователя](https://www.tencentcloud.com/document/product/1047/67819)
- [Получение атрибутов пользователя](https://www.tencentcloud.com/document/product/1047/67817)
- [Добавление тегов пользователя](https://www.tencentcloud.com/document/product/1047/67821)
- [Получение тегов пользователя](https://www.tencentcloud.com/document/product/1047/67820)
- [Удаление тегов пользователя](https://www.tencentcloud.com/document/product/1047/67822)
- [Очистка тегов пользователя](https://www.tencentcloud.com/document/product/1047/67823)
- [Отзыв Push](https://www.tencentcloud.com/document/product/1047/67824)


---
*Источник: [https://trtc.io/document/67823](https://trtc.io/document/67823)*

---
*Источник (EN): [deleting-all-user-tags.md](./deleting-all-user-tags.md)*
