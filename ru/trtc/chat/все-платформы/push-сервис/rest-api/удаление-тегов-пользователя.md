# Удаление тегов пользователя

## Обзор функции

Администратор удаляет тег у пользователя. Обратите внимание, что вы можете удалить тег одновременно не более чем для 100 пользователей.

### Пример URL запроса

```
https://xxxxxx/v4/timpush/remove_tag?usersig=xxx&identifier=admin&sdkappid=88888888&random=99999999&contenttype=json
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса: HTTPSМетод запроса: POST |
| xxxxxx | Выделенный домен, соответствующий стране/региону вашего SDKAppID.Китай: `console.tim.qq.com`Сингапур: `adminapisgp.im.qcloud.com`Сеул: `adminapikr.im.qcloud.com`Франкфурт: `adminapiger.im.qcloud.com`Кремниевая долина: `adminapiusa.im.qcloud.com`Джакарта: `adminapiidn.im.qcloud.com` |
| v4/timpush/remove_tag | API запроса |
| usersig | Подпись, сгенерированная аккаунтом администратора приложения, см. [UserSig Background API](https://www.tencentcloud.com/document/product/1047/34385) |
| identifier | Должен быть аккаунт администратора приложения. Подробнее см. [App Admins](https://www.tencentcloud.com/document/product/1047/33517) |
| sdkappid | SdkAppid, назначенный консолью обмена мгновенными сообщениями при создании приложения |
| random | Случайное 32-битное целое число без знака в диапазоне от 0 до 4294967295 |
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
| To_Account | String | Обязательное | Целевой аккаунт пользователя, поддерживает UserID или RegistrationID. |
| Tags | Array | Обязательное | Массив тегов: каждый тег должен быть строкового типа, максимальная длина одного тега не должна превышать 50 байт |

### Пример пакета ответа

успешно:

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
| ActionStatus | String | Результат обработки запроса:OK: указывает на успешную обработкуFAIL: указывает на ошибку |
| ErrorCode | Integer | Код ошибки |
| ErrorInfo | String | Сообщение об ошибке |
| ErrorList | Object Array | Набор атрибутов может быть частично успешным для некоторых пользователей и частично ошибочным для других. Список сообщений об ошибках для ошибочных аккаунтов. |

Описание полей объекта JSON в массиве ErrorList

| Поле | Тип | Описание |
| --- | --- | --- |
| To_Account | String | Целевой аккаунт пользователя: UserID или RegistrationID. |
| ErrorCode | Integer | Код ошибки. |
| ErrorInfo | String | Описание ошибки, может быть пустым. |

## Коды ошибок

Если не происходит сетевая ошибка (например, ошибка 502), HTTP код возврата этого интерфейса всегда составляет 200. **Фактический код ошибки и сообщение об ошибке указаны в ErrorCode и ErrorInfo в полезной нагрузке ответа.**. Для общих кодов ошибок (60000–79999) см. документацию [Error Codes](https://intl.cloud.tencent.com/document/product/1047/34348).
Приватные коды ошибок для этого API следующие:

| Код ошибки | Описание |
| --- | --- |
| 90001 | Ошибка при разборе формата JSON. Убедитесь, что пакет запроса соответствует спецификации JSON. |
| 90009 | Запрос требует разрешений администратора приложения. |
| 90018 | Количество запрашиваемых аккаунтов превышает лимит. |
| 91000 | Внутренняя ошибка сервиса, пожалуйста, попробуйте еще раз. |

## Инструмент отладки API

Используйте инструмент [RESTful API Online Test](https://tcc.tencentcs.com/im-api-tool/index.html#/v4/timpush/remove_tag) для отладки этого интерфейса.

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
*Источник: [https://trtc.io/document/60569](https://trtc.io/document/60569)*

---
*Источник (EN): [deleting-user-tags.md](./deleting-user-tags.md)*
