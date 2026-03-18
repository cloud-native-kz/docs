# Получение атрибутов пользователя

## Обзор функции

Получение атрибутов пользователя (должно вызываться с учётной записью администратора). Вы можете получить атрибуты до 100 пользователей одновременно. Перед использованием сначала [установите имена атрибутов приложения](https://www.tencentcloud.com/document/product/1047/67816), а затем [установите атрибуты пользователя](https://www.tencentcloud.com/document/product/1047/67818).

### Пример URL запроса

```
https://xxxxxx/v4/timpush/get_attr?usersig=xxx&identifier=admin&sdkappid=88888888&random=99999999&contenttype=json
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса: HTTPS. Метод запроса: POST. |
| xxxxxx | Выделенный домен, соответствующий стране/региону вашего SDKAppID. Китай: `console.tim.qq.com` Сингапур: `adminapisgp.im.qcloud.com` Сеул: `adminapikr.im.qcloud.com` Токио: `adminapijpn.im.qcloud.com` Франкфурт: `adminapiger.im.qcloud.com` Кремниевая долина: `adminapiusa.im.qcloud.com` Джакарта: `adminapiidn.im.qcloud.com` |
| v4/timpush/get_attr | API запроса. |
| usersig | Подпись, созданная учётной записью администратора приложения. Подробнее см. [Генерирование UserSig](https://www.tencentcloud.com/document/product/1047/34385). |
| identifier | Вы должны быть учётной записью администратора приложения. Дополнительные сведения см. в разделе [Администраторы приложения](https://www.tencentcloud.com/document/product/1047/33517#app-admin). |
| sdkappid | Идентификатор SdkAppid, назначенный консолью обмена мгновенными сообщениями при создании приложения. |
| random | Случайное 32-битное целое число без знака в диапазоне от 0 до 4294967295. |
| contenttype | Фиксированное значение: `json` |

### Ограничение частоты вызовов

100 раз в секунду.

### Пример пакетов запроса

```
{    "To_Account": [        "Mary",        "xiaoming",        "xiaohua"    ]}
```

### Поля пакета запроса

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| To_Account | Array | Обязательно | Список целевых учётных записей пользователя |

### Пример пакетов ответа

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0,    "UserAttrs": [        {            "To_Account": "xiaoming",            "Attrs": {                "sex": "male",                "city": "ShenZhen"            }        },        {            "To_Account": "xiaohua",            "Attrs": {}        }    ],     "ErrorList": [        {            "ErrorCode": 70107, // account does not exist            "To_Account": "Mary"        }    ]}
```

### Описание полей пакета ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ActionStatus | String | Результат обработки запроса: OK: указывает на успешную обработку. FAIL: указывает на ошибку. |
| ErrorCode | Integer | Код ошибки. |
| ErrorInfo | String | Сообщение об ошибке. |
| UserAttrs | Object Array | Список содержимого атрибутов пользователя. |
| ErrorList | Object Array | Установка атрибутов. Некоторые пользователи могут успешно завершиться, а другие могут потерпеть неудачу. Список сообщений об ошибках для учётных записей, в которых произошли сбои. |

Описание полей объекта JSON в массиве UserAttrs

| Поле | Тип | Описание |
| --- | --- | --- |
| To_Account | String | Учётная запись пользователя. |
| Attrs | Object | Содержимое атрибута. Каждый атрибут — это пара "ключ-значение", где ключ — это имя атрибута, а значение — это значение атрибута для этого пользователя. значение атрибута пользователя не должно превышать 50 байт. |

Описание полей объекта JSON в массиве ErrorList

| Поле | Тип | Описание |
| --- | --- | --- |
| To_Account | String | Целевая учётная запись пользователя. |
| ErrorCode | Integer | Код ошибки. |
| ErrorInfo | String | Описание ошибки, может быть пустым. |

## Коды ошибок

Если не возникает сетевая ошибка (например, ошибка 502), код состояния HTTP для этого интерфейса всегда будет 200. **Реальные коды ошибок и сообщения указаны в теле ответа с помощью ErrorCode и ErrorInfo**. Для общих кодов ошибок (60000–79999) см. документ [Код ошибки](https://www.tencentcloud.com/document/product/1047/34348).

Частные коды ошибок для этого API приведены ниже:

| Код ошибки | Описание |
| --- | --- |
| 90001 | Ошибка при анализе формата JSON. Убедитесь, что пакет запроса соответствует спецификации JSON. |
| 90018 | Количество запрашиваемых учётных записей превышает лимит. |
| 91000 | Внутренняя ошибка сервиса, попробуйте ещё раз. |

## Инструмент отладки API

Используйте [инструмент онлайн-тестирования RESTful API](https://tcc.tencentcs.com/im-api-tool/index.html#/v4/timpush/get_attr) для отладки этого интерфейса.

## Ссылки

- [Массовая рассылка/рассылка по тегам](https://www.tencentcloud.com/document/product/1047/67814)
- [Установка имени атрибута приложения](https://www.tencentcloud.com/document/product/1047/67816)
- [Получение имени атрибута приложения](https://www.tencentcloud.com/document/product/1047/67815)
- [Установка атрибутов пользователя](https://www.tencentcloud.com/document/product/1047/67818)
- [Удаление атрибутов пользователя](https://www.tencentcloud.com/document/product/1047/67819)
- [Получение атрибутов пользователя](https://www.tencentcloud.com/document/product/1047/67817)
- [Добавление тегов пользователя](https://www.tencentcloud.com/document/product/1047/67821)
- [Получение тегов пользователя](https://www.tencentcloud.com/document/product/1047/67820)
- [Удаление тегов пользователя](https://www.tencentcloud.com/document/product/1047/67822)
- [Очистка тегов пользователя](https://www.tencentcloud.com/document/product/1047/67823)
- [Отзыв рассылки](https://www.tencentcloud.com/document/product/1047/67824)


---
*Источник: [https://trtc.io/document/67817](https://trtc.io/document/67817)*

---
*Источник (EN): [obtaining-user-attributes.md](./obtaining-user-attributes.md)*
