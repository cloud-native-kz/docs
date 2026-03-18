# Установка атрибутов пользователя

## Обзор функции

Администратор устанавливает атрибуты для пользователей. Каждый раз можно присвоить атрибуты максимум 100 пользователям. Перед использованием сначала [установите имя атрибута приложения](https://www.tencentcloud.com/document/product/1047/60563).

### Пример URL запроса

```
https://xxxxxx/v4/timpush/set_attr?usersig=xxx&identifier=admin&sdkappid=88888888&random=99999999&contenttype=json
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса: HTTPSМетод запроса: POST |
| xxxxxx | Выделенный домен, соответствующий стране/региону вашего SDKAppID.Китай: `console.tim.qq.com`Сингапур: `adminapisgp.im.qcloud.com`Сеул: `adminapikr.im.qcloud.com`Франкфурт: `adminapiger.im.qcloud.com`Кремниевая долина: `adminapiusa.im.qcloud.com`Джакарта: `adminapiidn.im.qcloud.com` |
| v4/timpush/set_attr | API запроса |
| usersig | Подпись, созданная учетной записью администратора приложения. Подробнее см. [Создание UserSig](https://www.tencentcloud.com/document/product/1047/34385) |
| identifier | Должна быть учетная запись администратора приложения. Подробнее см. [Администраторы приложения](https://www.tencentcloud.com/document/product/1047/33517) |
| sdkappid | Идентификатор SdkAppid, назначенный консолью мгновенных сообщений при создании приложения |
| random | Случайное 32-битное целое число без знака в диапазоне от 0 до 4294967295 |
| contenttype | Фиксированное значение: `json` |

### Ограничение частоты вызовов

100 раз в секунду.

### Пример пакета запроса

```
{    "UserAttrs":    [        {            "To_Account": "379C2F0D-290D-47AE-94D1-919058C39C77", // System-generated RegistrationID upon successful push service registration            "Attrs": {                "sex": "female",                "city": "NewYork"            }        },        {            "To_Account": "xiaoming",            "Attrs": {                "sex": "male",                "city": "ShenZhen"            }        }    ]}
```

### Описание полей пакета запроса

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| To_Account | String | Обязательно | Целевая учетная запись пользователя, поддерживает UserID или RegistrationID. |
| Attrs | Object | Обязательно | Коллекция атрибутов. Каждый атрибут представляет собой пару ключ-значение, где ключ — это имя атрибута, а значение — соответствующее значение атрибута для пользователя. Значения атрибутов пользователя не должны превышать 50 байт |

### Пример пакета ответа

Все операции выполнены успешно:

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
| ActionStatus | String | Результат обработки запроса:OK: Указывает на успешную обработкуFAIL: Указывает на ошибку |
| ErrorCode | Integer | Код ошибки |
| ErrorInfo | String | Сообщение об ошибке |
| ErrorList | Object Array | Установка атрибутов. Некоторые пользователи могут успешно пройти, в то время как другие могут потерпеть неудачу. Список сообщений об ошибках для неудачных учетных записей. |

Описание полей объекта json в массиве ErrorList

| Поле | Тип | Описание |
| --- | --- | --- |
| To_Account | String | Целевая учетная запись пользователя: UserID или RegistrationID. |
| ErrorCode | Integer | Код ошибки |
| ErrorInfo | String | Описание ошибки, которое может быть пустым. |

## Коды ошибок

Если не происходит ошибка сети (например, ошибка 502), код возврата HTTP этого интерфейса всегда равен 200.**Фактический код ошибки и сообщение об ошибке указаны в ErrorCode и ErrorInfo в полезной нагрузке ответа.**. Для общих кодов ошибок (60000–79999) см. документацию [Коды ошибок](https://intl.cloud.tencent.com/document/product/1047/34348).
Коды ошибок, специфичные для этого API:

| Код ошибки | Описание |
| --- | --- |
| 90001 | Ошибка при анализе формата JSON. Убедитесь, что пакет запроса соответствует спецификации JSON. |
| 90009 | Запрос требует разрешений администратора приложения. |
| 90018 | Количество запрашиваемых учетных записей превышает предел. |
| 90033 | Атрибут недействителен. |
| 91000 | Ошибка внутреннего сервиса, попробуйте еще раз. |
| 90035 | Свойство применимо только к одному типу учетной записи. При успешной регистрации службы push для типа учетной записи Chat автоматически генерируется RegistrationID. Подробнее см. [Введение в типичные сценарии push](https://www.tencentcloud.com/document/product/1047/69236#). |

## Инструмент отладки API

Используйте инструмент [Онлайн-тестирование RESTful API](https://tcc.tencentcs.com/im-api-tool/index.html#/v4/timpush/set_attr) для отладки этого интерфейса.

## Справочные материалы

- [Push для всех пользователей/тегам](https://www.tencentcloud.com/document/product/1047/60561)
- [Одиночный push с userID](https://www.tencentcloud.com/document/product/1047/67553)
- [Получение имен атрибутов приложения](https://www.tencentcloud.com/document/product/1047/60562)
- [Установка имен атрибутов приложения](https://www.tencentcloud.com/document/product/1047/60563)
- [Получение атрибутов пользователя](https://www.tencentcloud.com/document/product/1047/60564)
- [Установка атрибутов пользователя](https://www.tencentcloud.com/document/product/1047/60565)
- [Удаление атрибутов пользователя](https://www.tencentcloud.com/document/product/1047/60566)
- [Получение тегов пользователя](https://www.tencentcloud.com/document/product/1047/60567)
- [Добавление тегов пользователя](https://www.tencentcloud.com/document/product/1047/60568)
- [Удаление тегов пользователя](https://www.tencentcloud.com/document/product/1047/60569)
- [Очистка тегов пользователя](https://www.tencentcloud.com/document/product/1047/60570)
- [Отозвание push](https://www.tencentcloud.com/document/product/1047/60571)


---
*Источник: [https://trtc.io/document/60565](https://trtc.io/document/60565)*

---
*Источник (EN): [setting-user-attributes.md](./setting-user-attributes.md)*
