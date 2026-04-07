# Удаление атрибутов пользователя

## Обзор функции

Администратор удаляет атрибуты у пользователей. Обратите внимание, что за один раз можно удалить атрибуты только для максимум 100 пользователей. Перед использованием, пожалуйста, [установите имена атрибутов приложения](https://www.tencentcloud.com/document/product/1047/60563).

### Пример URL запроса

```
https://xxxxxx/v4/timpush/remove_attr?usersig=xxx&identifier=admin&sdkappid=88888888&random=99999999&contenttype=json
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса: HTTPS. Метод запроса: POST |
| xxxxxx | Выделенный домен, соответствующий стране/региону вашего SDKAppID. Китай: `console.tim.qq.com`. Сингапур: `adminapisgp.im.qcloud.com`. Сеул: `adminapikr.im.qcloud.com`. Токио: `adminapijpn.im.qcloud.com`. Франкфурт: `adminapiger.im.qcloud.com`. Кремниевая долина: `adminapiusa.im.qcloud.com`. Джакарта: `adminapiidn.im.qcloud.com` |
| v4/timpush/remove_attr | API запроса. |
| usersig | Подпись, сгенерированная учётной записью администратора приложения. Подробнее см. [Генерирование UserSig](https://www.tencentcloud.com/document/product/1047/34385). |
| identifier | Должна быть учётная запись администратора приложения. Подробнее см. [Администраторы приложения](https://www.tencentcloud.com/document/product/1047/33517#app-admin). |
| sdkappid | SdkAppid, назначенный консолью мгновенного обмена сообщениями при создании приложения. |
| random | Случайное 32-битное беззнаковое целое число в диапазоне от 0 до 4294967295. |
| contenttype | Фиксированное значение: `json` |

### Ограничение частоты вызовов

100 раз в секунду.

### Пример пакета запроса

```
{    "UserAttrs": [        {            "To_Account": "Mary",            "Attrs": [                "sex",                "city"            ]        },        {            "To_Account": "xiaoming",            "Attrs": [                "sex",                "city"            ]        }    ]}
```

### Поля пакета запроса

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| UserAttrs | Array | Требуется | Массив атрибутов пользователя. Один атрибут пользователя состоит из To_Account и Attrs. |
| To_Account | String | Требуется | Учётная запись целевого пользователя. |
| Attrs | Array | Требуется | Набор имён атрибутов. Обратите внимание, что здесь требуются только имена атрибутов, не пары "ключ-значение". |

### Пример пакета ответа

Все успешно:

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0}
```

Частично успешно:

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0,    "ErrorList": [        {            "ErrorCode": 70107,            "To_Account": "Mary"        }    ]}
```

### Описание полей пакета ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ActionStatus | String | Результат обработки запроса: OK: обработка успешна. FAIL: обработка не удалась. |
| ErrorCode | Integer | Коды ошибок. |
| ErrorInfo | String | Сообщение об ошибке. |
| ErrorList | Object Array | Установка атрибутов может быть частично успешной для одних пользователей и частично неудачной для других. Список сообщений об ошибках для неудачных учётных записей. |

Описание полей объекта json в массиве ErrorList

| Поле | Тип | Описание |
| --- | --- | --- |
| To_Account | String | Учётная запись целевого пользователя. |
| ErrorCode | Integer | Код ошибки. |
| ErrorInfo | String | Описание ошибки, может быть пусто. |

## Коды ошибок

Если только не происходит сетевая ошибка (например, ошибка 502), HTTP код состояния для этого интерфейса всегда будет 200. **Реальные коды ошибок и сообщения указаны в теле ответа с помощью ErrorCode и ErrorInfo**. Для распространённых кодов ошибок (60000 до 79999) см. документ [Код ошибки](https://intl.cloud.tencent.com/document/product/1047/34348).

Приватные коды ошибок для этого API приведены ниже:

| Код ошибки | Описание |
| --- | --- |
| 90001 | Ошибка парсинга формата JSON. Пожалуйста, проверьте, соответствует ли пакет запроса спецификации JSON. |
| 90009 | Запрос требует прав администратора приложения. |
| 90018 | Количество запрошенных учётных записей превышает лимит. |
| 90033 | Недействительный атрибут. |
| 91000 | Внутренняя ошибка сервера, пожалуйста, повторите попытку. |

## Инструмент отладки API

Используйте инструмент [Онлайн тестирование RESTful API](https://tcc.tencentcs.com/im-api-tool/index.html#/v4/timpush/remove_attr) для отладки этого интерфейса.

## Ссылки

- [Отправка всем пользователям/по тегам](https://www.tencentcloud.com/document/product/1047/67814)
- [Установка имена атрибута приложения](https://www.tencentcloud.com/document/product/1047/67816)
- [Получение имена атрибута приложения](https://www.tencentcloud.com/document/product/1047/67815)
- [Установка атрибутов пользователя](https://www.tencentcloud.com/document/product/1047/67818)
- [Удаление атрибутов пользователя](https://www.tencentcloud.com/document/product/1047/67819)
- [Получение атрибутов пользователя](https://www.tencentcloud.com/document/product/1047/67817)
- [Добавление тегов пользователя](https://www.tencentcloud.com/document/product/1047/67821)
- [Получение тегов пользователя](https://www.tencentcloud.com/document/product/1047/67820)
- [Удаление тегов пользователя](https://www.tencentcloud.com/document/product/1047/67822)
- [Очистка тегов пользователя](https://www.tencentcloud.com/document/product/1047/67823)
- [Отозвание отправки](https://www.tencentcloud.com/document/product/1047/67824)


---
*Источник: [https://trtc.io/document/67819](https://trtc.io/document/67819)*

---
*Источник (EN): [deleting-user-attributes.md](./deleting-user-attributes.md)*
