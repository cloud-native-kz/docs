# Ответы

## Ответ на успешные запросы

Например, при вызове API CAM (версия: 2017-03-12) для просмотра статуса экземпляров (DescribeInstancesStatus), если запрос выполнен успешно, вы можете увидеть ответ, как показано ниже:

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
, который содержит
RequestId
, как только он обработает запрос. Неважно, успешен ли запрос или нет.
RequestId — это уникальный идентификатор запроса API. Свяжитесь с нами с этим идентификатором при возникновении исключения.
Кроме фиксированных полей все остальные поля зависят от действия. Определения полей, зависящих от действия, см. в соответствующей документации API. В этом примере
TotalCount
и
InstanceStatusSet
— это поля, указанные API
DescribeInstancesStatus
. Значение 0 в поле
TotalCount
означает, что запрашивающий владеет 0 экземплярами CVM, поэтому
InstanceStatusSet
пуст.

## Ответ на неудачные запросы

Если запрос не выполнен, вы можете увидеть ответ, как показано ниже:

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
— это код ошибки, который помогает вам определить причину и решение. Существует два типа кодов ошибок, поэтому вы можете найти код либо в общих кодах ошибок, либо в кодах ошибок, зависящих от API.
Message объясняет причину ошибки. Обратите внимание, что возвращаемые сообщения подлежат обновлению сервиса. Информация, которую предоставляют сообщения, может быть неактуальной и не должна быть единственным источником справки.
RequestId — это уникальный идентификатор запроса API. Свяжитесь с нами с этим идентификатором при возникновении исключения.

## Общие коды ошибок

Если в ответе присутствует поле Error, это означает, что вызов API не выполнен. Поле Code в Error указывает на код ошибки. В таблице ниже перечислены общие коды ошибок, которые могут быть возвращены всеми действиями.

| Код ошибки | Описание |
| --- | --- |
| AuthFailure.InvalidSecretId | Недействительный ключ (не тип ключа API TencentCloud). |
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
| InvalidParameter | Неправильный параметр. |
| InvalidParameterValue | Неправильное значение параметра. |
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
| UnsupportedProtocol | Ошибка метода HTTPS запроса. Поддерживаются только GET и POST запросы. |
| UnsupportedRegion | API не поддерживает запрашиваемый регион. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/33631](https://www.tencentcloud.com/document/product/1041/33631)*

---
*Источник (EN): [responses.md](./responses.md)*
