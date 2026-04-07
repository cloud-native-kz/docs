# Удаление всех тегов пользователя

## Обзор функции

Администратор удаляет все теги для пользователя. Обратите внимание, что вы можете удалить все теги максимум для 100 пользователей одновременно.

### Пример URL запроса

```
https://xxxxxx/v4/timpush/clear_all_tags?usersig=xxx&identifier=admin&sdkappid=88888888&random=99999999&contenttype=json
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса: HTTPSМетод запроса: POST |
| xxxxxx | Выделенный домен, соответствующий стране/регионе вашего SDKAppID.Китай: `console.tim.qq.com`Сингапур: `adminapisgp.im.qcloud.com`Сеул: `adminapikr.im.qcloud.com`Франкфурт: `adminapiger.im.qcloud.com`Кремниевая долина: `adminapiusa.im.qcloud.com`Джакарта: `adminapiidn.im.qcloud.com` |
| v4/timpush/clear_all_tags | API запроса |
| usersig | Подпись, созданная администратором приложения. Дополнительные сведения см. в разделе [Генерирование UserSig](https://www.tencentcloud.com/document/product/1047/34385) |
| identifier | Необходимо использовать учетную запись администратора приложения. Дополнительные сведения см. в разделе [Администраторы приложения](https://www.tencentcloud.com/document/product/1047/33517) |
| sdkappid | SdkAppid, назначенный консолью обмена мгновенными сообщениями при создании приложения |
| random | Случайное 32-битное беззнаковое целое число в диапазоне от 0 до 4294967295 |
| contenttype | Фиксированное значение: `json` |

### Ограничение частоты вызовов

100 раз в секунду.

### Пример пакета запроса

```
{    "To_Account": [        "xiaoming",        "xiaohong"    ]}
```

### Поля пакета запроса

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| To_Account | Array | Обязательно | Список целевых учетных записей пользователей, поддерживает UserID или RegistrationID. |

### Пример пакета ответа

Все успешно:

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
| ActionStatus | String | Результат обработки запроса:OK: Указывает на успешную обработкуFAIL: Указывает на ошибку |
| ErrorCode | Integer | Код ошибки |
| ErrorInfo | String | Сообщение об ошибке |
| ErrorList | Object Array | Установленные атрибуты. Некоторые пользователи могут быть успешно обработаны, а другие могут завершиться неудачей. Список сообщений об ошибках для неудачных учетных записей. |

Описание полей объекта json в массиве ErrorList

| Поле | Тип | Описание |
| --- | --- | --- |
| To_Account | String | Целевая учетная запись пользователя: UserID или RegistrationID. |
| ErrorCode | Integer | Код ошибки. |
| ErrorInfo | String | Описание ошибки, которое может быть пустым. |

## Коды ошибок

Если не происходит ошибка сети (например, ошибка 502), HTTP-код возврата этого интерфейса всегда равен 200. **Фактический код ошибки и сообщение об ошибке указаны в полях ErrorCode и ErrorInfo в полезной нагрузке ответа.** Для общих кодов ошибок (60000–79999) см. документацию [Коды ошибок](https://www.tencentcloud.com/document/product/1047/34348).
Приватные коды ошибок для этого API:

| Код ошибки | Описание |
| --- | --- |
| 90001 | Ошибка синтаксического анализа формата JSON. Убедитесь, что пакет запроса соответствует спецификации JSON. |
| 90009 | Запрос требует разрешений администратора приложения. |
| 90018 | Количество запрошенных учетных записей превышает лимит. |
| 91000 | Внутренняя ошибка сервиса, повторите попытку. |

## Инструмент отладки API

Используйте [инструмент онлайн-отладки RESTful API](https://tcc.tencentcs.com/im-api-tool/index.html#/v4/timpush/clear_all_tags) для отладки этого API.

## Справочник

- [Массовая отправка по тегам](https://www.tencentcloud.com/document/product/1047/60561)
- [Отправка одному пользователю с userID](https://www.tencentcloud.com/document/product/1047/67553)
- [Получение имен атрибутов приложения](https://www.tencentcloud.com/document/product/1047/60562)
- [Установка имен атрибутов приложения](https://www.tencentcloud.com/document/product/1047/60563)
- [Получение атрибутов пользователя](https://www.tencentcloud.com/document/product/1047/60564)
- [Установка атрибутов пользователя](https://www.tencentcloud.com/document/product/1047/60565)
- [Удаление атрибутов пользователя](https://www.tencentcloud.com/document/product/1047/60566)
- [Получение тегов пользователя](https://www.tencentcloud.com/document/product/1047/60567)
- [Добавление тегов пользователя](https://www.tencentcloud.com/document/product/1047/60568)
- [Удаление тегов пользователя](https://www.tencentcloud.com/document/product/1047/60569)
- [Очистка тегов пользователя](https://www.tencentcloud.com/document/product/1047/60570)
- [Отзыв отправки](https://www.tencentcloud.com/document/product/1047/60571)


---
*Источник: [https://trtc.io/document/60570](https://trtc.io/document/60570)*

---
*Источник (EN): [deleting-all-user-tags.md](./deleting-all-user-tags.md)*
