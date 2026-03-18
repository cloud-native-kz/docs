# CreateProcessImageTemplate

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для создания шаблона обработки изображений.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд функциональных возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически создаваемые примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: CreateProcessImageTemplate. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| ProcessImageTemplate | Да | [ImageTaskInput](https://www.tencentcloud.com/document/api/1041/33690#ImageTaskInput) | Шаблон обработки изображений. |
| Name | Нет | String | Имя шаблона обработки изображений. Длина не может превышать 64 символа. |
| Comment | Нет | String | Информация описания шаблона обработки изображений. Длина не может превышать 256 символов. |
| StdExtInfo | Нет | String | Расширенные параметры для шаблона обработки изображений. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | Уникальный идентификатор шаблона обработки изображений. |
| RequestId | String | Уникальный ID запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для локализации проблемы. |

## 4. Примеры

### Пример 1. Создание шаблона обработки изображений

Этот пример показывает, как создать шаблон обработки изображений.

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: CreateProcessImageTemplate
<Common request parameters>

{
    "Name": "Template1",
    "Comment": "ProcessImageTemplate",
    "ProcessImageTemplate": {
        "EncodeConfig": {
            "Format": "jpeg",
            "Quality": 75
        },
        "EnhanceConfig": {
            "SuperResolution": {
                "Switch": "ON"
            }
        }
    }
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "03b25aab-8883-497e-838f-d760c3e220f6",
        "Definition": 200043
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, что облегчает вызов API.

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

Ниже перечислены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError | Внутренняя ошибка. |
| InternalError.GenDefinition | Внутренняя ошибка: ошибка при генерировании ID шаблона. |
| InvalidParameter | Ошибка параметра. |
| InvalidParameterValue | Неверное значение параметра. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/74710](https://www.tencentcloud.com/document/product/1041/74710)*

---
*Источник (EN): [createprocessimagetemplate.md](./createprocessimagetemplate.md)*
