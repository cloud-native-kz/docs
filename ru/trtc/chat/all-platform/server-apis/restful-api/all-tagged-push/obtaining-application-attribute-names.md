# Получение имен атрибутов приложения

## Обзор функции

Администратор получает имя атрибута приложения. Пожалуйста, сначала [установите имя атрибута приложения](https://www.tencentcloud.com/document/product/1047/67816).

### Пример URL запроса

```
https://xxxxxx/v4/timpush/get_attr_name?usersig=xxx&identifier=admin&sdkappid=88888888&random=99999999&contenttype=json
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса — HTTPS, метод запроса — POST |
| xxxxxx | Выделенный домен, соответствующий стране/региону вашего SDKAppID. Китай: `console.tim.qq.com`. Сингапур: `adminapisgp.im.qcloud.com`. Сеул: `adminapikr.im.qcloud.com`. Токио: `adminapijpn.im.qcloud.com`. Франкфурт: `adminapiger.im.qcloud.com`. Силиконовая долина: `adminapiusa.im.qcloud.com`. Джакарта: `adminapiidn.im.qcloud.com` |
| v4/timpush/get_attr_name | API запроса. |
| usersig | Подпись, созданная учётной записью администратора приложения. Для деталей см. [Генерирование UserSig](https://www.tencentcloud.com/document/product/1047/34385). |
| identifier | Должен быть учётной записью администратора приложения. Для деталей см. [Администраторы приложения](https://www.tencentcloud.com/document/product/1047/33517). |
| sdkappid | Sdkappid, присвоенный консолью обмена сообщениями при создании приложения. |
| random | Случайное 32-битное целое число без знака в диапазоне от 0 до 4294967295. |
| contenttype | Фиксированное значение: `json` |

### Ограничение частоты вызовов

100 раз в секунду.

### Пример пакета запроса

```
{}
```

### Поля пакета запроса

Отсутствуют.

### Пример пакета ответа

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0,    "AttrNames": {        "0": "sex",        "1": "city",        "2": "country"    },    "AttrTypes": {        "0": 0,         "1": 0,        "2": 1 // Ключ номер 2 соответствует атрибуту "country", который может быть установлен только типом учётной записи 1 (RegistrationID автоматически генерируется при успешной регистрации в сервисе push    }}
```

### Описание полей пакета ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ActionStatus | String | Результат обработки запроса: OK — указывает на успешную обработку. FAIL — указывает на ошибку. |
| ErrorCode | Integer | Код ошибки. |
| ErrorInfo | String | Сообщение об ошибке. |
| AttrNames | Object | Содержит несколько пар ключ-значение. Каждая пара представляет имя, соответствующее определённому атрибуту. Например, "0":"xxx" указывает, что имя атрибута 0 — это xxx |
| AttrTypes | Object | Содержит несколько пар ключ-значение. Каждая пара ключ-значение указывает тип учётной записи, соответствующий n-му атрибуту. "0": 0 означает, что тип учётной записи атрибута № 0 — это 0 (тип учётной записи IM). "0": 1 означает, что тип учётной записи атрибута № 0 — это 1 (RegistrationID автоматически генерируется при успешной регистрации в сервисе push). |

## Коды ошибок

Если не происходит ошибка сети (например, ошибка 502), код возврата HTTP этого интерфейса всегда равен 200. **Фактический код ошибки и сообщение об ошибке указаны ErrorCode и ErrorInfo в полезной нагрузке ответа.** Для публичных кодов ошибок (60000–79999) см. документацию [Коды ошибок](https://www.tencentcloud.com/document/product/1047/34348).
Приватные коды ошибок для этого API следующие:

| Код ошибки | Описание |
| --- | --- |
| 90001 | Ошибка при разборе формата JSON. Пожалуйста, убедитесь, что пакет запроса соответствует спецификации JSON. |
| 90009 | Запрос требует прав администратора приложения. |
| 90018 | Число запрашиваемых учётных записей превышает лимит. |
| 91000 | Внутренняя ошибка сервиса, пожалуйста, попробуйте ещё раз. |

## Инструмент отладки API

Используйте инструмент [RESTful API Online Test](https://tcc.tencentcs.com/im-api-tool/index.html#/v4/timpush/get_attr_name) для отладки этого интерфейса.

## Ссылки

- [Рассылка всем пользователям/по тегам](https://www.tencentcloud.com/document/product/1047/67814)
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
*Источник: [https://trtc.io/document/67815](https://trtc.io/document/67815)*

---
*Источник (EN): [obtaining-application-attribute-names.md](./obtaining-application-attribute-names.md)*
