# Ответы

## Ответ при успешном выполнении запроса

Например, при вызове CAM API (версия: 2017-03-12) для просмотра статуса экземпляров (DescribeInstancesStatus), если запрос выполнен успешно, вы можете увидеть ответ, как показано ниже:

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
, которая содержит
RequestId
, как только обработает запрос. Неважно, успешен запрос или нет.
RequestId — это уникальный идентификатор запроса API. Обратитесь к нам с этим идентификатором при возникновении исключения.
Кроме фиксированных полей все остальные поля зависят от действия. Определения полей, зависящих от действия, см. в соответствующей документации API. В этом примере
TotalCount
и
InstanceStatusSet
— это поля, определённые API
DescribeInstancesStatus
. Значение
TotalCount
, равное 0, означает, что запрашивающая сторона владеет 0 экземплярами CVM, поэтому
InstanceStatusSet
пуста.

## Ответ при ошибке запроса

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
указывает на то, что запрос не выполнен. Ответ при ошибке запроса будет содержать поля
Error
,
Code
и
Message
.
Code
— это код ошибки, который помогает вам определить причину и решение. Существует два типа кодов ошибок, поэтому вы можете найти код либо в общих кодах ошибок, либо в кодах ошибок, зависящих от API.
Message
объясняет причину ошибки. Обратите внимание, что возвращаемые сообщения могут обновляться вместе с сервисом. Информация в сообщениях может быть неактуальной и не должна быть единственным источником справки.
RequestId — это уникальный идентификатор запроса API. Обратитесь к нам с этим идентификатором при возникновении исключения.

## Общие коды ошибок

Если в ответе есть поле Error, это означает, что вызов API не выполнен. Поле Code в Error указывает код ошибки. В следующей таблице указаны общие коды ошибок, которые могут быть возвращены всеми действиями.

| Код ошибки | Описание |
| --- | --- |
| AuthFailure.InvalidSecretId | Неверный ключ (не является ключом TencentCloud API). |
| AuthFailure.MFAFailure | Ошибка MFA. |
| AuthFailure.SecretIdNotFound | Ключ не существует. |
| AuthFailure.SignatureExpire | Подпись истекла. |
| AuthFailure.SignatureFailure | Ошибка подписи. |
| AuthFailure.TokenFailure | Ошибка токена. |
| AuthFailure.UnauthorizedOperation | Запрос не имеет авторизации CAM. |
| DryRunOperation | Операция DryRun. Это означает, что запрос был бы успешным, но использован параметр DryRun. |
| FailedOperation | Операция не выполнена. |
| InternalError | Внутренняя ошибка. |
| InvalidAction | API не существует. |
| InvalidParameter | Неверный параметр. |
| InvalidParameterValue | Неверное значение параметра. |
| LimitExceeded | Квота превышена. |
| MissingParameter | Отсутствует параметр. |
| NoSuchVersion | Версия API не существует. |
| RequestLimitExceeded | Количество запросов превышает предел частоты. |
| ResourceInUse | Ресурс используется. |
| ResourceInsufficient | Недостаточно ресурсов. |
| ResourceNotFound | Ресурс не существует. |
| ResourceUnavailable | Ресурс недоступен. |
| UnauthorizedOperation | Несанкционированная операция. |
| UnknownParameter | Неизвестный параметр. |
| UnsupportedOperation | Неподдерживаемая операция. |
| UnsupportedProtocol | Ошибка метода запроса HTTPS. Поддерживаются только запросы GET и POST. |
| UnsupportedRegion | API не поддерживает запрошенный регион. |


---
*Источник: [https://trtc.io/document/34266](https://trtc.io/document/34266)*

---
*Источник (EN): [responses.md](./responses.md)*
