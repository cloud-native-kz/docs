# Добавление пользовательских тегов

## Обзор функции

Администратор добавляет теги для пользователей.

> **Примечание:** Каждый запрос может добавить теги для до 100 пользователей. Максимум 10 тегов может быть добавлено для одного пользователя в теле запроса. Один пользователь может установить до 100 тегов. Если количество тегов пользователя превышает 100, пожалуйста, удалите старые теги перед добавлением новых. Приложение может установить максимум 1000 тегов. Это дедублицированный итог для тегов всех пользователей. Максимальная длина одного тега составляет 50 байт.

### Примеры URL запроса

```
https://xxxxxx/v4/timpush/add_tag?usersig=xxx&identifier=admin&sdkappid=88888888&random=99999999&contenttype=json
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса: HTTPSМетод запроса: POST |
| xxxxxx | Выделенный домен, соответствующий стране/региону вашего SDKAppID.Китай: `console.tim.qq.com`Сингапур: `adminapisgp.im.qcloud.com`Сеул: `adminapikr.im.qcloud.com`Токио: `adminapijpn.im.qcloud.com`Франкфурт: `adminapiger.im.qcloud.com`Силиконовая долина: `adminapiusa.im.qcloud.com`Джакарта: `adminapiidn.im.qcloud.com` |
| v4/timpush/add_tag | API запроса. |
| usersig | Подпись, созданная учетной записью администратора приложения. Дополнительные сведения см. в разделе [Генерирование UserSig](https://www.tencentcloud.com/document/product/1047/34385). |
| identifier | Вы должны быть учетной записью администратора приложения. Дополнительные сведения см. в разделе [Администраторы приложения](https://www.tencentcloud.com/document/product/1047/33517#app-admin). |
| sdkappid | SdkAppid, назначенный консолью мгновенного обмена сообщениями при создании приложения. |
| random | Случайное 32-битное беззнаковое целое число в диапазоне от 0 до 4294967295. |
| contenttype | Фиксированное значение: `json` |

### Ограничение частоты вызовов

100 раз в секунду.

### Примеры пакетов запроса

```
{    "UserTags": [        {            "To_Account": "xiaoming",             "Tags": ["GoldMember", "WeekPassUser"]        },        {            "To_Account": "379C2F0D-290D-47AE-94D1-919058C39C77"  // Automatically generated RegistrationID when push service registration is successful            "Tags": ["PlatinumMember", "MonthPassUser"]        }    ]}
```

```
{    "Replace": 1, // Overwrite ALL tags of the current user    "UserTags": [        {            "To_Account": "xiaoming",             "Tags": ["GoldMember", "WeekPassUser"]        },        {            "To_Account": "379C2F0D-290D-47AE-94D1-919058C39C77", // Automatically generated RegistrationID when push service registration is successful            "Tags": ["PlatinumMember", "MonthPassUser"]        }    ]}
```

### Описание полей пакета запроса

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| Replace | Integer | Опционально | 0 означает добавить тег на основе существующих, 1 означает перезаписать ВСЕ теги текущего пользователя. Значение по умолчанию 0 |
| UserTags | Object Array | Обязательно | Информация о теге учетной записи. |

Описание полей объекта JSON в массиве UserTags

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| To_Account | String | Обязательно | Целевой аккаунт пользователя. |
| Tags | Array | Обязательно | Массив строк тегов, максимальная длина одного тега не должна превышать 50 байт.Максимальная длина массива составляет 10 при Replace=0Максимальная длина массива составляет 100 при Replace=1 |

### Примеры пакетов ответа

Все успешно:

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0}
```

Частично успешно:

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0,    "ErrorList": [        {            "ErrorCode": 90035, // A tag can only be applicable to one account type.            "To_Account": "379C2F0D-290D-47AE-94D1-919058C39C77"        }    ]}
```

### Описание полей пакета ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ActionStatus | String | Результат обработки запроса:OK: Указывает на успешную обработку.FAIL: Указывает на ошибку. |
| ErrorCode | Integer | Код ошибки. |
| ErrorInfo | String | Сообщение об ошибке. |
| ErrorList | Object Array | Установка атрибутов может привести к частичному успеху и частичной ошибке некоторых пользователей. Список сообщений об ошибках для не прошедших проверку учетных записей. |

Описание полей объекта JSON в массиве ErrorList

| Поле | Тип | Описание |
| --- | --- | --- |
| To_Account | String | Целевой аккаунт пользователя. |
| ErrorCode | Integer | Код ошибки. |
| ErrorInfo | String | Описание ошибки, может быть пустым. |

## Коды ошибок

Если не происходит ошибка сети (например, ошибка 502), код возврата HTTP этого интерфейса всегда равен 200. **Фактический код ошибки и сообщение об ошибке указаны в ErrorCode и ErrorInfo в полезной нагрузке ответа.** Для кодов ошибок общего назначения (60000–79999) см. документацию [Коды ошибок](https://intl.cloud.tencent.com/document/product/1047/34348).

Приватные коды ошибок для этого API:

| Код ошибки | Описание |
| --- | --- |
| 90001 | Ошибка разбора формата JSON. Пожалуйста, убедитесь, что пакет запроса соответствует спецификации JSON. |
| 90009 | Запрос требует прав администратора приложения. |
| 90018 | Количество запрашиваемых учетных записей превышает лимит. |
| 91000 | Внутренняя ошибка сервиса, пожалуйста, повторите попытку. |
| 90035 | Тег может применяться только к одному типу учетной записи. При успешной регистрации сервиса push автоматически генерируется RegistrationID для типа учетной записи IM. Дополнительные сведения см. в разделе [Введение в типовые сценарии push-уведомлений](https://www.tencentcloud.com/document/product/1047/69236). |

## Инструмент отладки API

Используйте инструмент [Онлайн-тест RESTful API](https://tcc.tencentcs.com/im-api-tool/index.html#/v4/timpush/add_tag) для отладки этого интерфейса.

## Ссылки

- [Push-уведомления для всех пользователей/по тегам](https://www.tencentcloud.com/document/product/1047/67814)
- [Установка названия атрибута приложения](https://www.tencentcloud.com/document/product/1047/67816)
- [Получение названия атрибута приложения](https://www.tencentcloud.com/document/product/1047/67815)
- [Установка атрибутов пользователя](https://www.tencentcloud.com/document/product/1047/67818)
- [Удаление атрибутов пользователя](https://www.tencentcloud.com/document/product/1047/67819)
- [Получение атрибутов пользователя](https://www.tencentcloud.com/document/product/1047/67817)
- [Добавление пользовательских тегов](https://www.tencentcloud.com/document/product/1047/67821)
- [Получение пользовательских тегов](https://www.tencentcloud.com/document/product/1047/67820)
- [Удаление пользовательских тегов](https://www.tencentcloud.com/document/product/1047/67822)
- [Очистка пользовательских тегов](https://www.tencentcloud.com/document/product/1047/67823)
- [Отзыв push-уведомления](https://www.tencentcloud.com/document/product/1047/67824)


---
*Источник: [https://trtc.io/document/67821](https://trtc.io/document/67821)*

---
*Источник (EN): [adding-user-tags.md](./adding-user-tags.md)*
