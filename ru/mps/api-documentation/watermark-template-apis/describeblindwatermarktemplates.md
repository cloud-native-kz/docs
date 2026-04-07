# DescribeBlindWatermarkTemplates

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для запроса пользовательского шаблона цифрового водяного знака, поддерживается постраничный запрос на основе условий.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет набор возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса предоставляет только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Требуется | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: DescribeBlindWatermarkTemplates. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Definitions.N | Нет | Array of Integer | Условие фильтрации для уникального идентификатора шаблона цифрового водяного знака. Длина массива не может превышать 100. |
| Name | Нет | String | Условие фильтрации для уникального идентификатора шаблона цифрового водяного знака. Длина не может превышать 64 символов. |
| Type | Нет | String | Тип цифрового водяного знака. Допустимые значения: blind-basic: базовый водяной знак авторского права; blind-nagra: водяной знак судебно-технической экспертизы NAGRA. |
| Offset | Нет | Integer | Смещение постраничной разбивки. Значение по умолчанию — 0. |
| Limit | Нет | Integer | Количество возвращаемых записей. Значение по умолчанию: 10. Максимальное значение: 100. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TotalCount | Integer | Общее количество записей, соответствующих условиям фильтрации. |
| BlindWatermarkTemplateSet | Array of [BlindWatermarkTemplate](https://www.tencentcloud.com/document/api/1041/33690#BlindWatermarkTemplate) | Список сведений о шаблонах цифрового водяного знака. |
| RequestId | String | Уникальный идентификатор запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не доходит до сервера по другим причинам, RequestId не будет получен). RequestId необходим для локализации проблемы. |

## 4. Пример

### Пример 1. Запрос пользовательского шаблона цифрового водяного знака

Этот пример показывает, как запросить пользовательский шаблон цифрового водяного знака.

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeBlindWatermarkTemplates
<Common request parameters>

{
    "Definitions": [
        10,
        20,
        30
    ],
    "Type": "blind-basic",
    "Offset": 0,
    "Limit": 10
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "TotalCount": 1,
        "BlindWatermarkTemplateSet": [
            {
                "Definition": 1001,
                "Type": "blind-basic",
                "Name": "Digital watermark template 1",
                "Comment": "Test template",
                "TextContent": "Text content",
                "CreateTime": "2018-10-01T10:00:00Z",
                "UpdateTime": "2018-10-01T10:00:00Z"
            }
        ],
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, чтобы облегчить вызов API.

Tencent Cloud SDK 3.0 для Python
Tencent Cloud SDK 3.0 для Java
Tencent Cloud SDK 3.0 для PHP
Tencent Cloud SDK 3.0 для Go
Tencent Cloud SDK 3.0 для Node.js
Tencent Cloud SDK 3.0 для .NET
Tencent Cloud SDK 3.0 для C++

### Интерфейс командной строки

Tencent Cloud CLI 3.0

## 6. Коды ошибок

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvalidMpsUser | Ошибка операции: неавторизованный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InvalidParameterValue.Definitions | Ошибка параметра: Definitions. |
| InvalidParameterValue.Limit | Ошибка параметра: Limit. |
| InvalidParameterValue.Type | Ошибка параметра: некорректное значение `Type`. |
| ResourceNotFound.TemplateNotExist | Ресурс не существует: шаблон не существует. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/74702](https://www.tencentcloud.com/document/product/1041/74702)*

---
*Источник (EN): [describeblindwatermarktemplates.md](./describeblindwatermarktemplates.md)*
