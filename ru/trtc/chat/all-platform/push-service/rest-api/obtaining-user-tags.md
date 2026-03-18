# Получение тегов пользователя

## Обзор функции

Получение тегов пользователя (должно выполняться с учетной записью администратора). Вы можете получить теги максимум для 100 пользователей одновременно.

### Пример URL запроса

```
https://xxxxxx/v4/timpush/get_tag?usersig=xxx&identifier=admin&sdkappid=88888888&random=99999999&contenttype=json
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса: HTTPSМетод запроса: POST |
| xxxxxx | Выделенный домен, соответствующий стране/региону вашего SDKAppID.Китай: `console.tim.qq.com`Сингапур: `adminapisgp.im.qcloud.com`Сеул: `adminapikr.im.qcloud.com`Франкфурт: `adminapiger.im.qcloud.com`Кремниевая долина: `adminapiusa.im.qcloud.com`Джакарта: `adminapiidn.im.qcloud.com` |
| v4/timpush/get_tag | API запроса |
| usersig | Подпись, созданная учетной записью администратора приложения. Дополнительные сведения см. в разделе [Создание UserSig](https://www.tencentcloud.com/document/product/1047/34385) |
| identifier |必须是应用管理员账号。有关详细信息，请参阅 [Администраторы приложения](https://www.tencentcloud.com/document/product/1047/33517) |
| sdkappid | Sdkappid, назначенный консолью обмена мгновенными сообщениями при создании приложения |
| random | Случайное 32-битное целое число без знака в диапазоне от 0 до 4294967295 |
| contenttype | Фиксированное значение: `json` |

### Ограничение частоты вызовов

100 раз в секунду.

### Примеры пакетов запросов

```
{    "To_Account": [        "xiaoming",        "xiaohong",        "Mary"    ]}
```

### Описание полей пакета запроса

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| To_Account | Array | Обязательное | Список целевых учетных записей пользователей, поддерживает UserID или RegistrationID. |

### Примеры пакетов ответов

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0,    "UserTags": [        {            "To_Account": "xiaoming",            "Tags": ["GoldMember", "WeekPassUser"]        },        {            "To_Account": "xiaohong",            "Tags": ["PlatinumMember", "MonthPassUser"]        }    ],    "ErrorList": [        {            "ErrorCode": 70107,            "To_Account": "Mary"        }    ]}
```

### Описание полей пакета ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ActionStatus | String | Результат обработанного запроса:OK: указывает на успешную обработкуFAIL: указывает на ошибку |
| ErrorCode | Integer | Код ошибки |
| ErrorInfo | String | Сообщение об ошибке |
| UserTags | Object Array | Список содержимого тегов пользователя |
| ErrorList | Object Array | Установить атрибуты. Некоторые пользователи могут добиться успеха, в то время как другие могут потерпеть неудачу. Список сообщений об ошибках для неудачных учетных записей. |

Описание полей объекта json в массиве UserTags

| Поле | Тип | Описание |
| --- | --- | --- |
| To_Account | String | Целевая учетная запись пользователя: UserID или RegistrationID. |
| Tags | Array | Массив тегов. Максимальная длина одного тега не должна превышать 50 байт. Каждый тег — это строковый тип. |

Описание полей объекта json в массиве ErrorList

| Поле | Тип | Описание |
| --- | --- | --- |
| To_Account | String | Целевая учетная запись пользователя: UserID или RegistrationID. |
| ErrorCode | Integer | Код ошибки |
| ErrorInfo | String | Описание ошибки, которое может быть пусто. |

## Коды ошибок

Если не возникает ошибка сети (например, ошибка 502), код возврата HTTP этого интерфейса всегда равен 200. **Фактический код ошибки и сообщение об ошибке указаны в ErrorCode и ErrorInfo в полезной нагрузке ответа.**. Для общих кодов ошибок (60000–79999) см. документацию [Коды ошибок](https://intl.cloud.tencent.com/document/product/1047/34348).
Приватные коды ошибок для этого API следующие:

| Код ошибки | Описание |
| --- | --- |
| 90001 | Не удалось разобрать формат JSON. Убедитесь, что пакет запроса соответствует спецификации JSON. |
| 90009 | Запрос требует разрешений администратора приложения. |
| 90018 | Количество запрошенных учетных записей превышает лимит. |
| 91000 | Внутренняя ошибка сервиса, пожалуйста, попробуйте еще раз. |

## Инструмент отладки API

Используйте инструмент [RESTful API Online Test](https://tcc.tencentcs.com/im-api-tool/index.html#/v4/timpush/get_tag) для отладки этого интерфейса.

## Ссылки

- [All-user/Tag Push](https://www.tencentcloud.com/document/product/1047/60561)
- [Single push with userID](https://www.tencentcloud.com/document/product/1047/67553)
- [Obtaining Application Attribute Names](https://www.tencentcloud.com/document/product/1047/60562)
- [Setting Application Attribute Names](https://www.tencentcloud.com/document/product/1047/60563)
- [Getting User Attributes](https://www.tencentcloud.com/document/product/1047/60564)
- [Setting User Attributes](https://www.tencentcloud.com/document/product/1047/60565)
- [Deleting User Attributes](https://www.tencentcloud.com/document/product/1047/60566)
- [Getting User Tags](https://www.tencentcloud.com/document/product/1047/60567)
- [Adding User Tags](https://www.tencentcloud.com/document/product/1047/60568)
- [Deleting User Tags](https://www.tencentcloud.com/document/product/1047/60569)
- [Clearing User Tags](https://www.tencentcloud.com/document/product/1047/60570)
- [Recall Push](https://www.tencentcloud.com/document/product/1047/60571)


---
*Источник: [https://trtc.io/document/60567](https://trtc.io/document/60567)*

---
*Источник (EN): [obtaining-user-tags.md](./obtaining-user-tags.md)*
