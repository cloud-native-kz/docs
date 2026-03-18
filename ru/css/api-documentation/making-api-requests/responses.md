# Ответы

## Ответ для успешных запросов

Например, при вызове API CAM (версия: 2017-03-12) для просмотра статуса экземпляров (DescribeInstancesStatus), если запрос выполнен успешно, вы можете увидеть ответ, приведённый ниже:

```
{
    "Response": {
        "TotalCount": 0,
        "InstanceStatusSet": [],
        "RequestId": "b5b41468-520d-4192-b42f-595cc34b6c1c"
    }
}
```

API вернёт
Response
, содержащий
RequestId
, при обработке запроса. Неважно, был ли запрос успешным или нет.
RequestId — это уникальный идентификатор запроса API. Обратитесь к нам с этим идентификатором при возникновении исключения.
Кроме фиксированных полей все остальные поля зависят от действия. Определения полей, зависящих от действия, см. в соответствующей документации API. В этом примере
TotalCount
и
InstanceStatusSet
— это поля, указанные API
DescribeInstancesStatus
. Значение 0 для
TotalCount
означает, что запрашивающий владеет 0 экземплярами CVM, поэтому
InstanceStatusSet
пуст.

## Ответ для неудачных запросов

Если запрос не выполнен, вы можете увидеть ответ, приведённый ниже:

```
{
    "Response": {
        "Error": {
            "Code": "AuthFailure.SignatureFailure",
            "Message": "The provided credentials could not be validated. Please ensure your signature is correct."
        },
        "RequestId": "ed93f3cb-f35e-473f-b9f3-0d451b8b79c6"
    }
}
```

Наличие поля
Error
указывает на то, что запрос не выполнен. Ответ на неудачный запрос будет включать поля
Error
,
Code
и
Message
.
Code
— это код ошибки, который помогает определить причину и решение. Существует два типа кодов ошибок, поэтому вы можете найти код либо в общих кодах ошибок, либо в кодах ошибок API.
Message
объясняет причину ошибки. Учтите, что возвращаемые сообщения могут изменяться при обновлении сервиса. Информация, предоставляемая в сообщениях, может быть устаревшей и не должна быть единственным источником справки.
RequestId — это уникальный идентификатор запроса API. Обратитесь к нам с этим идентификатором при возникновении исключения.

## Общие коды ошибок

Если в ответе присутствует поле Error, это означает, что вызов API не выполнен. Поле Code в Error указывает на код ошибки. В таблице ниже приведены общие коды ошибок, которые могут быть возвращены всеми действиями.

| Код ошибки | Описание |
| --- | --- |
| AuthFailure.InvalidSecretId | Неверный ключ (не тип ключа API TencentCloud). |
| AuthFailure.MFAFailure | Ошибка MFA. |
| AuthFailure.SecretIdNotFound | Ключ не существует. |
| AuthFailure.SignatureExpire | Подпись истекла. |
| AuthFailure.SignatureFailure | Ошибка подписи. |
| AuthFailure.TokenFailure | Ошибка токена. |
| AuthFailure.UnauthorizedOperation | Запрос не имеет авторизации CAM. |
| DryRunOperation | Операция DryRun. Это означает, что запрос был бы успешным, но был использован параметр DryRun. |
| FailedOperation | Операция не выполнена. |
| InternalError | Внутренняя ошибка. |
| InvalidAction | API не существует. |
| InvalidParameter | Неверный параметр. |
| InvalidParameterValue | Неверное значение параметра. |
| LimitExceeded | Превышен лимит квоты. |
| MissingParameter | Отсутствует параметр. |
| NoSuchVersion | Версия API не существует. |
| RequestLimitExceeded | Количество запросов превышает лимит частоты. |
| ResourceInUse | Ресурс используется. |
| ResourceInsufficient | Недостаточно ресурсов. |
| ResourceNotFound | Ресурс не существует. |
| ResourceUnavailable | Ресурс недоступен. |
| UnauthorizedOperation | Неавторизованная операция. |
| UnknownParameter | Неизвестный параметр. |
| UnsupportedOperation | Неподдерживаемая операция. |
| UnsupportedProtocol | Ошибка метода запроса HTTPS. Поддерживаются только запросы GET и POST. |
| UnsupportedRegion | API не поддерживает запрашиваемый регион. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30765](https://www.tencentcloud.com/document/product/267/30765)*

---
*Источник (EN): [responses.md](./responses.md)*
