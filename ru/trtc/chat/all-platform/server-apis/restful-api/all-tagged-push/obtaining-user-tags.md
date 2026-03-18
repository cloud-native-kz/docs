# Получение тегов пользователя

## Обзор функции

Получение тегов пользователя (должно быть вызвано с учётной записью администратора). Вы можете получать теги только для максимум 100 пользователей одновременно.

### Пример URL запроса

```
https://xxxxxx/v4/timpush/get_tag?usersig=xxx&identifier=admin&sdkappid=88888888&random=99999999&contenttype=json
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса: HTTPSМетод запроса: POST |
| xxxxxx | Выделенный домен, соответствующий стране/региону вашего SDKAppID.Китай: `console.tim.qq.com`Сингапур :`adminapisgp.im.qcloud.com`Сеул : `adminapikr.im.qcloud.com`Токио :`adminapijpn.im.qcloud.com`Франкфурт :`adminapiger.im.qcloud.com`Кремниевая долина :`adminapiusa.im.qcloud.com`Джакарта:` adminapiidn.im.qcloud.com` |
| v4/timpush/get_tag | API запроса. |
| usersig | Подпись, созданная администратором приложения. Для получения дополнительной информации см. [Генерирование UserSig](https://www.tencentcloud.com/document/product/1047/34385). |
| identifier | Вы должны быть администратором приложения. Для получения дополнительной информации см. [Администраторы приложения](https://www.tencentcloud.com/document/product/1047/33517#app-admin). |
| sdkappid | SdkAppid, назначенный консолью обмена мгновенными сообщениями при создании приложения. |
| random | Случайное 32-битное целое число без знака, находящееся в диапазоне от 0 до 4294967295. |
| contenttype | Фиксированное значение: `json` |

### Ограничение частоты вызовов

100 раз в секунду.

### Пример пакета запроса

```
{    "To_Account": [        "xiaoming",        "xiaohong",        "Mary"    ]}
```

### Поля пакета запроса

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| To_Account | Array | Обязательно | Список учётных записей целевых пользователей. |

### Пример пакета ответа

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0,    "UserTags": [        {            "To_Account": "xiaoming",            "Tags": ["GoldMember", "WeekPassUser"]        },        {            "To_Account": "xiaohong",            "Tags": ["PlatinumMember", "MonthPassUser"]        }    ],    "ErrorList": [        {            "ErrorCode": 70107,            "To_Account": "Mary"        }    ]}
```

### Описание полей пакета ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ActionStatus | String | Результат обработки запроса:OK: Указывает на успешную обработку.FAIL: Указывает на ошибку. |
| ErrorCode | Integer | Код ошибки. |
| ErrorInfo | String | Сообщение об ошибке. |
| UserTags | Object Array | Список содержимого тегов пользователя. |
| ErrorList | Object Array | Набор атрибутов. Некоторые пользователи могут пройти успешно, в то время как другие могут не пройти. Список сообщений об ошибке для неудачных учётных записей. |

Описание полей объекта JSON в массиве UserTags

| Поле | Тип | Описание |
| --- | --- | --- |
| To_Account | String | Учётная запись пользователя. |
| Tags | Array | Массив тегов. Максимальная длина отдельного тега не должна превышать 50 байт. Каждый тег — это строковый тип. |

Описание полей объекта JSON в массиве ErrorList

| Поле | Тип | Описание |
| --- | --- | --- |
| To_Account | String | Учётная запись целевого пользователя. |
| ErrorCode | Integer | Код ошибки. |
| ErrorInfo | String | Описание ошибки, которое может быть пустым. |

## Коды ошибок

Если не происходит ошибка сети (например, ошибка 502), HTTP код возврата этого интерфейса всегда равен 200.**Фактический код ошибки и сообщение об ошибке указаны ErrorCode и ErrorInfo в полезной нагрузке ответа.**. Для общих кодов ошибок (60000–79999) см. документацию [Коды ошибок](https://intl.cloud.tencent.com/document/product/1047/34348).
Приватные коды ошибок для этого API приведены ниже:

| Код ошибки | Описание |
| --- | --- |
| 90001 | Ошибка при разборе формата JSON. Пожалуйста, убедитесь, что пакет запроса соответствует спецификации JSON. |
| 90009 | Запрос требует разрешений администратора приложения. |
| 90018 | Количество запрошенных учётных записей превышает лимит. |
| 91000 | Ошибка внутреннего сервиса, пожалуйста, попробуйте снова. |

## Инструмент отладки API

Используйте инструмент [RESTful API Online Test](https://tcc.tencentcs.com/im-api-tool/index.html#/v4/timpush/get_tag) для отладки этого интерфейса.

## Справочные материалы

- [Массовая рассылка по всем пользователям/тегам](https://www.tencentcloud.com/document/product/1047/67814)
- [Установка названия атрибута приложения](https://www.tencentcloud.com/document/product/1047/67816)
- [Получение названия атрибута приложения](https://www.tencentcloud.com/document/product/1047/67815)
- [Установка атрибутов пользователя](https://www.tencentcloud.com/document/product/1047/67818)
- [Удаление атрибутов пользователя](https://www.tencentcloud.com/document/product/1047/67819)
- [Получение атрибутов пользователя](https://www.tencentcloud.com/document/product/1047/67817)
- [Добавление тегов пользователя](https://www.tencentcloud.com/document/product/1047/67821)
- [Получение тегов пользователя](https://www.tencentcloud.com/document/product/1047/67820)
- [Удаление тегов пользователя](https://www.tencentcloud.com/document/product/1047/67822)
- [Очистка тегов пользователя](https://www.tencentcloud.com/document/product/1047/67823)
- [Отзыв рассылки](https://www.tencentcloud.com/document/product/1047/67824)


---
*Источник: [https://trtc.io/document/67820](https://trtc.io/document/67820)*

---
*Источник (EN): [obtaining-user-tags.md](./obtaining-user-tags.md)*
