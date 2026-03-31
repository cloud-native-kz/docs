# Установка имен атрибутов приложения

## Обзор функции

Каждое приложение может устанавливать пользовательские атрибуты пользователя с максимумом 10. Этот интерфейс позволяет установить имя каждого атрибута. После установки они могут быть использованы для push-уведомлений по атрибутам пользователя и т.д.

### Пример URL запроса

```
https://xxxxxx/v4/timpush/set_attr_name?usersig=xxx&identifier=admin&sdkappid=88888888&random=99999999&contenttype=json
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса: HTTPSМетод запроса: POST |
| xxxxxx | Выделенный домен, соответствующий стране/региону вашего SDKAppID.Китай: `console.tim.qq.com`Сингапур: `adminapisgp.im.qcloud.com`Сеул: `adminapikr.im.qcloud.com`Франкфурт: `adminapiger.im.qcloud.com`Кремниевая долина: `adminapiusa.im.qcloud.com`Джакарта: `adminapiidn.im.qcloud.com` |
| v4/timpush/set_attr_name | API запроса |
| usersig | Подпись, созданная учетной записью администратора приложения. Подробнее см. [Создание UserSig](https://www.tencentcloud.com/document/product/1047/34385) |
| identifier | Должна быть учетная запись администратора приложения. Подробнее см. [Администраторы приложения](https://www.tencentcloud.com/document/product/1047/33517) |
| sdkappid | SdkAppid, назначенный консолью Chat при создании приложения |
| random | Случайное 32-битное целое число без знака в диапазоне от 0 до 4294967295 |
| contenttype | Фиксированное значение: `json` |

### Ограничение частоты вызовов

100 раз в секунду.

### Пример пакетов запроса

Установка 0-го атрибута приложения означает пол, 1-й атрибут означает город, 2-й атрибут означает страну.

```
{    "AttrNames": {        "0": "sex",        "1": "city",        "2": "country"    },    "AttrTypes": {        "0": 0, // ccount type corresponding to setting attributes, which does not support modification afterward.        "1": 0,        "2": 0    }}
```

### Описание полей пакета запроса

Описание объекта AttrNames

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| Числовой ключ | String | Обязательно | Указывает, какой атрибут (между "0" и "9") |
| Имя атрибута | String | Обязательно | Имя атрибута не должно превышать 50 байт. Приложение может иметь до 10 атрибутов push (пронумерованных от 0 до 9), пользователь определяет значение каждого атрибута |

Описание объекта AttrTypes

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| Числовой ключ | String | Опционально | Указывает, какой атрибут (между "0" и "9"), должен быть числовым ключом, включенным в AttrNames. |
| Тип учетной записи | Integer | Опционально | Тип учетной записи, соответствующий атрибуту, по умолчанию 0. Атрибут может соответствовать только одному типу учетной записи. Подробнее см. [Введение в типичные сценарии push](https://www.tencentcloud.com/document/product/1047/69236).0: Тип учетной записи представляет: пользователи входят в учетную запись IM для передачи UserID.1: Тип учетной записи представляет RegistrationID, автоматически созданный при успешной регистрации push-сервиса. |

### Пример пакетов ответа

Все успешно:

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0}
```

Все неудачно:

```
{    "ActionStatus": "FAIL",    "ErrorInfo": "attrName:city already exists at index:1",    "ErrorCode": 90033}
```

### Описание полей пакета ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ActionStatus | String | Результат обработки запроса:OK: Указывает на успешную обработкуFAIL: Указывает на ошибку |
| ErrorCode | Integer | Код ошибки |
| ErrorInfo | String | Сообщение об ошибке |

## Коды ошибок

Если не произойдет сетевая ошибка (например, ошибка 502), HTTP-код возврата для этого интерфейса всегда 200.**Фактический код ошибки и информация об ошибке представлены ErrorCode и ErrorInfo в теле ответа**. Распространенные коды ошибок (60000–79999) подробно описаны в документации [Коды ошибок](https://intl.cloud.tencent.com/document/product/1047/34348).

Коды ошибок, специфичные для этого API:

| Код ошибки | Описание |
| --- | --- |
| 90001 | Ошибка анализа формата JSON. Убедитесь, что пакет запроса соответствует спецификации JSON. |
| 90009 | Запрос требует разрешений администратора приложения. |
| 91000 | Внутренняя ошибка сервиса, повторите попытку. |
| 90033 | Неверные параметры атрибутов: дублирование AttrNames не допускается, тип учетной записи в AttrTypes не может быть изменен. |

## Инструмент отладки API

Используйте инструмент [RESTful API Online Test](https://tcc.tencentcs.com/im-api-tool/index.html#/v4/timpush/set_attr_name) для отладки этого интерфейса.

## Ссылки

- [Push всем пользователям/по тегам](https://www.tencentcloud.com/document/product/1047/60561)
- [Одиночный push по userID](https://www.tencentcloud.com/document/product/1047/67553)
- [Получение имен атрибутов приложения](https://www.tencentcloud.com/document/product/1047/60562)
- [Установка имен атрибутов приложения](https://www.tencentcloud.com/document/product/1047/60563)
- [Получение атрибутов пользователя](https://www.tencentcloud.com/document/product/1047/60564)
- [Установка атрибутов пользователя](https://www.tencentcloud.com/document/product/1047/60565)
- [Удаление атрибутов пользователя](https://www.tencentcloud.com/document/product/1047/60566)
- [Получение тегов пользователя](https://www.tencentcloud.com/document/product/1047/60567)
- [Добавление тегов пользователю](https://www.tencentcloud.com/document/product/1047/60568)
- [Удаление тегов пользователя](https://www.tencentcloud.com/document/product/1047/60569)
- [Очистка тегов пользователя](https://www.tencentcloud.com/document/product/1047/60570)
- [Отзыв push](https://www.tencentcloud.com/document/product/1047/60571)


---
*Источник: [https://trtc.io/document/60563](https://trtc.io/document/60563)*

---
*Источник (EN): [setting-application-attribute-names.md](./setting-application-attribute-names.md)*
