# Обратный вызов после изменения атрибута группы

## Обзор функции

Backend приложения может использовать этот обратный вызов для просмотра информации в реальном времени об изменениях пользовательских атрибутов группы, включая: изменение, очистку, сброс и удаление пользовательских атрибутов группы. Backend приложения может использовать этот обратный вызов для операций, таких как синхронизация данных.

## Примечания

- Чтобы включить обратный вызов, необходимо настроить URL обратного вызова и включить соответствующий переключатель протокола. Подробные методы конфигурации см. в документе [Конфигурация сторонних обратных вызовов](https://www.tencentcloud.com/document/product/1047/34520).
- Во время этого обратного вызова Chat backend инициирует HTTP POST запрос к backend приложения.
- После получения запроса обратного вызова backend приложения должен проверить, совпадает ли SDKAppID, содержащийся в URL запроса, с его собственным SDKAppID.
- По другим вопросам безопасности см. [Введение в сторонние обратные вызовы - Рассмотрение вопросов безопасности](https://www.tencentcloud.com/document/product/1047/34354#.E5.AE.89.E5.85.A8.E8.80.83.E8.99.91).

## Сценарии, которые могут вызвать этот обратный вызов

- Пользователи приложения изменяют, очищают, сбрасывают, удаляют пользовательские атрибуты группы через клиент.
- Администраторы приложения изменяют, очищают, сбрасывают, удаляют пользовательские атрибуты группы через REST API.

## Время срабатывания обратного вызова

После изменения пользовательских атрибутов группы.

## Описание API

### Пример URL запроса

В следующем примере URL обратного вызова, настроенный в приложении — `https://www.example.com`.
**Пример:**

```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json&ClientIP=$ClientIP&OptPlatform=$OptPlatform
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса — HTTPS, метод запроса — POST |
| www.example.com | URL обратного вызова |
| SdkAppid | SDKAppID, выделенный консолью Instant Messaging при создании приложения |
| CallbackCommand | Установлено на Group.CallbackAfterGroupAttrChanged |
| contenttype | Фиксированное значение: JSON |
| ClientIP | IP адрес клиента, например 127.0.0.1 |
| OptPlatform | Платформа клиента, см. значение параметра OptPlatform в [Введение в сторонние обратные вызовы - Протокол обратного вызова](https://www.tencentcloud.com/document/product/1047/34354#.E5.9B.9E.E8.B0.83.E5.8D.8F.E8.AE.AE) |

### Пример пакета запроса

```
{    "CallbackCommand": "Group.CallbackAfterGroupAttrChanged",    "GroupId": "@TGS#2J4SZEAEL",    "Type": "Public",    "Operator_Account": "leckie",    "OptionType":"set",   // "set": Reset the attribute defined by the user; "modify": Modify the attribute defined by the user;  "clear": Clear the attribute defined by the user;  "delete": Delete the attribute defined by the user    "GroupAttr": [        {            "key": "key1",            "value": "value1"        },        {            "key": "key2",            "value": "values"        }    ],    "EventTime":"1670574414123"// Event trigger timestamp in milliseconds		}
```

### Описание полей пакета запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда обратного вызова |
| GroupId | String | ID операционной группы |
| Type | String | Тип группы [Введение в тип группы](https://www.tencentcloud.com/document/product/1047/33529#GroupType), например Public |
| Operator_Account | String | UserID оператора, инициирующего запрос на изменение пользовательских атрибутов группы |
| GroupAttr | Array | Список пользовательских атрибутов, где key — имя пользовательского атрибута, а value — значение пользовательского атрибута |
| EventTime | Integer | Временная метка срабатывания события в миллисекундах |

### Пример пакета ответа

После синхронизации данных backend приложения отправляет пакет ответа обратного вызова.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0 // Ignore callback result}
```

### Описание полей пакета ответа

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Обязательное | Результат обработки запроса: OK: указывает на успешную обработку FAIL: указывает на ошибку |
| ErrorCode | Integer | Обязательное | Код ошибки, указание здесь 0 означает игнорирование результата ответа |
| ErrorInfo | String | Обязательное | Сообщение об ошибке |

## Ссылки

- [Обзор сторонних обратных вызовов](https://www.tencentcloud.com/document/product/1047/34354)
- REST API: [Изменение пользовательских атрибутов группы](https://www.tencentcloud.com/document/product/1047/44188)
- REST API: [Очистка пользовательских атрибутов группы](https://www.tencentcloud.com/document/product/1047/44189)
- REST API: [Сброс пользовательских атрибутов группы](https://www.tencentcloud.com/document/product/1047/44190)
- REST API: [Удаление пользовательских атрибутов группы](https://www.tencentcloud.com/document/product/1047/59499)


---
*Источник: [https://trtc.io/document/60394](https://trtc.io/document/60394)*

---
*Источник (EN): [callback-after-group-attribute-changed.md](./callback-after-group-attribute-changed.md)*
