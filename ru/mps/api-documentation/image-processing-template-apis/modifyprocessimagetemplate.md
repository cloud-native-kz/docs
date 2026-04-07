# ModifyProcessImageTemplate

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для изменения шаблона обработки изображений.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет просматривать запрос, ответ и автоматически генерируемые примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: ModifyProcessImageTemplate. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Definition | Да | Integer | Уникальный идентификатор шаблона обработки изображений. |
| Name | Нет | String | Имя шаблона обработки изображений. Длина не может превышать 64 символа. |
| Comment | Нет | String | Информация описания шаблона. Длина не может превышать 256 символов. |
| ProcessImageTemplate | Нет | [ImageTaskInput](https://www.tencentcloud.com/document/api/1041/33690#ImageTaskInput) | Параметры шаблона обработки изображений. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный идентификатор запроса, генерируемый сервером, будет возвращаться для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Пример

### Пример1 Изменение шаблона обработки изображений

Этот пример показывает, как изменить шаблон обработки изображений.

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: ModifyProcessImageTemplate
<Common request parameters>

{
    "Definition": 200043,
    "Name": "Template100",
    "Comment": "ProcessImageTemplate100",
    "ProcessImageTemplate": {
        "EncodeConfig": {
            "Format": "jpeg",
            "Quality": 50
        },
        "EnhanceConfig": {
            "SuperResolution": {
                "Switch": "OFF"
            }
        }
    }
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "7c43b64a-8f21-4c2e-ab6e-a490ee5c439d"
    }
}
```

## 5. Ресурсы разработчика

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

Ниже указаны только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError | Внутренняя ошибка. |
| InvalidParameter | Ошибка параметра. |
| InvalidParameterValue | Неверное значение параметра. |
| ResourceNotFound.TemplateNotExist | Ресурс не существует: шаблон не существует. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/74707](https://www.tencentcloud.com/document/product/1041/74707)*

---
*Источник (EN): [modifyprocessimagetemplate.md](./modifyprocessimagetemplate.md)*
