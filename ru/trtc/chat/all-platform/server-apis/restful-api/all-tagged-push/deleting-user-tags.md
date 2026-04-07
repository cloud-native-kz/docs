# Удаление тегов пользователя

## Обзор функции

Администратор удаляет тег у пользователя. Обратите внимание, что вы можете удалить тег только для 100 пользователей одновременно.

### Пример URL запроса

```
https://xxxxxx/v4/timpush/remove_tag?usersig=xxx&identifier=admin&sdkappid=88888888&random=99999999&contenttype=json
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса: HTTPSМетод запроса: POST |
| xxxxxx | Выделенный домен, соответствующий стране/региону вашего SDKAppID.Китай: `console.tim.qq.com`Сингапур: `adminapisgp.im.qcloud.com`Сеул: `adminapikr.im.qcloud.com`Токио: `adminapijpn.im.qcloud.com`Франкфурт: `adminapiger.im.qcloud.com`Кремниевая долина: `adminapiusa.im.qcloud.com`Джакарта: `adminapiidn.im.qcloud.com` |
| v4/timpush/remove_tag | API запроса. |
| usersig | Подпись, созданная учетной записью администратора приложения, см. [UserSig Background API](https://www.tencentcloud.com/document/product/1047/34385). |
| identifier | Должен быть учетная запись администратора приложения. Дополнительные сведения см. в разделе [Администраторы приложений](https://www.tencentcloud.com/document/product/1047/33517#app-admin). |
| sdkappid | SdkAppid, назначенный консолью обмена сообщениями при создании приложения. |
| random | Случайное 32-битное целое число без знака в диапазоне от 0 до 4294967295. |
| contenttype | Фиксированное значение: `json` |

### Ограничение частоты вызовов

100 раз в секунду.

### Пример пакета запроса

```
{    "UserTags": [        {            "To_Account": "xiaoming",            "Tags": ["GoldMember", "WeekPassUser"]        },        {            "To_Account": "xiaohong",            "Tags": ["Platinum Member", "MonthPassUser"]        }    ]}
```

### Поля пакета запроса

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| To_Account | String | Обязательное | Целевая учетная запись пользователя. |
| Tags | Array | Обязательное | Массив тегов: каждый тег должен быть типа string, а максимальная длина одного тега не должна превышать 50 байт. |

### Пример пакета ответа

Все успешно:

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0}
```

Частичный успех:

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0,    "ErrorList": [        {            "ErrorCode": 70107,            "To_Account": "xiaohong"        }    ]}
```

### Описание полей пакета ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ActionStatus | String | Результат обработки запроса:OK: указывает на успешную обработку.FAIL: указывает на сбой. |
| ErrorCode | Integer | Код ошибки. |
| ErrorInfo | String | Сообщение об ошибке. |
| ErrorList | Object Array | Установка атрибутов может быть частично успешной для некоторых пользователей и частично неудачной для других. Список сообщений об ошибках для учетных записей, которые не удались. |

Описание полей объекта JSON в массиве ErrorList

| Поле | Тип | Описание |
| --- | --- | --- |
| To_Account | String | Целевая учетная запись пользователя. |
| ErrorCode | Integer | Код ошибки. |
| ErrorInfo | String | Описание ошибки, может быть пусто. |

## Коды ошибок

Если не возникает сетевая ошибка (например, ошибка 502), код возврата HTTP этого интерфейса всегда равен 200.**Фактический код ошибки и сообщение об ошибке указаны в ErrorCode и ErrorInfo в полезной нагрузке ответа.**. Для общих кодов ошибок (60000–79999) см. документацию [Коды ошибок](https://intl.cloud.tencent.com/document/product/1047/34348).
Приватные коды ошибок для этого API приведены ниже:

| Код ошибки | Описание |
| --- | --- |
| 90001 | Ошибка анализа формата JSON. Убедитесь, что пакет запроса соответствует спецификации JSON. |
| 90009 | Запрос требует разрешений администратора приложения. |
| 90018 | Количество запрошенных учетных записей превышает ограничение. |
| 91000 | Внутренняя ошибка сервиса, пожалуйста, повторите попытку. |

## Инструмент отладки API

Используйте инструмент [RESTful API Online Test](https://tcc.tencentcs.com/im-api-tool/index.html#/v4/timpush/remove_tag) для отладки этого интерфейса.

## Справочные материалы

- [Всем пользователям/Push по тегам](https://www.tencentcloud.com/document/product/1047/67814)
- [Установить имя атрибута приложения](https://www.tencentcloud.com/document/product/1047/67816)
- [Получить имя атрибута приложения](https://www.tencentcloud.com/document/product/1047/67815)
- [Установить атрибуты пользователя](https://www.tencentcloud.com/document/product/1047/67818)
- [Удалить атрибуты пользователя](https://www.tencentcloud.com/document/product/1047/67819)
- [Получить атрибуты пользователя](https://www.tencentcloud.com/document/product/1047/67817)
- [Добавить теги пользователя](https://www.tencentcloud.com/document/product/1047/67821)
- [Получить теги пользователя](https://www.tencentcloud.com/document/product/1047/67820)
- [Удалить теги пользователя](https://www.tencentcloud.com/document/product/1047/67822)
- [Очистить теги пользователя](https://www.tencentcloud.com/document/product/1047/67823)
- [Push отзыв](https://www.tencentcloud.com/document/product/1047/67824)


---
*Источник: [https://trtc.io/document/67822](https://trtc.io/document/67822)*

---
*Источник (EN): [deleting-user-tags.md](./deleting-user-tags.md)*
