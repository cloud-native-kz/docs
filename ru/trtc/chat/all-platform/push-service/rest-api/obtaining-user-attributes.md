# Получение атрибутов пользователя

## Обзор функции

Получение атрибутов пользователя (должно быть вызвано с учетной записью администратора). Вы можете одновременно получить атрибуты до 100 пользователей. Перед использованием сначала [установите имена атрибутов приложения](https://www.tencentcloud.com/document/product/1047/60563), затем [установите атрибуты пользователя](https://www.tencentcloud.com/document/product/1047/60565).

### Пример URL запроса

```
https://xxxxxx/v4/timpush/get_attr?usersig=xxx&identifier=admin&sdkappid=88888888&random=99999999&contenttype=json
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса: HTTPSМетод запроса: POST |
| xxxxxx | Выделенный домен, соответствующий стране/региону вашего SDKAppID.Китай: `console.tim.qq.com`Сингапур: `adminapisgp.im.qcloud.com`Сеул: `adminapikr.im.qcloud.com`Франкфурт: `adminapiger.im.qcloud.com`Кремниевая долина: `adminapiusa.im.qcloud.com`Джакарта: `adminapiidn.im.qcloud.com` |
| v4/timpush/get_attr | API запроса |
| usersig | Подпись, сгенерированная учетной записью администратора приложения. Дополнительные сведения см. в разделе [Генерирование UserSig](https://www.tencentcloud.com/document/product/1047/34385) |
| identifier | Должна быть учетная запись администратора приложения. Дополнительные сведения см. в разделе [Администраторы приложения](https://www.tencentcloud.com/document/product/1047/33517) |
| sdkappid | SdkAppid, назначенный консолью обмена сообщениями при создании приложения |
| random | Случайное 32-битное целое число без знака в диапазоне от 0 до 4294967295 |
| contenttype | Фиксированное значение: `json` |

### Лимит частоты вызовов

100 раз в секунду.

### Пример пакетов запроса

```
{    "To_Account": [        "Mary",        "xiaoming",        "xiaohua"    ]}
```

### Поля пакета запроса

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| To_Account | Array | Обязательно | Список целевых учетных записей пользователя, поддерживает UserID или RegistrationID. |

### Пример пакетов ответа

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0,    "UserAttrs": [        {            "To_Account": "xiaoming",            "Attrs": {                "sex": "male",                "city": "ShenZhen"            }        },        {            "To_Account": "xiaohua",            "Attrs": {}        }    ],     "ErrorList": [        {            "ErrorCode": 70107, // account does not exist            "To_Account": "Mary"        }    ]}
```

### Описание поля пакета ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ActionStatus | String | Результат обработанного запроса:OK: указывает на успешную обработкуFAIL: указывает на ошибку |
| ErrorCode | Integer | Код ошибки |
| ErrorInfo | String | Сообщение об ошибке |
| UserAttrs | Object Array | Список содержимого тегов пользователя |
| ErrorList | Object Array | Установка атрибутов. Некоторые пользователи могут добиться успеха, в то время как другие могут потерпеть неудачу. Список сообщений об ошибках для неудавшихся учетных записей. |

Описание поля объекта json в массиве UserAttrs

| Поле | Тип | Описание |
| --- | --- | --- |
| To_Account | String | Целевая учетная запись пользователя: UserID или RegistrationID. |
| Attrs | Object | Содержимое атрибута. Каждый атрибут представляет собой пару ключ-значение, где ключ является именем атрибута, а значение — значением атрибута для этого пользователя. значение пользовательского атрибута не должно превышать 50 байт. |

Описание поля объекта json в массиве ErrorList

| Поле | Тип | Описание |
| --- | --- | --- |
| To_Account | String | Целевая учетная запись пользователя |
| ErrorCode | Integer | Код ошибки |
| ErrorInfo | String | Описание ошибки, которое может быть пустым. |

## Коды ошибок

Если не происходит сетевая ошибка (например, ошибка 502), код состояния HTTP для этого интерфейса всегда будет 200. **Реальные коды ошибок и сообщения указаны в теле ответа параметрами ErrorCode и ErrorInfo**. Для распространенных кодов ошибок (60000–79999) см. документ [Код ошибки](https://www.tencentcloud.com/document/product/1047/34348).

Приватные коды ошибок для этого API выглядят следующим образом:

| Код ошибки | Описание |
| --- | --- |
| 90001 | Не удалось разобрать формат JSON. Пожалуйста, убедитесь, что пакет запроса соответствует спецификации JSON. |
| 90018 | Количество запрашиваемых учетных записей превышает лимит. |
| 91000 | Ошибка внутреннего сервиса, пожалуйста, попробуйте еще раз. |

## Инструмент отладки API

Используйте инструмент [Онлайн-тест RESTful API](https://tcc.tencentcs.com/im-api-tool/index.html#/v4/timpush/get_attr) для отладки этого интерфейса.

## Ссылки

- [Push для всех пользователей/тег](https://www.tencentcloud.com/document/product/1047/60561)
- [Одиночная отправка с userID](https://www.tencentcloud.com/document/product/1047/67553)
- [Получение имен атрибутов приложения](https://www.tencentcloud.com/document/product/1047/60562)
- [Установка имен атрибутов приложения](https://www.tencentcloud.com/document/product/1047/60563)
- [Получение атрибутов пользователя](https://www.tencentcloud.com/document/product/1047/60564)
- [Установка атрибутов пользователя](https://www.tencentcloud.com/document/product/1047/60565)
- [Удаление атрибутов пользователя](https://www.tencentcloud.com/document/product/1047/60566)
- [Получение тегов пользователя](https://www.tencentcloud.com/document/product/1047/60567)
- [Добавление тегов пользователя](https://www.tencentcloud.com/document/product/1047/60568)
- [Удаление тегов пользователя](https://www.tencentcloud.com/document/product/1047/60569)
- [Очистка тегов пользователя](https://www.tencentcloud.com/document/product/1047/60570)
- [Отзыв Push](https://www.tencentcloud.com/document/product/1047/60571)


---
*Источник: [https://trtc.io/document/60564](https://trtc.io/document/60564)*

---
*Источник (EN): [obtaining-user-attributes.md](./obtaining-user-attributes.md)*
