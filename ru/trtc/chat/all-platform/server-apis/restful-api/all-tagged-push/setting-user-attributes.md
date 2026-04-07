# Установка атрибутов пользователя

## Обзор функции

Администратор устанавливает атрибуты для пользователей. Каждый раз можно назначить атрибуты максимум 100 пользователям. Перед использованием сначала [установите имя атрибута приложения](https://www.tencentcloud.com/document/product/1047/67816).

### Образец URL запроса

```
https://xxxxxx/v4/timpush/set_attr?usersig=xxx&identifier=admin&sdkappid=88888888&random=99999999&contenttype=json
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса: HTTPSМетод запроса: POST |
| xxxxxx | Выделенный домен, соответствующий стране/региону вашего SDKAppID.Китай: `console.tim.qq.com`Сингапур: `adminapisgp.im.qcloud.com`Сеул: `adminapikr.im.qcloud.com`Токио: `adminapijpn.im.qcloud.com`Франкфурт: `adminapiger.im.qcloud.com`Кремниевая долина: `adminapiusa.im.qcloud.com`Джакарта: `adminapiidn.im.qcloud.com` |
| v4/timpush/set_attr | Запрос API. |
| usersig | Подпись, созданная административной учетной записью приложения. Для деталей см. [Генерирование UserSig](https://www.tencentcloud.com/document/product/1047/34385). |
| identifier | Должна быть административная учетная запись приложения. Для получения более подробной информации см. [Администраторы приложений](https://www.tencentcloud.com/document/product/1047/33517#app-admin). |
| sdkappid | SdkAppid, назначенный консолью обмена сообщениями при создании приложения. |
| random | Случайное 32-битное целое число без знака в диапазоне от 0 до 4294967295. |
| contenttype | Фиксированное значение: `json` |

### Ограничение частоты вызовов

100 раз в секунду.

### Образец пакетов запроса

```
{    "UserAttrs":    [        {            "To_Account": "379C2F0D-290D-47AE-94D1-919058C39C77", // System-generated RegistrationID upon successful push service registration            "Attrs": {                "sex": "female",                "city": "NewYork"            }        },        {            "To_Account": "xiaoming",            "Attrs": {                "sex": "male",                "city": "ShenZhen"            }        }    ]}
```

### Описание полей пакета запроса

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| To_Account | String | Обязательный | Целевой аккаунт пользователя. |
| Attrs | Object | Обязательный | Коллекция атрибутов. Каждый атрибут представляет собой пару ключ-значение, где ключ — имя атрибута, а значение — соответствующее значение атрибута для пользователя. Значения атрибутов пользователя не могут превышать 50 байт. |

### Образец пакетов ответа

Все операции успешны:

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0}
```

Частично успешно:

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0,    "ErrorList": [        {            "ErrorCode": 90035, // A property can only be applicable to one account type            "To_Account": "379C2F0D-290D-47AE-94D1-919058C39C77"        }    ]}
```

### Описание полей пакета ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ActionStatus | String | Результат обработанного запроса:OK: указывает на успешную обработку.FAIL: указывает на ошибку. |
| ErrorCode | Integer | Код ошибки. |
| ErrorInfo | String | Сообщение об ошибке. |
| ErrorList | Object Array | Установка атрибутов. Некоторые пользователи могут быть успешными, а другие могут не пройти. Список сообщений об ошибках для учетных записей, которые не прошли. |

Описание полей объекта json в массиве ErrorList

| Поле | Тип | Описание |
| --- | --- | --- |
| To_Account | String | Целевой аккаунт пользователя. |
| ErrorCode | Integer | Код ошибки. |
| ErrorInfo | String | Описание ошибки, которое может быть пусто. |

## Коды ошибок

Если не происходит ошибка сети (например, ошибка 502), код возврата HTTP этого интерфейса всегда равен 200. **Фактический код ошибки и сообщение об ошибке указаны на основе ErrorCode и ErrorInfo в полезной нагрузке ответа.** Для публичных кодов ошибок (60000–79999) см. документацию [Коды ошибок](https://intl.cloud.tencent.com/document/product/1047/34348).

Приватные коды ошибок для этого API следующие:

| Код ошибки | Описание |
| --- | --- |
| 90001 | Не удалось разобрать формат JSON. Убедитесь, что пакет запроса соответствует спецификации JSON. |
| 90009 | Запрос требует прав администратора приложения. |
| 90018 | Количество запрошенных учетных записей превышает лимит. |
| 90033 | Атрибут недействителен. |
| 91000 | Внутренняя ошибка сервиса, пожалуйста, повторите попытку. |
| 90035 | Свойство применимо только к одному типу учетной записи. При успешной регистрации сервиса push для типа учетной записи Chat автоматически генерируется RegistrationID. Для деталей см. [Введение в типичные сценарии push](https://www.tencentcloud.com/document/product/1047/69236). |

## Средство отладки API

Используйте инструмент [RESTful API Online Test](https://tcc.tencentcs.com/im-api-tool/index.html#/v4/timpush/set_attr) для отладки этого интерфейса.

## Ссылки

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
- [Отзыв push-уведомления](https://www.tencentcloud.com/document/product/1047/67824)


---
*Источник: [https://trtc.io/document/67818](https://trtc.io/document/67818)*

---
*Источник (EN): [setting-user-attributes.md](./setting-user-attributes.md)*
